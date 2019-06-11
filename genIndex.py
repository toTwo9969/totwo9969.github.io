import os
import re

FOLDER = './source/_posts'

TITLE = re.compile(r'title: +(.*?)\n')

DATE = re.compile(r'date: +(\d{4})-(\d{1,2})-(\d{1,2})')

PRE = 'https://github.com/mbinary/mbinary.github.io/tree/hexo/source/_posts/'
BLOG = 'https://mbinary.github.io/'


def parseHeader(path):
    cont = open(path).read()
    date = title = ''

    m = TITLE.search(cont)
    if m:
        title = m.group(1)
    else:
        name = os.path.basename(path)
        title = name.rstrip('.md')

    match = DATE.search(cont)
    if match:
        y,m,d = match.groups()
        if len(m)<2:
            m = '0'+m
        if len(d)<2:
            d = '0'+d
        date = f'{y}-{m}-{d}'

    return title, date


def genIndex(folder=FOLDER):
    names = os.listdir(folder)
    li = []
    for name in names:
        title, date = parseHeader(os.path.join(folder, name))
        title = re.sub(r'[\(\[]', '{', title)
        title = re.sub(r'[\)\]]', '}', title)
        title = re.sub(r'[\*]', '-', title)
        li.append((date, title, name))
    li.sort(reverse=True)
    return '\n'.join(
                     f'- {date}: {title}--[GitHub 网页]({PRE+name}),[博客网页]({BLOG+name})' for date, title, name in li)


if __name__ == '__main__':
    with open('README.md', 'w') as f:
        cont = ''
        with open('README.md.tpl') as f2:
            cont = f2.read()
        f.write(cont.format(index=genIndex()))
