FROM python  

WORKDIR /app

COPY requirements.txt
RUN pip install -r requirements.txt

COPY ..

EXPOSE 500

CMD ["PYTHON, app.py"]
