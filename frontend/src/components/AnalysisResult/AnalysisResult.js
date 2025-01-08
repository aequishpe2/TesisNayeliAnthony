import React from 'react';
import './AnalysisResult.css';

const AnalysisResult = ({ result }) => {
  if (!result || result.error) return null;

  return (
    <div className="analysis-result">
      <h2>Resultado del Análisis</h2>
      <div className="prediction-results">
        {Object.entries(
          typeof result.prediccion === 'string'
            ? JSON.parse(result.prediccion)
            : result.prediccion
        ).map(([key, value]) => (
          <div
            key={key}
            className={`prediction-item ${value > 0.5 ? 'warning' : ''}`}
          >
            <span className="category">{key.replace(/_/g, ' ')}</span>
            <span className="probability">{(value * 100).toFixed(2)}%</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AnalysisResult; 