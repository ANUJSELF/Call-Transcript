import React from 'react';
import CallUploader from '../components/CallUploader';
import TranscriptViewer from '../components/TranscriptViewer';

function Dashboard({ calls, onRefresh }) {
  const latestCall = calls && calls.length > 0 ? calls[0] : null;

  return (
    <div>
      <div className="dashboard">
        <CallUploader onRefresh={onRefresh} />
        <TranscriptViewer call={latestCall} />
      </div>
      <div style={{ marginTop: '2rem', backgroundColor: 'white', padding: '2rem', borderRadius: '8px' }}>
        <h2>Quick Stats</h2>
        <div className="stats-grid">
          <div className="stat-card">
            <div className="stat-label">Total Calls</div>
            <div className="stat-value">{calls.length}</div>
          </div>
          <div className="stat-card">
            <div className="stat-label">Transcribed</div>
            <div className="stat-value">{calls.filter(c => c.transcription_status === 'completed').length}</div>
          </div>
          <div className="stat-card">
            <div className="stat-label">Success Rate</div>
            <div className="stat-value">
              {calls.length > 0 ? Math.round((calls.filter(c => c.transcription_status === 'completed').length / calls.length) * 100) : 0}%
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;