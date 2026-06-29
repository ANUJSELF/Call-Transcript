import React, { useState } from 'react';

function CallHistory({ calls }) {
  const [sortBy, setSortBy] = useState('date');

  const sortedCalls = [...calls].sort((a, b) => {
    if (sortBy === 'date') return new Date(b.call_date) - new Date(a.call_date);
    if (sortBy === 'customer') return (a.customer_name || '').localeCompare(b.customer_name || '');
    if (sortBy === 'category') return (a.primary_category || '').localeCompare(b.primary_category || '');
    return 0;
  });

  return (
    <div className="dashboard-card">
      <h1>Call History</h1>

      <div className="form-group" style={{ marginBottom: '1rem' }}>
        <label className="form-label">Sort by:</label>
        <select
          value={sortBy}
          onChange={(e) => setSortBy(e.target.value)}
          className="form-select"
        >
          <option value="date">Date</option>
          <option value="customer">Customer Name</option>
          <option value="category">Category</option>
        </select>
      </div>

      <div className="table-container">
        <table className="call-table">
          <thead>
            <tr>
              <th>Date</th>
              <th>Customer</th>
              <th>Agent</th>
              <th>Category</th>
              <th>Duration</th>
              <th>Status</th>
              <th>Sentiment</th>
            </tr>
          </thead>
          <tbody>
            {sortedCalls.map(call => (
              <tr key={call.id}>
                <td>{new Date(call.call_date).toLocaleDateString()}</td>
                <td>{call.customer_name}</td>
                <td>{call.agent_name}</td>
                <td>{call.primary_category || 'N/A'}</td>
                <td>{call.duration_seconds ? `${Math.round(call.duration_seconds / 60)}m` : 'N/A'}</td>
                <td>
                  <span className={`badge badge-${call.transcription_status}`}>
                    {call.transcription_status}
                  </span>
                </td>
                <td>
                  {call.sentiment && (
                    <span>
                      {call.sentiment === 'positive' ? '😊' : call.sentiment === 'negative' ? '😞' : '😐'}
                    </span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {calls.length === 0 && (
        <p style={{ textAlign: 'center', padding: '2rem', color: '#666' }}>
          No calls recorded yet. Upload a call recording to get started!
        </p>
      )}
    </div>
  );
}

export default CallHistory;