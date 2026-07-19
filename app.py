import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="students_db",
    user="postgres",
    password="kiran@1719"
)

cur = conn.cursor()
from flask import Flask, render_template, request,redirect,url_for

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def home():
    if request.method=="POST":
       
       name=request.form["name"]
       age=request.form["age"]
       grade=request.form["grade"]

       cur.execute("INSERT INTO students(name,age,grade) VALUES(%s,%s,%s)",
        (name,age,grade))
       conn.commit()

       print("Student Added Successfully")

       print("Name:",name)
       print("Age:",age)
       print("Grade:",grade)

    return render_template("index.html")

@app.route("/about")

def about():
    return render_template("about.html")


@app.route("/contact")

def contact():
    return render_template("contact.html")


@app.route("/students")

def students():
    cur.execute("SELECT * FROM students")
    students=cur.fetchall()

    return render_template("students.html",students=students)

@app.route("/delete/<int:id>")

def delete_student(id):
    cur.execute("DELETE FROM students WHERE id=%s",(id,))
    conn.commit()

    return redirect(url_for("students"))

@app.route("/edit/<int:id>",methods=["GET","POST"])

def edit_student(id):
    cur.execute("SELECT * FROM students WHERE id=%s",(id,))
    student=cur.fetchone()

    if request.method=="POST":
        name=request.form["name"]
        age=request.form["age"]
        grade=request.form["grade"]

        cur.execute("UPDATE students SET name=%s,age=%s,grade=%s WHERE id=%s",
        (name,age,grade,id))
        conn.commit()

        return redirect(url_for("students"))

    return render_template("edit.html",student=student)


   

app.run(debug=True)
