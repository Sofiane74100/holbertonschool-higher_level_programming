class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    
    def __next__(self):
        item = next(self.iterator)  # Obtenez le prochain élément de l'itérateur
        self.count += 1  # Incrémentez le compteur
        return item
    
    def get_count(self):
        return self.count

# Code de test
if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
