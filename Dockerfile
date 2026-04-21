# 1. Define a imagem base (Python)
FROM python:3.9-slim

# 2. Define onde os ficheiros ficarão dentro do container
WORKDIR /app

# 3. Copia a lista de dependências e as instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia todo o conteúdo da sua pasta para dentro do container
COPY . .

# 5. Comando que executa o seu script quando o container subir
CMD ["python", "src/app.py"]