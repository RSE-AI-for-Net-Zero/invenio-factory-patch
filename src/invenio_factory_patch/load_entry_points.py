import sys
from importlib.metadata import entry_points as iter_entry_points


'''
Enforcing order of a subset of entry points from a list of entry point groups.

Input: 

(name, value, group)

UnOrderedSegment0 iter[tuple[str,str]
OrderedSegment tuple[str,str] 


Output: List[Object]  
'''
def _epgs_to_set(*groups):
    entry_points = iter_entry_points()
    
    _eps = set()
    _map = dict()

    for group in groups:
        for ep in entry_points[group]:
            attr_tup = (ep.name, ep.group)
            _eps.add(attr_tup)
            _map.setdefault(attr_tup, []).append(ep)
            
    return _eps, _map
    

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

    _eps, _map = _epgs_to_set(*groups)
    
    attr_tups = _epgs_to_semi_ordered_list(unordered_initial_segment,
                                           ordered_middle_segment,
                                           _eps)

    out = []

    for a in attr_tups:
        out.extend(_map[a])

    return out


