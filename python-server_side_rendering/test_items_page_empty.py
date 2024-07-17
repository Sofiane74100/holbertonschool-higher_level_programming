import requests

def test_items_page_empty():
    base_url = 'http://127.0.0.1:5000'  # Assurez-vous que le port est correct
    response = requests.get(f'{base_url}/items')
    assert response.status_code == 200, f"Failed: Status code is {response.status_code}"
    content = response.text
    assert 'No items found' in content, "Failed: Empty items list message not displayed"

if __name__ == '__main__':
    test_items_page_empty()
