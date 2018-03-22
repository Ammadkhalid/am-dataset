import dataset

class Database(object):

    def __init__(self, database):
        self.db = dataset.connect(database)

    def insert(self, table, data):
        Table = self.db[table]

        if self.checkIfExists(table, data):
            return

        Table.insert(data)

    def getFirst(self, table, data):
        Table = self.db[table]

        return Table.find_one(**data)


    def checkIfExists(self, table, data):
        if self.getFirst(table, data):
            return True

        return None

    def update(self, table, where, data):
        Table = self.db[table]

        return Table.update(data, where)

    def delete(self, table, **data):
        Table = self.db[table]

        return Table.delete(**data)

    def getAll(self, table, data = None):

        if data is None:
            return self.db[table].all()
        else:
            return self.db[table].find(data)
