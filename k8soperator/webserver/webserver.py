class Webserver:
    def __init__(self, name, port, server_type, image):
        self.__port = port
        self.__server_type = server_type
        self.__image = image
        self.__pod = {
            'apiVersion': 'v1',
            'metadata': {'name': name, 'labels': {'app': 'webserver', 'servertype': self.__server_type}},
            'spec':
            {
                'containers':
                [{
                    'image': self.__image, 'name': 'apache',
                    'ports': [{'containerPort': port}]
                }]
            }
        }
        self.__svc = {
            'apiVersion': 'v1',
            'metadata': {'name': name},
            'spec': {
                'selector': {'app': 'webserver', 'servertype': self.__server_type},
                'type': 'ClusterIP',
                'ports': [{'port': port, 'targetPort': port}]
            }
        }

    @property
    def pod(self):
        return self.__pod

    @property
    def svc(self):
        return self.__svc
