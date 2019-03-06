---
title: 『数据结构』inc,dec,getMin,getMax 均为 O(1)
date: 2018-1-24
categories: 数据结构与算法
tags: [数据结构]
keywords: O(1),有趣,数据结构,最大值,最小值,leetcode

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
from allOoneDS import AllOne
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


op_origin = ['inc','dec','getMinKey','getMaxKey','getMinKey','getMaxKey','getMinKey','getMaxKey','getMinKey','getMaxKey','getMinKey','getMaxKey']
ch=list('qwertyuiopasdfghjklzxcvbnm')
keys =[ ''.join(sample(ch,i)) for j in range(10) for i in range(1,20,5)]

def testCase(n=1000):
    ops=[]
    data=[]
    for i in range(n):
        p = randint(0,len(op_origin)-1)
        ops.append(op_origin[p])
        if p<2:
            data.append([randint(1,10)])
        else:data.append([])
    return ops,data

def test(repeat=1000):
    t1,t2=0,0
    for i in range(repeat):
        allOne = AllOne()
        hsmp = hashMap()
        ops,data = testCase()
        t1-=time()
        for op,datum in zip(ops,data):
            allOne.op[op](*datum)
        t1+=time()

        t2-=time()
        for op,datum in zip(ops,data):
            hsmp.op[op](*datum)
        t2+=time()
    return t1,t2


if __name__=='__main__':
    t1,t2= test()
    print(t1,t2)
```
---
# 5. allOne 代码
```python
class node:
    def __init__(self,val=None,data_mp=None,pre=None,next=None):
        self.val=val
        self.data_mp = {} if data_mp is None else data_mp
        self.pre=pre
        self.next=next
    def __lt__(self,nd):
        return  self.val<nd.val
    def getOne(self):
        if not self.data_mp:
            return ''
        else:return list(self.data_mp.items())[0][0]
    def __getitem__(self,key):
        return self.data_mp[key]
    def __iter__(self):
        return iter(self.data_mp)
    def __delitem__(self,key):
        del self.data_mp[key]
    def __setitem__(self,key,val):
        self.data_mp[key]= val
    def isEmpty(self):
        return self.data_mp=={}
    def __repr__(self):
        return 'node({},{})'.format(self.val,self.data_mp)
class doubleLinkedList:
    def __init__(self):
        self.head=  self.tail = node(0)
        self.head.next = self.head
        self.head.pre = self.head
        self.chain_mp={0:self.head}
    def __str__(self):
        li = list(self.chain_mp.values())
        li = [str(i) for i in li]
        return  'min:{}, max:{}\n'.format(self.head.val,self.tail.val)   \
               + '\n'.join(li)
    def getMax(self):
        return self.tail.getOne()
    def getMin(self):
        return self.head.getOne()
    def addIncNode(self,val):
        # when adding a node,inc 1, so it's guranted that node(val-1)  exists
        self.chain_mp[val].pre= self.chain_mp[val-1]
        self.chain_mp[val].next= self.chain_mp[val-1].next
        self.chain_mp[val-1].next.pre = self.chain_mp[val-1].next = self.chain_mp[val]
    def addDecNode(self,val):
        # when adding a node,dec 1, so it's guranted that node(val+1)  exists
        self.chain_mp[val].next= self.chain_mp[val+1]
        self.chain_mp[val].pre= self.chain_mp[val+1].pre
        self.chain_mp[val+1].pre.next = self.chain_mp[val+1].pre = self.chain_mp[val]
    def addNode(self,val,dec=False):
        self.chain_mp[val] = node(val)
        if dec:self.addDecNode(val)
        else:self.addIncNode(val)
        if self.tail.val<val:self.tail = self.chain_mp[val]
        if self.head.val>val or self.head.val==0:self.head= self.chain_mp[val]
    def delNode(self,val):
        self.chain_mp[val].next.pre = self.chain_mp[val].pre
        self.chain_mp[val].pre.next = self.chain_mp[val].next
        if self.tail.val==val:self.tail = self.chain_mp[val].pre
        if self.head.val==val:self.head = self.chain_mp[val].next
        del self.chain_mp[val]
    def incTo(self,key,val):
        if val not in self.chain_mp:
            self.addNode(val)
        self.chain_mp[val][key] = val
        if val!=1 :  # key in the pre node
            del self.chain_mp[val-1][key]
            #print(self.chain_mp[val-1])
            if self.chain_mp[val-1].isEmpty():
                #print('*'*20)
                self.delNode(val-1)
    def decTo(self,key,val):
        if val not in self.chain_mp:
            self.addNode(val,dec=True)
        # notice that the headnode(0) shouldn't add key
        if val!=0: self.chain_mp[val][key] = val
        del self.chain_mp[val+1][key]
        if self.chain_mp[val+1].isEmpty():
            self.delNode(val+1)

class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.op = {"inc":self.inc,"dec":self.dec,"getMaxKey":self.getMaxKey,"getMinKey":self.getMinKey}
        self.mp = {}
        self.dll = doubleLinkedList()
    def __str__(self):
        return str(self.dll)
    def __getitem__(self,key):
        return self.mp[key]
    def __delitem__(self,key):
        del self.mp[key]
    def __setitem__(self,key,val):
        self.mp[key]= val
    def __iter__(self):
        return iter(self.mp)
    def inc(self, key,n=1):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self:
            self[key]+=n
        else:self[key]=n
        for i in range(n): self.dll.incTo(key, self[key])
    def dec(self, key,n=1):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.mp:
            mn = min( self[key],n)
            for i in range(mn): self.dll.decTo(key, self[key]-i-1)
            if self[key] == n:
                del self[key]
            else:
                self[key] = self[key]-n
    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.dll.getMax()

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.dll.getMin()
```

