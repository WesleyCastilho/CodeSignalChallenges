class FirstDuplicate:
    def first_duplicate(self):
        my_set = set()
        for element in self:
            if element in my_set:
                return element
            my_set.add(element)
        return -1
