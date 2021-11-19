FROM python:3.9
COPY ./42069 /42069
COPY ./requirements.txt /42069
WORKDIR /42069
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "server:app", "--reload", "--host=0.0.0.0"]