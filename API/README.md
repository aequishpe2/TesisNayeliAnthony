# API Flask-RESTful con Flask-SQLAlchemy y PostgreSQL

## Descripción
Esta API utiliza Flask-RESTful para gestionar recursos y Flask-SQLAlchemy para interactuar con una base de datos PostgreSQL. La API permite realizar predicciones utilizando un modelo de Machine Learning (Random Forest) entrenado previamente y guardar las predicciones en la base de datos.

---

## Estructura del Proyecto

```
project/
│
├── app/
│   ├── __init__.py          # Inicialización de la aplicación
│   ├── models.py            # Modelos de la base de datos
│   ├── resources/           # Recursos de la API
│   │   ├── __init__.py      # Inicialización del módulo de recursos
│   │   ├── predict.py       # Endpoint para predicciones
│   │   ├── data.py          # Endpoint para datos almacenados
│   └── utils/               # Utilidades
│       ├── __init__.py      # Inicialización del módulo de utilidades
│       ├── load_model.py    # Carga del modelo y el vectorizador
│
├── random_forest_model.pkl  # Modelo entrenado (Random Forest)
├── vectorizer.pkl           # Vectorizador Tfidf entrenado
├── run.py                   # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación del proyecto
```

---

## Endpoints de la API

### 1. Predicción (`POST /predict`)

**Descripción:**
Recibe un texto, realiza una predicción con el modelo de Machine Learning y guarda el texto junto con las predicciones en la base de datos.

**Ejemplo de Solicitud:**
```json
{
    "texto": "Este es un mensaje ofensivo de prueba"
}
```

**Respuesta de Ejemplo:**
```json
{
    "texto": "Este es un mensaje ofensivo de prueba",
    "prediccion": {
        "insulto": 1,
        "amenaza": 0,
        "rumores_dif": 0,
        "comentarios": 1,
        "lenguaje_dis": 0,
        "acoso_sexual": 0,
        "manipulacion": 0,
        "lenguaje_vul": 1,
        "acoso_gener": 0,
        "redes_social": 1,
        "suicidio_autolesion": 0
    }
}
```

### 2. Consultar Datos Almacenados (`GET /data`)

**Descripción:**
Devuelve todos los textos y predicciones almacenados en la base de datos.

**Respuesta de Ejemplo:**
```json
{
    "data": [
        {
            "id": 1,
            "texto": "Este es un mensaje ofensivo de prueba",
            "prediccion": {
                "insulto": 1,
                "amenaza": 0,
                "rumores_dif": 0,
                "comentarios": 1,
                "lenguaje_dis": 0,
                "acoso_sexual": 0,
                "manipulacion": 0,
                "lenguaje_vul": 1,
                "acoso_gener": 0,
                "redes_social": 1,
                "suicidio_autolesion": 0
            }
        }
    ]
}
```

---

## Configuración

### 1. Crear la Base de Datos en PostgreSQL

Ejecuta el siguiente comando en PostgreSQL para crear la base de datos:
```sql
CREATE DATABASE predicciones;
```

### 2. Instalar Dependencias
Ejecuta el siguiente comando para instalar las dependencias:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación
Inicia la aplicación con:
```bash
python run.py
```

---

## Pruebas con Postman

### Predicción
1. Método: `POST`
2. URL: `http://localhost:5000/predict`
3. Body:
   ```json
   {
       "texto": "Este es un mensaje ofensivo de prueba"
   }
   ```
4. Respuesta esperada:
   ```json
   {
       "texto": "Este es un mensaje ofensivo de prueba",
       "prediccion": {
           "insulto": 1,
           "amenaza": 0,
           "rumores_dif": 0,
           "comentarios": 1,
           "lenguaje_dis": 0,
           "acoso_sexual": 0,
           "manipulacion": 0,
           "lenguaje_vul": 1,
           "acoso_gener": 0,
           "redes_social": 1,
           "suicidio_autolesion": 0
       }
   }
   ```

### Consultar Datos
1. Método: `GET`
2. URL: `http://localhost:5000/data`
3. Respuesta esperada:
   ```json
   {
       "data": [
           {
               "id": 1,
               "texto": "Este es un mensaje ofensivo de prueba",
               "prediccion": {
                   "insulto": 1,
                   "amenaza": 0,
                   "rumores_dif": 0,
                   "comentarios": 1,
                   "lenguaje_dis": 0,
                   "acoso_sexual": 0,
                   "manipulacion": 0,
                   "lenguaje_vul": 1,
                   "acoso_gener": 0,
                   "redes_social": 1,
                   "suicidio_autolesion": 0
               }
           }
       ]
   }
   ```

---

## Notas
- Asegúrate de que PostgreSQL esté en ejecución antes de iniciar la aplicación.
- Verifica que los archivos `random_forest_model.pkl` y `vectorizer.pkl` estén en la raíz del proyecto.
- Modifica las credenciales de conexión a la base de datos en `app/__init__.py` si es necesario.

---

## Dependencias

Listado en `requirements.txt`:
```plaintext
Flask==2.2.2
Flask-RESTful==0.3.9
Flask-SQLAlchemy==2.5.1
psycopg2-binary==2.9.6
joblib==1.2.0
pandas==1.5.2
```
