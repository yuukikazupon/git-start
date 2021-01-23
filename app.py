from flask import Flask
from flask import render_template,request,redirect,url_for
import json
import sqlite3

app=Flask(__name__)

# @app.route('/')
# def hello():
#     name="Hello World"
#     return name

# @app.route("/dot-pro")
# def hive():
#     return "Hello,dot-pro!"

#flask1 課題
# @app.route("/profile")
# def pro():
#     return "Hello profile"

# @app.route("/hive")
# def hive():
#     return render_template("index.html")
#
# @app.route("/var")
# def var():
#     message="こんにちは"
#     return render_template("var.html",message=message)

# @app.route("/length")
# def leng():
#     message="こん"
#     return render_template("length.html",message=message)
#
# @app.route("/greeting")
# def greeting():
#     message_list=["おはよう", "こんにちは", "こんばんは"]
#     return render_template("greeting.html",message_list=message_list)

#flask2 課題
# @app.route("/fizzbuzz")
# def fizzbuzz():
#     num_list=[]
#     for i in range(1,16):
#         num_list.append(i)
#     return render_template("fizzbuzz.html",num_list=num_list)

# @app.route("/get")
# def get():
#     name=request.args.get("name")
#     return render_template("get.html",title="Flask GET request",name=name   )

#flask3 課題

# @app.route("/get")
# def sosu():
#     count=0
#     number= request.args.get("number")
#     for i in range(2,int(number)):
#         if int(number)%i == 0:
#             count+=1
#     # print(request.args)
#     return render_template("sosu.html",title="素数判定",number=number,count=count)

# def get_profile():
#     file_json="data/profile.json"
#     prof = open(file_json,encoding="utf-8")
#     json_str = prof.read()
#     prof.close()
#
#     # print(json_str)
#     prof_dict = json.loads(json_str)
#     # print(prof_dict)
#     return prof_dict

def get_profile():
    conn=sqlite3.connect("profile.sqlite3")
    c=conn.cursor()
    prof_list=[]
    for i in c.execute("select * from persons"):
        # print(type(i))
        # print(i)
        prof_list.append({"id":i[0],"name":i[1],"age":i[2],"sex":i[3]})
    conn.commit()
    conn.close()
    return prof_list



# def update_profile(prof):
#     f=open("data/profile.json","w")
#     json.dump(prof,f)
#     f.close()

def update_profile(prof):
    conn=sqlite3.connect("profile.sqlite3")
    c=conn.cursor()
    c.execute("update persons set name='{0}',age={1},sex='{2}' \
    where id={3}".format(prof["name"],prof["age"],prof["sex"],prof["id"]))
    conn.commit()
    conn.close()

def addsql(prof):
    conn=sqlite3.connect("profile.sqlite3")
    c=conn.cursor()
    c.execute("insert into persons(name,age,sex) values('{0}',{1},'{2}')"\
    .format(prof["name"],prof["age"],prof["sex"]))
    conn.commit()
    conn.close()

def deletesql(prof):
    conn=sqlite3.connect("profile.sqlite3")
    c=conn.cursor()
    c.execute("delete from persons where id={0}".format(prof["id"]))
    conn.commit()
    conn.close()

# @app.route("/")
# def root():
#     return redirect(url_for("profile"))

# @app.route("/profile")
# def profile():
#     prof_dict = get_profile()
#     return render_template("profile.html",title="json",users=prof_dict)

@app.route("/profile")
def profile():
    prof_dict = get_profile()
    return render_template("profile.html",title="sql",user=prof_dict)

# @app.route("/edit/<int:id>")
# def edit(id):
#     prof_dict = get_profile()
#     user_dict=""
#     for data in prof_dict :
#         if data["id"]==id:
#             user_dict=data
#     return render_template("edit.html",title="json",user=user_dict)

@app.route("/edit/<int:id>")
def edit(id):
    prof_list=get_profile()
    # prof_dict=prof_list[id-1]
    prof_num_list=[]
    for i in range(len(prof_list)):
        prof_num_list.append(prof_list[i]["id"])
        if prof_list[i]["id"]==id:
            num=prof_num_list.index(id)
            prof_dict=prof_list[num]

    return render_template("edit.html",title="sql",user=prof_dict)


# @app.route("/update",methods=["POST"]) #質問する
# def update():
#     id_str=request.form["id"]
#     name=request.form["name"]
#     age=request.form["age"]
#     sex=request.form["sex"]
#
#     prof_dict_before = get_profile()
#     prof_dict_after = []
#     # print(prof_dict_before)
#     for data in prof_dict_before :
#         if str(data["id"]) == id_str:
#             prof_dict_after.append({"id":int(id_str),"name":name,"age":age,"sex":sex})
#         else:
#             prof_dict_after.append(data)
#
#     update_profile(prof_dict_after)
#
#     return redirect(url_for("profile"))

@app.route("/update/<int:id>",methods=["POST"])
def update(id):
    prof_list=get_profile()
    prof_num_list=[]
    # print(prof_list)
    # prof_dict=prof_list[id-1]
    for i in range(len(prof_list)):
        prof_num_list.append(prof_list[i]["id"])
        if prof_list[i]["id"] == id:
            num=prof_num_list.index(id)
            prof_dict=prof_list[num]
            prof_dict["name"]=request.form["name"]
            prof_dict["age"]=request.form["age"]
            prof_dict["sex"]=request.form["sex"]
    # print(prof_dict["name"])
            update_profile(prof_dict)
    return redirect(url_for("profile"))

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    prof_list=get_profile()
    prof_num_list=[]
    for i in range(len(prof_list)):
        prof_num_list.append(prof_list[i]["id"])
        if prof_list[i]["id"]==id:
            num=prof_num_list.index(id)
            # print(num)
            prof_dict=prof_list[num]

    return render_template("delete.html",user=prof_dict)

@app.route("/add/profile",methods=["POST"])
def addprofile():
    prof_dict={}
    prof_dict["name"]=request.form["name"]
    prof_dict["age"]=request.form["age"]
    prof_dict["sex"]=request.form["sex"]
    addsql(prof_dict)
    return redirect(url_for("profile"))

@app.route("/delete/profile/<int:id>",methods=["POST"])
def deleteprofile(id):
    # print(request.form)
    prof_dict={}
    # print(request.form["id"])
    prof_dict["id"]=request.form["id"]
    deletesql(prof_dict)
    return redirect(url_for("profile"))







if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,threaded=True)
