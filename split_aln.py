#!/usr/bin/env python3
"""
Script to split FASTA sequences into three regions:
1. 5' end (1 to first marker)
2. Core (first marker to second marker)
3. 3' end (second marker to end)
"""

def read_fasta(filename):
    """Read FASTA file and return dictionary of sequences"""
    sequences = {}
    current_id = None
    current_seq = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_id is not None:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:]  # Remove '>'
                current_seq = []
            else:
                current_seq.append(line)
        
        # Don't forget the last sequence
        if current_id is not None:
            sequences[current_id] = ''.join(current_seq)
    
    return sequences

def find_sequence_position(seq, target):
    """Find position of target sequence (case-insensitive)"""
    seq_upper = seq.upper()
    target_upper = target.upper()
    pos = seq_upper.find(target_upper)
    return pos

def write_fasta(filename, sequences):
    """Write sequences to FASTA file"""
    with open(filename, 'w') as f:
        for seq_id, seq in sequences.items():
            f.write(f'>{seq_id}\n')
            # Write sequence in lines of 60 characters
            for i in range(0, len(seq), 60):
                f.write(seq[i:i+60] + '\n')

def main():
    # Input file
    input_file = input("Enter FASTA filename: ")
    
    # Reference sample to search for coordinates
    reference_sample = 'LSDV_KX894508.1_155920_2012_Israel_19_Dec_2012'
    
    # Marker sequences
#    marker1 = 'attagctatgatttatgttt'  # ~16100 OLD
  #  marker1 = 'acataatagacattatcgta'  # 18900
    marker1 = 'tattacttaaacacataat'
    marker2 = 'tagatataagcgacgagat'  # ~115500
    
    print(f"\nReading FASTA file: {input_file}")
    sequences = read_fasta(input_file)
    print(f"Found {len(sequences)} sequences")
    
    # Find the reference sequence
    if reference_sample not in sequences:
        print(f"\nERROR: Reference sample '{reference_sample}' not found in FASTA file!")
        print("\nAvailable sequences:")
        for seq_id in list(sequences.keys())[:10]:
            print(f"  {seq_id}")
        if len(sequences) > 10:
            print(f"  ... and {len(sequences) - 10} more")
        return
    
    first_seq = sequences[reference_sample]
    print(f"\nSearching for markers in reference sequence: {reference_sample}")
    pos1 = find_sequence_position(first_seq, marker1)
    pos2 = find_sequence_position(first_seq, marker2)
    
    if pos1 == -1:
        print(f"ERROR: Marker 1 '{marker1}' not found!")
        return
    if pos2 == -1:
        print(f"ERROR: Marker 2 '{marker2}' not found!")
        return
    
    # Calculate cut points (end of marker sequences)
    cut1 = pos1 + len(marker1)
    cut2 = pos2
    
    print(f"\nMarker 1 found at position: {pos1}")
    print(f"  Cut point 1 (end of marker 1): {cut1}")
    print(f"Marker 2 found at position: {pos2}")
    print(f"  Cut point 2 (start of marker 2): {cut2}")
    
    # Split all sequences
    five_prime = {}
    core = {}
    three_prime = {}
    
    for seq_id, seq in sequences.items():
        five_prime[seq_id] = seq[:cut1]
        core[seq_id] = seq[cut1:cut2]
        three_prime[seq_id] = seq[cut2:]
    
    # Write output files
    print("\nWriting output files...")
    write_fasta('all.5end.aln', five_prime)
    print(f"  all.5end.aln: bases 1-{cut1}")
    
    write_fasta('all.core.aln', core)
    print(f"  all.core.aln: bases {cut1}-{cut2}")
    
    write_fasta('all.3end.aln', three_prime)
    print(f"  all.3end.aln: bases {cut2}-end")
    
    print("\nDone!")
    print(f"\nSummary:")
    print(f"  5' end length: {len(five_prime[reference_sample])} bases")
    print(f"  Core length: {len(core[reference_sample])} bases")
    print(f"  3' end length: {len(three_prime[reference_sample])} bases")
    print(f"  Total: {len(first_seq)} bases")

if __name__ == '__main__':
    main()
