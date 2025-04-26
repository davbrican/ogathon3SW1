# Imagen base
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY main.py .

# Instala FastAPI y Uvicorn
RUN pip install fastapi uvicorn

# Expone el puerto 8080
EXPOSE 8080

# Comando para ejecutar la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
