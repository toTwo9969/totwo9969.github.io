---
title: leetcode
keyword: [leetcode,oj,python,C]
mathjax: true
fancybox: true
---

记录一些 编程题目, 大多数是用 leetcoode 上的, 使用的语言主要是 python 
[my profile](https://leetcode-cn.com/mbinary/) @leetcode


# 分类目录
## 数学
* [Nth-digit](#Nth-digit)
* [Single-Number](#Single-Number)
* [super-pow](#super-pow)
* [2-Keys-Keyboard](#2-Keys-Keyboard)
* [4Sum-II](#4Sum-II)
* [Gray-Code](#Gray-Code)
* [Bulb switch](#bulb-switch)
* [bitwise-and-of-numbers-range](#bitwise-and-of-numbers-range)
* [numbers-at-most-n-given-digit](#numbers-at-most-n-given-digit)
* [minimum-area-rectangle](#minimum-area-rectangle)

## 搜索
* [3Sum](#3Sum)
* [word-search](#word-search)
* [八数码](#八数码)
* [01-Matrix](#01-Matrix)
* [24-Game](#24-Game)
* [Remove-Invalid-Parentheses](#Remove-Invalid-Parentheses)
* [Valid-Triangle-Number](#Valid-Triangle-Number)


## 回溯
* [N-Queens](#N-Queens)
* [Partition-to-K-Equal-Sum-Subsets](#Partition-to-K-Equal-Sum-Subsets)

## 图
* [Evaluate-Division](#Evaluate-Division)
* [Redundant-Connection](#Redundant-Connection)
* [Clone-Graph](#Clone-Graph)

## 哈希表
* [All-Oone-Data-Structure](#All-Oone-Data-Structure)


## 栈
* [Daily-Temperatures-monotonous stack](#Daily-Temperatures)

## 堆
* [Top-K-Frequent-Words](#Top-K-Frequent-Words)
* [Design-Twitter](#Design-Twitter)
* [Merge-k-Sorted-Lists(多路归并)](#Merge-k-Sorted-Lists)

## 树
* [Longest-Univalue-Path](#Longest-Univalue-Path)
* [Symmetric-Tree](#Symmetric-Tree)
* [Path-Sum-II](#Path-Sum-II)
* [Path-Sum-III](#Path-Sum-III)
* [Unique-Binary-Search-Trees](#Unique-Binary-Search-Trees)

* [Trie-Prefix-Tree](#Trie-Prefix-Tree)
* [Trim-a-Binary-Search-Tree](#Trim-a-Binary-Search-Tree)
* [range-sum-query-2d](#range-sum-query-2d)
* [complete-binary-tree-inserter](#complete-binary-tree-inserter)

## 排序
* [Top-K-Frequent-Words](#Top-K-Frequent-Words)

## 字符串
* [Longest-Palindromic-Substring (Manacher算法)](#Longest-Palindromic-Substring)
* [Integer to Roman](#Roman)
* [Integer-to-English-Words](#Integer-to-English-Words)
* [Word-Search-II( trie优化) ](#Word-Search-II)



## 动态规划
* [2-Keys-Keyboard](#2-Keys-Keyboard)
* [Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee](#Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee)
* [Decode-Ways](#Decode-Ways)
* [Number-of-Longest-Increasing-Subsequence](#Number-of-Longest-Increasing-Subsequence)
* [Knight-Probability-in-Chessboard](#Knight-Probability-in-Chessboard)
* [Longest Valid Parentheses](#Longest-Valid-Parentheses)
* [perfect-squares](#perfect-squares)
* [counting-bits](#counting-bits)
* [wildcard-matching](#wildcard-matching)
* [stone-game](#stone-game)
* [integer-break](#integer-break)

## 其他
* [jump-game](#jump-game)
* [ZigZag-Conversion ](#ZigZag-Conversion-)
* [Insert-Interval](#Insert-Interval)
* [Valid-Parenthesis-String](#Valid-Parenthesis-String)
* [squirrel and tree](#One-line-task:squirrel-and-tree)
* [nim-game](#nim-game)
* [max-ramp](#max-ramp)


# 日志
## 2018-12-28
![](/uploads/divider.png)
 <a id="complete-binary-tree-inserter"></a>
### [complete-binary-tree-inserter](https://leetcode-cn.com/problems/complete-binary-tree-inserter)--leetcode 919
#### 题目
 完全二叉树是每一层（除最后一层外）都是完全填充（即，结点数达到最大）的，并且所有的结点都尽可能地集中在左侧。

设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：

CBTInserter(TreeNode root) 使用头结点为 root 的给定树初始化该数据结构；
CBTInserter.insert(int v) 将 TreeNode 插入到存在值为 node.val = v  的树中以使其保持完全二叉树的状态，并返回插入的 TreeNode 的父结点的值；
CBTInserter.get_root() 将返回树的头结点。
 

```
示例 1：

输入：inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
输出：[null,1,[1,2]]
示例 2：

输入：inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
输出：[null,3,4,[1,2,3,4,5,6,7,8]]
```

#### 思路
完全二叉树的编码
#### 代码
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class CBTInserter:
    def __init__(self, root):
        """
        :type root: TreeNode
        """        
        self.root=root
        self.num = self.getNum(root)
        self.dic={'0':'left','1':'right'}
    def getNum(self,nd):
        if nd is None:return 0
        return 1+self.getNum(nd.left)+self.getNum(nd.right)
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        if self.root is None:
            self.root = TreeNode(v)
            self.num=1
            return 0
        
        self.num+=1
        s= bin(self.num)[3:]
        cur = self.root
        for i in s[:-1]:
            cur = getattr(cur,self.dic[i])
        setattr(cur,self.dic[s[-1]],TreeNode(v))
        return cur.val
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
```
![](/uploads/divider.png)
 <a id="minimum-area-rectangle"></a>
### [最小矩形面积](https://leetcode-cn.com/problems/minimum-area-rectangle)--leetcode 963
#### 题目
 给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边不一定平行于 x 轴和 y 轴。

如果没有任何矩形，就返回 0。

输入：[[1,2],[2,1],[1,0],[0,1]]
输出：2.00000
解释：最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。

输入：[[0,1],[2,1],[1,1],[1,0],[2,0]]
输出：1.00000
解释：最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。

输入：[[0,3],[1,2],[3,1],[1,3],[2,1]]
输出：0
解释：没法从这些点中组成任何矩形。


输入：[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
输出：2.00000
解释：最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。
 
 要注意的细节很多, 主要是矩形的判定, 有两条平行边向量的情况下, 不能在一条直线上, 而且有两条邻边垂直 (否则为平行四边形), 涉及到 向量的内积与外积
#### 代码
```python
class Solution:
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        vec = {}
        n = len(points)
        mn = None
        visited=set()
        for i in range(n-1):
            for j in range(i+1,n):
                x1,y1=points[i]
                x2,y2 = points[j]
                dx = x1-x2
                dy = y1-y2
                new = (i,j)
                if dx<0:
                    dx = -dx
                    dy = -dy
                    new = (j,i)
                v = (dx,dy)  # edge  vec
                if v in vec:
                    for p,q in vec[v]: # edge vecs are the same, namely  line ij//pq
                        if p==i or p==j or q==i or q==j:continue
                        xp,yp= points[p]
                        xq,yq=points[q]
                        ip = tuple(sorted([i,j,p,q]))
                        if  ip not in visited:
                            visited.add(ip) # line  ij//pq or  iq//pj,  just judge them once
                            dx2,dy2 = x1-xq, y1-yq
                            if dx*dx2+dy*dy2!=0:  # line ij,line iq are not vertical. line iq may be a diagonal
                                dx2,dy2 = x1-xp,y1-yp
                            if dx*dx2+dy*dy2!=0: # not rectangle, it's Parallelogram
                                continue
                            s = abs(dx*dy2-dy*dx2)
                            if s!=0:  # Three points shouldn't be on one line
                                if  mn is None or mn>s:mn = s
                    vec[v].add(new)
                else:vec[v]={new}
        return 0 if mn is None else mn
```

![](/uploads/divider.png)
 <a id="max-ramp"></a>
### [最大坡](https://leetcode-cn.com/problems/maximum-width-ramp)--leetcode 962
#### 题目
 给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。

找出 A 中的坡的最大宽度，如果不存在，返回 0 。

```
示例 1：

输入：[6,0,8,2,1,5]
输出：4
解释：
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
示例 2：

输入：[9,8,1,0,1,9,4,0,4,1]
输出：7
解释：
   最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
```
#### 思路
这种题目就是从给定一个 criterion, 目标函数A[i]<=A[j], 求 最值 j-i最大.
从左往右扫描, 保留当前最小值, 记录最优的结果. 这里要注意应该用 排名 来记录.

#### 代码

```python
class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        li = sorted(range(n),key=lambda i: A[i])
        last = n
        mx = 0
        for i in li:
            if i<last:
                last = i
            else:
                mx = max(mx,i-last)
        return mx
```
   
## 2018-12-21
![](/uploads/divider.png)
 <a id="numbers-at-most-n-given-digit"></a>
### [numbers-at-most-n-given-digit](https://leetcode-cn.com/problems/numbers-at-most-n-given-digit)--leetcode 902
#### 题目
我们有一组排序的数字 D，它是  {'1','2','3','4','5','6','7','8','9'} 的非空子集。（请注意，'0' 不包括在内。）

现在，我们用这些数字进行组合写数字，想用多少次就用多少次。例如 D = {'1','3','5'}，我们可以写出像 '13', '551', '1351315' 这样的数字。

返回可以用 D 中的数字写出的小于或等于 N 的正整数的数目。
```
输入：D = ["1","4","9"], N = 1000000000
输出：29523
解释：
我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
81 个四位数字，243 个五位数字，729 个六位数字，
2187 个七位数字，6561 个八位数字和 19683 个九位数字。
总共，可以使用D中的数字写出 29523 个整数。
```
#### 思路
idea 很简单, 比 N 低位的直接 枚举相加, 与 N 位数相同的, 就从高位到低位依次比较, 当前位, 有 k 位 小于等于 若 k 位全小于, 则结束比较 若 有一位 等于, k-1 小于, 则递归地继续比较

只是处理边界条件要仔细点
#### 代码
```python
class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        digits = []
        D = [int(i) for i in D]
        while N :
            digits.append(N%10)
            N//=10
        self.n = len(D)
        if self.n==1:
            if digits[-1]<D[0]:
                return len(digits)-1 
            else:return len(digits)
        return ( int(self.n**len(digits))-self.n)//(self.n-1)+self.get(digits,D)
    def get(self,digits,D):
        if digits ==[]:
            return 1
        if digits[-1]<D[0]:return 0
        ct = 0
        while ct<self.n and digits[-1]>=D[ct]:
            ct+=1
        exp = int(self.n**(len(digits)-1))
        if D[ct-1]==digits[-1]:
            return (ct-1)*exp + self.get(digits[:-1],D)
        else:return  ct*exp
```
## 2018-12-18
![](/uploads/divider.png)
 <a id="bitwise-and-of-numbers-range"></a>
### [bitwise-and-of-numbers-range](https://leetcode-cn.com/problems/bitwise-and-of-numbers-range) --leetcode 201
#### 题目
bitwise-and-of-numbers-range
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
#### 思路
可以发现 上界n在范围$[2^k,2^{k+1}-1]$, 而下界$m<2^k$时, 结果为0, 当下界$m=2^k$时, 结果为$2^k$,由此可以递归求解
#### 代码
```python
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 1<<(len(bin(n))-3)
        return i+self.rangeBitwiseAnd(m%i,n%i) if m>=i else 0
```
## 2018-12-17
![](/uploads/divider.png)
 <a id="integer-break"></a>
### [integer-break](https://leetcode-cn.com/problems/integer-break) --leetcode
#### 题目
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:
```python
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

#### 思路
这个可以用动态规划解答

后来想到, 这不就是均值不等式吗? 给定和, 求积最大, 即
$$
a_1+a_2 \ldots a_k = \sum_{i=1}^{k}a_i = n,\quad \text{find } max(\prod_{i=1}^{k}a_i)
$$
如果先不考虑整数的话,易知当所有数相等时最大,但是注意这里并不知道数的个数 k, 所以设各个数为 x, 有 n/x个
要求出 x, 可以用导数. 各个数的积即为 $x^{\frac{n}{x}}$, 求其最大值
$$
f(x) = x^{\frac{n}{x}},\quad x>0
$$
求导得
$$
f'(x) = nx^{\frac{n}{x}-2}(1-lnx)
$$

易知当 x = e 的时候函数 f(x)有最大值

下面考虑整数, x=2 或者 3

即比较 $2^{\frac{n}{2}}$, $3^{\frac{n}{3}}$
的增长速度, 这很简单了, 其实都是指数函数, 换个形式即为
$\sqrt{2}^{n}$, $\sqrt[3]{3}^{n}$

由于 n > 0 , 底数大的增长快,

计算得
$\sqrt{2} = 1.414, \sqrt[3]{3} = 1.442$
所以, 尽量将整数 n 分成 3即可,
本来是个很简单的题, 但是给我的感觉就是:
**动态规划是种系统的方法, 它依靠计算机的算力对问题直接求解, 不用了解其背后的数学原理.
而有时候, 如果我们跳出常规思维, 思考问题背后的数学规律, 就可能发现更加好的解法. 更加完备,快速, 健壮.**
#### 代码
* 动态规划版本

```python
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dic={1:1}
        for i in range(2,n+1):
            mx = 1
            for j in range(1,i):
                prod = j*self.dic[i-j]
                mx =max(mx,prod,j*(i-j))
            self.dic[i] = mx
        return self.dic[n]
```

* 非动态规划解法
```python
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<5:
            return [0, 0, 1, 2, 4][n]
        x = n % 3
        if x == 0:
            return 3 ** (n // 3)
        if x == 1:
            return 3 ** (n // 3 - 1) * 4
        return 3 ** (n // 3) * 2
```

## 2018-12-15
![](/uploads/divider.png)
 <a id="nim-game"></a>
### [Nim game](https://leetcode-cn.com/problems/nim-game) --leetcode-cn 292
#### 题目
 你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。
 你们是聪明人，判断在什么情况下 先手可以在给定石头数量  赢得游戏。
#### 思路
 233333 上次看见这题还是在小学的 <<举一反三>>上面, 可以说是脑经急转弯了

策略: 要得到最后一块, 可以的取法是 1,2,3.  
我们可以控制这样的局面, 对手取1, 我取3, 对手取2, 我取2, 对手取3, 我取1, 这样石头数量在多个回合内被我方控制得只能以4的数量减少, 所以记为 4n, 要取到最后一个, 则必须还有石头让先手(我方)取一次, 所以石头数是 4n+i (i=1,2,3)的时候, 先手必胜, 
即先手取 i, 然后每个回合取 `4-对方取的数量`
#### 代码
`return n%4!=0`

 ![divider](/uploads/divider.png)
 <a id="stone-game"></a>
### [stone-game](https://leetcode-cn.com/problems/stone-game/) --leetcode-cn 877
#### 题目
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 li[i] 。游戏以谁手中的石子最多来决出 胜负。石子的总数是奇数，所以没有平局。
亚历克斯和李轮流进行. 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
那么先手一定会赢吗? 是的, 求出先手比后手多的石子数.
#### 代码
```python
def stoneGame(li):
    '''li: list, len(li)%2==0, sum(li)%2==1'''
   def f(p,q):
       ret = dp[p][q]
       if ret is None:
           if p+1==q:
               ret =  abs(li[p]-li[q])
           else:
               # max min
               # take the first one
               n1 = li[p] + min(-li[p+1]+f(p+2,q),-li[q]+f(p+1,q-1))
               # take the last one
               n2 = li[q] + min(-li[p]+f(p+1,q-1),-li[q-1]+f(p,q-2))
               ret =  max(n1,n2)
           dp[p][q] = ret
       #print(li[p:q+1],ret)
       return ret
   n = len(li)
   dp = [[None for i in range(n)] for i in range(n)]
   return f(0,n-1)
```
 ![divider](/uploads/divider.png)
 <a id="wildcard-matching"></a>
### [wildcard-matching](https://leetcode.com/problems/wildcard-matching/description/)  --leetcode 44 
#### 题目
wild card:
`*`: matches 0 or any chars,
`?`: matches any single char.

Given two strings `s` and `p`.  `s` doesn't contain wild card and `p` may contain wild card.
Judge if they are matched.
#### 思路
dynamic programming

dp[m+1][n+1]:  bool

i:n,  j:m
dp[j][i] indicates if s[:i+1] matches p[:j+1]

initial: dp[0][0] = True, dp[0][i],dp[j][0] = False
only if p startswith '*',  dp[1][0] = True.

if   p[j] = '*': dp[j][i] = dp[j-1][i] or dp[j][i-1]
elif p[j] = '?': dp[j][i] = dp[j-1][i-1]
else           : dp[j][i] = dp[j-1][i-1] and s[i] == p[j]


#### 代码
```python
def isMatch(self, s, p):
    """
    :type s: str
    :type p: str   pattern str including wildcard
    :rtype: bool
    """
    n,m = len(s),len(p)
    last =  [False]*(n+1)
    last[0] = True
    for j in range(m):
        if p[j]=='*':
            for i in range(n):
                last[i+1] = last[i+1] or last[i]
        elif p[j]=='?':
            last.pop()
            last.insert(0,False)
        else:
            li = [False]
            for i in range(n):
                li.append( last[i] and p[j]==s[i])
            last = li
    return last[-1]
```
 ![divider](/uploads/divider.png)
 <a id="bulb-switch"></a>
### [bulb-switch](https://leetcode-cn.com/problems/bulb-switcher/) -- leetcode-cn 319
#### 题目
初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。

示例
```
输入: 3
输出: 1 
解释: 
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭]. 

你应该返回 1，因为只有一个灯泡还亮着。
```
### 思路
因数分解, 只有平方数才有奇数个因数, 即开关从关闭开始置反奇数次,

### 代码
`int(n**0.5)`

## 2018-11-12
 ![divider](/uploads/divider.png)
 <a id="spiral"></a>
### [One line task:squirrel and tree](https://www.codewars.com/kata/one-line-task-squirrel-and-tree/train/python) --codewars 4kyu
#### 题目
 Task
Since the weather was good, some students decided to go for a walk in the park after the first lectures of the new academic year. There they saw a squirrel, which climbed a tree in a spiral at a constant angle to the ground. They calculated that in one loop the squirrel climbes h meters (vertical height), the height of the tree is equal to H (v in Ruby), and the length of its circumference equals S.

These calculations were exhausting, so now the students need your help to figure out how many meters the path length of squirrel climbed when it reached the tree top. The result should be rounded to 4 decimal places.

Code Limit
Less than 52 characters (JavaScript & Python)

Less than 48 characters (Ruby)

Example
For h = 4, H = 16, S = 3, the output should be 20.

For h = 8, H = 9, S = 37, the output should be 42.5869

#### 思路
螺旋线, 求出一个周期的长度,设周期为 $T$
则可以写出参数方程
$$
\begin{aligned}
z& = \frac{h}{T}t \\
x& = \frac{S}{2\pi}cos\frac{2\pi}{T}t\\
y& = \frac{S}{2\pi}sin\frac{2\pi}{T}t \\  
\end{aligned}
$$
然后求出每一个周期的长度,
$$ 
\text{length}_T = \int_0^T \sqrt{(\frac{dx}{dt})^2+(\frac{dy}{dt})^2+(\frac{dz}{dt})^2} dt
$$

最后算有几个周期即可, 即$\text{length}_T*\frac{H}{h}$
最后的表达式就是
result = $\sqrt{S^2+h^2}\frac{H}{h}$


#### 代码
最开始这样写, 后来注意到 必须少于 52个字符
```python
def squirrel(h,H,S):
    return round((S*S+h*h)**0.5*H/h,4)
```
想了很久就缩短成这样
```python
def squirrel(h,H,S):return round((S*S/h/h+1)**.5*H,4)
```
然而还是有53个字符
在网上找了很多关于舍入, 函数值返回的缩短代码的方法, 都没找到. 
后来看到return, 觉得很多余, 就想到了lambda
```python
squirrel=lambda h,H,S:round((S*S/h/h+1)**.5*H,4)
```
这样就可以pass 了 :smiley:

然后看到别人还有更好的代码, 利用了虚数的模, 
```python
squirrel=lambda h,H,S:round(abs(S/h+1j)*H,4)
```
佩服 :bow:
## 2018-8-26
 ![divider](/uploads/divider.png)
 <a id="counting-bits"></a>
### [counting-bits](https://leetcode.com/problems/counting-bits/description/) --leetcode 338
#### 题目
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
```python Example 1
Input: 2
Output: [0,1,1]
```
#### 思路
这道题也很简单, 只是要想到好的子问题, 我这里通过向右移一位得到
#### 代码
```python
def coutBits(self,num):
    rst = [0]*(1+num)
    for i in range(1,num+1): rst[i] = (i&1)+ rst[i>>1]
    return rst
```
 ![divider](/uploads/divider.png)
 <a id="range-sum-query-2d"></a>
### [range-sum-query-2d](https://leetcode.com/problems/range-sum-query-2d/description/) --leetcode 304
#### 题目
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#### 思路
这道题还是很简单的, 就是计算前缀和就行了, 用二维的数组来保存, 为了方便, 我增加了一行,一列, $A_{ij}就表示 matrix[0][0] 到matrix[i-1][j-1] 所有元素之和$.  需要求解的时候拼凑一下做一个加减法就行了.

最开始我用了四维数组来直接保存结果, 但是内存超了, 而且速度并不会快多少. 
#### 代码
通过了的代码
```python python
class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix == [[]] or matrix ==[]:return
        m,n = len(matrix), len(matrix[0])
        self.data = [[0]*(1+n) for i in range(1+m)]
        for i in range(1,1+m):
            for j in range(1,1+n):
                lval = self.data[i][j-1]
                uval = self.data[i-1][j]-self.data[i-1][j-1]
                self.data[i][j] = matrix[i-1][j-1]+lval+uval
    def sumRegion(self, row1, col1, row2, col2):
        row1+=1
        col1+=1
        row2+=1
        col2+=1
        lval = self.data[row2][col1-1]
        uval = self.data[row1-1][col2] - self.data[row1-1][col1-1]
        return self.data[row2][col2]-lval-uval
```

直接保存结果, 空间 $O(n^4)$, memory excess
```python
class NumMatrix:
    def __init__(self, matrix):
        if matrix == [[]] or matrix ==[]:return
        m,n = len(matrix), len(matrix[0])
        self.transpose = False
        if m>n:
            self.transpose = True
            n,m = m,n
            newMatrix = [[0]*n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    newMatrix[i][j] = matrix[j][i]
            matrix = newMatrix
                    
        self.data = [[[[0]*n for i in range(m)]for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                self.data[i][j][i][j] = matrix[i][j]
        for l in range(n): # note that use the bigger val n, not m
            for d in range(n):
                for i in range(n): # use n not m
                    k = i+l
                    for j in range(n):
                        r = j+d
                        if 0<=k<m and 0<r <n:self.data[i][j][k][r] = self.data[i][j][k][r-1]+self.data[i][r][k][r]
                        if 0<=k<n and 0<r<m: self.data[j][i][r][k] = self.data[j][i][r-1][k]+self.data[r][i][r][k] # tranpose
        print(self.data)
    def sumRegion(self, row1, col1, row2, col2):
        if self.transpose: return self.data[col1][row1][col2][row2]
        else:              return self.data[row1][col1][row2][col2]
```
 ![divider](/uploads/divider.png)
 <a id="perfect-squares"></a>
### [perfect-squares](https://leetcode.com/problems/perfect-squares/description/) --leetcode 279
#### 题目
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
`Example 1:`
>
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

#### 思路
numSquare2是 DFS, numSquare是BFS, DFS会超时. DFS优点就是节省空间, 但是时间上会较慢, 而BFS 正好相反.
#### 代码
```python python
class Solution:

    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:return 0
        self.sq = [i*i for i in range(1,int(n**0.5)+1)]
        self.dic={1:1,0:0}
        return self.get(n)
    def get(self,n):
        if n in self.dic:return self.dic[n]
        ml = n
        for j in self.sq:
            if j>n :break
            ml = min(ml,1+self.get(n-j))
        self.dic[n] = ml
        return ml
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        edges = []
        for i in range(1, int(math.ceil(math.sqrt(n)))+1):
            edges.append(i*i)
        
        depth = 1
        nodes = set([n])
        
        while nodes:
            nextLevel = set()
            for node in nodes:
                
                for e in edges:
                    if node - e == 0:
                        return depth
                    elif node - e > 0:
                        nextLevel.add(node-e)
                    else:
                        break
            
            depth += 1
            nodes = nextLevel
```
## 2018-8-25

 ![divider](/uploads/divider.png)
 <a id="All-O`one-Data-Structure"></a>
### [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) --leetcode 32
#### 题目
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses **substring*****.
#### 思路
cont 变量用来看是否连续的好括号, 用来连接, 用栈的数据结构可以记录当"(" 多于")" 时 的状态.
#### 代码
```python python
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        cont = 0
        maxl = 0
        stk = []
        for i,ch in enumerate(s):
            if ch=="(":
                stk.append(0)
            elif ch==')':
                if stk==[]:
                    cont =0
                else:
                    val = stk.pop()
                    if stk==[]:
                        cont += val+1
                        maxl = max(maxl,cont*2)
                    else:
                        stk[-1] += val+1
                        maxl = max(stk[-1]*2, maxl)
            
        return maxl
```

## 2018-1-23
 ![divider](/uploads/divider.png)
 <a id="All-Oone-Data-Structure"></a>
### [All-O`one-Data-Structure](https://leetcode.com/problems/all-oone-data-structure/description/) --leetcode 432
#### 题目
Implement a data structure supporting the following operations:

* `Inc(Key)` - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
* `Dec(Key)` - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
* `GetMaxKey()` - Returns one of the keys with maximal value. If no element exists, return an empty string "".
* `GetMinKey()` - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity.

#### 思路
详细可以看[这篇文章](../all-one-data-structure.html)

#### 代码
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
        return  'min:{}, max:{}\n'.format(self.head.val,self.tail.val) + '\n'.join(li)
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
        self.op = {"inc":self.inc,"dec":self.dec,"getMaxKey":self.getMaxKey,"getMinKey":self.getMinKey}  # use for testing
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
    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self:
            self[key]+=1
        else:self[key]=1
        self.dll.incTo(key, self[key])
    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.mp:
            self.dll.decTo(key, self[key]-1)
            if self[key] == 1:
                del self[key]
            else:
                self[key] -=1
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

## 2018-1-21
 ![divider](/uploads/divider.png)
 <a id="Partition-to-K-Equal-Sum-Subsets"></a>
### [Partition-to-K-Equal-Sum-Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/)--leetcode 698
#### 题目
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

`Example 1`:

    * Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
    * Output: True
    * Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
`Note`:

* 1 <= k <= len(nums) <= 16.
* 0 < nums[i] < 10000

#### 思路
先排好序，然后对当前剩余的最大的数，判断是否存在一组数使等于平均值。通过将两个数相加，一直归并，如果不成立，则回溯，直到成立，或者没有选择则返回False

#### 代码
```python
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        s , res= divmod(sum(nums),k)
        if res!=0 :return False
        nums.sort()
        return self._util(nums,s,k)
        
    def _util(self,nums,s,n):
#print(nums,s,n)
        if nums == [] and n==0:return True
        elif nums ==[] or n==0:return False
        if nums[-1] >s:return False
        elif nums[-1] ==s:return self._util(nums[:-1],s,n-1)
        else:
            if nums[-1]+nums[0]>s:return False
            elif nums[-1]+nums[0]==s:return self._util(nums[1:-1],s,n-1)
            else:
                ln = len(nums)
                i=1
                for i in range(1,ln-1):
                    if nums[i]+nums[-1]==s:
                        nums.remove(nums[i])
                        return self._util(nums[:-1],s,n-1)
                    elif nums[i]+nums[-1]>s:
                        break
                for j in range(i):
                    li =nums[0:j] +nums[j+1:]
                    li[-1]+=nums[j]
                    if self._util(li,s,n):return True
                else:return False
```

## 2017-12-8
 ![divider](/uploads/divider.png)
 <a id="Word-Search-II"></a>
### [Word-Search-II](https://leetcode.com/problems/word-search-ii/description/)--leetcode 212
#### 题目
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = `["oath","pea","eat","rain"] `and board =
```
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
```
Return `["eat","oath"]`
#### 思路
直接搜索如果遇到前缀几乎相同的，会重复很多次，很慢，所以可以利用trie树
#### 代码
```python
class node:
    def __init__(self,val = None):
        self.val = val
        self.isKey = False
        self.children = {}
    def __getitem__(self,i):
        return self.children[i]
    def __iter__(self):
        return iter(self.children.values())
    def __setitem__(self,i,x):
        self.children[i] = x
    def __bool__(self):
        return self.children!={}
    def __str__(self):
        return 'val: '+str(self.val)+'\nchildren: '+' '.join(self.children.keys())
    def __repr__(self):
        return str(self)
    def __delitem(self,i):
        del self[i]
    
class Trie(object):

    def __init__(self):
        self.root=node('') 
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:return 
        nd = self.root
        for i in word:
            for child in  nd:
                if i==child.val:
                    nd = nd[i]
                    break
            else:
                newNode= node(i)
                nd[i] = newNode
                nd = newNode
        else:nd.isKey = True
    def display(self):
        print('preOrderTraverse  data of the Trie')
        self.preOrder(self.root,'')
    def preOrder(self,root,s):
        s=s+root.val
        if  root.isKey:
            print(s)
        for i in root:
            self.preOrder(i,s)
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.trie = Trie()
        for i in words:
            self.trie.insert(i)
#self.trie.display()
        self.rst = {}
        self.data=board
        self.n = len(board[0])
        self.m = len(board)
        for nd in self.trie.root:
            for i in range(self.m):
                for j in range(self.n):
                    if nd.val ==board[i][j]:
                        self.f(nd,i,j,'')
        return list(self.rst.values())
    def f(self,nd,i,j,s):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if (not (0<=i<self.m and 0<=j<self.n) ) :return
        if  nd.val!=self.data[i][j]:return 
        s=s+nd.val
        if nd.isKey:self.rst[s]=s
        tmp = self.data[i][j]
        self.data[i][j]=None
        bl = False
        offset=[(1,0),(-1,0),(0,1),(0,-1)]
        for child in nd:
            for g,h in offset:
                self.f(child,i+g,j+h,s)
        self.data[i][j]=tmp
```

## 2017-12-5
 ![divider](/uploads/divider.png)
 <a id="Clone-Graph"></a>
### [Clone-Graph](https://leetcode.com/problems/clone-graph/description/)--leetcode 133
#### 题目
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:
```
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
```
#### 思路
dfs,以及记录哪些被访问了，而且要注意复制的时候用self.nd里的结点
#### 代码
1. python
```python
## Definition for a undirected graph node
## class UndirectedGraphNode:
## def __init__(self, x):
## self.label = x
## self.neighbors = []

class Solution:
# @param node, a undirected graph node
# @return a undirected graph node
    
    def __init__(self):
        self.nd={}
    def cloneGraph(self, node):
        if not node :return None
        cur = UndirectedGraphNode(node.label)
        self.nd[cur.label]=cur
        for i in node.neighbors:
            if i.label==node.label:
                cur.neighbors.append(cur)
                continue
            if i.label in self.nd:
                cur.neighbors.append(self.nd[i.label])
            else:
                ret = self.cloneGraph(i)
                if ret!=None :cur.neighbors.append(ret)
        return cur
```

2. c++
```c++
class Solution {
public:
    map<Node*,Node*> st;
    Node *cloneGraph(Node *node){
        Node* ret = new Node(node->val,vector<Node*>());
        st[node]=ret;
        for(auto x:node->neighbors){
            auto p = st.find(x);
            if(p==st.end()){
                ret->neighbors.push_back(cloneGraph(x));
            }else ret->neighbors.push_back(p->second);
        }
        return ret;
    }
};
```

 ![divider](/uploads/divider.png)
 <a id="Knight-Probability-in-Chessboard"></a>
### [Knight-Probability-in-Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/description/)--leetcode 688
#### 题目
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
![knight](https://leetcode.com/static/images/problemset/knight.png)

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.
* Example:
    * Input: 3, 2, 0, 0
    * Output: 0.0625
    * Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
* Note:
    * N will be between 1 and 25.
    * K will be between 0 and 100.
    * The knight always initially starts on the board.

#### 思路
如果用递归写会超时，重复计算太多，用动态规划，状态由k,r,c确定，注意到第二十六行代码，最开始我加的`dp[i-1][j][t]`，这样是错的，要加上由上一状态能到当前状态的，可以发现，当前状态能到上一状态的上一状态能到当前状态，
#### 代码
```python
class Solution:
    def knightProbability(self, N, k, r, c):
        self.one=[(i,j) for i in (1,-1) for j in (2,-2)]
        self.one+=[(j,i) for i in (1,-1) for j in (2,-2)]
        if k==0:return 1
        dp=[[[1]*N for i in range(N)] for j in range(k+1)]
        if N<4:
            for i,j in self.one:
                tr,tc = r+i,j+c 
                if 0<=tr<N and 0<=tc<N:break
            else:return 0
        for i in range(1,k+1):
            for j in range(N):
                for t in range(N):
                    sm =0
                    for g,h in self.one:
                        tr,tc = j+g, t+h
                        if 0<=tr<N and 0<=tc<N:
                            sm+=dp[i-1][tr][tc]
                    dp[i][j][t] = sm/8
#for i in dp:print(i)
        return dp[k][r][c]
```
## 2017-12-4
 ![divider](/uploads/divider.png)
 <a id="Trim-a-Binary-Search-Tree"></a>
### [Trim-a-Binary-Search-Tree](https://leetcode.com/problems/trim-a-binary-search-tree/description/)--leetcode 669
#### 题目
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
#### 思路
#### 代码
```python
class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:return None
        if L>root.val:
            return self.trimBST(root.right,L,R)
        elif R<root.val:
            return self.trimBST(root.left,L,R)
        root.left=self.trimBST(root.left,L,R)
        root.right=self.trimBST(root.right,L,R)
        return root
```
 ![divider](/uploads/divider.png)
 <a id="Number-of-Longest-Increasing-Subsequence"></a>
### [Number-of-Longest-Increasing-Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/)--leetcode 673
#### 题目
Given an unsorted array of integers, find the number of longest increasing subsequence.
Input: [2,2,2,2,2]
Output: 5
#### 思路
找最长子序列dp很好找，但是要求数目的话，还需要对最长序列的第几个字符进行一次dp，这里编程实现还是有点麻烦，要考虑相同的字符
如果相同的subsequence不计，只需将31，32两行改为`dics[t+1][i]=ct`
**总结**
做了近两个月的题，我好菜呀
#### 代码
```python
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        maxval,minval,n=nums[0],nums[0],0
        for i in nums:
            if i>maxval:maxval = i
            if i<minval:minval=i
            n+=1
        if maxval==minval:return n
        
        dics=[{-1<<30:1}]
        mn=[-1<<30]
        lv=1
        for i in nums:
            for j in  range(lv):
                t = lv-1-j
                if i>mn[t]:
                    ct=0
                    for k in dics[t]:
                        if i>k:ct+=dics[t][k]
                    if t+1==lv:  # t+1 out of range, append
                        mn.append(i)
                        dics.append({i:ct})
                        lv+=1
                    else:
                        mn[t+1] = min(i,mn[t+1])
                        if i in dics[t+1]:dics[t+1][i]+=ct
                        else:dics[t+1][i]=ct
                    break
#print(dics,mn)
        return sum(dics[-1].values())
```
 ![divider](/uploads/divider.png)
 <a id="Daily-Temperatures"></a>
### [Daily-Temperatures](https://leetcode.com/contest/weekly-contest-61/problems/daily-temperatures/)--leetcode 729

#### 题目
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
#### 思路
看了别人的答案，以及评论（如下），自己再写的，
>When I saw the question in this competition, I firstly think about Monotonous stack inspired by Largest Rectangle in Histogram.
Because Monotonous stack can help us find first largest element in O(n) time complexity.
But I can't implement use Monotonous stack idea to solve the problem.But you did it, brilliant bro.

**总结**
多读书

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stk =[]
        rst=[0]*n
        for i in range(n):
            while stk and temperatures[stk[-1]]<temperatures[i]:
                tmp = stk.pop()
                rst[tmp]=i-tmp
            stk.append(i)
        return rst
        
```
## 2017-12-1
 ![divider](/uploads/divider.png)
 <a id="Merge-k-Sorted-Lists"></a>
### [Merge-k-Sorted-Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)  --leetcode23
#### 题目
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#### 思路
多路归并，用堆更快，而且python中提供了此模块heapq，注意其用法，这不是一个类，而是一些函数，还有就是merge函数接收的是一些lists，所以要将data解包，见代码21行
#### 代码
```python
## Definition for singly-linked list.
## class ListNode:
## def __init__(self, x):
## self.val = x
## self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        li=[i for i in lists if i !=None]
        if not li:return []
        data=[]
        for i in li:
            data.append([])
            while i!=None:
                data[-1].append(i.val)
                i=i.next
        hp =list(heapq.merge(*data))
        rst = ListNode(heapq.heappop(hp))
        last = rst
        while hp:
            last.next=ListNode(heapq.heappop(hp))
            last = last.next
        last.next = None
        return rst
```
## 2017-11-27
 ![divider](/uploads/divider.png)
 <a id="Longest-Palindromic-Substring"></a>
### [Longest-Palindromic-Substring](https://leetcode.com/problems/longest-palindromic-substring/description/)
#### 题目
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#### 思路
由于回文的对称性。为减少匹配， 可以用[Manacher算法](https://baike.baidu.com/item/Manachar%E7%AE%97%E6%B3%95/20415813?fr=aladdin)
#### 代码
```python
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s2='$#'+'#'.join(s)+'#@'
        ct =[0]*(2*n+4)
        mid=1
        for cur in  range(1,2*n+2):
            if cur<mid+ct[mid]:
                ct[cur] = min(ct[2*mid-cur],mid+ct[mid]-cur)
            else:
                ct[cur]=1
            while s2[cur-ct[cur]]==s2[cur+ct[cur]]:
                ct[cur]+=1
            if cur+ct[cur] > mid+ct[mid]:mid = cur
        mx = max(ct)
        idxs = [i for i,j in enumerate(ct) if j == mx]
        p = idxs[0]
        for i in idxs:
            if s2[i]=='#':p = i
        rst =s2[p-mx+1:p+mx].replace('#','')
        return  rst
        
```

## 2017-11-18
 ![divider](/uploads/divider.png)
 <a id="Decode-Ways"></a>
### [Decode-Ways](https://leetcode.com/problems/decode-ways/description/) --leetcode 91
#### 题目
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.


#### 思路
这道题用动态规划，可以发现，
\[ f(n+1)=\begin{cases}
f(n),\quad when \ \ p(s[n]) \\
f(n-k)*fib(k),\quad when\ p(s[k]),p(s[k+1]) ...p(s[n])    >0
\end{cases} \]
f(n)表示位数有多少种，  fib(N)求fibnaci数列，fib(0)=1,fi(1)=1 ,p(s[n])表示满足性质,大体上是这未为1或2，这样就可能有多种选择， 但要考虑27，28，29，不存在，以及，下一位为0的时候也不算， 具体实现见代码
注意到当后k位都满足p时， 则分步计数，f(n-k) 已经算出，求后面k位有多少种，即时fib数列，然后乘起来即可

#### 代码
```python
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':return 0
        self.fibNum = [1,1]
        ct = 0
        cur = 1
        n = len(s)
        for i in range(n):
#print(i,cur,ct)
            if s[i]=='1'  or s[i]=='2' :
                if i==n-1:ct+=1
                elif not(s[i+1]=='0' or (s[i]=='2' and s[i+1]>'6')): ct+=1
            elif s[i] == '0' and (s[i-1] >'2' or s[i-1]=='0'):return 0
            else:
                if s[i]=='0':
                    cur*= self.fib(ct)
                else:cur*= self.fib(ct+1)
                ct=0
        else:cur*= self.fib(ct)
        return cur
    def fib(self,n):
        sz=len(self.fibNum)
        if n<sz:
            return self.fibNum[n]
        a,b = self.fibNum[-2:]
        for i in range(sz,n+1):
            a,b = b,a+b
            self.fibNum.append(b)
        return self.fibNum[n]
```
**其他**
这里有稍微难一点的
[Decode-Ways II](https://leetcode.com/problems/decode-ways-ii/description/)  --leetcode 639

A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

`Example 1`:

* Input: "*"
* Output: 9
* Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H

```python
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0]=='0':return 0
        n = len(s)
        last = 1
        ans=9 if s[0]=='*' else 1
        for i in range(1,n):
            if s[i]=='*':
                tmp = last
                last = ans
                if s[i-1]=='1' :
                    ans= ans*9+tmp*9
                elif s[i-1]=='2':
                    ans= ans*9+tmp*6
                elif s[i-1]=='*':
                    ans= ans*9+tmp*15                    
                else:ans*=9
            elif s[i]=='0':
                tmp = last
                last = ans
                if s[i-1]=='*':
                    ans = tmp * 2
                elif s[i-1] in '12':ans = tmp
                else:return 0
            else:
                tmp = last
                last = ans
                if s[i-1]=='1' :
                    ans+=tmp
                elif s[i-1]=='2':
                    if s[i]<='6':ans+=tmp
                elif s[i-1]=='*':
                    ans= ans+2*tmp if s[i]<='6' else ans+tmp
        return ans%(10**9+7)
```




## 2017-11-13
 ![divider](/uploads/divider.png)
 <a id="Gray-Code"></a>
### [Gray-Code](https://leetcode.com/problems/gray-code/description//) --leetcode 89
#### 题目
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer?n?representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
For example, given?n?= 2, return?[0,1,3,2]. Its gray code sequence is:0132
`Note`:
For a given?n, a gray code sequence is not uniquely defined.
For example,?[0,2,3,1]?is also a valid gray code sequence according to the above definition.
For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
#### 思路
最开始想到暴力求解：即每次求下一个数，都是列出所有可能，然后找最小的。结果TLE. 后来发现，这个顺序很像卡诺图，然后就找到规律了
#### 代码
```python
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        karnaugh=[0]
        for i in range(n):
            karnaugh+=[j+2**i for j in karnaugh[::-1]]
        return karnaugh
```
## 2017-11-7
 ![divider](/uploads/divider.png)
 <a id="Redundant-Connection"></a>
### [Redundant-Connection](https://leetcode.com/problems/redundant-connection/description/)leetcode 684
#### 题目
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v
#### 思路
这道题即判断图是否存在环。很简单，用并查集来做即可，c++代码只需一行
#### 代码
```c++
class Solution {
public:
    Solution(){for(int i=0;i<1001;++i)s[i]=i;}
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        for(int i=0;i<edges.size();++i){
            if(findset(edges[i][0])==findset(edges[i][1])){
                vector<int> rst;
                rst.push_back(edges[i][0]);
                rst.push_back(edges[i][1]);
                return rst;
            }
            merge(edges[i][0],edges[i][1]);
        }
    }
    
    void merge(int n,int x){s[findset(n)]=s[findset(x)];}
    int findset(int i){return s[i]!=i?s[i]=findset(s[i]):i;}
private:
    int s[10001];
};
```

## 2017-11-4
 ![divider](/uploads/divider.png)
 <a id="Evaluate-Division"></a>
### [Evaluate-Division](https://leetcode.com/problems/evaluate-division/description/) --leetcode 399
#### 题目
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given `a / b = 2.0, b / c = 3.0. `
queries are:` a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . `
return `[6.0, 0.5, -1.0, 1.0, -1.0 ].`

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

        equations = [ ["a", "b"], ["b", "c"] ],
        values = [2.0, 3.0],
        queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
#### 思路
这道题由于是除法，会想到有向图，但是发现，a->b, c->b有可以推出a,b关系，所以连通即可。为了能方便搜索，我又增加了一条反向边vuy(代码第161行)，当然权值为倒数，可是这样增加了深搜难度，于是要解决环的搜索问题(代码第127行)
#### 代码
```python
from collections import Iterable,deque
class vertex:
    def __init__(self,mark,val=None ,firstEdge = None):
        self.mark = mark
        self.val = val
        self.firstEdge = firstEdge
        self.isVisited = False
    def __str__(self):
        if '0'<=self.mark[0]<='9':return 'v'+str(self.mark)
        return str(self.mark)
    def __repr__(self):
        li=[]
        arc= self.firstEdge
        while arc!=None:
            li.append(arc)
            arc= arc.outNextEdge
        return str(self)+ '  to:'+str([str(i.inArrow) for i in li])
class edge:
    def __init__(self,outArrow,inArrow,outNextEdge = None,inNextEdge = None, weight = 1): 
        self.weight = weight
        self.inNextEdge = inNextEdge 
        self.outNextEdge = outNextEdge
        self.outArrow = outArrow
        self.inArrow=inArrow
        self.isVisited = False
    def __str__(self):
        return '--'+str(self.weight)+'-->'
    def __repr__(self):
        return str(self)
class graph:
    def __init__(self): 
        self.vertexs = {}
        self.edges = {}
    def __getitem__(self,i): 
        return self.vertexs[i]
    def __setitem__(selfi,x):
        self.vertexs[i]= x
    def __iter__(self):
        return iter(self.vertexs.values())
    def __bool__(self):
        return len(self.vertexs)!=0
    def addVertex(self,vertexs):
        '''vertexs is a iterable or just a mark that marks the vertex,whichc can be every imutable type'''
        if not isinstance(vertexs,Iterable):vertexs=[vertexs]
        for i in vertexs:
            if  not isinstance(i,vertex) and  i not in self.vertexs:self.vertexs[i]= vertex(i)
            if isinstance(i,vertex) and  i not in self.vertexs:self.vertexs[i.mark]= i
    def isConnected(self,v,u):
        v = self.__getVertex(v)
        u = self.__getVertex(u)
        arc= v.firstEdge
        while arc!=None:
            if arc.inArrow==u:return True
            arc = arc.inNextEdge
        return False
    def __getVertex(self,v):
        if not isinstance(v,vertex):
            if v not in self.vertexs:
                self.vertexs[v]=vertex(v)
            return self.vertexs[v]
        return v
    def addEdge(self,v,u,weight = 1):
        v = self.__getVertex(v)
        u = self.__getVertex(u)
        arc = v.firstEdge
        while arc!=None:         #examine that if v,u have been already connected
            if arc.inArrow==u: return
            arc= arc.outNextEdge
        newEdge = edge(v,u,v.firstEdge,u.firstEdge,weight)
        self.edges[(v.mark,u.mark)] = newEdge
        v.firstEdge = newEdge
    def delEdge(self,v,u):
        if not isinstance(v,vertex):v= self.vertexs[v]
        if not isinstance(u,vertex):u= self.vertexs[u]
        self._unrelated(v,u)
        del self.edges[(v.mark,u.mark)]
    def _unrelated(self,v,u):
        if v.firstEdge==None:return 
        if v.firstEdge.inArrow == u:
            v.firstEdge =v.firstEdge.outNextEdge
        else:
            arc = v.firstEdge
            while arc.outNextEdge!=None:
                 if arc.outNextEdge.inArrow ==u:
                     arc.outNextEdge = arc.outNextEdge.outNextEdge
                     break
    def revisit(self):
        for i in self.vertexs:
            self.vertexs[i].isVisited=False
        for i in self.edges:
            self.edges[i].isVisited=False
    def __str__(self):
        arcs= list(self.edges.keys())
        arcs=[str(i[0])+'--->'+str(i[1])+'  weight:'+str(self.edges[i].weight) for i in arcs]
        s= '\n'.join(arcs)
        return s
    def __repr__(self):
        return str(self)
    def notIn(self,v):
        if (isinstance(v,vertex) and  v.mark not in self.vertexs) or v not in self.vertexs:
            return True
        return False
    def visitPath(self,v,u):
        '''bfs'''
        if self.notIn(v) or  self.notIn(u):
            return  None,None
        v = self.__getVertex(v)
        u = self.__getVertex(u)
        if v.firstEdge==None:return None,None
        q=deque([v.firstEdge])
        isFind=False
        vs,es=[],[]
        while len(q)!=0:
            vs,es=[],[]
            arc= q.popleft()
            if arc.outNextEdge!=None and not arc.outNextEdge.isVisited:q.append(arc.outNextEdge)
            while arc!=None:
                if arc.isVisited:break
                arc.isVisited=True
                es.append(arc)
                vs.append(arc.inArrow)
                arc.outArrow.isVisited=True
                if arc.inArrow==u:
                     isFind=True
                     break
                arc = arc.inArrow.firstEdge
                while arc.inArrow.isVisited and arc.outNextEdge:arc = arc.outNextEdge
            if isFind:break
        else:return None,None
        '''
        se = [str(i) for i in es]
        sv = [str(i)  for i in vs]
        print(str(v),end='')
        for i,j in zip(se,sv):
            print(i,j,end='')
        '''
        return vs,es
    def hasVertex(self,mark):
        return mark in self.vertexs
    def display(self):
        print('vertexs')
        for i in self.vertexs:
            print(self.vertexs[i].__repr__())
        print('edges')
        for i in self.edges:
            arc=self.edges[i]
            print(str(arc.outArrow)+str(arc)+str(arc.inArrow))

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        rst =[]
        g= graph()
        for edge,wt in zip(equations,values):
            g.addEdge(edge[0],edge[1],wt)
            g.addEdge(edge[1],edge[0],1/wt)###### to serach quickly but sacrifacing some space
        g.display()
        for i in queries:
            if i[0]==i[1]:
                if i[0] in g.vertexs:rst.append(1.0)
                else:rst.append(-1.0)
                continue
            _,path = g.visitPath(i[0],i[1])
            if path==None:
                if not path:rst.append(-1.0)
            else:
                mul = 1
                for i in path:mul*=i.weight
                rst.append(mul)
            g.revisit()
        return rst
```


## 2017-10-30
 ![divider](/uploads/divider.png)
 <a id="Design-Twitter"></a>
### [Design-Twitter](https://leetcode.com/problems/4sum-ii/discuss/) --leetcode 355
#### 题目
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

* postTweet(userId, tweetId): Compose a new tweet.
* follow(followerId, followeeId): Follower follows a followee.
* unfollow(followerId, followeeId): Follower unfollows a followee.
* getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least \* recent.
#### 思路
我另外定义了一个user类，以及用得我前面写的<a href="#binaryHeap">优先队列</a>，写了很长，一点都不简洁。看了别人的代码（如下），真的很佩服。踩知道python有`heapq`模块，功能很强大，比如，heapify , merge等等
#### 代码
```python
class Twitter(object):

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)
```
## 2017-10-25
 ![divider](/uploads/divider.png)
 <a id="4Sum-II"></a>
### [4Sum-II](https://leetcode.com/problems/4sum-ii/discuss/) --leetcode 454
#### 题目
我想的使用counter再sort后，用4个for， 再加一点判断，可是本质上还是O(N<sup>4</sup>)，对于随机数来说，都是很差的算法。下面的代码是别人写的O(N<sup>2</sup>)，就两行,啊，我好菜呀T_T
#### 思路
#### 代码
```python
def fourSumCount(self, A, B, C, D):
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)
```
## 2017-10-23
 ![divider](/uploads/divider.png)
 <a id="Trie-Prefix-Tree"></a>
### [Trie( Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/) --leetcode 208
#### 题目
Implement a [trie](https://baike.baidu.com/item/Trie/140945?fr=aladdin) with insert, search, and startsWith methods
#### 思路
trie还是很有趣的，最开始我没弄清楚，以为a->b  再插入abc是  
>b 
>&nbsp;/
>a->b->c

正确的应该在每个节点设一个ISKEY  来判断当前前缀是否是存储的一个str。
最开始我用的列表来存children，也不好， 用字典来存，函数实现就更简洁，而且访问效率高。
代码里后面一些是调试用的，在leetcode上提交应去掉
#### 代码
<a id="binaryHeap"></a>
```python
class node:
    def __init__(self,val = None):
        self.val = val
        self.isKey = False
        self.children = {}
    def __getitem__(self,i):
        return self.children[i]
    def __iter__(self):
        return iter(self.children.keys())
    def __setitem__(self,i,x):
        self.children[i] = x
    def __bool__(self):
        return self.children!={}
    def __str__(self):
        return 'val: '+str(self.val)+'\nchildren: '+' '.join(self.children.keys())
    def __repr__(self):
        return str(self)
    
class Trie(object):

    def __init__(self):
        self.root=node('')
        self.dic ={'insert':self.insert,'startsWith':self.startsWith,'search':self.search}
 
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:return 
        nd = self.root
        for i in word:
            if i in nd:
                nd = nd[i]
            else:
                newNode= node(i)
                nd[i] = newNode
                nd = newNode
        else:nd.isKey = True
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        nd = self.root
        for i in word:
            if i in nd:
                nd = nd[i]
            else:return False
        else:return nd.isKey
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        nd = self.root
        for i in prefix:
            if i in  nd:
                nd= nd[i]
            else:return False
        return True
    def display(self):
        print('preOrderTraverse  data of the Trie')
        self.preOrder(self.root,'')
    def preOrder(self,root,s):
        s=s+root.val
        if  root.isKey:
            print(s)
        for i in root:
            self.preOrder(root[i],s)
    
if __name__=='__main__':
    t = Trie()
    rsts = [None,None,None,None,None,None,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True]
    op = ["insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
    data = [["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
    for i,datum,rst in zip(op,data,rsts):
        if t.dic[i](datum[0]) != rst:print(i,datum[0],rst)
    t.display()
```
 ![divider](/uploads/divider.png)
 <a id="Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee"></a>
### [Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee](https://leetcode.com/contest/leetcode-weekly-contest-55/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) --leetcode 714
#### 题目
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

**Example 1**:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
* Buying at prices[0] = 1
* Selling at prices[3] = 8
* Buying at prices[4] = 4
* Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#### 思路
动态规划，弄清楚，f(n),与f(n+1)的关系，确定转移方程，以及当再次加入一组时是否可以多于两次的fee，代码29，30行就是处理这点
#### 代码
```python
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n<2:return 0
        li = []
        if prices[1]-prices[0]>fee:
            li.append([0,1])
            idx = -1
        else:
            if (prices[0]>prices[1]):idx = 1
            else:idx = 0
        for i in range(2,n):
            if not li:
                if  prices[i]-prices[idx]>fee:li.append([idx,i])
                elif prices[i]<prices[idx]:idx = i
            else:
                last = li[-1]
                if last[1] == i-1 :
                    if prices[i]>prices[last[1]]: 
                        last[1] = i
                    else:idx = i
                else:
                    if prices[i]>prices[idx]+fee:
                        if prices[last[1]]-prices[idx]<fee:
                                last[1] = i
                        else:li.append([idx,i])
                    elif prices[i]>prices[last[1]]: last[1]=i
                    elif prices[i]<prices[idx]:idx=i
        s=[prices[i[1]]-prices[i[0]]-fee for i in li]
        return sum(s)
```



## 2017-10-19
 ![divider](/uploads/divider.png)
 <a id="Valid-Triangle-Number"></a>
### [Valid-Triangle-Number](https://leetcode.com/problems/valid-triangle-number/description/) --leetcode 611
#### 题目
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
#### 思路
注意只要三角形的最大边小于另两边之和，所以排序后，进行搜索，避免不必要的比较
#### 代码
```python
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = 0
        nums.sort()
        n = len(nums)
        for i in range(2,n):
            lo , hi = 0,i-1
            while lo < hi:
                if nums[lo]+nums[hi]>nums[i]:
                    ct+=hi-lo
                    hi-=1
                else:lo+=1
        return ct
```

## 2017-10-16
 ![divider](/uploads/divider.png)
 <a id="Path-Sum-III"></a>
### [Path-Sum-III](https://leetcode.com/problems/path-sum-iii/description/) --leetcode 437
#### 题目
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#### 思路
可以自顶向下传递，为了避免反复求和，可传递路径的前缀和，而且瑶注意不能重复求相同的路径，所以可以在每个节点处，前缀和减去前面所有的节点的前缀和，应该以0开始
#### 代码
```python
## Definition for a binary tree node.
## class TreeNode(object):
## def __init__(self, x):
## self.val = x
## self.left = None
## self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:return 0
        self.sum = sum
        self.total  =0
        self.preOrder(root,[0],0)
        return self.total
    def preOrder(self,root,path,n):
        tmp =root.val+ path[-1]
        for i in path:
            if tmp -i ==self.sum:
                self.total+=1
        path.append(tmp)
        if root.left:self.preOrder(root.left,list(path),n)
        if root.right:self.preOrder(root.right,list(path),n)
```

## 2017-10-14
 ![divider](/uploads/divider.png)
 <a id="Top-K-Frequent-Words"></a>
### [Top-K-Frequent-Words](https://leetcode.com/problems/top-k-frequent-words/description/) --leetcode 692
#### 题目
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
#### 思路
用map就很简单。但这道题是考堆排序的，所以我写了个二叉堆来排序。
#### 代码
```python
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hp = binaryHeap(sortByFrequency = True,reverse=True)
        for i in words:
            hp.insert(i)
        rst = []
        n = len(hp)
        for i in hp.data:
           print(i.val,i.freq)
        mp = {}
        while hp:
            top = hp.deleteTop()
            if top.freq in mp:
                mp[top.freq].append(top.val)
            else:
                mp[top.freq] = [top.val]
        for i in mp:
            mp[i].sort()
        key = sorted(mp.keys(),reverse = True)
        count = 0
        for i in key:
            for j in mp[i]:
                rst.append(j)
                count+=1
                if count == k:return rst
```
二叉堆的实现，支持最大，最小，以及关键字排序或者频率排序
```python
from collections import Iterable           
class node:
    def __init__(self,val,freq=1):
        self.val=val
        self.freq = freq
    def __eq__(self,a):
        return self.val == a.val 
    def __lt__(self,a):
        return self.val<a.val
    def __le__(self,a):
        return self.val<=a.val
    def __gt__(self,a):
        return self.val>a.val
    def __ge__(self,a):
        return self.val>=a.val
    def __ne__(self,a):
        return not self == a
class binaryHeap:
    def __init__(self,s=[],sortByFrequency = False,reverse=False):
        self.sortByFrequency=sortByFrequency
        self.reverse = reverse
        if not isinstance(s,Iterable):s = [s]
        self.data = [node(0)]
        for i in s:
            self.insert(i)
    def __bool__(self):
        return len(self)
    def _cmp(self,a,b):
        if self.sortByFrequency:
            if self.reverse:return a.freq>b.freq
            else:return a.freq<b.freq
        else:
            if self.reverse:return a>b
            else:return a<b
    def insert(self,k):
        if not  isinstance(k,node): k = node(k)
        for j in range(self.data[0].val):
            i = self.data[j+1]
            if i==k:
                i.freq+=1
                if self.sortByFrequency:
                    idx = self.percolateDown(j+1)
                    self.percolateUp(idx)
                return 
        self.data.append(k)
        self.data[0].val += 1
        self.percolateUp()
    def percolateUp(self,n=None):
        if n ==None:n=self.data[0].val
        tmp = self.data[n]
        while n!=1 and self._cmp(tmp,self.data[n//2]):
            self.data[n] = self.data[n//2]
            n = n//2
        self.data[n] = tmp
    def deleteTop(self):
        tmp = self.data[1]
        i = self.percolateDown(1)
        self.data[i] = self.data[-1]
        self.data[0].val-= 1
        del self.data[-1]
        return tmp
    def percolateDown(self,i):
        tmp = self.data[i]
        while self.data[0].val>=2*i+1:
                if self._cmp(self.data[i*2],self.data[2*i+1]):
                    self.data[i] = self.data[2*i]
                    i = 2*i
                else:
                    self.data[i] = self.data[2*i+1]
                    i = 2*i+1
        self.data[i] = tmp
        return i
    def __len__(self):
        return self.data[0].val
    def Nth(self,n=1):
        tmp = []
        for i in range(n):
            tmp.append(self.deleteTop())
        for i in tmp:
            self.insert(i)
        return tmp[-1]
    def display(self):
        val =self.data[0].val+1
        if self.sortByFrequency:
            info='heapSort by Frequency:'
        else:info = 'heapSort by Value:'
        if self.reverse:
            info +=' From big to small'
        else:info +=' From small to big'
        print('*'*15)
        print(info)
        print('total items:%d\nval\tfreq'%(val-1))
        fmt = '{}\t{}'
        for i in range(1,val):
            print(fmt.format(self.data[i].val,self.data[i].freq))
        print('*'*15)
```

 ![divider](/uploads/divider.png)
 <a id="2-Keys-Keyboard"></a>
### [2-Keys-Keyboard](https://leetcode.com/problems/2-keys-keyboard/description/) --leetcode 692
#### 题目
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

`Copy All`: You can copy all the characters present on the notepad (partial copy is not allowed).
`Paste`: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.
Note:The n will be in the range [1, 1000]
#### 思路
分析可知，可以复制一个，然后粘贴n个，胆这样次数太多。要想减少次数，就要复制个数较多（注意复制个数只能越来越多），但复制多了可能会超过。可以发现，若需2n个，可复制n个，需3n个，可复制nge，粘贴2次。而且越早复制越好。这其实就是将n质因数分解。代码7--15行求的li，是用素数筛求小于一个数的所有素数，后面只需将n的所有非1因数加起来即可
#### 代码
```python
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        li = [i for i in range(2,1001)]
        i = 1
        while  i <len(li):
            prod =2 * li[i] 
            while prod <=li[-1]:
                if prod i ''''''n li:
                    li.remove(prod)
                prod+=li[i]
            i+=1
        rst = 0
        for i in li:
            if i > n:break
            ct = 0
            while n%i == 0:
                n/=i
                ct +=1
            rst +=ct*i
        return rst
        
```

## 2017-10-12
 ![divider](/uploads/divider.png)
 <a id="Unique-Binary-Search-Trees"></a>
### [Unique-Binary-Search-Trees](https://leetcode.com/problems/unique-binary-search-trees/description/) --leetcode 96
#### 题目
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#### 思路
注意到给定一棵树，只有一种对应的BST（1，2，...,n)。所以这道题就使求N个节点能形成多少种不同的树，就很简单了，直接用Catalan数C(<sup>n</sup><sub>2n</sub>)/(1+n)，不过在计算中我优化了一下，而且注意最后结果用了round，不能直接用int（），这会截断小数的
#### 代码
```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 1
        for i in range(2,n+1):
            rst *=(n+i)*1.0/i
        return int(round(rst))
```

下面是可以生成bst的代码

```python
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n<1:return []
        self.ts=[TreeNode(1)]
        for i in range(2,n+1):
            self.add(i)
        return  self.ts
    def add(self,i):
        self.cur=[]
        for j in self.ts:
            nd = TreeNode(i)
            nd.left = self.copyT(j)
            self.cur.append(nd)
            self.add_util(j,j,i)
        self.ts=self.cur
    def add_util(self,origin,nd,i):
        if not nd:return 
        new = TreeNode(i)
        new.left = nd.right
        nd.right=new
        self.cur.append(self.copyT(origin))
#print(self.cur)        
        nd.right = new.left
        self.add_util(origin,nd.right,i)
    def copyT(self,root,val=1<<30):
        if not root :return None
        nd=TreeNode(root.val)
        if root.val<val:
            nd.left = self.copyT(root.left)
            nd.right = self.copyT(root.right)
        return nd
```

 ![divider](/uploads/divider.png)
 <a id="Path-Sum-II"></a>
### [Path-Sum-II](https://leetcode.com/problems/path-sum-ii/description/) --leetcode 113
#### 题目
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
```
#### 思路
分四种情况讨论即可
#### 代码
```python
## Definition for a binary tree node.
## class TreeNode(object):
## def __init__(self, x):
## self.val = x
## self.left = None
## self.right = None
class Solution(object):
    def pathSum(self, root, sm):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:return []
        paths = self.getPath(root)
        print paths
        return [i for i in paths if sum(i) == sm]
    def getPath(self,root):
        if not root.left and not root.right:
            return [[root.val]]
        li = []
        if root.left :
            li+=self.getPath(root.left)
        if root.right :
            li+=self.getPath(root.right)
        for i in li:
            i.insert(0,root.val)
        return li
```

## 2017-10-8
 ![divider](/uploads/divider.png)
 <a id="Symmetric-Tree"></a>
### [Symmetric-Tree](https://leetcode.com/problems/symmetric-tree/description/) --leetcode 101
#### 题目

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#### 思路
挺简单的，不过对称挺美的
#### 代码

`recursive solution`

```python
## Definition for a binary tree node.
## class TreeNode(object):
## def __init__(self, x):
## self.val = x
## self.left = None
## self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        return  self.judge(root.left,root.right)
    def judge(self,p,q):
        if not p and not q:return True
        if (not p  and q) or (p  and not q):return False
        return p.val == q.val and self.judge(p.left,q.right) and self.judge(p.right,q.left)
```

漂亮的`iterative solution`

```python
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        q = deque([root.left,root.right])
        while len(q)>1:
            left = q.popleft()
            right = q.popleft()
            if not left and not right:continue
            elif (left == None) ^ (right ==None) or  left.val != right.val:return False
            q.extend([left.left,right.right,left.right,right.left])
        return True
```
 ![divider](/uploads/divider.png)
 <a id="Longest-Univalue-Path"></a>
### [Longest-Univalue-Path](https://leetcode.com/problems/longest-univalue-path/description/) --leetcode 687
#### 题目
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.
`example`:output 3
```
              4
             / \
            4   4
           / \   \
          4   4   5
```
#### 思路
将左右汇聚到根节点再进行比较即可，为了能使代码更简洁，我把None的值赋为root.val-1.注意是求路径，而不是边数最多的子树，要求后者，只需将最后一行代码改为`return r+l+2`
#### 代码
```python
## Definition for a binary tree node.
## class TreeNode(object):
## def __init__(self, x):
## self.val = x
## self.left = None
## self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        self.mx = 0
        self.find(root)
        return self.mx
    def find(self,root):
        if not root.left and not root.right:return 0
        if root.left:
            lval = root.left.val
            l = self.find(root.left) 
        else:
            lval = root.val-1
            l = 0
        if root.right:
            r = self.find(root.right)
            rval = root.right.val            
        else:
            rval = root.val-1
            r = 0
        if root.val != lval and root.val!=rval:
            self.mx = max(self.mx,l,r)
            print '00'
            return 0
        elif  root.val == lval and root.val!=rval:
            self.mx = max(self.mx,l+1,r)
            print '10'
            return l+1
        elif  root.val != lval and root.val==rval:
            self.mx = max(self.mx,l,1+r)
            print '01'
            return r+1
        else:
            print '11'
            self.mx = max(self.mx,l+2+r)
            return max(l,r)+1
```
## 2017-9-25
 ![divider](/uploads/divider.png)
 <a id="Remove-Invalid-Parentheses"></a>
### [Remove-Invalid-Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/description/) --leetcode 301
#### 题目
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

    Examples:
    "()())()" -> ["()()()", "(())()"]
    "(a)())()" -> ["(a)()()", "(a())()"]
    ")(" -> [""]
#### 思路
代码是别人的，我写得太矬。我写了几十行代码，人家只用了几行:sob:。这道题可以用BFSFS，注意到对于一个坏括号列，要变成好括号列，要删去的括号种类（即`(`或者`)`）和数目是固定的，所以可以逐个搜索删去1，2，3...个后，是否有好括号列。不过这样不足的一点就是太慢了，搜索得太多了。
#### 代码
```
def removeInvalidParentheses(self, s):
    def isvalid(s):
        ctr = 0
        for c in s:
            if c == '(':
                ctr += 1
            elif c == ')':
                ctr -= 1
                if ctr < 0:
                    return False
        return ctr == 0
    level = {s}
    while True:
        valid = filter(isvalid, level)
        if valid:
            return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
```

 ![divider](/uploads/divider.png)
 <a id="Valid-Parenthesis-String"></a>
### [Valid-Parenthesis-String](https://leetcode.com/problems/valid-parenthesis-string/description/) --leetcode 678
#### 题目
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5. An empty string is also valid.
`example`:  `()`,`(*`,`(*)` are all valid.
#### 思路
根据好括号的判断充要条件：从左往右数，左括号数不少于右括号数，且最终左右括号数相等。在这里，加入了\*号，有些难度。可以改进为：<mark>从左往右数，左括号数不大于右括号与*号之和</mark>。比如`((*)(*))((*`，本来是错的，但会判对，所以要再改进一下， 可以再来一遍从右往左数。
#### 代码
```
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        left = 0 
        right = 0
        star = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                right += 1
            else:
                star += 1
            if left+star < right :
                return False
        n = len(s) -1
        left = right = star = 0
        for i in range(n,-1,-1):
            if s[i] == '(':
                left+=1
            elif s[i] == ')':
                right+=1
            else:
                star +=1
            if left>right+star:
                return False
        return True
```


## 2017-9-21
 ![divider](/uploads/divider.png)
 <a id="24-Game"></a>
### [24-Game](https://leetcode.com/problems/24-game/description/) --leetcode 679
#### 题目
>You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

    `Example 1`:
    Input: [4, 1, 8, 7]
    Output: True
    Explanation: (8-4) * (7-1) = 24
    `Example 2`:
    Input: [1, 2, 1, 2]
    Output: False

`Note`:

    1. The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
    2. Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as 3. input, the expression -1 - 1 - 1 - 1 is not allowed.
    3. You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2],   we cannot write this as 12 + 12.

#### 思路
搜索4则运算，与两两结合的所有可能。由于python函数的一等性，写代码很简洁。注意3，3，8，8， 要用浮点数比较来判断是否等于一个浮点数，`abs(nums[0] -24)<0.01`.还有一点比较坑的是，leetcode上的pythonde `/`居然是截断除法，调试了很久:sob:
#### 代码
```python
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.exam(nums,4)
    def div(a,b):
        if abs(b)< 0.01:
            return 10000
        return a/float(b)
    from operator import mul,add,sub
    ops = [mul,add,sub,div]
    def exam(self,nums,n):
        if n is 1 :
            if abs(nums[0] -24)<0.01:
                return True
            else:return False
        for op in self.ops:
            for i in range(n-1):
                for j in range(i+1,n):
                    rst1 = op(nums[i],nums[j])
                    rst2 = op(nums[j],nums[i]) 
                    tmp = nums[:]
                    tmp.remove(nums[i])
                    tmp.remove(nums[j])
                    tmp.append(rst1)
                    if self.exam(tmp,n-1):
                        return True
                    if rst1 != rst2:
                        tmp[-1] = rst2
                        if self.exam(tmp,n-1):
                            return True
        return False
```
我拓展了一下，改进了代码，把表达式也打出来了.(这个可以直接提交，能过的)
```python
from operator import mul,add,sub

def div(a,b):
    if abs(b)<0.01:
        return 10000
    return a/float(b)
    
ops = [mul,add,sub,div]
sym = {'mul':'*','sub':'-','div':'/','add':'+'}
fmt = '({0}{1}{2})'

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.exam(nums,[],4)
    def exam(self,nums,expr_str,n):
        if n is 1 :
            if abs(nums[0] - 24) < 0.01:
                print expr_str[0]+'=24'
                return True
            else:return False
        for op in ops:
            for i in range(n-1):
                for j in range(i+1,n):
                    rst1 = op(nums[i],nums[j])
                    rst2 = op(nums[j],nums[i]) 
                    tmp = nums[:]
                    tmp.remove(nums[i])
                    tmp.remove(nums[j])
                    tmp.append(rst1)
                    expr = expr_str[:]
                    length = len(expr)
                    name = sym[op.__name__]
                    if length == 1:
                        expr[0] = fmt.format(nums[i],name,expr[0])
                    elif length ==0:
                        expr.append(fmt.format(nums[i],name,nums[j]))
                    else:
                        expr = [fmt.format(expr[0],name,expr[1])]
                    if self.exam(tmp,expr,n-1):
                        return True
                    if rst1 != rst2:
                        expr = expr_str[:]
                        if length == 1:
                            expr[0] = fmt.format(expr[0],name,nums[i])
                        elif length == 0:
                            expr.append(fmt.format(nums[j],name,nums[i]))
                        else:
                            expr = [fmt.format(expr[0],name,expr[1])]            
                        tmp[-1] = rst2
                        if self.exam(tmp,expr,n-1):
                            return True
        return False
```
## 2017-9-18
 ![divider](/uploads/divider.png)
 <a id="01-Matrix"></a>
### [01-Matrix](https://leetcode.com/problems/01-matrix/description/) --leetcode 542
#### 题目
>Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
>The distance between two adjacent cells is 1.

    Input:
    0 0 0
    0 1 0
    1 1 1 

    Output:
    0 0 0
    0 1 0
    1 2 1

>`Note`:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and righ

#### 思路
由于是找最小的步骤，所以可以采用BFS。最开始我用
```
n1 = len(matrix)
n2 = len(matrix[0])
tmp = [0 for k in range(n2)]
isVisited = [tmp for k in range(n1)]
```
来记录是否访问，结果总出现一些奇怪的错误，打印出来，发现上面的创建列表的方法，会使isVisited的元素萨都是tmp，同样的id。因为tmp使可变的，都是同一列表的引用。
可以这样`isVisited = [[0]*n2 for i in range(n1)]` ，0是基础类型，直接复制，不是引用。
为了简便，使用队列保持有序。为了记录移动的步数，我没有写一个类，而是让用另一个队列与队列列表形成映射。
#### 代码
```python
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        ans=[]
        n1 = len(matrix)
        n2 = len(matrix[0])
        def search(i,j):
            num = deque([0])
            que = deque([(i,j)])
# notice that the initialization of deque should pass an iterable object ,
# and a tuple should be in a list .
            while que != []:
                p,q = que.popleft()
                count = num.popleft()
                if matrix[p][q] == 0:
                    return count
                if p>0 and (p-1,q) not in que :
                    que.append((p-1,q))
                    num.append(count+1)
                if p<n1-1 and (p+1,q) not in que:
                    que.append((p+1,q))
                    num.append(count+1)
                if q>0 and (p,q-1) not in que:
                    que.append((p,q-1))
                    num.append(count+1)
                if q<n2-1 and (p,q+1) not in que:
                    que.append((p,q+1))
                    num.append(count+1)
        for i in range(n1):
            ans.append([])
            for j in range(n2):
                ans[i].append(search(i,j))
        return ans
```


 ![divider](/uploads/divider.png)
 <a id="Integer-to-English-Words"></a>
### [Integer-to-English-Words](https://leetcode.com/problems/integer-to-english-words/description/) --leetcode 273
#### 题目
>Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
    
    For example,    
    123 -> "One Hundred Twenty Three"
    12345 -> "Twelve Thousand Three Hundred Forty Five"
    1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

#### 思路
用递归。难点在于十几的数的表示，12不能是ten two。以及要处理好零：比如10000，如果不加判断，直接会得到ten zero thousand zero zero zero。同样的，由于字符串是不可变的，所有、以在过程都使用列表，最后再join。再如100000不能是one milion thousand 
#### 代码
```python
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """                
        s1 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        s12 = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        s2 = ['Zero','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        s3 = ['','Thousand','Million','Billion']
        if num == 0:
            return 'Zero'
        num = list(str(num))[::-1]
        ans = []        
        
        def parse(s,count,ans):
            if s == []:
                return
            n = int(s[0])
            del s[0]
            parse(s,count+1,ans)
            if count%3 == 2 and n is not 0:
                ans.append(s2[n])
            else :
                if n == 0:
                    if  count in [4,7,11] and  ans[-1] not in s3:
                        ans.append(s3[(count-1)/3])
                    return
                ans.append(s1[n])
                if  count % 3 == 0:
                    ans.append('Hundred')
                elif count%3 == 1:
                    if n is not 0 and len(ans)>1 and ans[-2] =='Ten':
                        del ans[-1]
                        ans[-1] = s12[n]
                    if  count > 1:ans.append(s3[(count-1)/3])
         
        parse(num,1,ans)
        return ' '.join(ans)
        
```

## 2017-9-12
 ![divider](/uploads/divider.png)
 <a id="Insert-Interval"></a>
### [Insert-Interval](https://leetcode.com/problems/insert-interval/description/) --leetcode 57

#### 题目
> Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
>
>You may assume that the intervals were initially sorted according to their start times.
>
>Example 1:
Given intervals `[1,3],[6,9]`, insert and merge `[2,5]` in as `[1,5],[6,9]`.
>
>Example 2:
Given `[1,2],[3,5],[6,7],[8,10],[12,16]`, insert and merge `[4,9] in as [1,2],[3,10],[12,16]`.
>
>This is because the new interval `[4,9]` overlaps with `[3,5],[6,7],[8,10]`.

#### 思路
 理清思路，显然只有4种情况，即newintreval的`start`，`end`分别<mark>在原来的区间</mark>（cross）、 <mark>不在原来区间</mark>（即在两区间之间)，当然，新区间中可能含有若干原来的区间。分类后，为了使原来的第一个和最后一个，与其他区间有同等“地位”，即可以使用同样的代码，我将intervals首尾插入了两个很大的区间。
#### 代码
```python
## class Interval(object):
## def __init__(self, s=0, e=0):
## self.start = s
## self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        MAX=100000000
        first=Interval()
        first.start=first.end=-MAX
        last=Interval
        last.start=last.end=MAX
        intervals.insert(0,first)
        intervals.append(last)
        l = len(intervals)
        for i in  range(l):
            if intervals[i].start>newInterval.start :
                j = i
                isCross = False
                while intervals[j].start<=newInterval.end:
                    if intervals[j].end<newInterval.end:
                        del intervals[j]
                    else:
                        isCross = True
                        break
                if isCross:
                    intervals[j].start=newInterval.start
                else:intervals.insert(j,newInterval)
                break
            else :
                if intervals[i].end >= newInterval.start:
                    if intervals[i].end >= newInterval.end:break
                    j = i+1
                    isCross = False
                    while intervals[j].start<=newInterval.end:
                        if intervals[j].end<newInterval.end :
                            del intervals[j]
                        else:
                            isCross = True
                            break
                    if isCross:
                        intervals[j].start=intervals[i].start
                        del intervals[i]
                    else:intervals[i].end = newInterval.end
                    break
        del intervals[0]
        del intervals[-1]
        return intervals
```

 ![divider](/uploads/divider.png)
 <a id="N-Queens"></a>
### [N-Queens ](https://leetcode.com/problems/n-queens/description/) --leetcode 51
#### 题目
>The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
>
>Given an integer n, return all distinct solutions to the n-queens puzzle.
>
>Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
>
>For example,
There exist two distinct solutions to the 4-queens puzzle:
>
```
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```


#### 思路
 利用递归，依次摆放第i个皇后，注意要求的返回结果是字符串，imutable，不可变，所以先用列表，然后join

#### 代码
```python
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        rst = []
        nums = [0]*n
        def abs(x):
            if x > 0:
                return x
            return -x
        def find(i):
            if i == n:
                tmp = []
                for count,index in enumerate(nums):
                    s = ['.']*n
                    s[index] = 'Q'
                    tmp.append(''.join(s))
                rst.append(tmp)
                return
            
            for j in range(0,n):
                ok = True
                for index,k in zip(range(i),nums):
                    if abs(index-i) == abs(j-k) or k == j:
                            ok = False
                            break
                if not ok:
                    continue
                nums[i] = j
                find(i + 1)

        find(0)
        return rst
```

## 2017-8-31
 ![divider](/uploads/divider.png)
 <a id="八数码"></a>
### 八数码  --[ustc-oj](https://www.ustcoj.com/#/)
#### 题目
>3×3九宫棋盘，放置数码为1-8的8个棋牌，剩下一个空格，只能通过棋牌向空格的移动来改变棋盘的布局。要求：根据给定初始布局，问：至少移动几次才能从初始布局到达目标布局。
>
>目标布局如下：876543210  (九宫格依次从上到下，从左到右)
Input Description
>
>3行，每行3个0-8的不重复整数，其中0表示空格所在的位置，数字间用空格隔开，表示初始布局，数据保证该初始布局一定能移到目标布局。
Output Description
>
>一个整数，表示最少移动到目标布局的次数。
eg 
input:0 7 6 8 4 3 5 2 1
output:4

#### 思路
 这道题是搜索题，而且是广搜，需要一个队列来存放状态，我为了简便，就用的一个数组，容量是所有可能的状态数，即9! = 362800 。为了减少储存量，我将每个状态储存为一个长度为9的字符串，为了能一一映射，可以使用[Cantor(康托展开)](https://zh.wikipedia.org/wiki/%E5%BA%B7%E6%89%98%E5%B1%95%E5%BC%80),注意cantor函数的实现，当前数字的系数是它右边比它小的数字的个数（当然也可以是左边，不过是顺序反过来而已）。
若想提高搜索效率，可以用A*算法，启发式搜索，可以看[这篇文章](http://www.cnblogs.com/luxiaoxun/archive/2012/08/05/2624115.html)里面还用了，双向搜索。
 
#### 代码
```c
#include<stdio.h>
#include<string.h>
#include<malloc.h>
#define ALL 362880

int fac[9]={1,1,2,6,24,120,720,5040,40320};
char flag[ALL];


class node
{
  public:
    int g;    //steps
    int zero;
    char s[9];
    char last;
};
node states[ALL];
node *head = states;
node *tail;

//notice how to get cantor func
int cantor(char *s)
{
    int sum = 1;
    for(int i = 0;i<9;++i){
        int n = 0;
        for(int j= i+1;j < 9 ;++j){
            if(s[j] < s[i]){
                ++ n;
            }
        }
        sum += n * fac[8-i];
    }
    return sum;
}
void init(char *s)
{
    memset(states,0,sizeof(node)*ALL);
    memset(flag,0,sizeof(flag));
    flag[cantor(s)] = 1;
    tail = head+1;
    head -> g = 0;
    head ->last = -1;
    for(int i = 0; i<9;++i){
        if(s[i] == '0'){
            head -> zero = i;
        }
        head->s[i] = s[i];
    }
}

int move()
{
    while(head!=tail){
        node *tmp = head;
        ++head;
        if(cantor(tmp->s) == ALL)
            return tmp -> g;
        flag[cantor(tmp -> s)] = 1;
        int dir[4] = {-3,1,3,-1};
        if(tmp -> last!= -1)
            dir[tmp-> last] = 0;
        if(tmp -> zero < 3) dir[0] = 0;
        if(tmp -> zero > 5) dir[2] = 0;
        if((tmp -> zero) %3 == 0) dir[3] = 0;
        if((tmp -> zero) %3 == 2) dir[1] = 0;
        for(int i = 0; i < 4;++i){
            if(dir[i] != 0){
                *tail = * tmp;
                int p = tail ->zero;
                tail -> zero = p + dir[i];
                tail -> s[p] = tmp -> s[p+dir[i]];
                tail -> s[p+dir[i]] = '0';
                int pn = cantor(tail -> s);
                if(flag[pn] == 0){
                    tail -> g += 1;
                    tail->last = (2+i)%4;  //下一次不能返回,即移动（2+i）%4
                    ++tail;
                    flag[pn] = 1;
                }
            }
        }
    }
}
char readChar()
{
    char c =' ';
    while (c==' ' || c== '\n')
        c=getchar();
    return c;
}
int main(void)
{
   // char s[10] = "876543210";
    char s[9];
    for(int i = 0 ;i<9;++i){
        s[i] = readChar();
    }
    init(s);
    printf("%d\n",move());
    return 0;
}
```

## 2017-8-23
 ![divider](/uploads/divider.png)
 <a id="Nth-digit"></a>
### [Nth-digit](https://leetcode.com/problems/nth-digit/description/) --leetcode 400
#### 题目
>Find the n<sup>th</sup> digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2<sup>31</sup>).
>
>example:
```
Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
```
#### 思路
这道题和前面的<a href="#Roman">Integer to Roman</a> 方法类似，要根据n的范围来划分不同的结构，这里就是一个数字的位数，9 , 90 * 2, 900 * 3,... 找到n在的“区间”，然后即找出这个区间的某个数，这个数的某位（digit）

#### 代码
```python
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        begin = 0 
        num = 0
        while n >= begin:
            begin += 9 * (10 **num) *(num + 1)
            num += 1
        begin  -=  9 * (10**(num-1))*num
        if n == begin :
            return 9
        n -= begin
        tmp  = int((n-1)/ num) + 1 + int("9"*(num -1))  #floor 
        n = (n-1) % num 
        return int(str(tmp)[n])
            
```
 ![divider](/uploads/divider.png)
 <a id="Single-Number"></a>
### [Single-Number](https://leetcode.com/problems/single-number/description/) --leetcode 136
#### 题目
>Given an array of integers, every element appears twice except for one. Find that single one.
>
>Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Question 2: How about every element appearing tree times except for one?
Question 3: 一列数中, 除了两个数只出现一次, 其他数都出现两次, 找出这两个数

#### 思路
如果直接用O(n<sup>2</sup>)会超时，想到用位运算异或XOR(^)就很简单了，几行代码

对于第二个问题, 其他数字出现了三次的数字, 只有一个数字出现了一次

可以用两个数字来记录, 一个记录当前所有数字出现一次的异或值, 第二个记录当前数字出现两次的异或值.

对于第三个问题:
先全部异或一次, 得到的结果, 考察其的某个非 0 位 (比如最高非 0 位), 那么只出现一次的两个数中, 在这个位上一个为 0, 一个为 1, 由此可以将数组中的元素分成两部分, 重新遍历, 求两个异或值



#### 代码
第一问
```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for i in nums:
            num ^= i
        return num
```
第二问:其他数字出现３次, 只有一个出现1次
```python
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once,twice = 0,0
        for i in nums:
            once = ~twice & (once^i)
            twice = ~once &(twice ^i)
        return once
```
第三问
```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        acc = 0
        for i in nums:
            acc ^=i
        n = len(bin(acc))-3
        a,b=0,0
        for i in nums:
            if i>>n&1:
                a^=i
            else:
                b^=i
        return b,a
```
## 2017-8-22
  ![divider](/uploads/divider.png)
 <a id="ZigZag-Conversion"></a>
### [ZigZag-Conversion](https://leetcode.com/problems/zigzag-conversion/description/) --leetcode 6
#### 题目
> The string "asdfghjklqw" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 原题目的例子有点难懂，我就自己举个例子吧   num > =  4
```
a        j 
s     h  k
d   g    l  w
f        q 

return   ajshkdglwfq
```
#### 思路
可以发现，第一行和最后一行，字母依次在s中相差一个周期，而其他行，有两个点开始，同样相差一个周期。


#### 代码
```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rst = ""
        l = len(s)
        if numRows == 1:
            return s
        delta = 2 * numRows -2   #period
        for i in range(numRows):
            index = i
            index2 = delta - i
            while index < l :
                rst += s[index]
                index += delta
                if 0 < i < numRows - 1 and index2 < l:
                    rst += s[index2]
                    index2 += delta
        return rst
```

## 2017-8-20
  ![divider](/uploads/divider.png)
 <a id="Roman"></a>
### [Integer to Roman](https://leetcode.com/problems/integer-to-roman/description/) --leetcode 13 
#### 题目 
 Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
[罗马数字](https://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97#.E6.8B.BC.E5.AF.AB.E8.A6.8F.E5.89.87)的规则如下：
>罗马数字共有7个，即Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）。按照下述的规则可以表示任意正整数。需要注意的是罗马数字中没有“0”，与进位制无关。一般认为罗马数字只用来记数，而不作演算。
>
>1. **重复数次**：一个罗马数字重复几次，就表示这个数的几倍。
>2. **右加左减**：
    * 在较大的罗马数字的右边记上较小的罗马数字，表示大数字加小数字。
    * 在较大的罗马数字的左边记上较小的罗马数字，表示大数字减小数字。
    * 左减的数字有限制，仅限于I、X、C。比如45不可以写成VL，只能是XLV
    * 左减时不可跨越一个位值。比如，99不可以用IC（ {\displaystyle 100-1} 100-1）表示，而是用XCIX（ {\displaystyle [100-10]+[10-1]} [100-10]+[10-1]）表示。（等同于阿拉伯数字每位数字分别表示。）
    * 左减数字必须为一位，比如8写成VIII，而非IIX。
    * 右加数字不可连续超过三位，比如14写成XIV，而非XIIII。（见下方“数码限制”一项。）
>3. **加线乘千**：
    在罗马数字的上方加上一条横线或者加上下标的Ⅿ，表示将这个数乘以1000，即是原数的1000倍。
同理，如果上方有两条横线，即是原数的1000000（ {\displaystyle 1000^{2} } 1000^{2}）倍。
>4. **数码限制**：
    同一数码最多只能连续出现三次，如40不可表示为XXXX，而要表示为XL。
例外：由于IV是古罗马神话主神朱庇特（即IVPITER，古罗马字母里没有J和U）的首字，因此有时用IIII代替IV。

#### 思路
这道题还是蛮有意思的，同样用递归的方法，在了解拼写规则后，要从数值范围来判断罗马数字的结构，即取哪个字母？哪种组合？左或是右？
孪生题是[Roman to Interger](https://leetcode.com/problems/roman-to-integer/description/)比较简单
#### 代码 
```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {0:'',1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        ks = [1,5,10,50,100,500,1000]
        
        def convert(num):
            if num in dic.keys():
                return dic[num]
            if num > 1000:
                n = int(num/1000)
                num -= n * 1000
                return  'M'*n + convert(num)
            n = 1000
            for i in ks:
                if i > num :
                    n = i
                    break
            exp = 1
            flag = False
            while exp <= n:   # judge if n is 10 exp k
                if exp == n:
                    flag = True
                    break
                exp *= 10
            if flag:
                small = n / 10
                if num >= 9 * small:
                    return dic[small] + dic[n] + convert(small -(n-num)) 
                else:
                    return dic[n/2] + convert(num - n/2)
            else:
                small = n / 5
                if n - small <= num :
                    return dic[small] + dic[n] + convert(small - (n-num))
                else:
                    n2 = int(num / small)
                    num -= n2 * small
                    return dic[small] * n2 + convert(num)
        return convert(num)             
```
![divider](/uploads/divider.png)
<a id="word-search"></a>
### [word-search](https://leetcode.com/problems/word-search/description/) --leetcode 79
#### 题目 
>Given a 2D board and a word, find if the word exists in the grid.
>
>The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
>
```
For example,
Given board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
```
#### 思路
这道题可以用递归函数来解决，注意到，eg从“a” 中判断是否有“aa” ，如果直接递归是返回true的，这不对，要就是说在一次判断中，已判断过的字母不能再判断，所以参数应该还有一个board，记录当前的字母状态，考虑到python是用的引用，传递参数时没有复制，我又不想额外再去复制board，就在函数中记下当前位置的字母，在函数调用结束再改回来的。哈哈！
#### 代码 
```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        num = len(word)
        def find(r,c,n):
            if n == num-1 and board[r][c] == word[n]:
                return True
            if board[r][c] != word[n] or n == num-1:
                return  False
            tmp = board[r][c]    #save  the  val
            board[r][c] = 0
            if r < row-1 and find(r+1,c,n+1):
                return True
            if r > 0 and find(r-1,c,n+1):
                return True
            if c <col-1 and find(r,1+c,n+1):
                return True
            if c > 0 and find(r,c-1,n+1):
                return True
            board[r][c] = tmp
            return False
        for i in range(row):
            for j in range(col):
                if find(i,j,0):
                    return True
        return False
```
## 2017-8-19
![divider](/uploads/divider.png)

<a id="3Sum"></a>
### [3Sum](https://leetcode.com/problems/3sum/description/)  --leetcode 15
#### 题目    
>Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
>Note: The solution set must not contain duplicate triplets.
```
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

#### 思路
最开始我想的就直接3重循环，再加判重的循环，暴力求解，当然超时了，要高于O(n<sup>3</sup>)。后来想到可以将正负数，0，分成三组来组合，然而最后两个数据过不了，在网上搜了一下，可以固定一个数，头尾双指针来移动，这是O(n<sup>2</sup>)。哎，折腾了一晚上，我好菜啊

#### 代码
分成正负0三组，写了很多判断语句，唉，庸俗的代码。
```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        rst = []
        zero = []   #zeros
        neg = []    #negative
        pos = []    #positive
        for i in (nums):
            if i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)
            else:
                zero.append(i)
        if len(zero) > 2:
            rst.append([0,0,0])
        if neg == []  or  pos == []:
            return rst
        if zero != []:
            if len(neg) > len(pos):
                for i in pos:
                    if -i in neg:
                        rst.append([-i,0,i])
            else:
                for i in neg:
                    if -i in pos:
                        rst.append([i,0,-i])
        pos.sort()
        neg.sort()
        if len(pos) == 1 and len(neg) == 1:
            return rst
        elif len(pos) == 1 :
            tmp = len(neg) - 1
            while tmp > 0:
                sum = neg[tmp] + neg[tmp-1]
                if sum == - pos[0]:
                    rst.append([neg[tmp-1],neg[tmp],pos[0]])
                    break
                elif sum < - pos[0]:
                    break
                tmp -= 1
        elif len(neg) == 1:
            tmp = 0
            while tmp < len(pos) - 1 :
                sum = pos[tmp] + pos[tmp+1]
                if sum == - neg[0]:
                    rst.append([neg[0],pos[tmp],pos[tmp+1]])
                    break
                elif sum > - neg[0]:
                    break
                tmp -= 1
        sameI = []     #avoid test several same num
        for i in range(len(pos)-1):
            if i in sameI:
                continue
            sameI.append(i)
            sameJ=[]
            for j in range(i+1,len(pos)):
                if j in sameJ:
                    continue
                sameJ.append(j)
                sum = pos[i] + pos[j]
                for k in neg:
                    if   sum > -k:
                        break
                    elif sum == -k:
                        rst.append([k,pos[i],pos[j]])
        sameI = []
        for i in range(len(neg)-1):
            if i in sameI:
                continue
            sameI.append(i)
            sameJ=[]
            for j in range(i+1,len(neg)):
                if j in sameJ:
                    continue
                sameJ.append(j)
                sum = neg[i] + neg[j]
                for k in pos:
                    if   sum > -k:
                        break
                    elif sum == -k:
                        rst.append([neg[i],neg[j],k])
        fnl = []   
        for i in rst:
            if i not in fnl:
                fnl.append(i)
        return fnl 
```
#### 代码
头尾双指针，过了，注意判重的方法，前一个用的if，后面在找到答案时用while
```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            head = i+1
            tail = len(nums) - 1
            while head < tail:
                if nums[i] + nums[head] + nums[tail]  == 0:
                    rst.append([nums[i],nums[head],nums[tail]])
                    head += 1
                    tail -= 1
                    while head< tail and nums[head] == nums[head -1]:
                        head += 1
                    while head<tail and  tail < len(nums)-1 and nums[tail]== nums[tail +1]:
                        tail -= 1
                elif nums[i] + nums[head] + nums[tail]  < 0:
                    head += 1
                else:
                    tail -= 1
        return rst
```

## 2017-8-17

![divider](/uploads/divider.png)
<a id="jump-game"></a>
### [jump-game](https://leetcode.com/problems/jump-game/description/)  --leetcode 55
    
#### 题目    <br>
>Given an array of non-negative integers, you are initially positioned at the first index of the array.
>Each element in the array represents your maximum jump length at that position.
> Determine if you are able to reach the last index.  

>For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.      

#### 思路
由于只有非负数，不能成功的点一定是当前位置为0，所以可以将列表中所以的0找出来，并记下位置（下标），然后从这个位置开始往前搜索，若存在能跳过此位置的点，则能跳过，去除这个0，一直跳过所有0

<br>

#### 代码  
   
```python
    class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True
        zeros = []
        for i,j in enumerate(nums):
            if j == 0:
                zeros.append(i)
        while zeros != []:
            i = zeros[0]
            tmp = i - 1
            flag = 0
            while tmp >= 0:
                if nums[tmp] > i-tmp  or nums[tmp]+tmp+1 >=len(nums):
                    flag = 1
                    break
                tmp -= 1
            if flag == 0 :
                return False
            del zeros[0]
            
        return True
```
![divider](/uploads/divider.png)

<a id="super-pow"></a>
### [super-pow](https://leetcode.com/problems/super-pow/description/)  --leetcode 372
#### 题目

>Your task is to calculate a<sup>b</sup> mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.  
    
>Example1:
 a = 2
b = [3]
 Result: 8   

>Example2:
a = 2
b = [1,0]
Result: 1024


#### 思路
这道题显然不能直接计算，可以用欧拉定理
对任意正整数a,正整数m,(a,m) = 1,&fnof;(m) 为比m小的与m互质的(注意不一定是质数)正整数的个数，
则 a<sup>&fnof;(m)</sup> &equiv; 1 (mod m) 。
再利用性质： a &equiv; b (mod m) ,c &equiv; d (mod m) ,则ac &equiv; bd (mod m)  
证明就不写了，打数学符号太累了（T<sub>^</sub>T）,给个传送门吧--> [欧拉定理](https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%AE%9A%E7%90%86_(%E6%95%B0%E8%AE%BA))

    
#### 代码  
  
```python
    class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        m = 1337
        if a % m == 0:
            return 0
        sum = 0
        for i in b:
            sum = 10 * sum + i    
        phi = 0
        for i in range(1,m):
            if (i % 7 != 0) and (i % 191 != 0):
                phi += 1
        sum = sum % phi
        return (a**sum) % 1337
# if m a prime num ,use the small law of Fermat
# else use the law of Euler
    
```
