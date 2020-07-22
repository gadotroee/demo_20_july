from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_auth_stg_testr_io(unittest.TestCase):
  # authentication-related test
  @clear_session({'spanId': 6})
  def test_6_get_auth_realms_testr_broker_google_login(self):
    # endpoint 1
    stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', dummy_auth)
    resp = stg_testr_io.get('/')
    redirect_uri = url_part('?redirect_uri', get_data_from_header('location', resp))
    state = url_part('?state', get_data_from_header('location', resp))

    # endpoint 9
    qstr = '?' + urlencode([('client_id', 'react-client'), ('redirect_uri', redirect_uri), ('response_type', 'code'), ('state', state)])
    auth_stg_testr_io = get_http_target('TARGET_AUTH_STG_TESTR_IO', dummy_auth)
    resp = auth_stg_testr_io.get('/auth/realms/testr/protocol/openid-connect/auth' + qstr)
    session_code = url_part('?session_code', cssselect('form#kc-form-login[action] @action', resp))
    tab_id = url_part('?tab_id', cssselect('a#signupLink[href] @href', resp))

    # endpoint 6
    qstr = '?' + urlencode([('client_id', 'react-client'), ('session_code', session_code), ('tab_id', tab_id)])
    resp = auth_stg_testr_io.get('/auth/realms/testr/broker/google/login' + qstr)

  # authentication-related test
  @clear_session({'spanId': 10})
  def test_10_get_auth_realms_testr_protocol_openid_connect_login_status_iframe_html(self):
    # endpoint 10
    auth_stg_testr_io = get_http_target('TARGET_AUTH_STG_TESTR_IO', dummy_auth)
    resp = auth_stg_testr_io.get('/auth/realms/testr/protocol/openid-connect/login-status-iframe.html')

  # authentication-related test
  @json_dataset('data/test_11_get_auth_realms_testr_protocol_openid_connect_login_status_iframe_html_init.json')
  @clear_session({'spanId': 11})
  def test_11_get_auth_realms_testr_protocol_openid_connect_login_status_iframe_html_init(self, data_row):
    origin, = data_row

    # endpoint 11
    qstr = '?' + urlencode([('client_id', 'react-client'), ('origin', origin)])
    auth_stg_testr_io = get_http_target('TARGET_AUTH_STG_TESTR_IO', dummy_auth)
    resp = auth_stg_testr_io.get('/auth/realms/testr/protocol/openid-connect/login-status-iframe.html/init' + qstr)

  # authentication-related test
  @json_dataset('data/test_12_post_auth_realms_testr_protocol_openid_connect_token.json')
  @clear_session({'spanId': 12})
  def test_12_post_auth_realms_testr_protocol_openid_connect_token(self, data_row):
    nonce, redirect_uri, = data_row

    # endpoint 1
    stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', dummy_auth)
    resp = stg_testr_io.get('/')
    redirect_uri1 = url_part('?redirect_uri', get_data_from_header('location', resp))
    state = url_part('?state', get_data_from_header('location', resp))

    # endpoint 8
    qstr = '?' + urlencode([('client_id', 'react-client'), ('nonce', nonce), ('prompt', 'none'), ('redirect_uri', redirect_uri1), ('response_mode', 'fragment'), ('response_type', 'code'), ('scope', 'openid'), ('state', state)])
    auth_stg_testr_io = get_http_target('TARGET_AUTH_STG_TESTR_IO', dummy_auth)
    resp = auth_stg_testr_io.get('/auth/realms/testr/protocol/openid-connect/auth' + qstr)
    _code = url_part('#code', get_data_from_header('location', resp))

    # endpoint 12
    resp = auth_stg_testr_io.post('/auth/realms/testr/protocol/openid-connect/token', data=[('client_id', 'react-client'), ('code', _code), ('grant_type', 'authorization_code'), ('redirect_uri', redirect_uri)])

@data_driven_tests
class Tests_authdetector_stg_testr_io(unittest.TestCase):
  @json_dataset('data/test_60_get_detect.json')
  @clear_session({'spanId': 60})
  def test_60_get_detect(self, data_row):
    model, = data_row

    # endpoint 60
    qstr = '?' + urlencode([('model', model), ('subsystem', 'liraz')])
    authdetector_stg_testr_io = get_http_target('TARGET_AUTHDETECTOR_STG_TESTR_IO', authenticate)
    resp = authdetector_stg_testr_io.get('/detect' + qstr)

@data_driven_tests
class Tests_stg_testr_io(unittest.TestCase):
  @clear_session({'spanId': 1})
  def test_1_get_(self):
    # endpoint 1
    stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', authenticate)
    resp = stg_testr_io.get('/')

  @clear_session({'spanId': 2})
  def test_2_get_(self):
    # endpoint 2
    stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', authenticate)
    resp = stg_testr_io.get('/')

  # authentication-related test
  @json_dataset('data/test_3_get_oauth_cb.json')
  @clear_session({'spanId': 3})
  def test_3_get_oauth_cb(self, data_row):
    password, username, = data_row

    # endpoint 1
    stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', dummy_auth)
    resp = stg_testr_io.get('/')
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
    resp = stg_testr_io.get('/oauth_cb' + qstr)

  @clear_session({'spanId': 4})
  def test_4_get_silent_check_sso_html(self):
    # endpoint 4
    stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', authenticate)
    resp = stg_testr_io.get('/silent-check-sso.html')

  @json_dataset('data/test_5_get_param1_model_param2_lastResults_systems_liraz_summary.json')
  @clear_session({'spanId': 5})
  def test_5_get_param1_model_param2_lastResults_systems_liraz_summary(self, data_row):
    param, param2, = data_row

    # endpoint 5
    stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', authenticate)
    resp = stg_testr_io.get(f'/{param}/model/{param}/lastResults/systems/liraz/summary')

  @clear_session({'spanId': 25})
  def test_25_get_(self):
    # endpoint 25
    stg_testr_io = get_http_target('TARGET_STG_TESTR_IO', authenticate)
    resp = stg_testr_io.get('/')

@data_driven_tests
class Tests_trcc_stg_testr_io(unittest.TestCase):
  @clear_session({'spanId': 27})
  def test_27_get_models_(self):
    # endpoint 27
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get('/models/')

  @json_dataset('data/test_28_get_models_modelId_name_har_param.json')
  @clear_session({'spanId': 28})
  def test_28_get_models_modelId_name_har_param(self, data_row):
    modelId, modelId2, modelId3, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 35
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/har')
    param = jsonpath('$.[*]', resp)

    # endpoint 28
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/har/{param}')

  @json_dataset('data/test_29_get_models_modelId_name_all.json')
  @clear_session({'spanId': 29})
  def test_29_get_models_modelId_name_all(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 29
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all')

  @json_dataset('data/test_30_get_models_modelId_name_all_dataDependency.json')
  @clear_session({'spanId': 30})
  def test_30_get_models_modelId_name_all_dataDependency(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 30
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all/dataDependency')

  @json_dataset('data/test_31_get_models_modelId_name_all_dataDependency_span.json')
  @clear_session({'spanId': 31})
  def test_31_get_models_modelId_name_all_dataDependency_span(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 31
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all/dataDependency/span')

  @json_dataset('data/test_32_get_models_modelId_name_all_dataDependency_span_param.json')
  @clear_session({'spanId': 32})
  def test_32_get_models_modelId_name_all_dataDependency_span_param(self, data_row):
    modelId, modelId2, param, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 32
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all/dataDependency/span/{param}')

  @json_dataset('data/test_34_get_models_modelId_name_all_tests.json')
  @clear_session({'spanId': 34})
  def test_34_get_models_modelId_name_all_tests(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 34
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all/tests')

  @json_dataset('data/test_36_get_models_modelId_name_liraz.json')
  @clear_session({'spanId': 36})
  def test_36_get_models_modelId_name_liraz(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 36
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/liraz')

  @json_dataset('data/test_37_get_models_modelId_name_liraz_dataDependency.json')
  @clear_session({'spanId': 37})
  def test_37_get_models_modelId_name_liraz_dataDependency(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 37
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/liraz/dataDependency')

  @json_dataset('data/test_38_get_models_modelId_name_liraz_dataDependency_span.json')
  @clear_session({'spanId': 38})
  def test_38_get_models_modelId_name_liraz_dataDependency_span(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 38
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/liraz/dataDependency/span')

  @json_dataset('data/test_39_get_models_modelId_name_liraz_swagger.json')
  @clear_session({'spanId': 39})
  def test_39_get_models_modelId_name_liraz_swagger(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 39
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/liraz/swagger')

  @json_dataset('data/test_40_get_models_modelId_name_param_tests_detectedAuth.json')
  @clear_session({'spanId': 40})
  def test_40_get_models_modelId_name_param_tests_detectedAuth(self, data_row):
    modelId, modelId2, param, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 40
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/{param}/tests/detectedAuth')

  @json_dataset('data/test_41_get_models_modelId_performance.json')
  @clear_session({'spanId': 41})
  def test_41_get_models_modelId_performance(self, data_row):
    modelId, modelId2, modelId3, param, revisionId, = data_row

    # endpoint 26
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get('/agents/')

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 45
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/{param}')

    # endpoint 41
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/performance')

  @json_dataset('data/test_42_get_models_modelId_revisions.json')
  @clear_session({'spanId': 42})
  def test_42_get_models_modelId_revisions(self, data_row):
    modelId, modelId2, modelId3, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 33
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all/swagger')

    # endpoint 42
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/revisions')

  @json_dataset('data/test_43_get_models_modelId_revisions_latest.json')
  @clear_session({'spanId': 43})
  def test_43_get_models_modelId_revisions_latest(self, data_row):
    modelId, = data_row

    # endpoint 43
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/revisions/latest')

  @json_dataset('data/test_44_get_models_modelId_status.json')
  @clear_session({'spanId': 44})
  def test_44_get_models_modelId_status(self, data_row):
    modelId, = data_row

    # endpoint 44
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/status')

  @json_dataset('data/test_46_get_models_modelId_suites_name_param_targets.json')
  @clear_session({'spanId': 46})
  def test_46_get_models_modelId_suites_name_param_targets(self, data_row):
    modelId, modelId2, modelId3, param, param2, revisionId, = data_row

    # endpoint 26
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get('/agents/')

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 45
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/{param}')

    # endpoint 46
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/{param}/targets')

  @json_dataset('data/test_47_get_models_modelId_suites_name_param_tests.json')
  @clear_session({'spanId': 47})
  def test_47_get_models_modelId_suites_name_param_tests(self, data_row):
    modelId, modelId2, modelId3, param, param2, revisionId, = data_row

    # endpoint 26
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get('/agents/')

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 45
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/{param}')

    # endpoint 47
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/{param}/tests')

  @json_dataset('data/test_50_get_models_modelId_suites_name_runs_runId.json')
  @clear_session({'spanId': 50})
  def test_50_get_models_modelId_suites_name_runs_runId(self, data_row):
    modelId, modelId2, revisionId, runId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 50
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/runs/{runId}')

  @json_dataset('data/test_51_get_models_modelId_suites_name_runs_state.json')
  @clear_session({'spanId': 51})
  def test_51_get_models_modelId_suites_name_runs_state(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 51
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/runs/state')

  @json_dataset('data/test_52_post_models_modelId_suites_name_skipSpans.json')
  @clear_session({'spanId': 52})
  def test_52_post_models_modelId_suites_name_skipSpans(self, data_row):
    modelId, modelId2, param, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 52
    with open('data/payload_for_trcc_stg_testr_io_endp52.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, "$.[*]", param)
    resp = trcc_stg_testr_io.post(f'/models/{modelId}/suites/{name}/skipSpans', json=json_payload)

  @json_dataset('data/test_53_post_models_modelId_suites_name_unskipSpans.json')
  @clear_session({'spanId': 53})
  def test_53_post_models_modelId_suites_name_unskipSpans(self, data_row):
    modelId, modelId2, param, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 53
    with open('data/payload_for_trcc_stg_testr_io_endp53.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, "$.[*]", param)
    resp = trcc_stg_testr_io.post(f'/models/{modelId}/suites/{name}/unskipSpans', json=json_payload)

  # authentication-related test
  @json_dataset('data/test_54_post_models_modelId_suites_name1_agents_agentId_profiles_name2_.json')
  @clear_session({'spanId': 54})
  def test_54_post_models_modelId_suites_name1_agents_agentId_profiles_name2_(self, data_row):
    method, modelId, modelId2, modelId3, modelId4, modelId5, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', dummy_auth)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    agentId = jsonpath('$.[*].lastEnvInfo.agentId', resp)
    name = jsonpath('$.[*].name', resp)

    # endpoint 48
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/agents/{agentId}/profiles')
    formURL = jsonpath('$.[*].authentication.authHelper.formURL', resp)
    name1 = jsonpath('$.[*].name', resp)
    originalUrl = jsonpath('$.[*].authentication.authHelper.endpoints.[*].originalUrl', resp)
    regex = jsonpath('$.[*].authentication.authHelper.endpoints.[*].regex', resp)
    target = jsonpath('$.[*].authentication.authHelper.endpoints.[*].target', resp)

    # endpoint 29
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all')
    provider = jsonpath('$.contracts.[*].provider', resp)

    # endpoint 30
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all/dataDependency')
    knownValues = jsonpath('$.[*].inputParameters.[*].knownValues.[*]', resp)
    path = jsonpath('$.[*].path', resp)

    # endpoint 54
    with open('data/payload_for_trcc_stg_testr_io_endp54.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, "$.authentication.authHelper.additionalUrls.[*]", knownValues)
    apply_into_json(json_payload, "$.authentication.authHelper.endpoints.[*].method", method)
    apply_into_json(json_payload, "$.authentication.authHelper.endpoints.[*].originalUrl", originalUrl)
    apply_into_json(json_payload, "$.authentication.authHelper.endpoints.[*].path", path)
    apply_into_json(json_payload, "$.authentication.authHelper.endpoints.[*].regex", regex)
    apply_into_json(json_payload, "$.authentication.authHelper.endpoints.[*].service", provider)
    apply_into_json(json_payload, "$.authentication.authHelper.endpoints.[*].target", target)
    apply_into_json(json_payload, "$.authentication.authHelper.formURL", formURL)
    apply_into_json(json_payload, "$.authentication.authHelper.password", knownValues)
    apply_into_json(json_payload, "$.authentication.authHelper.username", knownValues)
    resp = trcc_stg_testr_io.post(f'/models/{modelId}/suites/{name}/agents/{agentId}/profiles/{name1}/', json=json_payload)

  @json_dataset('data/test_55_post_models_modelId_suites_name1_agents_agentId_profiles_name2_verify.json')
  @clear_session({'spanId': 55})
  def test_55_post_models_modelId_suites_name1_agents_agentId_profiles_name2_verify(self, data_row):
    modelId, modelId2, modelId3, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    agentId = jsonpath('$.[*].lastEnvInfo.agentId', resp)
    name = jsonpath('$.[*].name', resp)

    # endpoint 48
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/agents/{agentId}/profiles')
    name1 = jsonpath('$.[*].name', resp)

    # endpoint 55
    with open('data/payload_for_trcc_stg_testr_io_endp55.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    resp = trcc_stg_testr_io.post(f'/models/{modelId}/suites/{name}/agents/{agentId}/profiles/{name1}/verify', json=json_payload)

  @json_dataset('data/test_56_get_models_modelId_suites_name1_agents_agentId_profiles_name2_verify_param.json')
  @clear_session({'spanId': 56})
  def test_56_get_models_modelId_suites_name1_agents_agentId_profiles_name2_verify_param(self, data_row):
    modelId, modelId2, modelId3, param, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    agentId = jsonpath('$.[*].lastEnvInfo.agentId', resp)
    name = jsonpath('$.[*].name', resp)

    # endpoint 48
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/agents/{agentId}/profiles')
    name1 = jsonpath('$.[*].name', resp)

    # endpoint 56
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/agents/{agentId}/profiles/{name1}/verify/{param}')

  @json_dataset('data/test_57_post_models_modelId_suites_name_runs.json')
  @clear_session({'spanId': 57})
  def test_57_post_models_modelId_suites_name_runs(self, data_row):
    modelId, modelId2, modelId3, revisionId, revisionId2, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    agentId = jsonpath('$.[*].lastEnvInfo.agentId', resp)
    name = jsonpath('$.[*].name', resp)

    # endpoint 49
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/runs')
    envProfile = jsonpath('$.[*].envProfile', resp)

    # endpoint 57
    with open('data/payload_for_trcc_stg_testr_io_endp57.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, "$.agentId", agentId)
    apply_into_json(json_payload, "$.envProfileName", envProfile)
    apply_into_json(json_payload, "$.revisionId", revisionId)
    resp = trcc_stg_testr_io.post(f'/models/{modelId}/suites/{name}/runs', json=json_payload)

  @json_dataset('data/test_59_get_testData_param_testData.json')
  @clear_session({'spanId': 59})
  def test_59_get_testData_param_testData(self, data_row):
    param, = data_row

    # endpoint 59
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/testData/{param}/testData')

