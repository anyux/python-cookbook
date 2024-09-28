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

python的"*表达式"可以用来解决这个问题.例如,假设开设了一门课程,并决定去掉第一个,最后一个,只对中间的成绩做平均分统计,`*表达式`可以解决

```python

def drop_first_laster(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)

grades = [
    1,2,3,4,5,6,7,8,9,9
]

res = drop_first_laster(grades)
print(res)

```

另一个用例是,一个列表,由姓名邮件地址组成,后面跟着任意数量的电话号码,一样可以分解
```python

record = [
    'Dave', 'dave@example.com', '773-555-1212', '847-555-1212'
]

name,email,*phone = record

print(name)

print(email)

print(phone)

```

`*表达式`也可以位于列表的第一个位置,比如用一系列的值来代表公司过去8个月的季度销售

```python

*trailing,current = [
    10,8,7,1,9,5,10,3
]

print(trailing)

print(current)
```

对于分解未知或任意长度的可迭代对象,这种扩展的分解操作是合适的.通常这类可迭代对象中会有一些已知的组件或模式,利用`*表达式`分解可迭代对象使用得开发者能轻松利用这些模式

`*式`的语法在迭代一个变长的元组序列时有用

```python

record = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]

def do_foo(x,y):
    print(x,y)

def do_bar(s):
    print(s)

for tag,*args in record:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

```

当和某些特定的字符串处理操作相结合,比如做拆分(splitting)操作时,这种`*式`语法所支持的分解操作也非常有用

```python

from docker.utils.config import home_dir

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

uname,*fields,homedir,sh=line.split(":")

print(uname)

print(homedir)

print(sh)

```

有时候可能想分解出某些值然后丢弃它们.在分解的时候,不能只是指定一个单独的`*`,但是可以使用几个常用来表示待丢弃值的变量名

```python

record = ('ACME', 50, 123.45, (12, 18, 2012))

name,*_,(*_,year) = record

print(name)

print(year)
```

`*`分解操作和各种函数式语言中的列表处理功能有着一定的相似性.例如,如果有一个列表,可以像下面这样轻松将其分解为头部和尾部

```python

items=[
    1,10,7,4,5,9
]

head,*tail=items

print(head)

print(tail)
```

### 1.3 保存最后N个元素

在迭代或是其他形式的处理过程中对最后几项记录做一个有限的历史记录统计

保存有限的历史记录算是`collections.deque`的完美应用场景了