FROM python:2.7-slim
WORKDIR /app
COPY .  /app
RUN pip install -r /app/requirements.txt
RUN flask db upgrade
RUN python seed.py
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]