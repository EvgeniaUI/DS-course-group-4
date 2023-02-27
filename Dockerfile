FROM python:3.10
EXPOSE 8000
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app
RUN python -m pip config debug
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install python-multipart
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

