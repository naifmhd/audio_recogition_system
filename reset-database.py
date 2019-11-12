#!/usr/bin/python
from libs.db_sqlite import SqliteDatabase
from libs.db_mongo import MongoDatabase

if __name__ == '__main__':
    db = MongoDatabase()

    #
    # songs table

    db.drop_table('songs')
    print('removed db.songs')

    db.create_table('songs')
    print('created db.songs')

    #
    # fingerprints table

    db.drop_table('fingerprints')
    print('removed db.fingerprints')
    db.create_table('fingerprints')

    print('created db.fingerprints')

    print('done')
