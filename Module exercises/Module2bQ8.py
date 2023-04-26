Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
x = "4.66"
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: '4.66'
>>> float(x)
4.66
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: '4.66'
>>> int(float(x))
4
>>> str(x)
'4.66'
>>> 
