import pymongo


class Database(object):
    URI = "mongodb://localhost:27017/"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['newDB']

    @staticmethod
    def insert(collection, data):
        if data['std_id'] not in Database._find_id('users'):
            Database.DATABASE[collection].insert_one(data)
            print("add")
        else:
            raise Exception('already existed')

    @staticmethod
    def _find_id(collection):
        result = []
        for i in Database.find(collection):
            result.append(i['std_id'])
        return result

    @staticmethod
    def find(collection):
        result = []
        for data in Database.DATABASE[collection].find():
            result.append(data)
        return result

    @staticmethod
    def remove(collection, data):
        Database.DATABASE[collection].delete_one(data)

    @staticmethod
    def update(collection, query, value):
        Database.DATABASE[collection].update_one(query, value)


def start():
    Database.initialize()
    # Database.insert('users', {"std_id": "2",
    #   "std_fullname": "Dmitro Provodoff",
    #   "std_login": "dmitro",
    #   "std_password": 2})
    # Database.remove('users', {"std_id": "2"})
    print(Database.find('users'))
    Database.update('users', {"std_id": "2"}, {"$set": {"std_fullname": "Dmitrii"}})


if __name__ == '__main__':
    start()
