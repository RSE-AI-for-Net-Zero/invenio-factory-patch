from unittest.mock import MagicMock, Mock
import tempfile
import os
import shutil
import pytest


def _mock_entry_point_factory(name, value, group):
    mock = MagicMock(value=value, group=group)

    mock.name = name  # You can't set a name attrib on a Mock when constructing!

    return mock


@pytest.fixture
def mock_entry_points():
    def _factory():
        return {
            "invenio_base.apps": [
                _mock_entry_point_factory(
                    "invenio_accounts_ui",
                    "invenio_accounts:InvenioAccountsUI",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_indexer",
                    "invenio_indexer:InvenioIndexer",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_records_permissions",
                    "invenio_records_permissions:InvenioRecordsPermissions",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_admin", "invenio_admin:InvenioAdmin", "invenio_base.apps"
                ),
                _mock_entry_point_factory(
                    "invenio_i18n", "invenio_i18n:InvenioI18N", "invenio_base.apps"
                ),
                _mock_entry_point_factory(
                    "invenio_records_resources",
                    "invenio_records_resources:InvenioRecordsResources",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_search",
                    "invenio_search:InvenioSearch",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_pidstore",
                    "invenio_pidstore:InvenioPIDStore",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_jsonschemas",
                    "invenio_jsonschemas:InvenioJSONSchemasUI",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_oauth2server",
                    "invenio_oauth2server:InvenioOAuth2Server",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_previewer",
                    "invenio_previewer:InvenioPreviewer",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_access",
                    "invenio_access:InvenioAccess",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_db", "invenio_db:InvenioDB", "invenio_base.apps"
                ),
                _mock_entry_point_factory(
                    "invenio_mail", "invenio_mail:InvenioMail", "invenio_base.apps"
                ),
                _mock_entry_point_factory(
                    "invenio_theme", "invenio_theme:InvenioTheme", "invenio_base.apps"
                ),
                _mock_entry_point_factory(
                    "invenio_search_ui",
                    "invenio_search_ui:InvenioSearchUI",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_records_ui",
                    "invenio_records_ui:InvenioRecordsUI",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_records_ui",
                    "invenio_records_ui:SomethingElse",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_communities",
                    "invenio_communities:InvenioCommunities",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_app", "invenio_app:InvenioApp", "invenio_base.apps"
                ),
                _mock_entry_point_factory(
                    "invenio_users_resources",
                    "invenio_users_resources.ext:InvenioUsersResources",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_cache", "invenio_cache:InvenioCache", "invenio_base.apps"
                ),
                _mock_entry_point_factory(
                    "invenio_celery",
                    "invenio_celery:InvenioCelery",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_vocabularies",
                    "invenio_vocabularies:InvenioVocabularies",
                    "invenio_base.apps",
                ),
                _mock_entry_point_factory(
                    "invenio_ldapclient_ui",
                    "invenio_ldapclient:InvenioLDAPClientUI",
                    "invenio_base.apps",
                ),
            ],
            "invenio_db.models": [
                _mock_entry_point_factory(
                    "invenio_pidstore", "invenio_pidstore.models", "invenio_db.models"
                ),
                _mock_entry_point_factory(
                    "invenio_oauth2server",
                    "invenio_oauth2server.models",
                    "invenio_db.models",
                ),
                _mock_entry_point_factory(
                    "invenio_access", "invenio_access.models", "invenio_db.models"
                ),
                _mock_entry_point_factory(
                    "invenio_communities",
                    "invenio_communities.communities.records.models",
                    "invenio_db.models",
                ),
                _mock_entry_point_factory(
                    "invenio_communities_members",
                    "invenio_communities.members.records.models",
                    "invenio_db.models",
                ),
                _mock_entry_point_factory(
                    "invenio_drafts_resources",
                    "invenio_drafts_resources.records.models",
                    "invenio_db.models",
                ),
                _mock_entry_point_factory(
                    "affiliations",
                    "invenio_vocabularies.contrib.affiliations.models",
                    "invenio_db.models",
                ),
                _mock_entry_point_factory(
                    "awards",
                    "invenio_vocabularies.contrib.awards.models",
                    "invenio_db.models",
                ),
                _mock_entry_point_factory(
                    "funders",
                    "invenio_vocabularies.contrib.funders.models",
                    "invenio_db.models",
                ),
                _mock_entry_point_factory(
                    "names",
                    "invenio_vocabularies.contrib.names.models",
                    "invenio_db.models",
                ),
            ],
        }

    return _factory


@pytest.fixture
def setup_instance():
    tmp_instance_dir = tempfile.mkdtemp(prefix="inv_fac_patch")
    os.environ["INVENIO_INSTANCE_PATH"] = tmp_instance_dir

    names = ["invenio_ldapclient_ui", "invenio_accounts_ui"]

    with open(os.path.join(tmp_instance_dir, "invenio_factory_patch_ui.cfg"), "w") as f:
        for name in names:
            f.write("%s\n" % name)

    yield

    shutil.rmtree(tmp_instance_dir)
