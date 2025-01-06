from unittest.mock import patch
from .utils import instance_path, split_entry_points
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

ui_extension_entry_points = split_entry_points("invenio_base.apps", "invenio_factory_patch_ui.cfg")
api_extension_entry_points = split_entry_points("invenio_base.api_apps", "invenio_factory_patch_api.cfg")


create_ui = create_app_factory(
    "invenio",
    config_loader=config_loader,
    blueprint_entry_points=["invenio_base.blueprints"],
    extension_entry_points=ui_extension_entry_points,
    converter_entry_points=["invenio_base.converters"],
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
    wsgi_factory=wsgi_proxyfix(create_wsgi_factory({"/api": create_api})),
    instance_path=instance_path,
    static_folder=static_folder,
    root_path=instance_path,
    static_url_path=static_url_path(),
    app_class=app_class(),
)



