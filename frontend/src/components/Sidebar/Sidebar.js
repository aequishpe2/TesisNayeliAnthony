import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Sidebar.css';

const Sidebar = () => {
  const location = useLocation();

  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h2>CyberGuard</h2>
      </div>
      <nav className="sidebar-nav">
        <Link 
          to="/dashboard" 
          className={`nav-item ${location.pathname === '/dashboard' ? 'active' : ''}`}
        >
          <i className="fas fa-chart-line"></i>
          Dashboard
        </Link>
        <Link 
          to="/detect" 
          className={`nav-item ${location.pathname === '/detect' ? 'active' : ''}`}
        >
          <i className="fas fa-search"></i>
          Detección
        </Link>
      </nav>
    </div>
  );
};

export default Sidebar; 