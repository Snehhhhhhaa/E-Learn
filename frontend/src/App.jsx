import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  // Function to fetch the machine learning finance data
  const fetchData = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await axios.get('http://localhost:8000/machine-learning-finance');
      setData(response.data.data);  // Set the response data
    } catch (err) {
      setError('Error fetching data');
      console.error(err.response?.data || err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1>Machine Learning in Finance</h1>
      <button onClick={fetchData} style={styles.button}>Fetch Data</button>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {data.length > 0 && (
        <div style={styles.dataContainer}>
          <h2>Data</h2>
          <ul style={styles.list}>
            {data.map((item) => (
              <li key={item.id} style={styles.item}>
                <h3>{item.title}</h3>
                <p>{item.description}</p>
                <p><strong>Created at:</strong> {item.createdat}</p>
                <p><strong>Topic:</strong> {item.topic}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

// Styling
const styles = {
  container: {
    padding: '20px',
    maxWidth: '600px',
    margin: 'auto',
    backgroundColor: '#f9f9f9',
    borderRadius: '8px',
    boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
  },
  button: {
    padding: '10px',
    borderRadius: '4px',
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    fontSize: '16px',
    cursor: 'pointer',
    marginBottom: '20px',
  },
  dataContainer: {
    marginTop: '20px',
  },
  list: {
    listStyleType: 'none',
    paddingLeft: '0',
  },
  item: {
    marginBottom: '20px',
    padding: '10px',
    border: '1px solid #ddd',
    borderRadius: '5px',
    backgroundColor: '#f5f5f5',
  },
};

export default App;
