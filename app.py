
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

from database import init_db, add_record, get_records
from validator import validate_record

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"

init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        phone = request.form.get("phone", "")

        valid, result = validate_record(name, email, phone)

        if not valid:
            flash(result, "error")
            return redirect(url_for("index"))

        name, email, phone = result

        try:
            add_record(name, email, phone)
            flash("Record added successfully!", "success")
        except sqlite3.IntegrityError:
            flash("Duplicate email detected. Record was not added.", "error")

        return redirect(url_for("index"))

    records = get_records()
    return render_template("index.html", records=records)


if __name__ == "__main__":
    app.run(debug=True)
