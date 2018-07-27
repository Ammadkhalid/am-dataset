import dataset

"""
Extends dataset.Database class.

And put our additional functions.
"""
class Database(dataset.Database):

    def insert(self, table, data):
        """
        Insert Data to given table.
        
        Arguments:
            table {string} -- table name.
            data {dict} -- data in dict
        
        Returns:
            [int]
        """
        table = self[table]

        if self.check_if_exists(table, data):
            return

        return table.insert(data)

    def __getitem__(self, table):
        """Converts table type to str."""

        table = str(table)
        
        return self.get_table(table)

    def get_first(self, table, data = None):
        """Gets First Recorder of given table."""

        # if variable is dict
        if isinstance(data, dict):
            return self[table].find_one(**data)
        
        if sum(1 for k in self.get_all(table)):
            return [i for i in self.get_all(table)][0]

    def check_if_exists(self, table, data):
        """Check if data is exists in table."""

        return True if self.get_first(table, data) else False

    def update(self, table, where, data):
        """Update Exists Table data.

        for example we need to update user name with id 2
        so we will do:
        update('users', ['id'], {'name': 'ammadkhalid', 'id': 2})

        Arguments:
            table {str} -- [description]
            where {[str|dict]} -- [description]
            data {dict} -- [description]
        """
        return self[table].update(data, where)

    def delete(self, table, **data):
        """ Delete data from table."""
        return self[table].delete(**data)

    def get_all(self, table, data = None):
        """Gets all data of given table.
        
        Arguments:
            table {str}
        
        Keyword Arguments:
            data {[dict|null]} (default: {None})
        
        Returns:
            iter
        """
        table = self[table]

        if data is None:
            return table.all()
        else:
            return table.find(data)

# set custom Database class
dataset.Database = Database