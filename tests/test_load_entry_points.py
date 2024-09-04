from unittest.mock import patch, Mock
from invenio_factory_patch.load_entry_points import (_epg_to_set,
                                                     _epgs_to_set,
                                                     _epgs_to_semi_ordered_list,
                                                     mod_list)
#from invenio_factory_patch.load_entry_points import entry_points
import pytest



#from invenio_factory_patch.load_entry_points import _epg_to_list_of_modules

def test__epg_to_list_of_modules():
    
    def _factory(name, value, group):
        ep = Mock(group = group, value = value)
        ep.name = name

        ep.load = Mock(name = value.rpartition(':')[2])

        return ep

    group1 = (_factory('invenio_accounts_ui',
                       'invenio_accounts:InvenioAccountsUI',
                       'invenio_base.apps'),
              _factory('invenio_indexer',
                       'invenio_indexer:InvenioIndexer',
                       'invenio_base.apps'),
              _factory('invenio_records_permissions',
                       'invenio_records_permissions:InvenioRecordsPermissions',
                       'invenio_base.apps'),
              _factory('invenio_admin',
                       'invenio_admin:InvenioAdmin',
                       'invenio_base.apps'),
              _factory('invenio_i18n',
                       'invenio_i18n:InvenioI18N',
                       'invenio_base.apps'),
              _factory('invenio_records_resources',
                       'invenio_records_resources:InvenioRecordsResources',
                       'invenio_base.apps'),
              _factory('invenio_search',
                       'invenio_search:InvenioSearch',
                       'invenio_base.apps'),
              _factory('invenio_pidstore',
                       'invenio_pidstore:InvenioPIDStore',
                       'invenio_base.apps'),
              _factory('invenio_jsonschemas',
                       'invenio_jsonschemas:InvenioJSONSchemasUI',
                       'invenio_base.apps'),
              _factory('invenio_oauth2server',
                       'invenio_oauth2server:InvenioOAuth2Server',
                       'invenio_base.apps'),
              _factory('invenio_previewer',
                       'invenio_previewer:InvenioPreviewer',
                       'invenio_base.apps'),
              _factory('invenio_access',
                       'invenio_access:InvenioAccess',
                       'invenio_base.apps'),
              _factory('invenio_db',
                       'invenio_db:InvenioDB',
                       'invenio_base.apps'),
              _factory('invenio_mail',
                       'invenio_mail:InvenioMail',
                       'invenio_base.apps'),
              _factory('invenio_theme',
                       'invenio_theme:InvenioTheme',
                       'invenio_base.apps'),
              _factory('invenio_search_ui',
                       'invenio_search_ui:InvenioSearchUI',
                       'invenio_base.apps'),
              _factory('invenio_records_ui',
                       'invenio_records_ui:InvenioRecordsUI',
                       'invenio_base.apps'),
              _factory('invenio_communities',
                       'invenio_communities:InvenioCommunities',
                       'invenio_base.apps'),
              _factory('invenio_app',
                       'invenio_app:InvenioApp',
                       'invenio_base.apps'),
              _factory('invenio_users_resources',
                        'invenio_users_resources.ext:InvenioUsersResources',
                       'invenio_base.apps'),
              _factory('invenio_cache',
                       'invenio_cache:InvenioCache',
                       'invenio_base.apps'),
              _factory('invenio_celery',
                       'invenio_celery:InvenioCelery',
                       'invenio_base.apps'),
              _factory('invenio_vocabularies',
                       'invenio_vocabularies:InvenioVocabularies',
                       'invenio_base.apps'))
    
    
    group2 = (_factory('invenio_pidstore',
                       'invenio_pidstore.models',
                       'invenio_db.models'),
              _factory('invenio_oauth2server',
                       'invenio_oauth2server.models',
                       'invenio_db.models'),              
              _factory('invenio_access',
                       'invenio_access.models',
                       'invenio_db.models'),
              _factory('invenio_communities',
                       'invenio_communities.communities.records.models',
                       'invenio_db.models'),
              _factory('invenio_communities_members',
                       'invenio_communities.members.records.models',
                       'invenio_db.models'),
              _factory('invenio_drafts_resources',
                       'invenio_drafts_resources.records.models',
                       'invenio_db.models'),
              _factory('affiliations',
                       'invenio_vocabularies.contrib.affiliations.models',
                       'invenio_db.models'),
              _factory('awards',
                       'invenio_vocabularies.contrib.awards.models',
                       'invenio_db.models'),
              _factory('funders',
                       'invenio_vocabularies.contrib.funders.models',
                       'invenio_db.models'),
              _factory('names',
                       'invenio_vocabularies.contrib.names.models',
                       'invenio_db.models'))

    mockedEntryPoints = {'m_invenio_base.apps': group1,
                         'm_invenio_db.models': group2}

    def mocked_entry_points():
        return mockedEntryPoints
    
    unordered_initial_segment = [('invenio_communities',
                                  'invenio_communities.communities.records.models',
                                  'invenio_db.models'),
                                 
                                 ('invenio_accounts_ui',
                                  'invenio_accounts:InvenioAccountsUI',
                                  'invenio_base.apps'),
                                 
                                 ('invenio_communities_members',
                                  'invenio_communities.members.records.models',
                                  'invenio_db.models'),]

    ordered_middle_segment = [('affiliations',
                               'invenio_vocabularies.contrib.affiliations.models',
                               'invenio_db.models'),
                              
                              ('awards',
                               'invenio_vocabularies.contrib.awards.models',
                               'invenio_db.models'),
                              
                              ('invenio_oauth2server',
                               'invenio_oauth2server.models',
                               'invenio_db.models'),
                              
                              ('funders',
                               'invenio_vocabularies.contrib.funders.models',
                               'invenio_db.models'),
                              
                              ('names',
                               'invenio_vocabularies.contrib.names.models',
                               'invenio_db.models'),]

    @patch('invenio_factory_patch.load_entry_points.entry_points', mocked_entry_points)
    def test__epg_to_set():
        eps = mocked_entry_points()

        assert 'm_invenio_base.apps' in eps
        assert 'm_invenio_db.models' in eps

        eps_base = _epg_to_set('m_invenio_base.apps')
        eps_models = _epg_to_set('m_invenio_db.models')
        
        assert isinstance(eps_base, set)
        assert isinstance(eps_models, set)

        eps, _map = _epgs_to_set('m_invenio_base.apps', 'm_invenio_db.models')

        assert isinstance(eps, set)
        assert eps_base <= eps
        assert eps_models <= eps

    @patch('invenio_factory_patch.load_entry_points.entry_points', mocked_entry_points)
    def test__epgs_to_semi_ordered_list():

        eps, _map = _epgs_to_set('m_invenio_base.apps', 'm_invenio_db.models')
        
        m = _epgs_to_semi_ordered_list(unordered_initial_segment,
                                       ordered_middle_segment,
                                       eps)
        

        i0 = m.index(('invenio_communities',
                      'invenio_communities.communities.records.models',
                      'invenio_db.models'))

        i1 = m.index(('invenio_accounts_ui',
                      'invenio_accounts:InvenioAccountsUI',
                      'invenio_base.apps'))
                                 
        i2 = m.index(('invenio_communities_members',
                      'invenio_communities.members.records.models',
                      'invenio_db.models'))
        
        inds = [i0, i1, i2]
        inds.sort()

        
        assert inds == [0, 1, 2]
        
        assert m.index(('affiliations',
                        'invenio_vocabularies.contrib.affiliations.models',
                        'invenio_db.models')) == 3

        assert m.index(('awards',
                        'invenio_vocabularies.contrib.awards.models',
                        'invenio_db.models')) == 4
                              
        assert m.index(('invenio_oauth2server',
                        'invenio_oauth2server.models',
                        'invenio_db.models')) == 5
                              
        assert m.index(('funders',
                        'invenio_vocabularies.contrib.funders.models',
                        'invenio_db.models')) == 6
                              
        assert m.index(('names',
                        'invenio_vocabularies.contrib.names.models',
                        'invenio_db.models')) == 7

        
        
        
        assert len(m) == len(group1) + len(group2)

        mods = mod_list(unordered_initial_segment,
                        ordered_middle_segment,
                        'm_invenio_base.apps',
                        'm_invenio_db.models')



    test__epg_to_set()
    test__epgs_to_semi_ordered_list()
    


                       

                                 
                                 
                                 

    


