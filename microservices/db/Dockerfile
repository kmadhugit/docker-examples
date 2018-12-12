FROM python:3.6
RUN pip install Flask==1.0.2
RUN useradd -ms /bin/bash madhu
USER madhu
COPY db /db
WORKDIR /db
CMD ["python", "db.py"] 

