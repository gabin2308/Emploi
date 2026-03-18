from flask import render_template

from app import app

class IndexController:

    @app.route('/')
    def index():

        return "<p> Wilfried !</p>"