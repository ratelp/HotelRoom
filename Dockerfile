# uso:
# Atualizar ENV
# docker build -t ratelp/sprint5hotelprices . 
# docker run -p 8080:8080 --name flask-api-container --rm ratelp/sprint5hotelprices (teste)
# docker push ratelp/sprint5hotelprices:latest

FROM python:3.11.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src/api .

ENV AWS_ACCESS_KEY_ID ""
ENV AWS_SECRET_ACCESS_KEY ""
ENV AWS_SESSION_TOKEN ""
ENV AWS_DEFAULT_REGION ""
ENV AWS_S3_BUCKET ""
ENV AWS_MODEL_FILE_KEY ""
ENV PORT ""
ENV FLASK_DEBUG 0

EXPOSE 8080
# Por padrão o serviço Elastic Beanstalk abre acesso a porta 8080, 
# portanto é necessário que a aplicação esteja respondendo nessa mesma porta.

# Roda o servidor utilizando gunicorn
ENTRYPOINT ["gunicorn", "app:app"]