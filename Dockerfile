FROM python:3.7
RUN pip install kubernetes kopf
ENV PYTHONPATH=/app/lib
COPY k8soperator /app/lib/k8soperator
WORKDIR /app/lib
ENTRYPOINT kopf run --standalone k8soperator/handlers.py -m k8soperator.webserver