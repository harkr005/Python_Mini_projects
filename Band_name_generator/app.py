from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    city = request.form['city']
    animal = request.form['animal']
    band_name = f"{city} {animal}"
    return render_template('index.html', band_name=band_name)

if __name__ == '__main__':
    app.run(debug=True)