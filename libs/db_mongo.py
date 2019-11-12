from pymongo import MongoClient
from db import Database
from config import get_config
from termcolor import colored

class MongoDatabase(Database):
    TABLE_SONGS = 'songs'
    TABLE_FINGERPRINTS = 'fingerprints'

    def __init__(self):
        pass

    def connect(self):
        config = get_config()

        self.client = MongoClient(config['db.dsn'])
        self.db = self.client[config['db.database']]
        print(colored('mongodb - connection opened', 'white', attrs=['dark']))

    def insert(self, collection, document):
        # if not self.db:
        self.connect()

        return self.db[collection].insert_one(document).inserted_id

    def findOne(self, table, params):
        self.connect()
        return self.db[table].find_one(params)

    def insertMany(self, table, columns, values):
        self.connect()

        items = []
        for value in values:
            new = {}
            for i in range(len(columns)):
                new[columns[i]] = value[i]
            items.append(new)

        self.db[table].insert_many(items)

    def drop(self, collection):
        self.connect()
        return self.db[collection].drop()

    def create(self, collection):
        self.connect()
        return self.db[collection]
