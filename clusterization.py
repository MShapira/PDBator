from cluster import Cluster


def clusterisation_via_ligand_size(proteins_list):
    cluster = Cluster()

    for protein in proteins_list:
        if cluster.azole_type_dictionary.get(protein.azole_group) is None:
            cluster.azole_type_dictionary[protein.azole_group] = []
        cluster.azole_type_dictionary[protein.azole_group].append(protein)

    return cluster.azole_size_dictionary


def clusterisation_via_ligand_type(proteins_list):
    cluster = Cluster()

    for protein in proteins_list:
        if cluster.azole_type_dictionary.get(protein.azole) is None:
            cluster.azole_type_dictionary[protein.azole] = []
        cluster.azole_type_dictionary[protein.azole].append(protein)

    return cluster.azole_type_dictionary