from flask import Flask, request, render_template
import json
from meal_planner.model.db import insertrecipe2database

meal_dict = {
    1: {'link': "http.ex.com" , "title":  "Japchae", "tags": ["vegan", "tofu"] }
}


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("home.html")

@app.route('/full_list_meals', methods= ["GET"])
def get_meals():
    """
    Get all available meals, in database and display them **tbd on display format**
    :return: json of all available meals
    """
    if request.method == "GET":
        return json.dumps(meal_dict)

@app.route('/add_meal', methods = ["GET"])
def display_meal_addition_form():
    """
    display form to add new meal
    """
    return render_template("add_meal.html")

@app.route('/add_meal', methods = ["POST"])
def add_meal():
    """
    Add new meal to database
    """
    if request.method == "POST":
        #get meal inputs
        current_int = len(meal_dict) + 1
        meal_name = request.form.get("meal_name")
        meal_tags = request.form.getlist("tags")
        meal_link = request.form.get("meal_link")
        #make dictionary
        meal_inner_dict = {"link": meal_link, "title": meal_name, "tags": meal_tags}

        meal_dict[current_int] = meal_inner_dict

        #TODO: add to sql data

    return {'message': "Successfully added new meal"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9999)
    print("hi") (0)
    input(my_variable) 