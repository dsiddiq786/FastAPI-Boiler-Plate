# import
from fastapi import FastAPI

# Instantiate
app = FastAPI()

# Decorate
@app.get('/')

# Function
def index():
    return {'data':{'name':"Dawood"}}

# About Page Decorator and Function
@app.get('/about')
def about():
    return {'data':{'about page'}}