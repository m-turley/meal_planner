from flask import Flask, request
import json

meal_dict = {
    1: {'link': "http.ex.com" , "title":  "Japchae", "tags": ["vegan", "tofu"] }
}


app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello World")
    return "<p>Hello, World!</p>"

@app.route('/meals', methods= ["GET"])
def get_meals():
    """
    Get all available meals, in database and display them **tbd on display format**
    :return: json of all available meals
    """
    if request.method == "GET":
        return json.dumps(meal_dict)

@app.route('/add_meal', methods = ["POST"])
def add_meal():
    """
    Add new meal to database
    :return:
    """
    if request.method == "POST":
        #add meal
        current_int = len(meal_dict) + 1
        new_meal = request.get_json()
        meal_dict[current_int] = new_meal
    return {'message': "Successfully added new meal"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9999)