FROM python:3.6
RUN pip install Flask==1.0.2
RUN pip install requests
RUN useradd -ms /bin/bash madhu
USER madhu
COPY app /app
WORKDIR /app
CMD ["python", "app.py"] 

