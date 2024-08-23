# Importa o Blueprint e o módulo request do pacote Flask
from flask import Blueprint, request
from .controllers.prediction_controller import prediction_controller

# Cria um Blueprint chamado 'predict' com o nome do módulo atual (__name__)
predict_blueprint = Blueprint('predict', __name__)

# Cria uma instância do controller prediction_controller
controller = prediction_controller()

# Define a rota '/api/v1/predict' no Blueprint 'predict' que aceita apenas requisições do tipo POST
@predict_blueprint.route('/api/v1/predict', methods=['POST'])
def predict():
    # Chama o método predict do controller com o objeto de requisição (request) passado como argumento
    return controller.predict(request)