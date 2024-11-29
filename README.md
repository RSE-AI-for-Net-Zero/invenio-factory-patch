# Invenio factory patch

`invenio_app.factory.create_ui`, `create_api` and `create_app` load various objects by specifying an entry point group as an argument to `invenio_base.factory.create_app_factory`.
E.g., extensions and blueprints for the UI are loaded from
the groups `invenio_base.apps` and `invenio_base.blueprints`, respectively.

To add new modules to be loaded is simple - declare them as entry points in the appropriate group.  However, a problem arises if we need to enforce an order in which certain objects are loaded: e.g., if `ExtensionA` must 
**always** be loaded before `ExtensionB`.

This package is a drop-in for `invenio-app`, allowing enforced ordering of entry point loading.  It looks for two config files in the app's instance folder:  `config_ui` and `config_api`.  Each line of this
file is the name of an entry point in the groups `invenio_base.apps` and `invenio_base.api_apps`, respectively.  Entry points specified in these files are loaded first, in the order in which they appear in the
config files.  `invenio-factory-patch` replaces all things the factories `create_ui`, `create_api` and `create_app`, as well as the CLI (named `ae-datastore`) and the `celery` app.



## Usage
1. add as a dependency
2. add `config_ui` and `config_api` files to the app's instance path
3. instead of, e.g., doing this
   ```
   from invenio_app.celery import celery
   ```
   do this instead

   ```
   from invenio_factory_patch.celery import celery
   ```
   or instead of specifiy the uWSGI entry point in `uwsgi_ui.ini` as

   ```
   module = invenio_app.wsgi_ui:application
   ```
   specify it as

   ```
   module = invenio_factory_patch.wsgi_ui:application
   ```
   

## Development
