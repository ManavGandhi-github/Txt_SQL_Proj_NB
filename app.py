from flask import Flask, render_template, request
import database
import nlp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        intent = nlp.process_query(query)
        result = database.run_query(intent)
        return render_template('home.html', result=result)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
