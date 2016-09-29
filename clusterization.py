from cluster import Cluster


def clusterization_via_ligand_size(proteins_list):
    cluster = Cluster()
    for protein in proteins_list:
        if protein.azole_group == 1:
            cluster.small.append(protein)
        elif protein.azole_group == 2:
            cluster.medium.append(protein)
        elif protein.azole_group == 3:
            cluster.big.append(protein)
        else:
            cluster.without_formula.append(protein)

    return cluster


def clusterization_via_ligand_type(proteins_list):
    cluster = Cluster()

    for protein in proteins_list:
        if cluster.azole_dictionary.get(protein.azole) is None:
            cluster.azole_dictionary[protein.azole] = []
        cluster.azole_dictionary[protein.azole].append(protein.id)

    return cluster