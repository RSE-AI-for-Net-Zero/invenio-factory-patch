import os
from unittest.mock import patch
import pytest

def test_create_ui(setup_instance, mock_entry_points):
    @patch('invenio_app.factory.create_app_factory')
    @patch('invenio_factory_patch.utils.entry_points', mock_entry_points)
    def inner(mock_create_app_factory):
        from invenio_factory_patch.factory import create_ui

        extep_arg = call_kwargs = mock_create_app_factory.call_args[1]["extension_entry_points"]

        assert extep_arg[0][0].name == "invenio_ldapclient_ui"
        assert extep_arg[0][1].name == "invenio_accounts_ui"

    inner()
        

    

    

