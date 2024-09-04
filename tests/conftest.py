from unittest.mock import MagicMock, Mock
import pytest

class InvenioModuleMock(Mock):
    def __init__(self, name):
        self.name = name

class EntryPointMock(MagicMock):
    def __init__(self, name, group, extension_class):
        self.name = name
        self.group = group
        self.value = name + ':' + extension_class

    def load(self):
        m = InvenioModuleMock(name)
        return m

@pytest.fixture
def entry_points():
    return {'invenio_base.apps': EntryPointMock(name='invenio_accounts_ui',
                                                group='invenio_base.apps',
                                                extension_class='InvenioAccountsUI')}
    

    
    
