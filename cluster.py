class Cluster(object):
    def __init__(self, name=None, index=None):
        self.name = name
        self.index = index

        self.small = []
        self.medium = []
        self.big = []
        self.without_formula = []

        self.azole_dictionary = {}