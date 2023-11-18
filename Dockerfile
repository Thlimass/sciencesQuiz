# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos necessários para o contêiner (requirements.txt, etc.)
COPY . /app

# Instale as dependências do seu aplicativo
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar sua aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]
