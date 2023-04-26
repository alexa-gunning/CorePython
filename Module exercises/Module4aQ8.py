Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
data = 'Python Rules!'
>>> split(data,' ')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    split(data,' ')
NameError: name 'split' is not defined
>>> data.split(' ')
['Python', 'Rules!']
>>> data.upper()
'PYTHON RULES!'
>>> data.find('Rules')
7
>>> data.replace('!','?')
'Python Rules?'
>>> data.isalpha()
False
>>> 
