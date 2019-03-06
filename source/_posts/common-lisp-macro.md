---
title: 『common lisp』宏及函数的实现
date: 2017-11-1
tags: [common lisp, macro]
categories: 
		- 程序设计
		- common lisp
keywords: lisp,macro,function-programming
description: 学习lisp过程中自己实现的一些宏及函数，虽然效率可能不高，就做练习吧，其他人也可参考。

---
# 1. macros



## 1.1. once-only
```common lisp
(defmacro  once-only ((&rest names) &body  body)
    (let ((gensyms  (loop for n in names collect (gensym))))
        `(let (,@(for i in gensyms collect `(,i (gensym))))
            `(let (,,@(loop for g in gensyms for n in names collect ``(,,g ,,n)))
                ,(let (,@(loop for n in namws for g in gensyms collect `(,n  ,g)))
                    ,@body)))))
```
## 1.2. with-gensym   
```common lisp
(defmacro   with-gensym  (vars &rest body)
    `(let ( ,@(loop for i in vars collect `(,i (gensym))))
            ,@body))
```
`用法:`
                
    (defmacro a-macro  ((&rest vars) &body, body)
        (with-gensym ((somevars) `(......) ,@body))   


## 1.3. 测试框架
```common lisp

(defmacro combine-rsts  (&rest cases)
    (with-gensym (rst)
    `(let ((,rst t))
        ,@(loop for i in cases collect `(unless ,i (setf ,rst nil)))
        ,rst)))

(defmacro  check (&rest cases)
    `(combine-rsts ,@(loop for case in cases collect `(report ,case ',case) )))


(defmacro   with-gensym  ((&rest vars) &rest body)
    `(let ,(loop for i in vars collect `(,i (gensym)))
        ,@body))


(defun  report (expr form)
    (format t "~:[wrong  ~;correct~] --- ~a~%"  expr form)
        expr)
```

>**(check (= (+ 3 5)8 ) (zerop (- 8 7)))**
`correct --- (= (+ 3 5) 8)`
`wrong --- (ZEROP (- 8 7))`


### 1.3.1. 更高层次的抽象
```common lisp

(defvar *fun-name* nil)

(defmacro deftest (name parameters &body body )
    `(defun ,name  ,parameters
        (let ((*fun-name* '(append *fun-name* (list ',name)))
            ,@body)))

```
>(deftest test ()
>&emsp;(check 
>&emsp;&emsp;(= (+ 3 5)8 )
>&emsp;&emsp;(zerop (- 8 7))))

## 1.4. [cond](#cond)


```common-lisp
(defmacro my-cond (&rest body)
    (let ((rst nil) (body (reverse body)))
        (dolist (i body rst)  
            (setf rst `(if ,(car i),(second i),rst)))))
```


---
# 2. functions 

## 2.1. primep
```common lisp
(defun  primep (x)
    (when (> x 1)   (loop for fac  from 2 to  (sqrt x) never (zerop (mod x fac)))))

(defun next-prime (x)
    (loop for i from x when (primep i) return i))


(defmacro do-prime ((p begin end)  &rest body)
    (let ((end-val end))  ;end-val will evalute many times, so make it certain
	   `(do ((,p (next-prime ,begin) (next-prime (1+ ,p))))
		((> ,p ,end-val)) 
      ,@body)))

(defun cp-tree (li)
	   (if (null li) nil
	       (let ((x (car li)))
                (if (atom x) 
                    (cons x (cp-tree (cdr li)))  
                    (cons (cp-tree x) (cp-tree (cdr li))))))  
```
