[TOC]

考虑比如搜索、排序、排列以及筛选等这一类常见的问题
`collections`模块中也包含了针对各种数据结构的解决方案

### 1.1 将序列分解为单独的变量

将N个元素的元组或序列,分解为N个单独的变量

> 任何序列（或可迭代的对象）都可以通过一个简单的赋值操作来分解为单独的变量

```python
p = (4, 5)
x, y = p
x
Out[4]: 4
y
Out[5]: 5

data = ['ACME', 50, 91.1, (2012, 12, 21)]
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
p = (4, 5)
x, y, z = p
Traceback(most
recent
call
last):
File
"E:\soft\python\lib\site-packages\IPython\core\interactiveshell.py", line
3457, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-12-d59213f48878>", line
1, in < module >
x, y, z = p
ValueError: not enough
values
to
unpack(expected
3, got
2)
```

实际上不仅仅只是元组或列表，只要对象恰好是可迭代的，那么就可以执行分解操作，包括字符串，文件，迭代器，生成器

```python
s = 'Hello'
a, b, c, d, e = s
a, b, c, d, e

a
Out[10]: 'H'
```

当做分解操作时，有时候可能想丢弃某些特定的值。Python并没有提供特殊的语法来实现这一点，但是通常可以选一个用不到的变量名，以此来作为要丢弃的值的名称。

```python
data = ['ACME', 50, 91.1, (2012, 12, 21)]

_, shares, prices, _ = data

shares

_, shares, prices, _ = data

shares
>>> 50
prices
>>> 91.1

```

### 1.2 从任意长度的可迭代对象中分解元素

需要从某个可迭代对象中分解出N个元素,但是这个可迭代对象的长度可能超过N,这会导致出现"分解的值过多(too man values to unpack)"的异常

python的"*表达式"可以用来解决这个问题