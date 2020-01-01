---
title: WSL 中的 VIM 与 Windwos 剪切板通信
date: 2019-05-28  13:52
categories: linux
tags: [vim,操作系统]
keywords:  
mathjax: false
description: 
    WSL(Windows Subsystem for Linux)真香，然而还是存在一些瑕疵。比如 WSL不是使用的系统剪切板,与系统剪切板通信，进行复制粘贴，是一个很棘手的问题。本文谈谈解决这个问题的一些方法。
---


<!-- vim-markdown-toc GFM -->

* [前言](#前言)
* [说明](#说明)
* [复制](#复制)
    * [寄存器](#寄存器)
    * [新建文件](#新建文件)
    * [write命令](#write命令)
* [粘贴](#粘贴)
    * [pastetoggle](#pastetoggle)
    * [windows paste 程序](#windows-paste-程序)
* [参考](#参考)

<!-- vim-markdown-toc -->
## 前言
WSL 使用的不是系统剪切板,与系统剪切板通信，进行复制粘贴，是一个很棘手的问题。

问题:
- `vim --version | grep clipboard` 没有 加号（系统）寄存器， 重新编译 vim（开启 featured)太麻烦
- 用 ctrl+shift+c/v 进行复制粘贴,然而在粘贴 python 代码以及 vim 安装 indentpython 插件时，粘贴得到的代码缩进会出现错误。

我尝试了很多种方法，从操作的**舒适程度**，以及实现效果来得到最终最优的解决方法： 通过运行 windows 的 `paste.exe`, `clip.exe`程序进行复制粘贴


## 说明
环境如下
- Windows 10: 1709
- WSL: Ubuntu 1904


>说明
- `<c-r>` 代表组合键 `ctrl`+`r` 
- `<cr>` 代表回车键
- `<f1>` 可以从 1到12， 代表`F1`
- `^J` 代表换行的控制字符，而不是`^`,`J`的连接，在 linux 上 换行为 `^@`, 
在 VIM 输入控制字符，比如`^M`，需要按下`<c-r><c-m>`

## 复制
从 VIM 中 复制文本到 Windoes 剪切板。
### 寄存器
通过 VIM 寄存器实现： 将 visual 模式下选中的文本复制到 vim 寄存器，然后将寄存器内容通过 shell 处理进入到剪切板。

首先选中（在 visual 模式下），用`"ay`将内容保存到 `a`寄存器，然后在命令行模式下 `!echo <c-r>a \| /mnt/c/Windows/System32/clip.exe `(执行 shell 命令。  a 寄存器的内容直接 作为参数文本传递（命令行模式下, <c-r>再接寄存器名字，可以将寄存器内容拷贝过来)

然而拷贝的文本很可能不能直接在shell 下作为参数，有特殊字符，比如`"`,`$`等等。
所以要进行转义，用 vim 的 `escape`函数 （我试了`shellescape`, 效果不怎么好）

把上面的操作映射到按键下， 我映射的是 `;y`, 就得到如下的 vim 键盘映射
在 visual 模式下选中，依次按下 `;y`即可复制

`vmap ;y  "ay: let @a="'".escape(@a,"\\'\"")."'" <cr>:!echo <c-r>a \|"/mnt/c/Windows/System32/clip.exe"<cr>`

然而在复制多行时,寄存器中会包含换行控制字符`^J`或`^@`,`^M`，这在传递到shell 中时执行会截断这个参数（在参数还没有输入完全按下 enter 回车),所以有时不会成功。
而且有些字符 escape 也很难转换为 shell 的原文本参数

所以，这个方法行不通

### 新建文件
由于寄存器难以传到 shell 作为参数， 我就想到可以把寄存器的内容复制到一个新的 文件 buffer 中， 然后将文件内容拷贝到剪切板，然后删除文件。
如下，每个 `<cr>` 分隔开 两条 命令，


在 visual 模式下选中，依次按下 `;y`即可复制

`vmap ;y "ay: vs vim-copy<cr>"aP:wq<cr>:call system("/mnt/c/Windows/System32/clip.exe < vim-copy && rm vim-copy")<cr><cr>`

各部分解释如下
- `"ay`: 复制选中区域到 `a`寄存器
- `vs vim-copy`: 新建文件 `vim-copy`到新窗口
- `"aP:wq`: 拷贝 `a` 内容到 文件并保存退出
- `call system("...")`: 执行 shell 命令， shell 命令的内容就是复制 文件内容到剪切板，再删除文件

这个办法可以很好地复制， 唯一的缺点就是打开新buffer 窗口，再关闭，屏幕画面变化大，看着不舒服:astonished:

### write命令
write 命令缩写为 w， 直接使用就是 保存缓冲区

他后面可以接shell 命令与 shell 交互

如
`:w !echo`

这是对于整个文件，也可以选择一部分， 
而进入 visual 模式下选中，再按下`:`， 则进入命令行且将选择的位置也输入进命令行
这是可以 直接 传递给 `clip.exe` 程序。 执行后，选中的部分备剪切掉了，可以按 `u`恢复


在 visual 模式下选中，依次按下 `;y`即可复制
`vmap ;y : !/mnt/c/Windows/System32/clip.exe<cr>u''`
这也是最优的方法了，如果你有更好的方法，欢迎赐教。

## 粘贴
从 Windows 剪切板 粘贴到 VIM
### pastetoggle
如果 VIM 没有设置`set mouse=a`, 那么可以直接右击粘贴，设置了之后要按住 `shift`再右击粘贴

然而这样存在问题，就是 vim 设置了autoindent,它会错误的将粘贴进的文本进行缩进， 而不是粘贴原文。

这个办法可以 `set paste`， `set nopaste`解决，设置了`paste` 后，就可以原文粘贴，

而这样输入命令切换很麻烦， 可以`set pastetoggle=<f12>`，或者其他按键，这样按一次就可以切换 paste 状态。


这样比平常的 paste 动作 要多一个`pastetoggle` 操作，所以不好

### windows paste 程序
在 了解到上面 复制时使用的 `clip.exe`程序，我就在想是不是 windows 有也专门`paste`的程序 （这个程序是和 cmd 交互的，加之， wsl 也可以执行 `exe`程序)

很遗憾，windows 没有

但是令人高兴的是，一个网站上有，[点击这里下载](https://www.c3scripts.com/tutorials/msdos/paste.zip), 然后解压放到 `C:Windows/System32`目录下
使用 vim 的 read 命令进行与 shell 的交互， 即将 shell命令执行的输出 读到当前 buffer

映射如下

在任何模式下按下 `;p` 即可粘贴
```
map ;p :read !/mnt/c/Windows/System32/paste.exe <cr>
map! ;p <esc>:read !/mnt/c/Windows/System32/paste.exe <cr>
```
这个是在新行开始粘贴, 如果在行内粘贴，粘贴的内容在一行内，可以按下`i<bs><esc>l`执行退格操作（同样可以映射一下）

综上所述，最终解决方案为:
[点击这里下载](https://www.c3scripts.com/tutorials/msdos/paste.zip), 然后解压放到 `C:Windows\System32`目录下

再在 `.vimrc`文件中增加如下映射
```
vmap ;y : !/mnt/c/Windows/System32/clip.exe<cr>u''
map ;p :read !/mnt/c/Windows/System32/paste.exe <cr>
map! ;p <esc>:read !/mnt/c/Windows/System32/paste.exe <cr>
```

WSL 真香，强烈推荐入坑 :grimacing:
还想起一个 瑕疵， WSL 不支持32 位的程序， 不过可以安装  qemu 等解决。

另外 windows terminal 在今年 6月中旬也会来到，值得期待。


## 参考
- [MS-DOS-Tutorial](https://www.c3scripts.com/tutorials/msdos/paste.html)
- [vim-doc-zh-CN](http://vimcdoc.sourceforge.net/doc/eval.html#functions)
- [shell转义，单引号，双引号，反撇号](https://www.cnblogs.com/mydomain/archive/2011/10/15/2213017.html)
