from .utils import instance_path, split_entry_points

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

ui_extension_entry_points = list(split_entry_points("invenio_base.apps", "config_ui"))

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


create_api = base_create_api
"""Since we don't yet have ldap auth for the api, we'll use invenio's factory for now."""


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

