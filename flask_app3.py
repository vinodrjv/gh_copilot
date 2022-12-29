from flask import Flask, request    # Commentary: added import

# Commentary: typed this one line comment, rest of program was generated by Copilot
# flask app to server web page that collects three values and returns the average of the three values

# define string for average web page form
average_form = """
<!DOCTYPE html>
<html>
<head>
<title>Average</title>
</head>
<body>
<h1>Average</h1>
<form action="/average" method="post">
    <label for="num1">Number 1:</label>
    <input type="text" id="num1" name="num1"><br><br>
    <label for="num2">Number 2:</label>
    <input type="text" id="num2" name="num2"><br><br>
    <label for="num3">Number 3:</label>
    <input type="text" id="num3" name="num3"><br><br>
    <input type="submit" value="Submit">
</form>
</body>
</html>
"""

# define web page to display result of average function
average_result_page = """
<!DOCTYPE html>
<html>
<head>
<title>Average Result</title>
</head>
<body>
<h1>Average Result</h1>
<p>Result: {}</p>
</body>
</html>
"""   # Commentary: change variable name to have _page suffix

# define average function
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# setup flask app to serve average web page
app = Flask(__name__)

@app.route("/")
def index():
    return average_form

@app.route("/average", methods=["POST"])
def average_result():
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    num3 = int(request.form["num3"])
    result = average(num1, num2, num3)
    return average_result_page.format(result)   # Commentary: change to reference web page string

# run flask app
if __name__ == "__main__":  # Commentary: added this line
    app.run(host="0.0.0.0", port=8080) # Commentary: modified to run on port 8080 and any source



