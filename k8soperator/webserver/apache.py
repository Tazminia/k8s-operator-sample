from k8soperator.webserver.webserver import Webserver


class Apache(Webserver):
    def __init__(self, name):
        super().__init__(name, 8080, 'apache', 'tomcat:jdk8-adoptopenjdk-openj9')
