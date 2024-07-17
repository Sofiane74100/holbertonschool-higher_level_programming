import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Création de la table Products si elle n'existe pas déjà
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Vérification si les données existent déjà
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]
    
    # Insertion des données d'exemple dans la table Products seulement si la table est vide
    if count == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
