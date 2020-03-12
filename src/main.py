from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__, 
            static_url_path='',
            static_folder='static')
@app.route("/")
def home():
    return 'Hello World lmao'
    # return render_template("<!DOCTYPE html > <h1>Hello World lmao </h1>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)