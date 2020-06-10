from flask import Flask , render_template
app = Flask(__name__)

@app.route("/test")
def test():
    name = "flask"
    return render_template("test.html",name = name)
    

@app.route("/greet/<text>")
def greet(text):
    return text + "さん、こんにちは"

    
    
@app.errorhandler(404)
def notfound(code):
    return "404ペーーージ"

# ２日目
@app.route("/dbtest")
def dbtest():
    # データベースに接続
    conn =sqlite3.connect('flask.db')
    # どこのデータを抜くかカーソルをあてる。カーソル→目印
    c =conn.cursor()
    
    # 実行する
    c.execute("select name,age,adress from users where id =1")
    
    # fetchone フェッチ　実際に取得する
    user_info =c.fetchone()
    # データベース接続終了
    c.close()
    
    # user_info の中身を確認
    print(user_info)
    return render_template("dbtest.html",user_info =user_info)

























    
if __name__ == "__main__":
    app.run(debug=True)   
 
    