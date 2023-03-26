import pymongo
import hashlib
from loginGui import *
from commands import *


class dbconnect(LoginGui):
    def __init__(self) -> None:
        try:
            client = pymongo.MongoClient(
                "mongodb+srv://lakshayne:tyrell@cluster0.siopf.mongodb.net/?retryWrites=true&w=majority")

            db = client["voiceAssist"]

            self.col = db["users"]
            print("Successfully connected to database")
        except:
            print("Unable to connect to database")
        LoginGui.__init__(self, self.find)

    def find(self):
        # print('innnnn')
        email = self.emailInput.get()
        password = self.passInput.get()
        # print(email, password)
        hashpass = hashlib.sha256(password.encode('utf-8')).hexdigest()
        x = self.col.find_one({"email": email, "password": hashpass})
        if (x):
            print('user found')
            self.app.destroy()
            Commands()
        else:
            print('no user')
            self.update()
            return ('Not Found')
