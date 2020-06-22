from flask import Flask,request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/method', methods=['GET','POST'])
def method():
    if request.method == 'GET':
        # args_dict = request.args.to_dict() 
        # print(args_dict)
        num = request.args["num"]
        name = request.args.get("name")
        return "GET으로 전달된 데이터({}, {})".format(num, name)
    else:
        num = request.args["num"]
        name = request.args.get("name")
        return "POST로 전달된 데이터({}, {})".format(num, name)
@app.route('/hello')
def hellohtml():
    return render_template("hello.html")
@app.route('/naver')
def naver():
    return render_template('naver.html')


if __name__=='__main__':
    app.run(debug=True)
