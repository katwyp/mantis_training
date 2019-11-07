

class Project:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%s" % self.name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name
