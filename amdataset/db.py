import dataset

class Database(object):

    def __init__(self, database):
        self.db = dataset.connect('sqlite://{}'.format(database))

    def insert(self, table, data):
        Table = self.db[table]

        Table.insert_ignore(data)

    def checkIfExists(self, table, data):
        Table = self.db[table]

        if Table.find_one(data):
            return True

        return None

    def getAll(self, table, data = None):

        if data is None:
            return self.db[table].all()
        else:
            return self.db[table].find(data)
