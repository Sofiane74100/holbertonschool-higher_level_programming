import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Création de la table Products si elle n'existe pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insertion des données d'exemple dans la table Products
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Ordinateur portable', 'Électronique', 799.99),
        (2, 'Mug à café', 'Articles ménagers', 15.99)
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
