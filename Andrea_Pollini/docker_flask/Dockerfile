FROM python:3.10-alpine
WORKDIR /code
COPY requirements.txt .
COPY . .
# ENV FLASK_APP=code/app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.py
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "flask", "run" ]
# sudo sysctl -w vm.overcommit_memory=1