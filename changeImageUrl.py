import os
import re
from requests import get
from functools import partial
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', help='input directory', default='.')
parser.add_argument(
    '-o', '--output', help='output directory', default='images')
parser.add_argument('-g', '--get', help='get image from web', action='store_true')

PREFIX = 'https://raw.githubusercontent.com/mbinary/mbinary.github.io/hexo/source/images'
parser.add_argument('-p', '--prefix', help='set image prefix', default=PREFIX)

args = parser.parse_args()

INPUT = args.input
OUTPUT = args.output
ISGET = args.get
PRE = args.prefix

if not os.path.exists(OUTPUT):
    os.mkdir(OUTPUT)


IMAGE_PATTERN = re.compile(r'\!\[(.*?)\]\((.*?)\)')


def changeImageUrl(file_path):
    def sub_save_image(match, filename='image'):
        nonlocal dic
        s = match.group(1)
        url = match.group(2)
        if s == '':
            p = filename.rfind('.')
            if p != -1:
                filename = filename[:p]
            if filename in dic:
                dic[filename] += 1
            else:
                dic[filename] = 1
            s = f'{filename}-{dic[filename]}'
        new_path = os.path.join(OUTPUT, s+'.png')
        if (not os.path.exists(new_path)) and url.startswith('http'):
            with open(new_path, 'wb') as f:
                f.write(get(url).content)
        return f'![{s}]({new_path})'

    def sub_set_url(match, pre=PRE):
        name = match.group(1)
        url = match.group(2)
        filename = os.path.basename(url)
        return f'![{name}]({os.path.join(pre,filename)})'

    dic = {}
    s = ''
    try:
        with open(file_path) as fp:
            s = fp.read()
        if ISGET:
            name = os.path.basename(file_path)
            s = re.sub(IMAGE_PATTERN, partial(
                sub_save_image, filename=name), s)
        else:
            s = re.sub(IMAGE_PATTERN, sub_set_url, s)
        with open(file_path, 'w') as fp:
            fp.write(s)
    except Exception as e:
        print(e)
        print(file_path)


if __name__ == '__main__':
    files = []
    if os.path.isdir(INPUT):
        files = [os.path.join(INPUT, i) for i in os.listdir(INPUT)]
    else:
        files = [INPUT]
    for f in files:
        if f.endswith('.md'):
            changeImageUrl(f)
