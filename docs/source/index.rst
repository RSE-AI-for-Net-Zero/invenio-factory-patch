.. Invenio factory patch documentation master file, created by
   sphinx-quickstart on Fri Nov 29 17:03:34 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Invenio factory patch documentation
===================================

Replaces the factory functions, celery and wsgi entry points defined in :code:`invenio_app` to ensure certain extension modules are loaded in a specific order.  Also provides a replacement for the *invenio* CLI instance management tool.

Entry point names listed in :file:`invenio_factory_patch_ui.cfg` are loaded (in the order listed) before all other entry points in group :code:`invenio_base.apps`.  Similarly, entry point names listed in :file:`invenio_factory_patch_api.cfg` are loaded (in the order listed) before all other entry points in group :code:`invenio_base.api_apps`. 

.. automodule:: invenio_factory_patch.factory
   :members:

.. automodule:: invenio_factory_patch.celery
   :members:
      
.. automodule:: invenio_factory_patch.celery_ui
   :members:

.. automodule:: invenio_factory_patch.celery_api
   :members:

.. automodule:: invenio_factory_patch.wsgi
   :members:
      
.. automodule:: invenio_factory_patch.wsgi_ui
   :members:

.. automodule:: invenio_factory_patch.wsgi_api
   :members:

.. automodule:: invenio_factory_patch.cli
   :members:

