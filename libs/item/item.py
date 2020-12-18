class Item:
    def __init__(self, x, y, name, photo):
        """
        PRE : x et y doivent être des integers, name et photo doivent être un str
        POST : Donne x à x, y à y, donne name à itemName et photo à pType
        """
        self.x = x
        self.y = y
        self.itemName = name
        self.pType = photo

    @property
    def id(self):
        return "{},{}".format(self.x, self.y)
