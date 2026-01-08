from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/')
def home():
    return "<h3>welcome to my cloud Computing</h3>"

@app.route('/reg')
def registration():
    return "<h3>welcome to registration page</h3>"

@app.route('/sales')
def sales():
    return "<h3>welcome to home page</h3>"

@app.route('/multiply')
def multiply():
    a=89
    b=69
    c=a*b
    return "this is the multipliction result " + str(c)

@app.route('/division')
def division():
    a=89
    b=69
    c=a/b
    return "this is the division result " + str(c)

@app.route('/addition')
def addition():
    a=89
    b=69
    c=a+b
    return "this is the addition result " + str(c)










if __name__=="__main__":
    app.run(debug=True, port=5003,host="0.0.0.0")
