import kopf

from k8soperator.webserver.apache import Apache
from k8soperator.webserver.nginx import Nginx


class WebserverFactory:
    SUPPORTED_SERVER_TYPES = ["apache", "nginx"]

    @staticmethod
    def create_webserver(server_type, name):
        if server_type not in WebserverFactory.SUPPORTED_SERVER_TYPES:
            raise kopf.HandlerFatalError(f"Type must be one of {WebserverFactory.SUPPORTED_SERVER_TYPES}")
        if 'apache' == server_type:
            return Apache(name)
        if 'nginx' == server_type:
            return Nginx(name)
