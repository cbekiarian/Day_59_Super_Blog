from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
response = requests.get(url = "https://api.npoint.io/f744342cc40afa5df317").json()

@app.route("/")
def server():

    return render_template("index.html", posts = response)


@app.route("/<name>")
def change_site(name):

    return render_template(name)


@app.route("/posts/<int:id>")
def change_post(id):
    for potential_post in response:
        print(potential_post)
        if potential_post["id"] == id:
            post = potential_post
    return render_template("post.html", post=post )




if __name__ == "__main__":
    app.run()