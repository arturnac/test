FROM python:2.7
RUN pip install paho-mqtt
RUN pip install pymongo
RUN mkdir /rpi-useage
COPY database.py /rpi-useage
WORKDIR	/rpi-useage

CMD ["python", "database.py"]
