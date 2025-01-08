const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const handleResponse = async (response) => {
  try {
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.message || 'Error en la petición');
    }
    return data;
  } catch (error) {
    console.error('Error procesando respuesta:', error);
    throw error;
  }
};

export const fetchPrediction = async (text) => {
  try {
    const response = await fetch(`${API_URL}/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ texto: text }),
    });
    return handleResponse(response);
  } catch (error) {
    console.error('Error en fetchPrediction:', error);
    throw new Error('Error al procesar la predicción');
  }
};

export const fetchHistory = async () => {
  try {
    const response = await fetch(`${API_URL}/data`);
    return handleResponse(response);
  } catch (error) {
    console.error('Error en fetchHistory:', error);
    throw new Error('Error al cargar el historial');
  }
}; 