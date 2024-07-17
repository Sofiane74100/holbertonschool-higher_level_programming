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
    product_id = request.args.get('id')

    if source == 'json':
        try:
            products = read_json_file('products.json')
        except FileNotFoundError:
            return render_template('product_display.html', error="Fichier JSON non trouvé.")
    elif source == 'csv':
        try:
            products = read_csv_file('products.csv')
        except FileNotFoundError:
            return render_template('product_display.html', error="Fichier CSV non trouvé.")
    else:
        return render_template('product_display.html', error="Paramètre source incorrect.")

    if product_id:
        product = next((p for p in products if p['id'] == int(product_id)), None)
        if not product:
            return render_template('product_display.html', error="Produit non trouvé.")

        # Afficher seulement le produit sélectionné si l'id est fourni
        return render_template('product_display.html', products=[product])
    else:
        # Afficher tous les produits
        return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
