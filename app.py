from flask import Flask

app = Flask(__name__)
@app.route("/")

def anji():
    return "helo this is UAT CUSTEMER FINAL environment"
if __name__=="__main__":
    app.run(debug=True,port=5000)
