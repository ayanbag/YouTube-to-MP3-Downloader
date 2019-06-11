from flask import Flask,render_template,redirect,request
import requests
app= Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/download",methods=['GET', 'POST'])
def download():
    if request.method=="POST":
        result=request.form["name"]
        import app_data
        a=app_data.main_dw(result)
        if len(a)==0:
            return render_template("fail.html")
        else:
            return render_template("success.html",result=a)

if __name__=="__main__":
    app.run(debug=True)