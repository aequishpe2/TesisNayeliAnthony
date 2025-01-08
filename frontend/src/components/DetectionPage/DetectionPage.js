import React, { useState } from 'react';
import AnalysisForm from '../AnalysisForm/AnalysisForm';
import AnalysisResult from '../AnalysisResult/AnalysisResult';
import { fetchPrediction } from '../../services/api';
import './DetectionPage.css';

const DetectionPage = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const data = await fetchPrediction(text);
      setResult(data);
    } catch (error) {
      console.error('Error:', error);
      setResult({ error: 'Hubo un error al procesar tu solicitud' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="detection-page">
      <h1>Detector de Cyberbullying</h1>
      <div className="detection-content">
        <AnalysisForm
          text={text}
          setText={setText}
          loading={loading}
          onSubmit={handleSubmit}
        />
        <AnalysisResult result={result} />
      </div>
    </div>
  );
};

export default DetectionPage; 