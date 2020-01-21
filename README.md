# Kubernetes operator

## Description

This project was created for learning purposes. It aims to implement a Kubernetes operator to learn how it works.

The operator will create a webserver based on type which can be:

- Nginx 
- Apache tomcat 

A webserver consists of: 

- Pod 
- Service

The implementation is based on [zalando](https://www.zalando.fr/)'s [kopf](https://kopf.readthedocs.io/en/latest/)

The code is highly inspired from [Luc Juggery](https://medium.com/@lucjuggery)'s medium [post](https://medium.com/swlh/building-a-kubernetes-operator-in-python-with-zalandos-kopf-37c311d8edff)