import sys
from importlib.metadata import entry_points


'''
Enforcing order of a subset of entry points from a list of entry point groups.

Input: 

(name, value, group)

UnOrderedSegment0 iter[tuple[str,str,str]
OrderedSegment tuple[str,str,str] 


Output: List[Object]  
'''
 
def _epg_to_set(group, _map=None):
    eps = set()
    _map = dict() if _map is None else _map
    
    for ep in entry_points()[group]:
        attr_tup = (ep.name, ep.value, ep.group)
        eps.add(attr_tup)
        _map[attr_tup] = ep

    return eps

def _epgs_to_set(*groups):
    eps = set()
    _map = dict()
    
    sets = (_epg_to_set(group, _map) for group in groups)

    for _ in sets:
        eps = eps.union(_)

    return eps, _map
    

def _epgs_to_semi_ordered_list(unordered_initial_segment,
                               ordered_middle_segment,
                               eps):

    _unordered_init = set(unordered_initial_segment)
    _ordered_mid = set(ordered_middle_segment)

    assert _unordered_init.isdisjoint(_ordered_mid)

    _unordered_final = eps - _unordered_init - _ordered_mid

    out = list(unordered_initial_segment) + list(ordered_middle_segment) + \
        list(_unordered_final)
    
    return out

def mod_list(unordered_initial_segment,
             ordered_middle_segment,
             *groups):

    eps, _map = _epgs_to_set(*groups)
    
    m = _epgs_to_semi_ordered_list(unordered_initial_segment,
                                   ordered_middle_segment,
                                   eps)

    return [_map[_].load() for _ in m]


