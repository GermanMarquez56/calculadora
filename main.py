from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return '''
        
        aplicacion web con flask-afsr
        <h1>calculadora</h1>

'''