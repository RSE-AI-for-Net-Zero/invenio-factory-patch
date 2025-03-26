from invenio_base.app import create_cli

from .factory import create_app

cli = create_cli(create_app=create_app)
"""
Provides :code:`ae-datastore` Flask cli app, ensuring that

- :code:`InvenioDomainRDMRecords` is loaded **in place of** :code:`InvenioRDMRecords`

Registered in as *project.script* entry point.

Replaces :code:`invenio_app` factory function.
"""
