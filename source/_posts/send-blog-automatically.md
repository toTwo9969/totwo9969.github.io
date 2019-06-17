---
title: 『WEB』用 python 发送 csdn 博客
date: 2018-4-5
categories: web
tags: [python,web]
keywords:
description:
---


我有个基于 github pages 的[博客](https://mbinary.github.io), 又在很多其他网站上发博客。比如 [csdn](https://blog.csdn.net/marvellousbinary/) . 为了避免重复操作，想用程序实现自动发博客。
今天上午就试了一下 csdn 这个网站
<!-- more -->

# 方法一 -- 用 api 来发送博客
进入[开发者文档](http://open.csdn.net/wiki/api/blog/savearticle), 注册开发者，使用文档中的方式获得 access_token 来获取授权, 然后就可以 post 了，比如[这篇文章](https://blog.csdn.net/marvellousbinary/article/details/79832542),

# 方法二 -- 模拟登陆
用 python 来模拟登陆，为了简单，可以使用 cookies 来利用浏览器的会话 cookie 登陆

## 保存 cookie
用 chrome, 点击进入发文章的页面，F12-> network -> 选择 mdeditor.html -> header
就可以看到 cookie, 保存下来，等会在 python 脚本中使用

## 抓包
寻找 post, 提交内容的网址，我最开始一直以为是`https://mp.csdn.net/mdeditor/`, 返回的页面是成功的
但是刷新博客页面，并没有发表文章， 后来用 fiddler 抓包才找到正确的网址

![post](https://raw.githubusercontent.com/mbinary/mbinary.github.io/hexo/source/images/post.png)


## 元数据
然后构造发表的文章的元数据，在 fiddler 中可以发现

![form](https://raw.githubusercontent.com/mbinary/mbinary.github.io/hexo/source/images/form.png)
就是这样的一个字典，

```python
data = {"title":"do you know my name?",
             "markdowncontent":'# emm',
             "content": '''<h1>hello, world~</h1>''',
             "categories":"默认分类",
             "channel":33,
             "tags":"python",
            'type':'original',
             "artideedittype":1,
             "private":0,
             "status":0
             #"id":     修改已有文章
             }
```

那个 channel 就是要发表到的栏目，可以在网页右键审查元素发现各个值的含义

## 发表
最后就可以发送了，第一次失败, 显示的是 unicode,, 应该打印 json 就行，然后知道是标题不能为空，添加标题就可以了

尝试了多次，都成功了，返回的 json.


由于不支持 markdown, 我又下载安装了 python markdown 模块，可以转成 html,
这样使用
```python
def md2html(s):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
            <html lang="zh-cn">
            <head>
            <meta content="text/html; charset=utf-8" http-equiv="content-type" />
            </head>
            <body>
            {mdstr}
            </body>
            </html>
           '''

    mdstr = markdown.markdown(s,extensions=exts)
    return html.format(mdstr = mdstr)

```

当我沉浸在成功的喜悦中时，准备发一系列文章时，才知道 csdn 每天限制发 10 篇 QAQ


以下配置文件，最新完整的代码见 [github](https://github.com/mbinary/blog-sender), 欢迎 star, 如果想添加其他功能，欢迎 fork & PR
```python
#coding: utf-8
'''************************************************************************
    > File Name: config.py
    > Author: mbinary
    > Mail: zhuheqin1@gmail.com
    > Created Time: Fri 06 Apr 2018 11:06:16 AM DST
 ************************************************************************'''

# python 变量 配置参数


# 两者二选一
# CSDN_AUTH_DATA 在 使用 api  需要在 http://open.csdn.net/wiki/api/ 注册开发者，得到 cliet_id 和 client_secret
# CSDN_COOKIE 在发博客页面获取 cookie,
CSDN_AUTH_DATA = {'client_id' :'1100668',
               'client_secret': '********************************',
               'grant_type': 'password',
               'username': 'marvellousbinary',
               'password': 'R**********'
                }

CSDN_COOKIE = '''

              '''

# markdown 语法，需 pip install markdown
MDON  = True

# xdefault configuration


DEFAULT_DATA = {
             "title":"do you know my name?",
             "content": '''<h1>hello, world~</h1>''',
             "categories":"默认分类",
             "channel":33,
             "tags":"python,tag2",
             }

'''
channel  各个值的含义
1: 移动开发
2: 云计算大数据
3: 研发管理
6: 数据库
12: 运维
14: 前端
15: 架构
16: 编程语言
28: 人工智能
29: 物联网
30: 游戏开发
31: 后端
32: 安全
33: 程序人生
34: 区块链
35: 音视频开发
36: 资讯
37: 计算机理论与基础
'''
```
