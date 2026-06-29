import React from 'react';

function Analytics({ calls }) {
  const stats = React.useMemo(() => {
    const total = calls.length;
    const completed = calls.filter(c => c.transcription_status === 'completed').length;
    const categories = {};
    const sentiments = { positive: 0, negative: 0, neutral: 0 };

    calls.forEach(call => {
      if (call.primary_category) {
        categories[call.primary_category] = (categories[call.primary_category] || 0) + 1;
      }
      if (call.sentiment) {
        sentiments[call.sentiment] = (sentiments[call.sentiment] || 0) + 1;
      }
    });

    return { total, completed, categories, sentiments };
  }, [calls]);

  return (
    <div>
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-label">Total Calls</div>
          <div className="stat-value">{stats.total}</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Transcribed</div>
          <div className="stat-value">{stats.completed}</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Success Rate</div>
          <div className="stat-value">
            {stats.total > 0 ? Math.round((stats.completed / stats.total) * 100) : 0}%
          </div>
        </div>
      </div>

      <div className="dashboard-card">
        <h2>Calls by Category</h2>
        {Object.entries(stats.categories).map(([category, count]) => (
          <div key={category} style={{ marginBottom: '1rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
              <span>{category}</span>
              <strong>{count}</strong>
            </div>
            <div style={{ width: '100%', backgroundColor: '#eee', borderRadius: '4px', overflow: 'hidden' }}>
              <div
                style={{
                  width: `${(count / stats.total) * 100}%`,
                  backgroundColor: 'var(--amex-primary)',
                  height: '8px',
                  transition: 'width 0.3s ease'
                }}
              ></div>
            </div>
          </div>
        ))}
      </div>

      <div className="dashboard-card" style={{ marginTop: '2rem' }}>
        <h2>Sentiment Distribution</h2>
        <div className="stats-grid">
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '2rem' }}>😊</div>
            <div style={{ fontSize: '0.9rem', color: '#666' }}>Positive</div>
            <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: 'var(--amex-success)' }}>
              {stats.sentiments.positive}
            </div>
          </div>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '2rem' }}>😞</div>
            <div style={{ fontSize: '0.9rem', color: '#666' }}>Negative</div>
            <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: 'var(--amex-danger)' }}>
              {stats.sentiments.negative}
            </div>
          </div>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '2rem' }}>😐</div>
            <div style={{ fontSize: '0.9rem', color: '#666' }}>Neutral</div>
            <div style={{ fontSize: '1.5rem', fontWeight: 'bold', color: 'var(--amex-info)' }}>
              {stats.sentiments.neutral}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Analytics;