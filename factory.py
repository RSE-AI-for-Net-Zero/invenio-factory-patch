from invenio_app.factory import (create_app_factory,
                                 config_loader,
                                 wsgi_proxyfix,
                                 create_wsgi_factory,
                                 instance_path,
                                 static_folder,
                                 static_url_path,
                                 app_class,
                                 create_api as invenio_app_create_api)

from invenio_ldapclient import InvenioLDAPClient


create_ui = create_app_factory(
    'invenio',
    config_loader=config_loader,
    blueprint_entry_points=['invenio_base.blueprints'],
    extension_entry_points=['invenio_base.apps'],
    extensions=[InvenioLDAPClient],
    converter_entry_points=['invenio_base.converters'],
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


create_api = invenio_app_create_api
"""Since we don't yet have ldap auth for the api, we'll use invenio's factory for now."""

create_app = create_app_factory(
    'invenio',
    config_loader=config_loader,
    blueprint_entry_points=['invenio_base.blueprints'],
    extension_entry_points=['invenio_base.apps'],
    extensions=[InvenioLDAPClient],
    converter_entry_points=['invenio_base.converters'],
    wsgi_factory=wsgi_proxyfix(create_wsgi_factory({'/api': create_api})),
    instance_path=instance_path,
    static_folder=static_folder,
    root_path=instance_path,
    static_url_path=static_url_path(),
    app_class=app_class(),
)


""" UWSGI Entry Points """
ui = create_ui()
api = create_api()
app = create_app()


