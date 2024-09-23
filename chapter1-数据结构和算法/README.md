[TOC]

考虑比如搜索、排序、排列以及筛选等这一类常见的问题
`collections`模块中也包含了针对各种数据结构的解决方案

### 将序列分解为单独的变量

将N个元素的元组或序列,分解为N个单独的变量

> 任何序列（或可迭代的对象）都可以通过一个简单的赋值操作来分解为单独的变量

```python
p=(4,5)
x,y=p
x
Out[4]: 4
y
Out[5]: 5

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
name
Out[4]: 'ACME'
date
Out[5]: (2012, 12, 21)
name, shares, price, (year, mon, day) = data
name
Out[7]: 'ACME'
year
Out[8]: 2012
mon
Out[9]: 12
day
Out[10]: 21
``` 

<p style="background-color: rgba(68, 68, 68, 1); color: rgba(255, 0, 0, 1)">
如果元素的数量不匹配，将得到一个错误提示
</p>

```python
p=(4,5)
x,y,z=p
Traceback (most recent call last):
  File "E:\soft\python\lib\site-packages\IPython\core\interactiveshell.py", line 3457, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-12-d59213f48878>", line 1, in <module>
    x,y,z=p
ValueError: not enough values to unpack (expected 3, got 2)
```

