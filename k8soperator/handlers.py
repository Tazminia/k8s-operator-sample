import kopf
import kubernetes

import k8soperator.webserver.webserver_factory as ws_factory

RESOURCE_GROUP_NAME = "example.org"
RESOURCE_VERSION = "v1"
RESOURCE_TYPE = "webservers"


@kopf.on.create(RESOURCE_GROUP_NAME, RESOURCE_VERSION, RESOURCE_TYPE)
def create_webserver(body, spec, logger, **kwargs):
    logger.debug(body)
    logger.debug(spec)

    name = body['metadata']['name']
    namespace = body['metadata']['namespace']

    create_k8s_objects(namespace, ws_factory.WebserverFactory.create_webserver(spec['type'], name), body)

    # Update status
    msg = f"Pod and Service created for webserver {name}"
    return {'message': msg}


@kopf.on.delete(RESOURCE_GROUP_NAME, RESOURCE_VERSION, RESOURCE_TYPE)
def delete(body, **kwargs):
    msg = f'Database {body["metadata"]["name"]} and its Pod / Service children deleted'
    return {'message': msg}


def create_k8s_objects(namespace, webserver, webserver_definition):
    # Make the Pod and Service the children of the Database object
    kopf.adopt(webserver.pod, owner=webserver_definition)
    kopf.adopt(webserver.svc, owner=webserver_definition)

    # Object used to communicate with the API Server
    api = kubernetes.client.CoreV1Api()
    # Create Pod
    obj = api.create_namespaced_pod(namespace, webserver.pod)
    print(f"Pod {obj.metadata.name} created")
    # Create Service
    obj = api.create_namespaced_service(namespace, webserver.svc)
    print(f"Service {obj.metadata.name} created")