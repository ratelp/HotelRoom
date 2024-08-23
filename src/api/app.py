from flask import Flask
from dotenv import load_dotenv 
import os # Importação para lidar com as variáveis de ambiente

#Importa o blueprint definido no arquivo predict.predict
from predict.predict import predict_blueprint

load_dotenv() # Carrega o .env ao ambiente
PORT = os.getenv('PORT')

# Cria uma instância da classe Flask
app = Flask(__name__)

# Registra as rotas definidas no blueprint predict_blueprint na aplicação Flask
app.register_blueprint(predict_blueprint)

# Rota padrão ("/") que retorna uma mensagem de "Hello, World!"
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Inicializa o servidor Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT) # Porta definida na variável de ambiente PORT