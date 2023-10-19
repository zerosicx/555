# -------------------------- FUNCTIONS --------------------------
from itertools import permutations
import csv

def generate_motifs(input_str, length):
    # Check if the length is valid
    if length <= 0 or length > len(input_str):
        return []

    all_motifs = set()  # Use a set to ensure unique motifs

    # Generate all permutations of the characters in the input string
    char_permutations = permutations(input_str, length)

    # Create motifs from the permutations
    for motif_chars in char_permutations:
        motif = ''.join(motif_chars)
        all_motifs.add(motif)

    return list(all_motifs)  # Convert the set back to a list

def generate_CSV(motifs):
    # Read the file "mhc2023.txt". It should have the format <1 or 0> <peptide sequence>
    # Format the data such that it's in csv format with the following column titles: class,
    # sequence, <every possible motif> where the values of each motif are 1 or 0,
    # 1 indicating the peptide contains the motif and 0 indicating that it doesn't.
    # Save the title line and each line after that to a file called mhc2023motifs.csv

    input_file = "mhc2023.txt"
    output_file = "mhc2023motifs.csv"

    # Create a dictionary to store motifs and their occurrence status
    motif_data = {motif: 0 for motif in motifs}

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        # Create a CSV writer
        csv_writer = csv.writer(outfile)
        
        # Write the column titles to the CSV file
        column_titles = ["class", "sequence"] + list(motif_data.keys())
        csv_writer.writerow(column_titles)
        
        # Process each line in the input file
        for line in infile:
            line = line.strip()
            parts = line.split()
            class_label = parts[0]
            sequence = parts[1]
            
            # Update motif_data based on the sequence
            for motif in motifs:
                motif_data[motif] = int(motif in sequence)
            
            # Create a list of values for the CSV row
            row_data = [class_label, sequence] + list(motif_data.values())
            
            # Write the row to the CSV file
            csv_writer.writerow(row_data)

    print(f"CSV file '{output_file}' has been generated.")


# -------------------------- MAIN FUNCTION ----------------------
def main():
    values = "";
    
    # Amino acid string:
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    motif_length = 3
    motifs = generate_motifs(amino_acids, motif_length)
    generate_CSV(motifs)
    # print(motifs)

    return



# -------------------------- execution --------------------------
main()
