from flask import Flask, render_template, request

app = Flask (__name__)

egg_cooking_time = {
    "runny": 4 * 60,
    "soft": 6 * 60,
    "medium": 8 * 60,
    "hard": 12 * 60
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        egg_type = request.form.get("egg_type")
        seconds = egg_cooking_time.get(egg_type, 0)
        return render_template("timer.html", seconds=seconds, egg_type=egg_type)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)