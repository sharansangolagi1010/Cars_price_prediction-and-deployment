from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "chal madarchod"

if __name__=="__main__":
    app.run(debug=True)




