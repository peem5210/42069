FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
WORKDIR /42069/42069
CMD ["uvicorn", "server:app", "--reload", "--host=0.0.0.0"]