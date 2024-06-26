from flask import Blueprint, render_template
import json
import random


main = Blueprint('main', __name__)


def generate_unique_upc():
    return "#" + "".join([str(random.randint(0, 9)) for _ in range(10)])


def generate_unique_id():
    return "#" + "".join([str(random.randint(0, 9)) for _ in range(10)])


def generate_phone_number():
    return "+380 " + " ".join(["".join([str(random.randint(0, 9)) for _ in range(3)]) for _ in range(3)])


@main.route('/')
def home():
    return render_template('pages/home.html')


@main.route('/login')
def login():
    return render_template('pages/login.html')