from entry_point_util import entry_point_getter, get_partially_ordered_list

from invenio_app.factory import (create_app_factory,
                                 config_loader,
                                 wsgi_proxyfix,
                                 create_wsgi_factory,
                                 instance_path,
                                 static_folder,
                                 static_url_path,
                                 app_class,
                                 create_api as _create_api)


def _get_ui_ext_eps():
    ordered_ui_ext_eps = \
        list(entry_point_getter(('invenio_ldapclient', None, 'invenio_base.apps'))) + \
        list(entry_point_getter(('invenio_accounts_ui', None, 'invenio_base.apps')))


    ui_ext_eps = get_partially_ordered_list(entry_point_getter((None, None, 'invenio_base.apps')),
                                            set(),
                                            ordered_ui_ext_eps)

    return ui_ext_eps

def _get_ui_bp_eps():
    ui_bp_eps = entry_point_getter((None, None, 'invenio_base.blueprints'))

    return ui_bp_eps



create_ui = create_app_factory(
    'invenio',
    config_loader=config_loader,
    blueprints=[ep.load() for ep in _get_ui_bp_eps()],
    extensions=[ep.load() for ep in _get_ui_ext_eps()],
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


create_api = _create_api
"""Since we don't yet have ldap auth for the api, we'll use invenio's factory for now."""


create_app = create_app_factory(
    'invenio',
    config_loader=config_loader,
    blueprints=[ep.load() for ep in _get_ui_bp_eps()],
    extensions=[ep.load() for ep in _get_ui_ext_eps()],
    converter_entry_points=['invenio_base.converters'],
    wsgi_factory=wsgi_proxyfix(create_wsgi_factory({'/api': create_api})),
    instance_path=instance_path,
    static_folder=static_folder,
    root_path=instance_path,
    static_url_path=static_url_path(),
    app_class=app_class(),
)

