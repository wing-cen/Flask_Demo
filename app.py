from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  #无论是GET还是POST都处理这个请求
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])   #只有GET的时候处理这个请求
def signin_form():
    return render_template('login.html')

@app.route('/signin', methods=['POST'])  #只有POST的时候处理这个请求
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('index.html', username=username)
    return render_template('login.html', message='Bad username or password', username=username)
 
if __name__ == '__main__':   #模块判断，判断当前文件是否在主程序中运行还是import进来的
    app.run()