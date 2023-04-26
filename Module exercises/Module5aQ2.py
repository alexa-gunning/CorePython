Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = [5,3,7]
>>> 
data[0] = -5
>>> data.append(10)
>>> data
[-5, 3, 7, 10]
>>> data.insert(2,22)
>>> data
[-5, 3, 22, 7, 10]
>>> l.pop(1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l.pop(1)
NameError: name 'l' is not defined
>>> data.pop(1)
3
>>> data
[-5, 22, 7, 10]
>>> newData = [22, 17]
>>> data.extend(newData)
>>> data
[-5, 22, 7, 10, 22, 17]
>>> data.index(7)
2
>>> 
data.sort()
>>> data
[-5, 7, 10, 17, 22, 22]
>>> 
