from flask import Flask, render_template
import os





app = Flask(__name__, template_folder="frontend")

@app.route('/')
def hello():
    container_name = os.getenv("CONTAINER_NAME")
    return render_template('index.html', container_name=container_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
