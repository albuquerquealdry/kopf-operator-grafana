import kopf
import logging
from crds.pagmondirectory.create import create_fn
from crds.pagmondirectory.delete import delete_fn
from crds.pagmonusedashboard.create import create_ds

# URL e cabeçalhos
url = 'http://192.168.0.110:3000'


headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer glsa_y1I98GgvY1La7Ajsy2PyPFa74JjrW72Z_c1963e48'
}

@kopf.on.create('pagmondirectorys')
def create_handler(spec, **kwargs):
    url_directory = f"{url}/api/folders"
    directory = spec.get('directory')
    uid = spec.get('uuid')
    if not directory and uid:
        raise kopf.PermanentError("Directory and uid necessary.")
    create_fn(directory,uid, url_directory, headers)

@kopf.on.delete('pagmondirectorys')
def delete_handler(spec, body, **kwargs):
    url_directory = f"{url}/api/folders"
    uid = spec.get('uuid')
    if not uid:
        raise kopf.PermanentError("uid necessary.")
    delete_fn(url_directory, uid , headers)


@kopf.on.create('pagmondashboards')
def create_handler(spec, body, **kwargs):
    url_directory = f"{url}/api/dashboards/db"
    
    name = spec.get('name')
    uid = spec.get('uuid')
    server = spec.get('server')
    team = spec.get('team')
    labels = spec.get('labels')
    directory = spec.get('directory')
    
    if not uid:
        raise kopf.PermanentError("uid necessary.")
    create_ds(url_directory, headers, name, server, uid, team, labels, directory)