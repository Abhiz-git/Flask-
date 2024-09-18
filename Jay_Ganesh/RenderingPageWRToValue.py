#####################################################################################################
#
#   Name: Abhishek Dilipkumar Nale
#   
#   Original:   Flask Sample web application: Rendering Page WRT Value
#   Date: 18/09/2024
#
######################################################################################################

from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
   return "Welcome to Jay Ganesh"
   
   
@app.route('/result/<int:marks>') 
def result(marks):
    if marks >= 50:
        return f"Passed with {marks}"
    
    return f"Failed with {marks}"


if __name__ == "__main__":
  app.run(debug = True)
  