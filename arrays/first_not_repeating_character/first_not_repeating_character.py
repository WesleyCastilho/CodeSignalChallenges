from collections import Counter


class FirstNotRepeating:
    def first_not_repeating(self):
        c = Counter(self)
        for i in self:
            if c[i] == 1:
                return i
        return '_'
