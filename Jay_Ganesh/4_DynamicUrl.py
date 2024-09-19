#####################################################################################################
#
#   Name: Abhishek Dilipkumar Nale
#   
#   Original:   Flas Sample web appli.: Building Dynamic URL
#   Date: 18/09/2024
#
#   Note:
#           url_for():
#               is used to create a dynamic url with given parameter.
#
#           redirect():
#               redirects from present url to url given (location).
#
#           * Both are functions from <flask module>        
#
######################################################################################################

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/pass/<int:marks>")
def Pass(marks):
    return f"You are pass with {marks} marks."

@app.route("/fail/<int:marks>")
def fail(marks):
    return f"You are fail with {marks} marks."

@app.route("/results/<int:marks>")
def results(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "Pass"

    return redirect(url_for(result, marks=marks))
    

if __name__ == "__main__":
  app.run(debug=True)


