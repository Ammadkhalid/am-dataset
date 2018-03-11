# Simple Database CRUD Package Using databaset Package
```
┌─[ammadkhalid@TheKiller] - [/mnt/D0E0EC3BE0EC2A04/python/me/am-dataset] - [پير مارچ 12, 00:09]
└─[$] <git:(development*)> python
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from amdataset.db import Database
>>> path = ''
>>> # path to db, i will use memory in 
... 
>>> db = Database(path)
>>> db.insert('mytable', {'column': 'value'})
>>> # ^ this will ignore if same data is already inserted
... 
>>> print([k for k in db.getAll('mytable')])
[OrderedDict([('id', 1), ('column', 'value')])]
>>> # we also have access to our main package dataset
... 
>>> db.db
<Database(sqlite://)>
>>> db
<amdataset.db.Database object at 0x7f6c39c97ac8>
>>> # see? sounds cool to me that's why i created it will add more stuff time by time
```

