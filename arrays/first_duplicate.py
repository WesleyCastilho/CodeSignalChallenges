class FirstDuplicate():
    def first_duplicate(self):
        mySet = set()
        for element in self:
            if element in mySet:
                return element
            mySet.add(element)
        return -1
