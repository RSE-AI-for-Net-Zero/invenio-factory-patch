from invenio_base.app import create_cli

from .factory import create_app

cli = create_cli(create_app=create_app)
