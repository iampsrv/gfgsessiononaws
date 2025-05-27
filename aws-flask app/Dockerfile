FROM python
COPY . /app
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
EXPOSE 8080
CMD ["python", "app.py"]
