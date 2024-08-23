import xgboost as xgb
from flask import jsonify # Função jsonify do Flask para converter dados em JSON
import numpy as np # Biblioteca NumPy para operações numéricas

# Importações locais
from ..models.reservation import Reservation
from ..utils.load_model import load_model_from_s3

class prediction_controller:
    def __init__(self):
        # Carrega o modelo XGBoost do bucket S3 ao instanciar o controlador
        self.booster = load_model_from_s3()

    # Método para predict com base nos dados fornecidos na requisição
    def predict(self, request):
        try:
            # Cria uma instância de Reservation a partir dos dados JSON da requisição
            reservation = Reservation(**request.json)

            # Converte os valores dos atributos em um array NumPy e remodela para o formato adequado
            values = np.array([attr for attr in reservation.__dict__.values()]).reshape((1, 31))

            # Realiza a previsão usando o modelo XGBoost carregado
            prediction = self.booster.predict(values)

             # Converte a previsão para um inteiro e adiciona 1, pois o XGBoost considera os índices partindo de 0
            prediction = int(prediction[0]) + 1

            # Retorna o resultado da previsão como JSON
            return jsonify({
                "result": prediction
            })
        except ValueError:
            # Retorna uma resposta de erro 400 (Bad Request) se os dados fornecidos forem inválidos
            return "Dados fornecidos inválidos", 400
