from flask import render_template
import connexion


app = connexion.App(__name__, specification_dir = "./")
app.add_api("simple.yml")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__" :
    app.run(port=9000,debug= True)
