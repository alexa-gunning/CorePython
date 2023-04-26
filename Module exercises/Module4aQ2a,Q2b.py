Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
data = "myprogram.exe"
>>> data.split('.')
['myprogram', 'exe']
>>> 
data.split('.')[0]
'myprogram'
>>> lth = len(data)
>>> lth
13
>>> midl = round(lth/2)
>>> midl
6
>>> data[midl]
'r'
>>> 
