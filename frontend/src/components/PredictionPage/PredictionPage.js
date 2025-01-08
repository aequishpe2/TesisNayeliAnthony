import React, { useState } from 'react';
import AnalysisForm from '../AnalysisForm/AnalysisForm';
import AnalysisResult from '../AnalysisResult/AnalysisResult';
import { fetchPrediction } from '../../services/api';
import './PredictionPage.css';

const PredictionPage = () => {
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
    <div className="prediction-page">
      <h1>Análisis de Texto</h1>
      <div className="prediction-content">
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

export default PredictionPage; 