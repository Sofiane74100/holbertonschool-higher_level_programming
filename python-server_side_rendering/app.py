from flask import Flask, render_template, request

app = Flask(__name__)

# Fonction pour lire le fichier JSON et retourner les données
def read_json_file(filename):
    import json
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Fonction pour lire le fichier CSV et retourner les données
def read_csv_file(filename):
    import csv
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(dict(row))
    return data

# Route pour afficher les données des produits
@app.route('/products')
def display_products():
    source = request.args.get('source', 'json')

    if source == 'json':
        try:
            products = read_json_file('products.json')
            return render_template('product_display.html', products=products)
        except FileNotFoundError:
            return render_template('product_display.html', error="Fichier JSON non trouvé.")
    elif source == 'csv':
        try:
            products = read_csv_file('products.csv')
            return render_template('product_display.html', products=products)
        except FileNotFoundError:
            return render_template('product_display.html', error="Fichier CSV non trouvé.")
    else:
        # Gérer le cas où le paramètre source est incorrect
        return render_template('product_display.html', error="Wrong source")

if __name__ == '__main__':
    app.run(debug=True)
