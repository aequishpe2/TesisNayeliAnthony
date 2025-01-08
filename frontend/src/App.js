import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './components/Sidebar/Sidebar';
import Dashboard from './components/Dashboard/Dashboard';
import DetectionPage from './components/DetectionPage/DetectionPage';
import './styles/global.css';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Sidebar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/detect" element={<DetectionPage />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
