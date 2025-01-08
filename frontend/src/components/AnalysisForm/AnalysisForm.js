import React from 'react';
import './AnalysisForm.css';

const AnalysisForm = ({ text, setText, loading, onSubmit }) => {
  return (
    <form onSubmit={onSubmit} className="analysis-form">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Ingresa el texto a analizar..."
        rows="5"
        cols="50"
      />
      <button type="submit" disabled={loading || !text.trim()}>
        {loading ? 'Analizando...' : 'Analizar Texto'}
      </button>
    </form>
  );
};

export default AnalysisForm; 