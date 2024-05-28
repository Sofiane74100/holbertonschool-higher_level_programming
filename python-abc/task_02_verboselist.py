class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        super().extend(iterable)
        count = len(iterable)
        print(f"Extended the list with [{count}] items.")
    
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=None):
        if index is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
        else:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
        return item  # Make sure to return the popped item
