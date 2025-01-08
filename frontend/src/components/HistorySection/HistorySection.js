import React from 'react';
import { getMaxProbability } from '../../utils/helpers';
import './HistorySection.css';

const HistorySection = ({ history }) => {
  return (
    <div className="history-section">
      <h2>Historial de Análisis</h2>
      <div className="history-list">
        {Array.isArray(history) &&
          history.map((item) => (
            <div key={item.id} className="history-item">
              <p className="history-text">{item.texto}</p>
              <div className="history-result">
                {(() => {
                  const [category, value] = getMaxProbability(item.prediccion);
                  return (
                    <span className={value > 0.5 ? 'warning' : ''}>
                      {category.replace(/_/g, ' ')}: {(value * 100).toFixed(2)}%
                    </span>
                  );
                })()}
              </div>
            </div>
          ))}
      </div>
    </div>
  );
};

export default HistorySection; 