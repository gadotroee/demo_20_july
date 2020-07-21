from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_sockshop_haiut_dev_spyd_io(unittest.TestCase):
  @clear_session({'spanId': 1})
  def test_1_get_address(self):
    # endpoint 2
    sockshop_haiut_dev_spyd_io = get_http_target('TARGET_SOCKSHOP_HAIUT_DEV_SPYD_IO', authenticate)
    resp = sockshop_haiut_dev_spyd_io.get('/card', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)

    # endpoint 1
    resp = sockshop_haiut_dev_spyd_io.get('/address', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)
    resp.assert_jsonpath('$.city', expected_value='Kfar Saba')

  @json_dataset('data/test_3_get_cart.json')
  @clear_session({'spanId': 3})
  def test_3_get_cart(self, data_row):
    customerId, size, = data_row

    # endpoint 11
    sockshop_haiut_dev_spyd_io = get_http_target('TARGET_SOCKSHOP_HAIUT_DEV_SPYD_IO', authenticate)
    resp = sockshop_haiut_dev_spyd_io.get(f'/customers/{customerId}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)
    resp.assert_jsonpath('$.username', expected_value='alex01')

    # endpoint 9
    qstr = '?' + urlencode([('page', '1'), ('size', size), ('tags', '')])
    resp = sockshop_haiut_dev_spyd_io.get('/catalogue' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)
    _id = jsonpath('$.[*].id', resp)

    # endpoint 7
    resp = sockshop_haiut_dev_spyd_io.get(f'/catalogue/{_id}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)

    # endpoint 3
    resp = sockshop_haiut_dev_spyd_io.get('/cart', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)

  @clear_session({'spanId': 8})
  def test_8_get_catalogue_size(self):
    # endpoint 8
    qstr = '?' + urlencode([('tags', '')])
    sockshop_haiut_dev_spyd_io = get_http_target('TARGET_SOCKSHOP_HAIUT_DEV_SPYD_IO', authenticate)
    resp = sockshop_haiut_dev_spyd_io.get('/catalogue/size' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)

  @json_dataset('data/test_10_get_param.json')
  @clear_session({'spanId': 10})
  def test_10_get_param(self, data_row):
    order, param, = data_row

    # endpoint 10
    qstr = '?' + urlencode([('order', order)])
    sockshop_haiut_dev_spyd_io = get_http_target('TARGET_SOCKSHOP_HAIUT_DEV_SPYD_IO', authenticate)
    resp = sockshop_haiut_dev_spyd_io.get(f'/{param}' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)
    resp.assert_cssselect('div#top div.container div.offer a.btn.btn-success.btn-sm', expected_value='Offer of the day')

  # authentication-related test
  @clear_session({'spanId': 14})
  def test_14_get_login(self):
    # endpoint 14
    sockshop_haiut_dev_spyd_io = get_http_target('TARGET_SOCKSHOP_HAIUT_DEV_SPYD_IO', dummy_auth)
    resp = sockshop_haiut_dev_spyd_io.get('/login', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)
    resp.assert_cssselect('p', expected_value='Cookie is set')

  @json_dataset('data/test_18_get_orders_orderId.json')
  @clear_session({'spanId': 18})
  def test_18_get_orders_orderId(self, data_row):
    orderId, = data_row

    # endpoint 18
    sockshop_haiut_dev_spyd_io = get_http_target('TARGET_SOCKSHOP_HAIUT_DEV_SPYD_IO', authenticate)
    resp = sockshop_haiut_dev_spyd_io.get(f'/orders/{orderId}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)
    resp.assert_jsonpath('$.address.city', expected_value='Kfar Saba')

  @json_dataset('data/test_19_get_tags.json')
  @clear_session({'spanId': 19})
  def test_19_get_tags(self, data_row):
    customerId, size, = data_row

    # endpoint 11
    sockshop_haiut_dev_spyd_io = get_http_target('TARGET_SOCKSHOP_HAIUT_DEV_SPYD_IO', authenticate)
    resp = sockshop_haiut_dev_spyd_io.get(f'/customers/{customerId}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)
    resp.assert_jsonpath('$.username', expected_value='alex01')

    # endpoint 9
    qstr = '?' + urlencode([('page', '1'), ('size', size), ('tags', '')])
    resp = sockshop_haiut_dev_spyd_io.get('/catalogue' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)

    # endpoint 19
    resp = sockshop_haiut_dev_spyd_io.get('/tags', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
    resp.assert_status_code(200)
