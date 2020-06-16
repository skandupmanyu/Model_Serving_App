FROM python:3
ADD app.py /
ADD requirements.txt /
ADD templates /templates
ADD static /static
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./app.py"]
