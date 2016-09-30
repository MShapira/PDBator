import bio_utility, utility, clusterization

# Create folder for PDB structures and filling it with PDB files.
folder_name = utility.folder_creation(utility.folder_path_generation())
# Filling in the protein sequences.
protein_list = bio_utility.fill_proteins_sequences(bio_utility.construct_protein_list(
    input("Enter the filename: ")), folder_name, "PDBs")
# Obtaining and writing down the results of alignment in the "size" cluster
bio_utility.saving_alignment_results(bio_utility.alignment_at_cluster_group(
    clusterization.clusterisation_via_ligand_size(protein_list)), folder_name, 'ligand_size')
# Obtaining and writing down the results of alignment in the "size" cluster
bio_utility.saving_alignment_results(bio_utility.alignment_at_cluster_group(
    clusterization.clusterisation_via_ligand_type(protein_list)), folder_name, 'ligand_type')

print("All has been done, master!")