//Kavita Karmarkar
// This is the user interface, written in ReactJS using hooks
// Completed on March 8th, 2024
// App.js

import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios'; // Communication
import Lottie from 'lottie-web'; // Animations but I did not implement them
import Dna from './lotties/dna.json';
import Dna300 from './images/dna.png';

const DnaAnimation = () => {
  const lottieContainer = useRef(null);

  useEffect(() => {
    const anim = Lottie.loadAnimation({
      container: lottieContainer.current,
      renderer: 'svg',
      loop: true,
      autoplay: true,
      animationData: Dna,
    });

    return () => {
      anim.destroy();
    };
  }, []);
  return <div ref={lottieContainer} />;
};

function App() {
  // Hooks
  const [sequence, setSequence] = useState('');
  const [percentages, setPercentages] = useState({});
  const [complementedSequence, setComplementedSequence] = useState('');

  const handleChange = (e) => {
    setSequence(e.target.value);
  };

  const handleComplement = async () => {
    // This is where we interact with Python and get data. If I were to continue writing this code, I would implement the complement functionality.
    try {
      const response = await axios.post('http://127.0.0.1:5000/complement', { sequence });
      alert('Analysis complete!')
      setComplementedSequence(response.data.complemented_sequence);
    } catch (error) {
      alert('Error complementing sequence:', error);
    }
  };

  const handleSubmit = async () => {
    // This is where we interact with Python and get data
    try {
      const response = await axios.post('http://127.0.0.1:5000/analyze', { sequence });
      alert('Analysis complete! Click OK to see results.')
      setPercentages(response.data);
    } catch (error) {
      console.error('Error analyzing sequence:', error);
    }
  };

  return (
    <div>
      <h1>DNA Sequence Analyzer</h1>
      <h3>Provide a DNA sequence and we will break it down into its constituent bases</h3>
      <textarea
        rows="5"
        cols="50"
        placeholder="Enter DNA sequence..."
        value={sequence}
        onChange={handleChange}
      ></textarea>
      <br />
      <button onClick={handleSubmit}>Analyze</button>
      <br />
      <h2>Analysis Result:</h2>
      <p>Percentage of A: {percentages.A || 0}%</p>
      <p>Percentage of T: {percentages.T || 0}%</p>
      <p>Percentage of C: {percentages.C || 0}%</p>
      <p>Percentage of G: {percentages.G || 0}%</p>
      <img src={Dna300} alt="DNA" />
    </div>
  );
}

export default App;
