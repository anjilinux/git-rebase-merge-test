from flask import Flask

app = Flask(__name__)
@app.route("/")

def anji():
    return "helo this is UAT CUSTEMER FINAL environment"
if __name__=="__main__":
    app.run(debug=True,port=5000)

a = 10 
b = 5 
c = a + b 
print(c)

from flask import Flask


