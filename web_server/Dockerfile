FROM python:3.11.6

WORKDIR /app
COPY requirements.txt /app/requirements.txt

# Ya corre python3 sin decirle 3
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#El punto significa que todo el codigo se copiará 
COPY . /app

# Necesitamos que el contenedor corra continuamente
CMD {"uvicorn", "main:app", "--host". "0.0.0.0", "--port", "80"}
