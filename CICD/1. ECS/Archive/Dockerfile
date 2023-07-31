FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install scikit-learn==0.24.0
RUN pip3 install flask
COPY ./handler.py handler.py
COPY ./random_forest_regressor.pkl random_forest_regressor.pkl
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "handler.py" ]

