from protein import Protein
from extraction import construct_protein_list


def clasterization_via_ligand_size(proteins_list):
    small = []
    medium = []
    big = []
    without_formula = []

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


def clasterization_via_ligand_size(proteins_list):
    small = []
    medium = []
    big = []
    without_formula = []

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

