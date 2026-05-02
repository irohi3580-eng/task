import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#DB接続
def get_db():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

#トップページ（一覧表示）
@app.route("/")
def index():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

#追加
@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    conn = get_db()
    conn.execute("INSERT INTO tasks (content) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    return redirect("/")

#削除
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

#DB初期化（最初に1回だけ実行）
def init_db():
    conn = sqlite3.connect("tasks.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.close()

# 編集画面表示
@app.route("/edit/<int:id>")
def edit(id):
    conn = get_db()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", task=task)

# 更新処理
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    content = request.form["task"]
    conn = get_db()
    conn.execute("UPDATE tasks SET content = ? WHERE id = ?", (content, id))
    conn.commit()
    conn.close()
    return redirect("/")

#最初にDB作る
init_db()

app.run(debug=True)
