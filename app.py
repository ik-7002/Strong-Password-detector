from flask import Flask,render_template,request
from analyzer import analyze_password

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def Password_generator():

    result=None

    if request.method == "POST":

        password=request.form["password"]
        username=request.form["username"]
        generate_password=request.form.get("generate_password","no")

        result=analyze_password(password,username,generate_password)

    return render_template('index.html',result=result)

if __name__=="__main__":
    app.run(debug=True)
