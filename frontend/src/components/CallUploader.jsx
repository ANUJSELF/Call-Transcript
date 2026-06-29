import React, { useState } from 'react';

function CallUploader({ onUploadComplete, onRefresh }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({
    customer_name: '',
    agent_name: '',
    file: null
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleFileChange = (e) => {
    setFormData(prev => ({
      ...prev,
      file: e.target.files[0]
    }));
  };

  const handleDragDrop = (e) => {
    e.preventDefault();
    setFormData(prev => ({
      ...prev,
      file: e.dataTransfer.files[0]
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    if (!formData.file) {
      setError('Please select a file');
      setLoading(false);
      return;
    }

    const uploadFormData = new FormData();
    uploadFormData.append('file', formData.file);
    uploadFormData.append('customer_name', formData.customer_name);
    uploadFormData.append('agent_name', formData.agent_name);

    try {
      const response = await fetch('http://localhost:5000/api/transcription/upload', {
        method: 'POST',
        body: uploadFormData
      });

      const data = await response.json();

      if (response.ok) {
        alert('File uploaded and transcribed successfully!');
        setFormData({ customer_name: '', agent_name: '', file: null });
        onRefresh();
      } else {
        setError(data.error || 'Upload failed');
      }
    } catch (err) {
      setError('Network error: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="dashboard-card">
      <h2>Upload Call Recording</h2>

      <div className="form-group">
        <label className="form-label">Customer Name</label>
        <input
          type="text"
          name="customer_name"
          value={formData.customer_name}
          onChange={handleChange}
          className="form-input"
          placeholder="Enter customer name"
          required
        />
      </div>

      <div className="form-group">
        <label className="form-label">Agent Name</label>
        <input
          type="text"
          name="agent_name"
          value={formData.agent_name}
          onChange={handleChange}
          className="form-input"
          placeholder="Enter agent name"
          required
        />
      </div>

      <div
        className="upload-section"
        onDragOver={e => e.preventDefault()}
        onDrop={handleDragDrop}
      >
        <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>📁</div>
        <p>Drag and drop your audio file here or click to browse</p>
        <p style={{ fontSize: '0.875rem', color: '#666' }}>
          Supported formats: MP3, WAV, M4A, FLAC
        </p>
        <input
          type="file"
          accept="audio/*"
          onChange={handleFileChange}
          id="file-input"
        />
        <button
          type="button"
          className="btn btn-secondary"
          onClick={() => document.getElementById('file-input').click()}
        >
          Browse Files
        </button>
        {formData.file && <p style={{ marginTop: '1rem' }}>📄 {formData.file.name}</p>}
      </div>

      {error && <p style={{ color: 'var(--amex-danger)', marginTop: '1rem' }}>❌ {error}</p>}

      <button
        type="submit"
        className="btn btn-primary"
        style={{ marginTop: '1rem', width: '100%' }}
        disabled={loading}
      >
        {loading ? 'Uploading...' : 'Upload & Transcribe'}
      </button>
    </form>
  );
}

export default CallUploader;