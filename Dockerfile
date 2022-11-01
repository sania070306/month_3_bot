FROM python:3.10

EXPOSE 5009


RUN mkdir -p /opt/services/bot/insomnia
WORKDIR /opt/services/bot/insomnia

RUN mkdir -p /opt/services/bot/insomnia/requirements
ADD . requirements.txt /opt/services/bot/insomnia/

COPY . /opt/services/bot/insomnia/


RUN pip install -r requirements.txt

CMD ["python", "/opt/services/bot/insomnia/main.py"]