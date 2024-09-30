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
from invenio_accounts import InvenioAccountsUI

from .load_entry_points import mod_list

eps = mod_list([], [('invenio_ldapclient', 'invenio_base.apps'),
                    ('invenio_accounts_ui', 'invenio_base.apps')],
               'invenio_base.apps')

extensions = [ep.load() for ep in eps]

bps = mod_list([], [], 'invenio_base.blueprints')

blueprints = [bp.load() for bp in bps]

create_ui = create_app_factory(
    'invenio',
    config_loader=config_loader,
    #blueprint_entry_points=['invenio_base.blueprints'],
    blueprints=blueprints,
    #extension_entry_points=['invenio_base.apps'],
    extensions=extensions,
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
    #blueprint_entry_points=['invenio_base.blueprints'],
    blueprints=blueprints,
    #extension_entry_points=['invenio_base.apps'],
    extensions=extensions,
    converter_entry_points=['invenio_base.converters'],
    wsgi_factory=wsgi_proxyfix(create_wsgi_factory({'/api': create_api})),
    instance_path=instance_path,
    static_folder=static_folder,
    root_path=instance_path,
    static_url_path=static_url_path(),
    app_class=app_class(),
)

