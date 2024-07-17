from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), 'products.db')

# Fonction pour récupérer les données depuis la base de données SQLite
def fetch_data_from_sqlite():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

# Fonction pour lire les données depuis un fichier JSON
def read_json_file(filename):
    import json
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Fonction pour lire les données depuis un fichier CSV
def read_csv_file(filename):
    import csv
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
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
    elif source == 'sql':
        try:
            products = fetch_data_from_sqlite()
            return render_template('product_display.html', products=products)
        except Exception as e:
            return render_template('product_display.html', error="Erreur de base de données : " + str(e))
    else:
        return render_template('product_display.html', error="Source incorrecte")

if __name__ == '__main__':
    app.run(debug=True)
