class Cluster(object):
    def __init__(self, name=None, index=None):
        self.name = name
        self.index = index

        self.azole_size_dictionary = {}

        self.azole_type_dictionary = {}