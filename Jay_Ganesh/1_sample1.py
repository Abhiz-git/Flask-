#####################################################################################################
#
#   Name: Abhishek Dilipkumar Nale
#   
#   Original:   Flask Sample web application (without 'debug' parameter)
#   Date: 18/09/2024
#
######################################################################################################

from flask import Flask

app = Flask(__name__)

@app.route('/')              #parameter: (str)->url         '/' means root homepage
def welcome():
    return "Welcome to sample web application"

@app.route('/sample')       #parameter:(str)->url
def Welcome():
    return "Hi its Sample with debug off"

if __name__ == "__main__":
    app.run()                   #run method has 4 parameters we use none.



# '@' this symbol is known as decorater.

# python decorater is used to make a specific change in Python Syntax to alter fuction easily.