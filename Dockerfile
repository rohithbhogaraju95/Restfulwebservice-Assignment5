FROM python
WORKDIR /Assignment5-main
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8050
COPY . /Assignment5-main  
CMD ["python", "./app.py"]  