from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def main():
    if(request.method == "GET"):
        return render_template("personinfo2.html")
    else:
        return GetInfo()
    
def GetInfo():
    global headings, data
    headings = ("Course","Teacher")
    course1 = request.form.get("txtcoursename1")
    teacher1 = request.form.get("txtteacher1")
    course2 = request.form.get("txtcoursename2")
    teacher2 = request.form.get("txtteacher2")

    data = (
        (course1, teacher1),
        (course2, teacher2)
        )
    return DisplayInfo()

def DisplayInfo():
    return render_template("output2.html",headings=headings,data=data)


if __name__=="__main__":
    app.run();
