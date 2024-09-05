import connexion 
from flask import render_template,url_for

app = connexion.App(__name__)
app.add_api("api.yml")

@app.route("/")
def home():
    return render_template('homeUsers.html')

if __name__ == "__main__":
    app.run(port= 9000,debug= True)