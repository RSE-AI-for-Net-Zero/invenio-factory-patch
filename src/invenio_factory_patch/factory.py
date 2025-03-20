from unittest.mock import patch
from importlib_metadata import entry_points
from .utils import instance_path, split_entry_points, grab_and_remove_from_epgroup_by_name as grab
from .loader import app_loader

_loader_patch = patch('invenio_base.app.app_loader', app_loader)
_loader_patch.start()

from invenio_app.factory import (
    create_app_factory,
    config_loader,
    wsgi_proxyfix,
    create_wsgi_factory,
    instance_path,
    static_folder,
    static_url_path,
    create_api as base_create_api,
    app_class
)
_, api_apps_prime = grab('invenio_rdm_records',
                         entry_points(group = 'invenio_base.api_apps'))

_, ui_apps_prime = grab('invenio_rdm_records',
                         entry_points(group = 'invenio_base.apps'))

ui_extension_entry_points = split_entry_points(ui_apps_prime, "invenio_factory_patch_ui.cfg")
api_extension_entry_points = split_entry_points(api_apps_prime, "invenio_factory_patch_api.cfg")


create_ui = create_app_factory(
    "invenio",
    config_loader=config_loader,
    blueprint_entry_points=["invenio_base.blueprints"],
    extension_entry_points=ui_extension_entry_points,
    converter_entry_points=["invenio_base.converters"],
    finalize_app_entry_points=["invenio_base.finalize_app"],
    wsgi_factory=wsgi_proxyfix(),
    instance_path=instance_path,
    static_folder=static_folder,
    root_path=instance_path,
    static_url_path=static_url_path(),
    app_class=app_class(),
)
"""Flask application factory for Invenio UI.  Ensures invenio-ldapclient is loaded after 
   everything else since entry_points loaded before modules by factories created
   by invenio_base.app.create_app_factory"""

create_api = create_app_factory(
    'invenio',
    config_loader=config_loader,
    blueprint_entry_points=['invenio_base.api_blueprints'],
    extension_entry_points=api_extension_entry_points,
    converter_entry_points=['invenio_base.api_converters'],
    finalize_app_entry_points=["invenio_base.api_finalize_app"],
    wsgi_factory=wsgi_proxyfix(),
    instance_path=instance_path,
    root_path=instance_path,
    app_class=app_class(),
)
"""Flask application factory for Invenio REST API."""

create_app = create_app_factory(
    "invenio",
    config_loader=config_loader,
    blueprint_entry_points=["invenio_base.blueprints"],
    extension_entry_points=ui_extension_entry_points,
    converter_entry_points=["invenio_base.converters"],
    finalize_app_entry_points=["invenio_base.finalize_app"],
    wsgi_factory=wsgi_proxyfix(create_wsgi_factory({"/api": create_api})),
    instance_path=instance_path,
    static_folder=static_folder,
    root_path=instance_path,
    static_url_path=static_url_path(),
    app_class=app_class(),
)
