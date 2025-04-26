# Imagen base
FROM python:3.10

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el código desde src/
COPY ./src /app

# Instalar dependencias
RUN pip install fastapi uvicorn

# Exponer el puerto que usará FastAPI
EXPOSE 8080

# Comando para ejecutar la API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
