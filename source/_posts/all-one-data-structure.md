---
title: 『数据结构』inc,dec,getMin,getMax 均为 O(1) 并用于实现 LRU
date: 2018-1-24
categories: 数据结构与算法
tags: [数据结构,LRU]
keywords: O(1),数据结构,LRU,leetcode
---

做 leetcode 题时遇到这样一道题，挺有趣的数据结构，所以记下来：)
<!-- more -->
# 1. [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/description/) --leetcode 432

Implement a data structure supporting the following operations:

* `Inc(Key)` - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
* `Dec(Key)` - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
* `GetMaxKey()` - Returns one of the keys with maximal value. If no element exists, return an empty string "".
* `GetMinKey()` - Returns one of the keys with minimal value. If no element exists, return an empty string "".


Challenge: Perform all these in O(1) time complexity.


# 2. 想法
我们知道 hashmap 插入，删除，更改是 O(1) 的，为了得到最值也是 O(1)，关键是实现一个双向链表，同时利用到增减都为单位量。下面详细解释各部分

## 2.1. `node`
双向链表的结点，每个结点记录一个 val, 以及值为 val 的键的字典，val>0
* pre: 双向链表，指向前一结点
* next：双向链表，指向后一结点
* val: 关键字对应的值，可以看作频率，通过这个将不同值的关键值分组，类似分块查找，
* keys: 一个 dict, 用来容纳 val 相同的键值，查找插入删除都为 O(1)


## 2.2. `双向链表`
有头指针，尾指针。有一个 val=0 的结点，初始化时头尾指针指向此头结点。
还有一个 dict，键为 val, 值为对应 val 的结点，以便在 O(1) 内找到结点。

如果结点中不含任何关键字，则去掉此结点。如果还存在 key, 头指针指向 val 最小的除 0 的结点（必有关键字）, 尾指针则指向最大的结点，这样 getMin,getMax 都为 O(1)。如果没有任何 key, 则只有一个不含关键字的头节点 node(0)，初始化时也是这样，则头尾指针都指向它

在增减时，需更新头尾指针（最值），可以发现，只有在增加结点或删除结点时才需更新

*  `incTo(self,key,val)`:

    1. 判断 val 结点是否存在，若不，则创建此结点
    2. 使 node(val) 包含关键字 key
    3. 如果前一结点（可以保证一定存在）含此关键字，则删除此关键字
    4. 由上一步，如果删除了前一结点的关键字后，前一结点不再含任何关键字，则删除此结点

*  `dccTo(self,key,val)`:

    1. 判断 val 结点是否存在，若不，则创建此结点
    2. 使 node(val) 包含关键字 key
    3. 后一结点（可以保证一定存在）一定含此关键字，删除此关键字
    4. 由上一步，如果删除了后一结点的关键字后，后一结点不再含任何关键字，则删除此结点

*  `addNode(self,val)`:

注意 inc,dec 时代码不一样，但思路是一样的
    1. 将结点注册到双向链表的 access_mp，既给此 dict, 增加键值对`val:node(val)`
    2. 修改链连接
    3. 更新头尾指针指向的结点（由于 inc,dec 改变的是单位量，所以可以直接找到前一结点或后一节点，这是 O(1) 的

*  `delNode(self,val)`:

    1. 修改链连接
    2. 更新头尾指针指向的结点（由于 inc,dec 改变的是单位量，所以可以直接找到此次 dec 后的最大值或最小值，即若上次最小值是 val 的话，则新的最小值为 node(val).next，即下一节点（循环链表，如果为空时会自动指向头节点 node(0), 代码很简洁，同理可得上次最大值为 val 更新尾指针）
    3. 在 access_mp 中删除此结点

## 2.3. `AllOne`:
这个结构包含一个上述的双向链表和一个 (key:val) 键值对字典，通过此字典来增减关键字的 val，同时在双向链表中找到对应结点，再找到对应的 key

# 3. 总结
这有点像 chain_map 了，不过 python 中的 chain_map 只是简单的连接起来，方便操作多个 map(dict), 而这个数据结构通过双向链表将相同的 val 的 key 字典连接。由于增减的是单位量，所以更新时，更新最值可以通过链表在 O(1) 时间找到。
所以此结构可以用在更新关键字频繁且最好是单位量的地方，而且数据量很大时，查找最值也更有效。（不然创建删除结点费时间）

# 4. 测试
做了测试，与 hashmap 比较了一下（这里设定 hashmap 当值<=0 则删除该键，然后找最大值，最小值用 O(n) 时间）
测试是随机产生一些字符串，然后随机产生操作，inc,dec,getMin,getMax, 以及对应的数据（参数），默认产生 1000 个操作，然后重复 1000 次，取总时间

| | allOne | hashMap | ratio |
| - | - | - | - |
| 增减区间：[1,10]<br>增减与取最值操作的比例：1：1 | 2.83s |1.67s | 1.69 |
| 增减区间：[1,5]<br>增减与取最值操作的比例：1：1 | 4.06s |1.65s | 2.44 |
| 增减区间：[1,5]<br>增减与取最值操作的比例：1：5 | 1.59s |2.21s | 0.72 |


## 4.1. 测试代码
```python
from allOne import allOne
from time import time
from  random import choice,sample,randint

class hashMap:
    def __init__(self):
        self.op = {"inc":self.inc,"dec":self.dec,"getMaxKey":self.getMaxKey,"getMinKey":self.getMinKey}
        self.mp={'':0}
    def inc(self,key,n=1):
        if key in self.mp:self.mp[key]+=n
        else:self.mp[key]=n
    def dec(self,key,n=1):
        if key not in self.mp:return
        if self.mp[key]<=n:del self.mp[key]
        else: self.mp[key]-=n
    def getMinKey(self):
        return min(list(self.mp.keys()),key=lambda key:self.mp[key])
    def getMaxKey(self):
        return max(list(self.mp.keys()),key=lambda key:self.mp[key])


op_origin = ['inc','dec','getMinKey','getMaxKey']#'getMinKey','getMaxKey','getMinKey','getMaxKey','getMinKey','getMaxKey','getMinKey','getMaxKey']
ch=list('qwertyuiopasdfghjklzxcvbnm')
keys =[ ''.join(sample(ch,i)) for j in range(10) for i in range(1,20,5)]

def testCase(n=1000):
    ops=[]
    data=[]
    for i in range(n):
        p = randint(0,len(op_origin)-1)
        ops.append(op_origin[p])
        if p<2:
            data.append([randint(1,5)])
        else:data.append([])
    return ops,data

def test(repeat=100):
    t1,t2=0,0
    for i in range(repeat):
        obj = allOne()
        operate = {
            "inc": obj.inc,
            "dec": obj.dec,
            "getMaxKey": obj.getMaxKey,
            "getMinKey": obj.getMinKey
        }
        hsmp = hashMap()
        ops,data = testCase()
        t1-=time()
        for op,datum in zip(ops,data):
            operate[op](*datum)
        t1+=time()

        t2-=time()
        for op,datum in zip(ops,data):
            hsmp.op[op](*datum)
        t2+=time()
    return t1,t2


if __name__=='__main__':
    t1,t2= test()
    print(f'allOne: {t1}')
    print(f'hashmap: {t2}')
```
---
# 5. allOne 代码
```python
''' mbinary
#########################################################################
# File : allOne.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-05-19  23:07
# Description:
#########################################################################
'''


class node:
    def __init__(self, val=None, keys=None, pre=None, next=None):
        self.val = val
        self.keys = set() if keys is None else keys
        self.pre = pre
        self.next = next

    def __lt__(self, nd):
        return self.val < nd.val


    def __contains__(self, k):
        return k in self.keys

    def __bool__(self):
        return len(self.keys) != 0

    def __repr__(self):
        return 'node({},{})'.format(self.val, self.keys)
    def addKey(self, key):
        self.keys.add(key)


    def remove(self, key):
        self.keys.remove(key)

    def getOneKey(self):
        if self:
            key = self.keys.pop()
            self.keys.add(key)
            return key
        return None


class allOne:
    def __init__(self):
        self.head = self.tail = node(0)
        self.head.next = self.head
        self.head.pre = self.head
        self.val_node = {0: self.head}
        self.key_value = {}

    def __str__(self):
        li = list(self.val_node.values())
        li = [str(i) for i in li]
        return  'min:{}, max:{}\n'.format(self.head.val,self.tail.val)   \
                + '\n'.join(li)
    def __contains__(self,k):
        return k in self.key_value

    def getMaxKey(self):
        return self.tail.getOneKey()

    def getMinKey(self):
        return self.head.getOneKey()

    def getMaxVal(self):
        k = self.getMaxKey()
        if k is not None:
            return self.key_value[k]

    def getMinVal(self):
        k = self.getMinKey()
        if k is not None:
            return self.key_value[k]

    def addIncNode(self, val):
        # when adding a node,inc 1, so it's guranted that node(val-1)  exists
        self.val_node[val] = node(val)
        self.val_node[val].pre = self.val_node[val - 1]
        self.val_node[val].next = self.val_node[val - 1].next
        self.val_node[val - 1].next.pre = self.val_node[
                                                        val - 1].next = self.val_node[val]
        if self.tail.val < val:
            self.tail = self.val_node[val]
        if self.head.val > val or self.head.val == 0:
            self.head = self.val_node[val]

    def addDecNode(self, val):
        # when adding a node,dec 1, so it's guranted that node(val+1)  exists
        self.val_node[val] = node(val)
        self.val_node[val].next = self.val_node[val + 1]
        self.val_node[val].pre = self.val_node[val + 1].pre
        self.val_node[val + 1].pre.next = self.val_node[
                                                        val + 1].pre = self.val_node[val]
        if self.head.val > val:
            self.head = self.val_node[val]

    def delNode(self, val):
        self.val_node[val].next.pre = self.val_node[val].pre
        self.val_node[val].pre.next = self.val_node[val].next
        if self.tail.val == val: self.tail = self.val_node[val].pre
        if self.head.val == val: self.head = self.val_node[val].next
        del self.val_node[val]

    def inc(self, key):
        ''' inc key to value val'''
        val = 1
        if key in self.key_value:
            val += self.key_value[key]
        self.key_value[key] = val
        if val not in self.val_node:
            self.addIncNode(val)
        self.val_node[val].addKey(key)
        if val != 1:  # key in the pre node
            preVal = val - 1
            nd = self.val_node[preVal]
            if key in nd:
                nd.remove(key)
                if not nd:
                    self.delNode(preVal)

    def dec(self, key):
        if key in self.key_value:
            self.key_value[key] -= 1
            val = self.key_value[key]
            if val == 0:
                del self.key_value[key]
            elif val>0:
                if val not in self.val_node:
                    self.addDecNode(val)
                # notice that the headnode(0) shouldn't add key
                self.val_node[val].addKey(key)
            nextVal = val + 1
            nd = self.val_node[nextVal]
            if key in nd:
                nd.remove(key)
                if not nd:
                    self.delNode(nextVal)

    def delMinKey(self):
        key = self.getMinKey()
        if key is not None:
            val = self.key_value.pop(key)
            nd = self.val_node[val]
            nd.remove(key)
            if not nd:
                self.delNode(val)
        return key
    def append(self,key):
        if key in self.key_value:
            raise Exception(f'[Error]: key "{key}" exists')
        if self.key_value:
            val = self.key_value[self.getMaxKey()]
            self.key_value[key] = val
            self.val_node[val].addKey(key)
        self.inc(key)
    def move_to_end(self,key):
        val = self.key_value.pop(key)
        nd = self.val_node[val]
        nd.remove(key)
        if not nd:
            self.delNode(val)
        self.append(key)



if __name__ == '__main__':
    ops = [
           "inc", "inc", "inc", "inc", "inc", "dec", "dec", "getMaxKey",
           "getMinKey",'dec'
          ]
    obj = allOne()
    data = [["a"], ["b"], ["b"], ["b"], ["b"], ["b"], ["b"], [], [],['a']]
    operate = {
               "inc": obj.inc,
               "dec": obj.dec,
               "getMaxKey": obj.getMaxKey,
               "getMinKey": obj.getMinKey
              }
    for op, datum in zip(ops, data):
        print(f'{op}({datum}): {operate[op](*datum)}')
        print(obj)
        print()
```


## 应用
上面的数据结构可以用来实现 LRU 算法,如下
初始化, 定义 容量, eg cache
get 函数返回 key 对应的值, 如果没有返回 -1
put 函数将 key, value 存储起来. 如果容量未满, 直接存储, 否者要先按LRU 替换出去, 再存储

```python
from allOne import  allOne

'''In this implementation, the lru doesn't use some funcs of allOne,
    such as dec,addDecNode
'''
class lru:
    def __init__(self, capacity):
        self.capacity = capacity
        self.allOne = allOne()
        self.data = {}
    def get(self,key):
        if key in self.data:
            self.allOne.move_to_end(key)
            return self.data[key]
        return -1
    def put(self,key,value):
        if key not in self.data:
            if len(self.data)==self.capacity:
                k = self.allOne.delMinKey()
                if k in self.data:
                    del self.data[k]
            self.data[key]=value
            self.allOne.append(key)
        else:
            self.data[key]=value
            self.allOne.move_to_end(key)


if __name__ == '__main__':
    ops = ["put","put","get","put","get","put","get","get","get"]
    data = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    obj = lru(2)
    operate = {'get':obj.get,'put':obj.put}
    for op, args in zip(ops,data):
        print(f'{op}({args}): {operate[op](*args)}\n{obj.data}\n')
```
当然, LRU 用python 自带的 ordered dict 实现更简洁
```python
class LRUCache(object):

    def __init__(self, capacity):
        self.od, self.cap = collections.OrderedDict(), capacity

    def get(self, key):
        if key not in self.od: return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od: del self.od[key]
        elif len(self.od) == self.cap: self.od.popitem(False)
        self.od[key] = value 
```
