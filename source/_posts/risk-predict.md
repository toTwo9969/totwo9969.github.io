---
title: 信用卡持卡人风险预测
comments: true
tags: [机器学习]
date: 2018-05-27 15:37:46
categories: 机器学习
description: "在实验楼参加的一个小比赛"
keywords: 机器学习,人工智能,实验楼
---


<!-- TOC -->

- [题目](#题目)
    - [介绍](#介绍)
    - [目标](#目标)
    - [要求](#要求)
    - [提示](#提示)
    - [知识点](#知识点)
- [分析与解答](#分析与解答)
    - [模型选择](#模型选择)
    - [读取数据](#读取数据)
    - [非数值特征处理](#非数值特征处理)
    - [拟合预测](#拟合预测)
    - [保存数据](#保存数据)
- [总结与反思](#总结与反思)
- [代码](#代码)
- [参考资料](#参考资料)

<!-- /TOC -->

<!-- vim-markdown-toc -->
参加实验楼的[楼赛21期](https://www.shiyanlou.com/contests/lou21/challenges),关于机器学习的, 我以前没怎么接触过,所以是临时在网上查找资料解答的. 如果有一些错误或者是不完善的地方,欢迎指出.

<a id="markdown-题目" name="题目"></a>
# 题目

<a id="markdown-介绍" name="介绍"></a>
## 介绍

题目提供一个来自某银行的真实数据集，数据集前 10 行预览如下：

![](http://upload-images.jianshu.io/upload_images/7130568-1620a00dc4997329.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

其中：

*   第 1～6 列为客户近期历史账单信息。
*   第 7 列为该客户年龄。
*   第 8 列为该客户性别。（Female, Male）
*   第 9 列为该客户教育程度。（Graduate School, University, High School, Others)
*   第 10 列为该客户婚姻状况。（Married, Single, Others）
*   第 11 列为客户持卡风险状况 。（LOW, HIGH）


此外：

*   训练数据集 `credit_risk_train.csv` 总共有 20000 条数据。
*   测试数据集 `credit_risk_test.csv` 总共有 5000 条数据。


下载：

```
wget http://labfile.oss.aliyuncs.com/courses/1109/credit_risk_train.csv
wget http://labfile.oss.aliyuncs.com/courses/1109/credit_risk_test.csv

```

<a id="markdown-目标" name="目标"></a>
## 目标

你需要使用训练数据集构建机器学习分类预测模型，并针对测试数据集进行预测，准确率 <math><semantics><annotation encoding="application/x-tex">\displaystyle \geq 0.8</annotation></semantics></math>≥0.8 即为合格。

<a id="markdown-要求" name="要求"></a>
## 要求

1.  提交时，请将预测结果按测试数据集中每条数据的排列顺序，以单列数据的形式存入 `credit_risk_pred.csv` 数据文件中，列名为 `RISK`。

2.  需要将 `credit_risk_pred.csv` 放置于 `/home/shiyanlou/Code` 路径下方。

**`credit_risk_pred.csv` 数据文件仅存在 RISK 列，示例如下：**

![ ](http://upload-images.jianshu.io/upload_images/7130568-31806aeb15e230b5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

<a id="markdown-提示" name="提示"></a>
## 提示

*   你可能会用到 scikit-learn 提供的分类预测模型。
*   你可能会用到 Pandas 对数据进行预处理。
*   完成本题目可以自由使用第三方模块，在线环境 `/home/shiyanlou/anaconda3/bin/python` 路径下有 scikit-learn, pandas 等常用模块。


<a id="markdown-知识点" name="知识点"></a>
## 知识点

*   机器学习分类预测



<a id="markdown-分析与解答" name="分析与解答"></a>
# 分析与解答
<a id="markdown-模型选择" name="模型选择"></a>
## 模型选择
首先要选出合适的模型, 最开始随便试了 `SGDClassifier`,`LogisticRegression`等模型, 都没有达到0.8的准确度
然后上网查找,根据这张图选择了 svm 支持向量机模型
![model](http://upload-images.jianshu.io/upload_images/7130568-45e992be74e9205e?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
from sklearn.svm import SVC as MODEL
```

<a id="markdown-读取数据" name="读取数据"></a>
## 读取数据
可以用 pandas 读取 csv 数据, 并进行一些预处理, 并分好训练数据集与测试数据集 
```python
import pandas as pd
def getData():

    data = pd.read_csv(trainfile)  
    test = pd.read_csv(testfile)  #names = cols)   #.replace(to_replace ='"',value = np.nan)

    data = label(data)
    test = label(test)
    
    x_train,y_train =data.iloc[:,:-1].as_matrix(), data.iloc[:,-1].as_matrix()
    x_test = test.iloc[:,:].as_matrix()
    y_test=None
    return x_train,y_train, x_test,y_test
```
<a id="markdown-非数值特征处理" name="非数值特征处理"></a>
## 非数值特征处理
有些特征是非数值的, 需要进行编码, 比如 gender  education 等, 编码有很多方式, 比如 onehotkey, 由于这里是字符串类型的, 可以用 labelencoder , 它可以将一个特征下的值集合一次编码为 0,1,2... 

要想解码, 保存最后的预测结果. 我设置了一个全局变量 `converetor` , 来保存这个 encoder

```python
from sklearn.preprocessing import LabelEncoder as LE

convertor = None # result convertor

def label(data):
    global convertor
    for col in data.columns:
        if data[col].dtype == 'object':
            le = LE()
            if col=='RISK':
                convertor = le
            le.fit(data[col])
            data[col]= le.transform(data[col])
    return data
```

<a id="markdown-拟合预测" name="拟合预测"></a>
## 拟合预测
fit 函数拟合时, 不同的模型时间不一样, 适应的场景,数据也不一样, 准确度也不一样
```
def predict(model=MODEL):        
    predictor = model()
    x_train,y_train,x_test,_ = getData()
    predictor.fit(x_train,y_train)
    res = predictor.predict(x_test)
    save(res)
```
<a id="markdown-保存数据" name="保存数据"></a>
## 保存数据
用 pandas 保存为 csv
```python
def save(result):
    result = convertor.inverse_transform(result)
    dataframe = pd.DataFrame({'RISK':result})
    dataframe.to_csv('credit_risk_pred.csv',index=False,sep=',')
```

<a id="markdown-总结与反思" name="总结与反思"></a>
# 总结与反思
时间匆忙, 这个代码比较粗略,还有很多可以考虑的地方, 比如检验一些值的方差是否过大, 特征缩放, 评估模型的准确度等等

最后, 感觉这个网站,这个比赛挺有趣的, 如果想注册, 可以[点这里](http://www.shiyanlou.com/register?inviter=NTY0MzE5NTY3MDg4), 邀请了:)

<a id="markdown-代码" name="代码"></a>
# 代码
```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.svm import SVC as MODEL

trainfile = 'credit_risk_train.csv'
testfile = 'credit_risk_test.csv'
convertor = None # result convertor

def label(data):
    global convertor
    for col in data.columns:
        if data[col].dtype == 'object':
            le = LE()
            if col=='RISK':
                convertor = le
            le.fit(data[col])
            data[col]= le.transform(data[col])
    return data

def getData():

    data = pd.read_csv(trainfile)  
    test = pd.read_csv(testfile)  #names = cols)   #.replace(to_replace ='"',value = np.nan)

    data = label(data)
    test = label(test)
    
    x_train,y_train =data.iloc[:,:-1].as_matrix(), data.iloc[:,-1].as_matrix()
    x_test = test.iloc[:,:].as_matrix()
    y_test=None
    return x_train,y_train, x_test,y_test

def save(result):
    result = convertor.inverse_transform(result)
    dataframe = pd.DataFrame({'RISK':result})
    dataframe.to_csv('credit_risk_pred.csv',index=False,sep=',')

def predict(model=MODEL):        
    predictor = model()
    x_train,y_train,x_test,_ = getData()
    predictor.fit(x_train,y_train)
    res = predictor.predict(x_test)
    save(res)

if __name__=='__main__':
    predict()
```

<a id="markdown-参考资料" name="参考资料"></a>
# 参考资料
[1] : [数据预处理中的数据编码问题 | python 数据挖掘思考笔记 (2)](https://zhuanlan.zhihu.com/p/32669600)
[2] : [sklearn.preprocessing.LabelEncode](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
[3] : [sklearn: 选择正确的模型](https://blog.csdn.net/sa14023053/article/details/52077574)
[4] : [利用 Scikit Learn 的 Python 数据预处理实战指南](http://zhuanlan.51cto.com/art/201612/525283.htm)
