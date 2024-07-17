import requests

def test_items_page():
    base_url = 'http://127.0.0.1:5000'  # Assurez-vous que le port est correct
    response = requests.get(f'{base_url}/items')
    assert response.status_code == 200, f"Failed: Status code is {response.status_code}"
    content = response.text
    assert 'Items List' in content, "Failed: Items page title not found"
    assert 'Livre Python' in content, "Failed: 'Livre Python' not found in items list"
    assert 'Tasse Flask' in content, "Failed: 'Tasse Flask' not found in items list"
    assert 'Autocollant Jinja' in content, "Failed: 'Autocollant Jinja' not found in items list"

if __name__ == '__main__':
    test_items_page()
