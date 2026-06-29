import React, { useState } from 'react';

function TranscriptViewer({ call }) {
  const [showTranscript, setShowTranscript] = useState(false);

  return (
    <div className="dashboard-card">
      <h2>Transcript & Summary</h2>

      {call ? (
        <>
          <div style={{ marginBottom: '1rem' }}>
            <strong>Customer:</strong> {call.customer_name} | <strong>Agent:</strong> {call.agent_name}
            <br />
            <strong>Status:</strong> <span className={`badge badge-${call.transcription_status}`}>
              {call.transcription_status}
            </span>
          </div>

          {call.transcript && (
            <>
              <button
                className="btn btn-secondary"
                onClick={() => setShowTranscript(!showTranscript)}
                style={{ marginBottom: '1rem' }}
              >
                {showTranscript ? '▼ Hide Transcript' : '▶ Show Transcript'}
              </button>

              {showTranscript && (
                <div className="transcript-container">
                  <p>{call.transcript}</p>
                </div>
              )}

              {call.summary && (
                <div className="summary-panel">
                  <div style={{ fontSize: '1.1rem', fontWeight: '700', color: 'var(--amex-primary)', marginBottom: '0.5rem' }}>📋 Summary</div>
                  <div style={{ lineHeight: '1.6', color: '#555', marginBottom: '1rem' }}>
                    {call.summary}
                  </div>

                  {call.key_points && call.key_points.length > 0 && (
                    <div style={{ marginTop: '1rem' }}>
                      <div style={{ fontWeight: 600, color: 'var(--amex-dark)', marginBottom: '0.5rem' }}>Key Points:</div>
                      <ul style={{ listStyle: 'none', paddingLeft: '0' }}>
                        {call.key_points.map((point, idx) => (
                          <li key={idx} style={{ padding: '0.5rem 0 0.5rem 1.5rem', position: 'relative', color: '#555' }}>
                            <span style={{ position: 'absolute', left: '0', color: 'var(--amex-success)', fontWeight: 'bold' }}>✓</span>
                            {point}
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {call.sentiment && (
                    <div style={{ marginTop: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                      <span style={{ fontSize: '1.5rem' }}>
                        {call.sentiment === 'positive' ? '😊' : call.sentiment === 'negative' ? '😞' : '😐'}
                      </span>
                      <span>Sentiment: <strong>{call.sentiment}</strong></span>
                    </div>
                  )}
                </div>
              )}
            </>
          )}
        </>
      ) : (
        <p>No call selected</p>
      )}
    </div>
  );
}

export default TranscriptViewer;