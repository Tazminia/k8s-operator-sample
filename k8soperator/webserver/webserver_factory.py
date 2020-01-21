import kopf
from k8soperator.webserver.webserver import Webserver

__servers_conf = {
    'apache': (8080, 'tomcat:jdk8-adoptopenjdk-openj9'),
    'nginx': (80, 'nginx:stable')
}


def create_webserver(server_type, name):
    if server_type in __servers_conf:
        port, image = __servers_conf[server_type]
        return Webserver(name, port, server_type, image)

    raise kopf.HandlerFatalError(f"Type must be one of {list(__servers_conf.keys())}")
