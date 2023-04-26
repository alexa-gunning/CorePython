Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = {'b':20,'a':35}
>>> data['a']
35
>>> print(data.get('c',None))
None
>>> len(data)
2
>>> data.keys()
dict_keys(['b', 'a'])
>>> data.values()
dict_values([20, 35])
>>> data.pop('b')
20
>>> data
{'a': 35}
>>> 
