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
