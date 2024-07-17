import requests

def test_invalid_source():
    url = 'http://localhost:5000/products?source=xml'
    response = requests.get(url)
    content = response.text

    assert 'Wrong source' in content, "Failed: Wrong source error not found"

if __name__ == "__main__":
    test_invalid_source()
    print("Test passed successfully.")
