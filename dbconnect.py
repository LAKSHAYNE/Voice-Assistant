import pymongo
import hashlib


class dbconnect:
    def __init__(self) -> None:
        try:
            client = pymongo.MongoClient(
                "mongodb+srv://lakshayne:tyrell@cluster0.siopf.mongodb.net/?retryWrites=true&w=majority")

            db = client["voiceAssist"]

            self.col = db["users"]
            print("Successfully connected to database")
        except:
            print("Unable to connect to database")

    def find(self, email, password):
        hashpass = hashlib.sha256(password.encode('utf-8')).hexdigest()
        print(hashpass)
        x = self.col.find_one({"email": email, "password": hashpass})
        if (x):
            return ('Found')
        else:
            return ('Not Found')


if __name__ == '__main__':
    ob = dbconnect()

    print(ob.find('weeknd@hxp.com', 'lakshay1234'))
