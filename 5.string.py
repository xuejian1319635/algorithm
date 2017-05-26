Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #字符串
>>> #编码：#-*-coding
>>> print("hello world")
hello world
>>> #单引号和双引号都行
>>> #打印多行字符用三英豪
>>> print('''this is the first
second''')
this is the first
second
>>> age=3
>>> name="tom"
>>> print(“{0}was{1} years old".famat(name,age)
      
SyntaxError: invalid character in identifier
>>> print(“{0}was{1} years old".famat(name,age))
      
SyntaxError: invalid character in identifier
>>> print("{0}was{1} years old".famat(name,age))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("{0}was{1} years old".famat(name,age))
AttributeError: 'str' object has no attribute 'famat'
>>> print("{0}was{1} years old".format(name,age))
tomwas3 years old
>>> #format用法
>>> #用几个字符串串起来
>>> print(name+"was"+str(age)+"years old")
tomwas3years old
>>> #+表示联合的用法，要用str把数字型的变量改正成字符型
>>> 
>>> 
>>> #字面常量
>>> # 6    2.24    3.45e-3
>>> #变量
>>> #第一个必须是字母或者下划线，区分大小写 ，其余是字母数字下划线
