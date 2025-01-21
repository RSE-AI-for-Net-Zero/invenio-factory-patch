from importlib.metadata import EntryPoint, entry_points
from collections.abc import Iterable
from typing import Union, List
import os

from invenio_app.factory import instance_path

def grab_and_remove_from_epgroup_by_name(name: str,
                                         group_in: Iterable[EntryPoint],
                                         removed: Union[Iterable[EntryPoint],None] = None
                                         )-> tuple[List[EntryPoint], List[EntryPoint]]:
    
    _removed: List[EntryPoint] = [] if removed is None else list(removed)
    group_out: List[EntryPoint] = []

    def _filter(ep: EntryPoint,
                rem: List[EntryPoint],
                out: List[EntryPoint]) -> None:

        if ep.name == name:
            rem.append(ep)
        else:
            out.append(ep)
        
    for ep in group_in:
        _filter(ep, _removed, group_out)

    return _removed, group_out

def read_names_from_config(config: str):
    config_path: str = os.path.join(instance_path(), config)

    names: List[str] = []

    with open(config_path, 'r') as f:
        for line in f:
            names.append(line.rstrip())

    return names

def split_entry_points(group: str, config: str):
    group_in: Iterable[EntryPoint] = entry_points()[group]
    
    try:
        names: List[str] = read_names_from_config(config)
    except FileNotFoundError:
        return {group: group_in}

    removed: List[EntryPoint]  = []
    remaining = group_in
    
    for name in names:
        removed, remaining = grab_and_remove_from_epgroup_by_name(name,
                                                                  remaining,
                                                                  removed)

    return {'removed': removed,
            group: remaining}
