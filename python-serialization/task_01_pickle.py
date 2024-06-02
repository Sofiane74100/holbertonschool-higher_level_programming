import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError) as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (OSError, pickle.PickleError, EOFError) as e:
            print(f"Error deserializing object: {e}")
            return None
