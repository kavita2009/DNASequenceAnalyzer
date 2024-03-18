#Kavita Karmarkar
# dna_analysis.py
#This file contains the main algorithm behind the DNASequenceAnalyzer program (this file actually analyzes the DNA/user input)
# Completed on March 8th, 2024

'''The DNASequence class takes in an arbitrary sequence (ex, AGTGTGCTCA) 
The get_sequence method retrieves the sequence from the user input on the React frontend. 
The count_nucleotides method '''
class DNASequence:
    def __init__(self, sequence=""):
        self._sequence = sequence

    def set_sequence(self, sequence):
        self._sequence = sequence

    def get_sequence(self):
        return self._sequence

    def count_nucleotides(self):
      '''nucleotide_counts is a dictionary corresponding the occurance of each nucleotide to the specific letter (A, G, T, C).'''
        nucleotide_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        total_nucleotides = len(self._sequence)
        for nucleotide in self._sequence:
            if nucleotide in nucleotide_counts:
                nucleotide_counts[nucleotide] += 1
        '''percentages returns the percentage frequency of each nucleotide given the sequence length'''
        percentages = {key: (count / total_nucleotides) * 100 for key, count in nucleotide_counts.items()}
        return percentages

'''The DNAAnalyzer class is simply running the DNASequence class'''
class DNAAnalyzer:
    def __init__(self):
        self.dna_sequence = DNASequence()

    def analyze_sequence(self, sequence):
        self.dna_sequence.set_sequence(sequence)
        return self.dna_sequence.count_nucleotides()
    
