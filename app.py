from flask import Flask,render_template,request
import google.generativeai as palm
import os
import random

# api = os.getenv("MAKERSUITE_API_TOKEN")
# palm.configure(api_key = api)
palm.configure(api_key = "AIzaSyAoZL9Vi7joGfF9D-cIO4IkphC2-8-jJF8")

model = {"model": "models/text-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_QA", methods = ["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/makersuite", methods = ["GET","POST"])
def makersuite():
    q = request.form.get("q")
    r = palm.generate_text(prompt = q + "Limit your response to a maximum of two sentences.", **model)
    return(render_template("makersuite.html", r = r.result))

@app.route("/prediction", methods = ["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/joke", methods = ["GET","POST"])
def joke():
    randomNum = random.randint(0,1)
    if randomNum == 0:
        r = palm.generate_text(prompt = "Tell me a Singaporean joke! Limit your response to a maximum of two sentences.", **model)
    else:
        r = palm.generate_text(prompt = "Give me an insight on the current financial news! Limit your response to a maximum of two sentences.", **model)
    return(render_template("index.html", r = r.result))

if __name__ == "__main__":
    app.run()