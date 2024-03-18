#Kavita Karmarkar
#Create a python server to interact with React, along with routes and associated functions
#Completed on March 8th, 2024
# app.py


#Flask allows us to create a server so we can interact with React
from flask import Flask, request, jsonify
from dna_analysis import DNAAnalyzer, DNAComplement
#Take care of any cross-origin issues
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
analyzer = DNAAnalyzer()
complementer = DNAComplement()

#React will come to this route
@app.route('/analyze', methods=['POST'])

#Function to analyze DNA sequence
def analyze_sequence():
    data = request.get_json()
    sequence = data.get('sequence', '')
    percentages = analyzer.analyze_sequence(sequence)
    return jsonify(percentages)

#If I were to continue working on the code, I would complement DNA from the user's sequence and this is where axios would point to.
@app.route('/complement', methods=['POST'])
def complement_sequence():
    data = request.get_json()
    sequence = data.get('sequence', '')
    complemented_sequence = complementer.complement_sequence(sequence)
    return jsonify({"complemented_sequence": complemented_sequence})

if __name__ == '__main__':
    app.run(debug=True)
