from numpy import genfromtxt
from utility import b2str, write_to_file, folder_creation
from protein import Protein
from pypdb import get_pdb_file
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
from Bio.Align import MultipleSeqAlignment
import os

# simple array construction (array of proteins)
# Params file_name with input data(string)
def construct_protein_list(file_name):
    proteins_list = []

    input_data = genfromtxt(file_name, dtype=None, delimiter=';', names=True)
    for line in input_data:
        current_protein = Protein(id=b2str(line['pdb']), azole=b2str(line['azole']), azole_group=b2str(line['azole_group']))
        proteins_list.append(current_protein)

    return proteins_list


# extraction sequence from pdb file
# Params: filename(string)
def extract_sequence(file_name):
    file = open(file_name, 'r')
    seq = ''

    for record in SeqIO.parse(file, "pdb-seqres"):
        if len(record.seq) > len(seq):
            seq = record.seq

    file.close()
    return seq


# filling protein sequences from pdb files
# Params: protein_list(array)
def fill_proteins_sequences(proteins_list, folder_path, special_folder):

    for protein in proteins_list:
        pdb_structure = get_pdb_file(protein.id, filetype='pdb', compression=False)

        if not os.path.exists(folder_path + '/' + special_folder):
            os.makedirs(folder_path + '/' + special_folder)

        file = write_to_file(str(protein.id), "pdb", pdb_structure, folder_path + "/" + special_folder)
        protein.sequence = str(extract_sequence(file.name))

    return proteins_list


# making multiple alignment per group of clusters
# Params: dictionary(dictionary)
def alignment_at_cluster_group(dictionary):
    keys = dictionary.keys()
    cluster_group_alignment = []

    for key in keys:
        alignmented_group = []
        alignment = []

        for protein in dictionary[key]:
            alignment.append(SeqRecord(Seq(protein.sequence, generic_protein), id=protein.id))

        maxlen = max(len(protein.seq) for protein in alignment)

        for protein in alignment:
            print(len(protein.seq))
            if len(protein.seq) != maxlen:
                sequence = str(protein.seq).ljust(maxlen, '.')
                protein.seq = Seq(sequence)

        assert all(len(protein.seq) == maxlen for protein in alignment)

        alignmented_group.append(key)
        alignmented_group.append(MultipleSeqAlignment(alignment, generic_protein))

        cluster_group_alignment.append(alignmented_group)

    return cluster_group_alignment


# saving results after local alignment
# Params: cluster_group_alignment(array with arrays, where [0] - title, [1:-1] - objects)
def saving_alignment_results(cluster_group_alignment, folder_name, cluster_type_name):
    if not os.path.exists(folder_name + "/results"):
            os.makedirs(folder_name + "/results")

    file = open(folder_name + "/results" + "/" + cluster_type_name + ".phy", "w")

    for alignmented_group in cluster_group_alignment:

        file.write(alignmented_group[0] + "\n")
        for align in alignmented_group[0:-1]:
            for obj in align:
                file.write(obj.id + " " + obj.seq)
    file.close()
