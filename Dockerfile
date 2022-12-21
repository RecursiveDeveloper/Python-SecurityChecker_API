FROM python:3.10.6

WORKDIR /app/python_security_checker/

COPY . ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000/tcp

CMD [ "python3", "server.py" ]
