import pymongo
cilent = pymongo.MongoClient(host='local',port=27017)
# cilent = pymongo.MongoClient('mongodb://localhost:27017/')

db = cilent.test
# db = client['test']