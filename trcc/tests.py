from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_trcc_stg_testr_io(unittest.TestCase):
  @clear_session({'spanId': 27})
  def test_27_get_models_(self):
    # endpoint 27
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get('/models/')

  @json_dataset('data/test_29_get_models_modelId_name_all.json')
  @clear_session({'spanId': 29})
  def test_29_get_models_modelId_name_all(self, data_row):
    modelId, name, = data_row

    # endpoint 29
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all')

  @json_dataset('data/test_30_get_models_modelId_name_all_dataDependency.json')
  @clear_session({'spanId': 30})
  def test_30_get_models_modelId_name_all_dataDependency(self, data_row):
    modelId, name, = data_row

    # endpoint 30
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all/dataDependency')

  @json_dataset('data/test_33_get_models_modelId_name_all_swagger.json')
  @clear_session({'spanId': 33})
  def test_33_get_models_modelId_name_all_swagger(self, data_row):
    modelId, name, = data_row

    # endpoint 33
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/{name}/all/swagger')

  @json_dataset('data/test_40_get_models_modelId_name_param_tests_detectedAuth.json')
  @clear_session({'spanId': 40})
  def test_40_get_models_modelId_name_param_tests_detectedAuth(self, data_row):
    modelId, name, param, = data_row

    # endpoint 40
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
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

  @json_dataset('data/test_48_get_models_modelId_suites_name_agents_agentId_profiles.json')
  @clear_session({'spanId': 48})
  def test_48_get_models_modelId_suites_name_agents_agentId_profiles(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    agentId = jsonpath('$.[*].lastEnvInfo.agentId', resp)
    name = jsonpath('$.[*].name', resp)

    # endpoint 48
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/agents/{agentId}/profiles')

  @json_dataset('data/test_49_get_models_modelId_suites_name_runs.json')
  @clear_session({'spanId': 49})
  def test_49_get_models_modelId_suites_name_runs(self, data_row):
    modelId, modelId2, revisionId, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('revisionId', revisionId)])
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites' + qstr)
    name = jsonpath('$.[*].name', resp)

    # endpoint 49
    resp = trcc_stg_testr_io.get(f'/models/{modelId}/suites/{name}/runs')

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

  @json_dataset('data/test_59_get_testData_param_testData.json')
  @clear_session({'spanId': 59})
  def test_59_get_testData_param_testData(self, data_row):
    param, = data_row

    # endpoint 59
    trcc_stg_testr_io = get_http_target('TARGET_TRCC_STG_TESTR_IO', authenticate)
    resp = trcc_stg_testr_io.get(f'/testData/{param}/testData')

