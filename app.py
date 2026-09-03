# Make a calculator using pythonn .

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    a = ""
    op = "+"
    b = ""

    if request.method == "POST":

        try:
            a = float(request.form["a"])
            op = request.form["op"]
            b = float(request.form["b"])

            if op == "+":
                result = a + b

            elif op == "-":
                result = a - b

            elif op == "*":
                result = a * b

            elif op == "/":
                if b != 0:
                    result = a / b
                else:
                    result = "Cannot divide by zero"

            elif op == "%":
                if b != 0:
                    result = a % b
                else:
                    result = "Cannot find remainder"

            elif op == "**":
                result = a ** b

            else:
                result = "Invalid operator!"

        except ValueError:
            result = "Please enter valid numbers."

    return render_template(
        "index.html",
        result=result,
        a=a,
        op=op,
        b=b
    )


if __name__ == "__main__":
    app.run(debug=True)
