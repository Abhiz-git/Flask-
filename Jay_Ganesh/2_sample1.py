from flask import Flask

app = Flask(__name__)

@app.route('/')              #root address or base address
def welcome():
    return "Welcome to sample web application"

@app.route('/sample')
def Welcome():
    return "Hi its Sample with debug on"

if __name__ == "__main__":
    app.run(debug = True)   #run method has 4 parameters we used debug {True} now for any change in code we don't need to restart the code\
