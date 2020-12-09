from flask import Flask, render_template
import pymongo
from scrape_mars import out_put

app = Flask(__name__)

@app.route("/")
def index():
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    mars = db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scapper():
    print("Scrapping in course, please be patient.")
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    db.mars.drop()
    db.mars.insert_one(out_put)
    return render_template("scrape.html")


if __name__ == "__main__":
    app.run(debug = True)