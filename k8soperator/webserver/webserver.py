class Webserver:
    def __init__(self, name, port, server_type, image):
        self._port = port
        self._server_type = server_type
        self._image = image
        self._pod = {
            'apiVersion': 'v1',
            'metadata': {'name': name, 'labels': {'app': 'webserver', 'servertype': self._server_type}},
            'spec':
            {
                'containers':
                [{
                    'image': self._image, 'name': name,
                    'ports': [{'containerPort': port}]
                }]
            }
        }
        self._svc = {
            'apiVersion': 'v1',
            'metadata': {'name': name},
            'spec': {
                'selector': {'app': 'webserver', 'servertype': self._server_type},
                'type': 'ClusterIP',
                'ports': [{'port': port, 'targetPort': port}]
            }
        }

    @property
    def pod(self):
        return self._pod

    @property
    def svc(self):
        return self._svc
