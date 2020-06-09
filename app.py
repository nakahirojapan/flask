from flask import Flask , render_template
app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)
    
    @app.route("/test")
    def test():
        return render_template("test.html")