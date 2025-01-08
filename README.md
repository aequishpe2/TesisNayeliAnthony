# Proceso ETL y Modelos de Machine Learning para Clasificación Multietiqueta

## Descripción del Proyecto
Este proyecto implementa un sistema para:
1. **Cargar y procesar datos desde archivos CSV hacia MongoDB.**
2. **Preprocesar textos en español utilizando TfidfVectorizer.**
3. **Entrenar modelos de Machine Learning para clasificación multietiqueta**, centrados en identificar problemas relacionados con ciberacoso (cyberbullying).
4. **Evaluar el desempeño de los modelos** mediante métricas de precisión, recall, F1-score y accuracy.
5. **Guardar y reutilizar el modelo entrenado y el vectorizador** para realizar predicciones en nuevos textos.

## Tecnologías y Bibliotecas Utilizadas
- **Python 3.8+**
- **MongoDB**: Base de datos NoSQL para almacenar los datos procesados.
- **Bibliotecas de Python**:
  - `pandas` para manipulación de datos.
  - `pymongo` para interacción con MongoDB.
  - `nltk` para manejo de palabras vacías en español.
  - `scikit-learn` para preprocesamiento y modelos de Machine Learning.
  - `joblib` para guardar y cargar modelos y vectorizadores.

## Requisitos Previos
### 1. Instalación de Dependencias
Ejecuta el siguiente comando para instalar las bibliotecas necesarias:
```bash
pip install pandas pymongo scikit-learn nltk joblib
```

### 2. Configuración de MongoDB
Asegúrate de tener MongoDB instalado y ejecutándose en tu sistema. La configuración predeterminada del proyecto utiliza la URI:
```
mongodb://localhost:27017/
```
Puedes cambiar esta configuración en el código si es necesario.

### 3. Descargar Stopwords en Español
El proyecto utiliza palabras vacías en español de la biblioteca `nltk`. Para descargarlas, ejecuta:
```python
import nltk
nltk.download('stopwords')
```

## Estructura del Proyecto
- **Carga de datos:**
  Los datos de entrada se encuentran en formato CSV y se cargan en MongoDB mediante `pandas` y `pymongo`.
- **Preprocesamiento:**
  Se utiliza `TfidfVectorizer` para transformar el texto en vectores numéricos, eliminando palabras vacías.
- **Modelos de Machine Learning:**
  Los siguientes modelos se implementan para clasificación multietiqueta:
  - Random Forest
  - Naive Bayes
  - Regresión Logística
  - Support Vector Machine (SVM)
- **Evaluación:**
  Se genera un reporte para cada etiqueta con métricas como precisión, recall y F1-score, así como el accuracy general del modelo.
- **Guardado del modelo:**
  Los modelos y el vectorizador se guardan con `joblib` para reutilizarlos en predicciones futuras.

## Ejecución del Proyecto
### 1. Carga y Procesamiento de Datos
El ETL carga datos desde archivos CSV hacia MongoDB:
```python
load_csv_to_mongo(csv_files, DATABASE_NAME, COLLECTION_NAME)
```

### 2. Entrenamiento de Modelos
El código entrena los modelos con los datos cargados y procesados:
```python
rf_model.fit(X_train, y_train)  # Entrena Random Forest
```
Se implementan también Naive Bayes, Regresión Logística y SVM.

### 3. Evaluación
Se generan reportes con métricas individuales y generales:
```python
print(classification_report(y_test.iloc[:, i], rf_predictions[:, i]))
print(f"Accuracy general para Random Forest: {rf_accuracy:.2f}")
```

### 4. Guardar el Modelo
El modelo entrenado y el vectorizador se guardan para reutilización:
```python
joblib.dump(rf_model, "random_forest_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
```

### 5. Prueba del Modelo
Se puede cargar el modelo guardado y realizar predicciones en nuevos textos:
```python
loaded_model = joblib.load("random_forest_model.pkl")
loaded_vectorizer = joblib.load("vectorizer.pkl")
nuevo_texto = ["Este es un mensaje de prueba"]
nuevo_vectorizado = loaded_vectorizer.transform(nuevo_texto)
prediccion = loaded_model.predict(nuevo_vectorizado)
```

## Resultados Esperados
- **Ciberacoso Detectado:**
  La predicción devuelve un DataFrame con las etiquetas relevantes para el texto ingresado.
- **Métricas de Evaluación:**
  Precisión, recall, F1-score y accuracy general para cada modelo.

## Contribuciones
Sientete libre de contribuir al proyecto mejorando los modelos o extendiendo las funcionalidades.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Sé libre de usarlo y modificarlo según tus necesidades.
