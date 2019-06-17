---
title: 『WEB』从网易云音乐缓存文件得到MP3
date: 2018-1-27
categories: 
		- web
tags: [爬虫,python,api]
keywords: 网易云音乐,爬虫,解密,python,正则表达式,mutagen,文件
---


最近想获取几首好听的网易云音乐文件，但是不是会员，只有缓存文件，而且经过加工了的。
以前获取过某k歌的缓存文件，直接修改后缀名就行了，但是网易云音乐不行，sigh
<!-- more -->

下面开始探索网易云音乐之旅:D
<!-- TOC -->

- [解密缓存文件](#解密缓存文件)
- [获得歌曲信息](#获得歌曲信息)
- [获取歌词](#获取歌词)
    - [lyric文件](#lyric文件)
    - [利用API获取歌词](#利用api获取歌词)
- [成果](#成果)
    - [完整代码](#完整代码)
- [感想](#感想)
- [注意](#注意)
- [And finally](#and-finally)

<!-- /TOC -->


<a id="markdown-解密缓存文件" name="解密缓存文件"></a>
# 解密缓存文件

在手机上的缓存文件在 `netease/cloudmusic/Cache/Music1`里
观察可以发现，歌曲缓存文件包括两个，一个是index文件.idx!，另一个是歌曲文件，index文件和歌词文件(歌曲id命名)都是txt文件，可以直接打开，而歌曲文件.uc!打开错误。缓存文件是修改过的。


进一步地，缓存文件和源文件大小一样大，所以没有经过压缩，最简单的想法是异或运算，这样最简单，加密，解密一样的操作。逐个尝试，发现每字节和0xa3异或即可，得到正确的文件，可以播放，哈哈 :smiley: 下面是代码，注意用bytearray修改bytes

```python    
with open (fileName,'rb') as f:
    btay = bytearray(f.read())
with open(newFile,'wb') as out:
    for i,j in enumerate(btay):
        btay[i] = j ^ 0xa3
    out.write(bytes(btay))
```

<a id="markdown-获得歌曲信息" name="获得歌曲信息"></a>
# 获得歌曲信息
为了给歌曲文件正确命名，我想获得歌曲题目和歌手信息。虽然.idx!索引文件包含一些属性，但是没有歌曲标题和歌手，不过重要的是musicId，这是歌曲的唯一标识。然后发现.idx!  .uc!文件都是以id开头的，且歌词文件是id命名的。

可以用这个 api 来获取信息
`https://api.imjad.cn/cloudmusic/?type=detail&id=1234132`

还有另一种方法，mp3等文件格式有一些metadata (元素据)，mp3文件的 id3 tag里面就包含标题，歌手。这是[wiki的介绍](https://en.wikipedia.org/wiki/MP3)

![mp3](https://raw.githubusercontent.com/mbinary/mbinary.github.io/hexo/source/images/mp3.png)

然后找python模块，网上说eyeD3比较好用，但是我安装好后提示libmagic找不到，搜索问题未能解决（如果你有解决办法，请告诉我，十分感谢）， 然后用的mutagen模块，这个模块能操作很多格式的文件.

<a id="markdown-获取歌词" name="获取歌词"></a>
# 获取歌词
有两种方法
<a id="markdown-lyric文件" name="lyric文件"></a>
## lyric文件
这是歌词文件内容

![file](https://raw.githubusercontent.com/mbinary/mbinary.github.io/hexo/source/images/file.png)

从这个文件中读取。 解析这个文件，由于没有统一的键,所以可以用正则表达式`r'(lyric|lrc|klyric|kalaokLyric|tlyric)\s*[\'\"]:\s*[\'\"]\s*\[')
`来检查是否有歌词内容
```python
# self.hasLrcPt= re.compile(r'(lyric|lrc|klyric|kalaokLyric|tlyric)\s*[\'\"]:\s*[\'\"]\s*\[')
# self.lrcKey = 'lyric|lrc|klyric|kalaokLyric|tlyric'.split('|')

def noLrc(self,s):
        '''judge if a dict or a string  has lyrics'''
        if isinstance(s,str):
            return self.hasLrcPt.search(s) is  None
        else:
            return not  reduce(or_,[i in s and s[i]!='' for i in self.lrcKey]) 
```

检查到有歌词后，可以发现每句是这样的

`[0:09.000]平安夜，亵渎的夜晚\n`

最开始用的`r'\[\d+,\d+\](\(\d+,\d+\)(\w))+\n')`，然而总是匹配不到，在交互模式又匹配得很精确，在这里浪费了很多时间，最后发现是`\n`的问题，在正则表达式中要用`\\n`,作为字符串在交互模式下打印出来只显示了`\n`， :weary: ， 心累   ，改为`r'\[\d+:\d+\.\d+\](.*?)\\n'`.

<a id="markdown-利用api获取歌词" name="利用api获取歌词"></a>
## 利用API获取歌词
利用上面的 api , 传递 lyric 参数即可



注意由于是缓存文件，有极少的音乐可能id3 tag以及 api 都没有信息，对于这些，我直接用的id命名

<a id="markdown-成果" name="成果"></a>
# 成果
* 展示


![display](https://raw.githubusercontent.com/mbinary/mbinary.github.io/hexo/source/images/display.gif)


<a id="markdown-完整代码" name="完整代码"></a>
## 完整代码
[github](https://github.com/mbinary/netease-music-cracker.git)

<a id="markdown-感想" name="感想"></a>
# 感想
:flushed: (羞涩
有时看书有点没有耐心，想实践，然而如果没有掌握好知识，实践的话就会踩很多坑，甚至可能还爬不起来有些坑。 还差得远呢，还得加油哦！

<a id="markdown-注意" name="注意"></a>
# 注意
* 有极少数的缓存文件 在 api 中没有信息, 在 id3 tag 中也没有, 这些歌曲我用的 id 来命令
* 最新更新都在github上, 博客很少更新, 所以使用前最好去读一下 github 的 readme

<a id="markdown-and-finally" name="and-finally"></a>
# And finally
```
 mmmmmm mmmmm  mmmmm        m     m   mm   mmmmm  mm   m mmmmm  mm   m   mmm
 #      #    #   #          #  #  #   ##   #   "# #"m  #   #    #"m  # m"   "
 #mmmmm #mmmm"   #          " #"# #  #  #  #mmmm" # #m #   #    # #m # #   mm
 #      #    #   #           ## ##"  #mm#  #   "m #  # #   #    #  # # #    #
 #      #mmmm" mm#mm         #   #  #    # #    " #   ## mm#mm  #   ##  "mmm"


< 请尊重版权，此文章以及代码仅供学习交流之用 >
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
```
