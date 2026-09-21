from flask import Flask, render_template, request, redirect, url_for
import storage

app = Flask(__name__)

@app.route("/")
def index():
    tasks = storage.load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if title:
        tasks = storage.load_tasks()
        task = {"id": len(tasks) + 1, "title": title, "done": False}
        tasks.append(task)
        storage.save_tasks(tasks)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)