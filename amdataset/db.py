import dataset

class Database(object):

    def __init__(self, database):
        """initialize instance of Dataset"""
        self.db = dataset.connect(database)

    def insert(self, table, data):
        """Insert data if not exists.
        
        Arguments:
            table {string} -- [name of table]
            data {dict} -- [dict which contains columns and their values.]
        """
        Table = self.db[table]

        if self.checkIfExists(table, data):
            return

        Table.insert(data)

    def getFirst(self, table, data):
        """Get first item.
        
        Arguments:
            table {string} -- [name of table]
            data {dict} -- [dict which contains columns and their values.]
        
        Returns:
            [mix] -- [will return data from database.]
        """
        Table = self.db[table]

        return Table.find_one(**data)


    def checkIfExists(self, table, data):
        """Check if data exists in table.
        
        Arguments:
            table {string} -- [name of table]
            data {dict} -- [dict which contains columns and their values]
        
        Returns:
            bool -- [true or None]
        """
        if self.getFirst(table, data):
            return True

        return None

    def update(self, table, where, data):
        """Update Data
        
        Update data where = column name in data.
        
        Arguments:
            table {string} -- [table name]
            where {string} -- [column name as dict key in data]
            data {dict} -- [data]
        
        Returns:
            [bool]
        """
        Table = self.db[table]

        return Table.update(data, where)

    def delete(self, table, **data):
        """Delete Data
        
        Delete column where key=value .
        
        Arguments:
            table {string} -- [table name]
            **data {dict} -- []
        
        Returns:
            [bool] -- [deleted or not]
        """
        Table = self.db[table]

        return Table.delete(**data)

    def getAll(self, table, data = None):
        """Get All Data in given table.
        
        Get all data and tbh i also forget :p for what is data is argument.
        I wrote this doc after long time..
        
        Arguments:
            table {string} -- [Table name]
        
        Keyword Arguments:
            data {dict} -- [...] (default: {None})
        
        Returns:
            [mix] -- [..]
        """

        if data is None:
            return self.db[table].all()
        else:
            return self.db[table].find(data)
