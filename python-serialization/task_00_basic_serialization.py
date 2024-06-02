import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_and_deserialize(filename):
    """Load and deserialize a JSON file to recreate a Python dictionary."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
