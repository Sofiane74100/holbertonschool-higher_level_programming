from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), 'products.db')

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def read_csv_file(filename):
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def fetch_data_from_sqlite():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    products = cursor.fetchall()
    conn.close()
    # Convert the results to a list of dictionaries
    result = []
    for product in products:
        result.append({
            'id': product[0],
            'name': product[1],
            'category': product[2],
            'price': product[3]
        })
    return result

@app.route('/products')
def display_products():
    source = request.args.get('source', 'json')
    product_id = request.args.get('id')
    
    try:
        if source == 'json':
            products = read_json_file('products.json')
        elif source == 'csv':
            products = read_csv_file('products.csv')
        elif source == 'sql':
            products = fetch_data_from_sqlite()
        else:
            return render_template('product_display.html', error="Source incorrecte")

        if product_id:
            products = [p for p in products if p['id'] == int(product_id)]
            if not products:
                return render_template('product_display.html', error="Produit non trouvé")

        return render_template('product_display.html', products=products)
    
    except FileNotFoundError:
        return render_template('product_display.html', error="Fichier non trouvé.")
    except Exception as e:
        return render_template('product_display.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
