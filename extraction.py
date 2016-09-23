from numpy import genfromtxt
from utility import b2str, write_to_file, folder_creation
from protein import Protein
from Bio.PDB import PDBList, PPBuilder, PDBParser
from pypdb import get_pdb_file
from os import walk


def construct_protein_list(file_name):
    proteins_list = []

    input_data = genfromtxt(file_name, dtype=None, delimiter=';', names=True)
    for line in input_data:
        current_protein = Protein(id=b2str(line['pdb']), azole=b2str(line['azole']), azole_group=b2str(line['azole_group']))
        proteins_list.append(current_protein)

    return proteins_list


def fill_proteins_sequences(proteins_list):
    ppb = PPBuilder()
    parser = PDBParser()
    folder_path = folder_creation(input("Enter foldername to store pdb files: "))

    for protein in proteins_list:
        pdb_structure = get_pdb_file(protein.id, filetype='pdb', compression=False)
        file = write_to_file(str(protein.id), "pdb", pdb_structure, folder_path)
        structure = parser.get_structure(protein.id, file.name)

        for pp in ppb.build_peptides(structure):
            print(pp.get_sequence)



fill_proteins_sequences(construct_protein_list(input("filename: ")))