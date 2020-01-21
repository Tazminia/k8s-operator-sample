import kopf
import kubernetes
from k8soperator.webserver.webserver_factory import create_web_server

RESOURCE_GROUP_NAME = "example.org"
RESOURCE_VERSION = "v1"
RESOURCE_TYPE = "webservers"


@kopf.on.create(RESOURCE_GROUP_NAME, RESOURCE_VERSION, RESOURCE_TYPE)
def create_web_server_custom_resource(body, spec, logger, **kwargs):
    logger.debug(body)
    logger.debug(spec)

    name, namespace = body['metadata']['name'], body['metadata']['namespace']

    web_server = create_web_server(spec['type'], name)
    link_to_parent(web_server, web_server_base_object=body)
    create_k8s_objects(namespace, web_server, logger)

    return {'message': f"Pod and Service created for web server {name}"}


@kopf.on.delete(RESOURCE_GROUP_NAME, RESOURCE_VERSION, RESOURCE_TYPE)
def delete_web_server_custom_resource(body, logger, **kwargs):
    message = f'Web server {body["metadata"]["name"]} and its Pod / Service children deleted'
    logger.info(message)
    return {'message': message}


def link_to_parent(web_server, web_server_base_object):
    kopf.adopt(web_server.pod, owner=web_server_base_object)
    kopf.adopt(web_server.svc, owner=web_server_base_object)


def create_k8s_objects(namespace, web_server, logger):
    api = kubernetes.client.CoreV1Api()

    obj = api.create_namespaced_pod(namespace, web_server.pod)
    logger.info(f"Pod {obj.metadata.name} created")

    obj = api.create_namespaced_service(namespace, web_server.svc)
    logger.info(f"Service {obj.metadata.name} created")
