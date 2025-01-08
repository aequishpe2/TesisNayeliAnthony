import React, { useState, useEffect } from 'react';
import { fetchHistory } from '../../services/api';
import './Dashboard.css';

const Dashboard = () => {
  const [stats, setStats] = useState({
    totalAnalysis: 0,
    cyberbullyingDetected: 0,
    categories: {},
    recentAnalyses: []
  });

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      const response = await fetchHistory();
      if (response && response.data) {
        const history = response.data;
        
        const totalAnalysis = history.length;
        let cyberbullyingDetected = 0;
        const categories = {};

        history.forEach(item => {
          const prediccion = item.prediccion;

          const hasCyberbullying = Object.values(prediccion).some(value => value > 0.5);
          if (hasCyberbullying) cyberbullyingDetected++;

          Object.entries(prediccion).forEach(([category, value]) => {
            if (value > 0.5) {
              categories[category] = (categories[category] || 0) + 1;
            }
          });
        });

        setStats({
          totalAnalysis,
          cyberbullyingDetected,
          categories,
          recentAnalyses: history.slice(-5).reverse()
        });
      }
    } catch (error) {
      console.error('Error al cargar estadísticas:', error);
    }
  };

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total de Análisis</h3>
          <p className="stat-number">{stats.totalAnalysis}</p>
        </div>
        
        <div className="stat-card">
          <h3>Casos Detectados</h3>
          <p className="stat-number">{stats.cyberbullyingDetected}</p>
          <p className="stat-percentage">
            {stats.totalAnalysis > 0 
              ? ((stats.cyberbullyingDetected / stats.totalAnalysis) * 100).toFixed(1)
              : 0}%
          </p>
        </div>
      </div>

      <div className="dashboard-sections">
        <div className="categories-section">
          <h2>Detecciones por Categoría</h2>
          <div className="categories-grid">
            {Object.entries(stats.categories).map(([category, count]) => (
              <div key={category} className="category-card">
                <h4>{category.replace(/_/g, ' ')}</h4>
                <p className="category-count">{count}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="recent-analyses">
          <h2>Análisis Recientes</h2>
          <div className="recent-list">
            {stats.recentAnalyses.map((item) => (
              <div key={item.id} className="recent-item">
                <p className="recent-text">{item.texto}</p>
                <div className="recent-result">
                  {Object.entries(item.prediccion)
                    .filter(([_, value]) => value > 0.5)
                    .map(([category, value]) => (
                      <span key={category} className="category-tag">
                        {category.replace(/_/g, ' ')}: {(value * 100).toFixed(1)}%
                      </span>
                    ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard; 