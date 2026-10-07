from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        roll = request.form["roll"]

        python = int(request.form["python"])
        java = int(request.form["java"])
        dbms = int(request.form["dbms"])
        cn = int(request.form["cn"])
        web = int(request.form["web"])

        total = python + java + dbms + cn + web
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        status = "PASS" if percentage >= 40 else "FAIL"

        result = {
            "name": name,
            "roll": roll,
            "python": python,
            "java": java,
            "dbms": dbms,
            "cn": cn,
            "web": web,
            "total": total,
            "percentage": percentage,
            "grade": grade,
            "status": status
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)