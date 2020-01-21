from k8soperator.webserver.webserver import Webserver


class Nginx(Webserver):
    def __init__(self, name):
        super().__init__(name, 80, 'nginx', 'nginx:stable')
