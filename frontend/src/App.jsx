import React, { useState, useEffect } from 'react';
import './styles/amex-theme.css';
import Header from './components/Header';
import Dashboard from './pages/Dashboard';
import CallHistory from './pages/CallHistory';
import Analytics from './pages/Analytics';

function App() {
  const [currentPage, setCurrentPage] = useState('dashboard');
  const [calls, setCalls] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchCalls();
  }, []);

  const fetchCalls = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5000/api/transcription/all');
      const data = await response.json();
      setCalls(data.calls || []);
    } catch (error) {
      console.error('Error fetching calls:', error);
    }
    setLoading(false);
  };

  const renderPage = () => {
    switch (currentPage) {
      case 'dashboard':
        return <Dashboard calls={calls} onRefresh={fetchCalls} />;
      case 'history':
        return <CallHistory calls={calls} />;
      case 'analytics':
        return <Analytics calls={calls} />;
      default:
        return <Dashboard calls={calls} onRefresh={fetchCalls} />;
    }
  };

  return (
    <div className="app">
      <Header currentPage={currentPage} onPageChange={setCurrentPage} />
      <main className="main-content">
        {loading ? (
          <div className="loading-spinner">
            <div className="spinner"></div>
            <p>Loading...</p>
          </div>
        ) : (
          renderPage()
        )}
      </main>
    </div>
  );
}

export default App;