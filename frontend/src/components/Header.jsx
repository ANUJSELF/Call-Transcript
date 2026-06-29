import React from 'react';

function Header({ currentPage, onPageChange }) {
  return (
    <header className="header">
      <div className="header-brand">
        <span>💳</span>
        <span>AMEX Call Transcript System</span>
      </div>
      <nav className="header-nav">
        <button
          className={`nav-button ${currentPage === 'dashboard' ? 'active' : ''}`}
          onClick={() => onPageChange('dashboard')}
        >
          Dashboard
        </button>
        <button
          className={`nav-button ${currentPage === 'history' ? 'active' : ''}`}
          onClick={() => onPageChange('history')}
        >
          Call History
        </button>
        <button
          className={`nav-button ${currentPage === 'analytics' ? 'active' : ''}`}
          onClick={() => onPageChange('analytics')}
        >
          Analytics
        </button>
      </nav>
    </header>
  );
}

export default Header;