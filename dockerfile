FROM python:3.10.2-slim
#FROM dashboardmultimedia


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Actualizar pip
RUN pip install --no-cache-dir --upgrade pip

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
