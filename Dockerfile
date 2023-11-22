# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos necessários para o contêiner (requirements.txt, etc.)
COPY requirements.txt ./

# Instale as dependências do seu aplicativo
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

# Comando para iniciar sua aplicação quando o contêiner for iniciado
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
