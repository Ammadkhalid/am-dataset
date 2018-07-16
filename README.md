```
Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import amdataset

In [2]: db = amdataset.connect('sqlite:///:memory:')

In [3]: db.insert('users', {'name': 'ammadkhaads'})
Out[3]: 1

In [4]: db.update('users', ['name'], {'name': 'AmmadKhalid'})
Out[4]: 0

In [5]: db.get_first('users')
Out[5]: OrderedDict([('id', 1), ('name', 'ammadkhaads')])

In [6]: db.update('users', ['id'], {'name': 'AmmadKhalid', 'id': 1})
Out[6]: 1

In [9]: db.delete('users', name = 'AmmadKhalid')
Out[9]: True
```