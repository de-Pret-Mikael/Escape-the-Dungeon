class Chest:
    def __init__(self, x, y, name, photo):
        self.x = x
        self.y = y
        self.itemName = name
        self.pType = photo

    @property
    def id(self):
        return "{},{}".format(self.x, self.y)
