class Protein:
    def __init__(self, id, name=None, sequence=None, azole=None, azole_group=None, structure=None):
        self.id = id
        self.name = name
        self.sequence = sequence
        self.azole = azole
        self.azole_group = azole_group
        self.structure = structure


    def __str__(self):
        return '  ID: ' + self.id + '\n' + \
               '  Name: ' + self.name + '\n' + \
               '  Sequence: ' + self.sequence + '\n' + \
               '  Azole: ' + self.azole + '\n' + \
               '  Azole_group: ' + self.azole_group + '\n'


def find_protein_with_id(proteins, id):
    for protein in proteins:
        if protein.id == id:
            return protein

    return None
