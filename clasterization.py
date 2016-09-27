from claster import Claster
from extraction import construct_protein_list


def clasterization_via_ligand_size(proteins_list):
    claster = Claster()
    for protein in proteins_list:
        if protein.azole_group == 1:
            claster.small.append(protein)
        elif protein.azole_group == 2:
            claster.medium.append(protein)
        elif protein.azole_group == 3:
            claster.big.append(protein)
        else:
            claster.without_formula.append(protein)

    return claster


def clasterization_via_ligand_type(proteins_list):

    for protein in proteins_list:
        if protein.azole_group == 1:
            small.append(protein)
        elif protein.azole_group == 2:
            medium.append(protein)
        elif protein.azole_group == 3:
            big.append(protein)
        else:
            without_formula.append(protein)

    return small, medium, big, without_formula

