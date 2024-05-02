from flask import Flask, request
import json
import csv
app = Flask(__name__)
date= []
with open("imdb-movie-data.csv", "r", encoding="utf-8") as  flask_file:
    file_format = csv.reader(flask_file, delimiter=',')
    for f in file_format:
        date.append(f) 
@app.route('/<genre>')
def genre_action(genre):
    drink = [[e or None for e in i] for i in date[1:] if genre.title() in i [2]]
    return json.dumps([dict(zip(date[0], i)) for i in drink], separators=(",",":"))

@app.route("/")
def genre_find():
    genre = request.args.get("genre", default=None, type=str)
    drink = [[e or None for e in i] for i in date[1:] if genre.title() in i [2]]
    return json.dumps([dict(zip(date[0], i)) for i in drink], separators=(",",":"))


if __name__ == "main":
    app.run(host="0.0.0.0", port=8080)