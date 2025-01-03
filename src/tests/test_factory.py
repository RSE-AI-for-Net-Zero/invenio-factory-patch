import os
from unittest.mock import patch
import pytest

def test_create_ui(setup_instance, mock_entry_points):
    @patch('invenio_app.factory.create_app_factory')
    @patch('invenio_factory_patch.utils.entry_points', mock_entry_points)
    def inner(mock_create_app_factory):
        from invenio_factory_patch.factory import create_ui

        extension_entry_points = mock_create_app_factory.call_args[1]["extension_entry_points"]

        assert extension_entry_points == ['removed', 'invenio_base.apps']

    inner()
        

    

    

