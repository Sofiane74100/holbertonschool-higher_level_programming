from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Lire le fichier JSON
    try:
        with open('items.json') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erreur lors de la lecture du fichier JSON : {e}")
        items_list = []

    # Rendre le template avec les données
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
