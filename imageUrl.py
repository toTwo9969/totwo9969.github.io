import os
import re
from requests import get
from functools import partial
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('-d', '--dir', help='input directory', default='.')
parser.add_argument('-p', '--path', help='image pre path', default='images')

args = parser.parse_args()

PATH = args.path
DIR = args.dir

PT = re.compile(r'\!\[(.*?)\]\((.*?)\)')

if not os.path.exists(PATH):
    os.mkdir(PATH)

dic = {}


def getName(s, filetype=''):
    p = s.find('.'+filetype)
    if p != -1:
        s = s[:p]
    return s


def subFunc(match, filename='image'):
    s = match.group(1)
    url = match.group(2)
    s = getName(s, 'png')
    if not url.startswith('http'):
        url = getName(url, 'png')
    if s == '':
        p = filename.rfind('.')
        if p != -1:
            filename = filename[:p]
        if filename in dic:
            dic[filename] += 1
        else:
            dic[filename] = 1
        s = f'{filename}-{dic[filename]}'
    if filename.startswith('dead'):
        s = 'd'+s
    if filename.startswith('decrypt'):
        s = 'd'+s
    if filename.startswith('multi'):
        print(filename,s)
        s = 'm'+s
    new_path = os.path.join(PATH, s+'.png')
    if (not os.path.exists(new_path)) and url.startswith('http'):
        with open(new_path, 'wb') as f:
            f.write(get(url).content)
    return f'![{s}]({new_path})'


def changeImageUrl(file_path):
    s = ''
    try:
        with open(file_path) as fp:
            s = fp.read()
        s = re.sub(PT, partial(subFunc, filename=os.path.basename(file_path)), s)
        with open(file_path, 'w') as fp:
            fp.write(s)
    except Exception as e:
        print(e)
        print(file_path)


if __name__ == '__main__':
    files = []
    if os.path.isdir(DIR):
        files = os.listdir(DIR)
        files = [os.path.join(DIR, i) for i in files]
    else:
        files = [DIR]
    for f in files:
        if f.endswith('.md'):
            changeImageUrl(f)
