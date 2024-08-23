# Importação de bibliotecas necessárias
import boto3 # Interagir com serviços AWS
import gzip # Lidar com arquivos 'gz' 
import tarfile # Manipular arquivos 'tar'
import xgboost as xgb # Ações de Machine Learning
import io # Manipular entrada e saída de dados
import os # Interagir com o sistema operacional
from dotenv import load_dotenv # Carregar variáveis de ambiente

# Função para carregar o modelo treinado do S3
def load_model_from_s3():
    load_dotenv()

    # Obtém as informações do bucket e da chave do arquivo do modelo no S3 a partir das variáveis de ambiente
    S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET')
    MODEL_FILE_KEY =  os.getenv('AWS_MODEL_FILE_KEY')

    # Cria um cliente S3 usando a biblioteca boto3
    s3 = boto3.client('s3')

    # Faz uma solicitação para obter o objeto especificado pela key de uma bucket S3
    response = s3.get_object(Bucket=S3_BUCKET_NAME, Key=MODEL_FILE_KEY)

    # Lê os bytes do modelo
    model_bytes = response['Body'].read()
    
    # Descompacta o arquivo .tar.gz
    with gzip.open(io.BytesIO(model_bytes), 'rb') as f_in:
        with tarfile.open(fileobj=f_in, mode='r') as tar:
            tar.extractall(path='/tmp')  # Extração do arquivo tar para um diretório temporário
            model_path = '/tmp/xgboost-model' # Define o caminho do modelo

            booster = xgb.XGBClassifier() # Carrega o modelo
            booster.load_model(model_path)
            
    return booster # Retorna o modelo carregado