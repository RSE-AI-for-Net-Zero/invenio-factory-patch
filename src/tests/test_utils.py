from unittest.mock import patch
import importlib.metadata
import os
import pytest
from invenio_factory_patch.utils import (
    grab_and_remove_from_epgroup_by_name,
    read_names_from_config,
    split_entry_points,
)

from invenio_factory_patch.utils import instance_path


def test_get_ui_ext_eps(mock_entry_points):
    @patch("importlib.metadata.entry_points", mock_entry_points)
    def inner():
        group = importlib.metadata.entry_points()["invenio_base.apps"]

        names = ["invenio_pidstore", "invenio_db", "invenio_accounts_ui"]
        removed = []
        remaining = group

        for name in names:
            removed, remaining = grab_and_remove_from_epgroup_by_name(
                name, remaining, removed
            )

        removed_names = [ep.name for ep in removed]
        assert removed_names == names

        assert removed[0].name == "invenio_pidstore"
        assert removed[1].name == "invenio_db"
        assert removed[2].name == "invenio_accounts_ui"

        for ep in remaining:
            assert ep.name not in names

        assert set(ep.name for ep in group) - set(names) == set(
            ep.name for ep in remaining
        )

    inner()


def test_get_ui_ext_eps_not_in_grp(mock_entry_points):
    @patch("importlib.metadata.entry_points", mock_entry_points)
    def inner():
        group = importlib.metadata.entry_points()["invenio_base.apps"]

        names = ["something", "not", "present"]
        removed = []
        remaining = group

        for name in names:
            removed, remaining = grab_and_remove_from_epgroup_by_name(
                name, remaining, removed
            )

        assert removed == []

        assert set(ep.name for ep in group) == set(ep.name for ep in remaining)

    inner()


def test_read_names_from_config(setup_instance):
    assert (
        "INVENIO_INSTANCE_PATH" in os.environ
        and os.environ["INVENIO_INSTANCE_PATH"] == instance_path()
    )

    _instance_path = instance_path()

    with open(os.path.join(_instance_path, "config_ui"), "r") as f:
        assert next(f).rstrip() == "invenio_ldapclient_ui"
        assert next(f).rstrip() == "invenio_accounts_ui"

    names = read_names_from_config("config_ui")
    assert names == ["invenio_ldapclient_ui", "invenio_accounts_ui"]


def test_split_entry_points(setup_instance, mock_entry_points):
    @patch("invenio_factory_patch.utils.entry_points", mock_entry_points)
    def inner():
        grp = mock_entry_points()["invenio_base.apps"]

        assert "invenio_ldapclient_ui" in [ep.name for ep in grp]
        assert "invenio_accounts_ui" in [ep.name for ep in grp]

        first, second = split_entry_points("invenio_base.apps", "config_ui")

        assert len(first) + len(second) == len(grp)

        assert (
            first[0].name == "invenio_ldapclient_ui"
            and first[0].value == "invenio_ldapclient:InvenioLDAPClientUI"
            and first[0].group == "invenio_base.apps"
        )

        assert (
            first[1].name == "invenio_accounts_ui"
            and first[1].value == "invenio_accounts:InvenioAccountsUI"
            and first[1].group == "invenio_base.apps"
        )

        assert "invenio_ldapclient_ui" not in [ep.name for ep in second]
        assert "invenio_accounts_ui" not in [ep.name for ep in second]

    inner()
