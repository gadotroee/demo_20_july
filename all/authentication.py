from up9lib import *


def authenticate(target_key, target):
        with open('data/auth_data.json') as fp:
            auth_data = json.load(fp)
        
        if target_key == 'TARGET_AUTH_STG_TESTR_IO':
            password, username, =  get_first_row_from_dataset('test_3_get_oauth_cb.json')
        
            # endpoint 1
            stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', dummy_auth)
            resp = stg_testr_io.get('/')
            redirect_uri = url_part('?redirect_uri', get_data_from_header('location', resp))
            state = url_part('?state', get_data_from_header('location', resp))
        
            # endpoint 9
            qstr = '?' + urlencode([('client_id', 'react-client'), ('redirect_uri', redirect_uri), ('response_type', 'code'), ('state', state)])
            resp = target.get('/auth/realms/testr/protocol/openid-connect/auth' + qstr)
            execution = url_part('?execution', cssselect('form#kc-form-login[action] @action', resp))
            session_code = url_part('?session_code', cssselect('form#kc-form-login[action] @action', resp))
            tab_id = url_part('?tab_id', cssselect('a#signupLink[href] @href', resp))
        
            # endpoint 7
            qstr = '?' + urlencode([('client_id', 'react-client'), ('execution', execution), ('session_code', session_code), ('tab_id', tab_id)])
            resp = target.post('/auth/realms/testr/login-actions/authenticate' + qstr, data=[('password', password), ('username', username)])
            _code = url_part('?code', get_data_from_header('location', resp))
            session_state = url_part('?session_state', get_data_from_header('location', resp))
            state1 = url_part('?state', get_data_from_header('location', resp))
        
            # endpoint 3
            qstr = '?' + urlencode([('code', _code), ('session_state', session_state), ('state', state1)])
            resp = stg_testr_io.get('/oauth_cb' + qstr)
        
        elif target_key == 'TARGET_AUTHDETECTOR_STG_TESTR_IO':
            token = random.choice(auth_data['TARGET_AUTHDETECTOR_STG_TESTR_IO'])
            target.additional_headers({'Authorization': token})
        
        elif target_key == 'TARGET_STG_TESTR_IO':
            password, username, =  get_first_row_from_dataset('test_3_get_oauth_cb.json')
        
            # endpoint 1
            resp = target.get('/')
            redirect_uri = url_part('?redirect_uri', get_data_from_header('location', resp))
            state = url_part('?state', get_data_from_header('location', resp))
        
            # endpoint 9
            qstr = '?' + urlencode([('client_id', 'react-client'), ('redirect_uri', redirect_uri), ('response_type', 'code'), ('state', state)])
            auth_stg_testr_io = get_http_target('TARGET_AUTH_STG_TESTR_IO', dummy_auth)
            resp = auth_stg_testr_io.get('/auth/realms/testr/protocol/openid-connect/auth' + qstr)
            execution = url_part('?execution', cssselect('form#kc-form-login[action] @action', resp))
            session_code = url_part('?session_code', cssselect('form#kc-form-login[action] @action', resp))
            tab_id = url_part('?tab_id', cssselect('a#signupLink[href] @href', resp))
        
            # endpoint 7
            qstr = '?' + urlencode([('client_id', 'react-client'), ('execution', execution), ('session_code', session_code), ('tab_id', tab_id)])
            resp = auth_stg_testr_io.post('/auth/realms/testr/login-actions/authenticate' + qstr, data=[('password', password), ('username', username)])
            _code = url_part('?code', get_data_from_header('location', resp))
            session_state = url_part('?session_state', get_data_from_header('location', resp))
            state1 = url_part('?state', get_data_from_header('location', resp))
        
            # endpoint 3
            qstr = '?' + urlencode([('code', _code), ('session_state', session_state), ('state', state1)])
            resp = target.get('/oauth_cb' + qstr)
        
        elif target_key == 'TARGET_TRCC_STG_TESTR_IO':
            token = random.choice(auth_data['TARGET_TRCC_STG_TESTR_IO'])
            target.additional_headers({'Authorization': token})
        
        else:
          pass
        


