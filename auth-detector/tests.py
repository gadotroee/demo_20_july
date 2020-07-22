from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


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

