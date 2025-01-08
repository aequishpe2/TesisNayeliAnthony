export const getMaxProbability = (prediccion) => {
  try {
    const prediccionObj = typeof prediccion === 'string' ? JSON.parse(prediccion) : prediccion;
    const entries = Object.entries(prediccionObj);
    return entries.reduce((max, current) => 
      current[1] > max[1] ? current : max
    );
  } catch (error) {
    console.error('Error al procesar predicción:', error);
    return ['error', 0];
  }
}; 