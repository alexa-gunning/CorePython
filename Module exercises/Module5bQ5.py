Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
data = {'b': 20, 'a':35}
>>> 
data.key['b'] = -20
Traceback (most recent call last):
  File "<pyshell#1>", line 2, in <module>
    data.key['b'] = -20
AttributeError: 'dict' object has no attribute 'key'
>>> data['b'] = -20
>>> 
data['c'] = 40
>>> data
{'b': -20, 'a': 35, 'c': 40}
>>> sorted(data.keys())
['a', 'b', 'c']
>>> d.pop('b')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d.pop('b')
NameError: name 'd' is not defined
>>> data.pop('b')
-20
>>> 
