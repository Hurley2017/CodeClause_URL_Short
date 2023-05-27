from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import secrets, string
import dotenv
import os

dotenv.load_dotenv()

ui = Flask(__name__)

connection_address = os.environ.get("CONNECTION_URL")

def random_id(n):
    res = ''.join(secrets.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase)
                  for i in range(n))
    return res

def protocol_checker(URL):
    ret = ""
    if URL[:8] == "https://":
        ret = ret + URL
    elif URL[:7] == "http://":
        ret + URL
    else:
        ret =  "https://" + ret + URL
    while(True):
        if ret[-1] == '\n':
            ret = ret[:len(ret)-1]
        else:
            break
    return ret

@ui.route("/", methods=["GET"])
def browse():
    return render_template("index.html")


@ui.route("/send", methods=["POST"])
def process1():
    print("send called")
    Mongo_Connection = MongoClient(connection_address)
    Database = Mongo_Connection["URL_DATA"]
    Table = Database["Short"]
    data = request.json
    URL = data["URL"]
    if "ayeee.ga" in URL:
        return "You think you smart?"
    elif len(URL) == 0:
        return "No URL entered!"
    search_existing_data = Table.find_one({"longURL" : URL})
    if search_existing_data != None:
        shortkey = search_existing_data["shortURL"]
        shortkey = "ayeee.ga/" + shortkey
    else:
        shortkey = random_id(4)
        insert_document = {"shortURL" : shortkey, "longURL" : URL}
        Table.insert_one(insert_document)
        shortkey = "ayeee.ga/" + shortkey
    return shortkey


@ui.route("/<id>", methods=["GET"])
def process2(id):
    Mongo_Connection = MongoClient(connection_address)
    Database = Mongo_Connection["URL_DATA"]
    Table = Database["Short"]
    flag_document = Table.find_one({"shortURL" : str(id)})
    if flag_document != None:
        print(flag_document["longURL"])
        return redirect(protocol_checker(flag_document["longURL"]), code=302)
    else:
        return "invalid url"