from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_trdemo_client_trdemo(unittest.TestCase):
  @clear_session({'spanId': 3})
  def test_3_get_(self):
    # endpoint 3
    trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
    resp = trdemo_client_trdemo.get('/')

  @clear_session({'spanId': 5})
  def test_5_get_cart(self):
    # endpoint 5
    trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
    resp = trdemo_client_trdemo.get('/cart')

  @json_dataset('data/test_6_get_cart_remove_product_id.json')
  @clear_session({'spanId': 6})
  def test_6_get_cart_remove_product_id(self, data_row):
    source, startDate, = data_row

    # endpoint 4
    trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
    resp = trdemo_client_trdemo.get('/cart')
    value = cssselect('datalist#apt_list option[value] @value', resp)

    # endpoint 10
    qstr = '?' + urlencode([('destination', value), ('endDate', ''), ('source', source), ('startDate', startDate)])
    resp = trdemo_client_trdemo.get('/search' + qstr)
    product_id = url_part('?product_id', cssselect('div.container-fluid div table.table.table-striped tbody tr td a[href] @href', resp))

    # endpoint 1
    resp = trdemo_client_trdemo.get('/')

    # endpoint 6
    resp = trdemo_client_trdemo.get(f'/cart/remove/{product_id}')

  @json_dataset('data/test_7_get_cart_remove_product_id.json')
  @clear_session({'spanId': 7})
  def test_7_get_cart_remove_product_id(self, data_row):
    source, startDate, = data_row

    # endpoint 4
    trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
    resp = trdemo_client_trdemo.get('/cart')
    value = cssselect('datalist#apt_list option[value] @value', resp)

    # endpoint 10
    qstr = '?' + urlencode([('destination', value), ('endDate', ''), ('source', source), ('startDate', startDate)])
    resp = trdemo_client_trdemo.get('/search' + qstr)
    product_id = url_part('?product_id', cssselect('div.container-fluid div table.table.table-striped tbody tr td a[href] @href', resp))

    # endpoint 7
    resp = trdemo_client_trdemo.get(f'/cart/remove/{product_id}')

  # authentication-related test
  @clear_session({'spanId': 8})
  def test_8_get_login(self):
    # endpoint 8
    trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', dummy_auth)
    resp = trdemo_client_trdemo.get('/login')

  @clear_session({'spanId': 9})
  def test_9_get_logout(self):
    # endpoint 9
    trdemo_client_trdemo = get_http_target('TARGET_TRDEMO_CLIENT_TRDEMO', authenticate)
    resp = trdemo_client_trdemo.get('/logout')

@data_driven_tests
class Tests_trdemo_flights_trdemo(unittest.TestCase):
  @json_dataset('data/test_13_get_flight_param1_param2.json')
  @clear_session({'spanId': 13})
  def test_13_get_flight_param1_param2(self, data_row):
    param, param2, = data_row

    # endpoint 13
    trdemo_flights_trdemo = get_http_target('TARGET_TRDEMO_FLIGHTS_TRDEMO', authenticate)
    resp = trdemo_flights_trdemo.get(f'/flight/{param}/{param2}')

@data_driven_tests
class Tests_trdemo_shoppingcart_trdemo(unittest.TestCase):
  @clear_session({'spanId': 15})
  def test_15_delete_cart_email_product_id(self):
    # endpoint 12
    trdemo_users_trdemo = get_http_target('TARGET_TRDEMO_USERS_TRDEMO', authenticate)
    resp = trdemo_users_trdemo.get('/user/all')
    _email = jsonpath('$.[*].email', resp)

    # endpoint 14
    trdemo_shoppingcart_trdemo = get_http_target('TARGET_TRDEMO_SHOPPINGCART_TRDEMO', authenticate)
    resp = trdemo_shoppingcart_trdemo.get(f'/cart/{_email}')
    product_id = jsonpath('$.products.[*].product_id', resp)

    # endpoint 15
    resp = trdemo_shoppingcart_trdemo.delete(f'/cart/{_email}/{product_id}')

@data_driven_tests
class Tests_trdemo_users_trdemo(unittest.TestCase):
  @clear_session({'spanId': 11})
  def test_11_get_user_email(self):
    # endpoint 12
    trdemo_users_trdemo = get_http_target('TARGET_TRDEMO_USERS_TRDEMO', authenticate)
    resp = trdemo_users_trdemo.get('/user/all')
    _email = jsonpath('$.[*].email', resp)

    # endpoint 11
    resp = trdemo_users_trdemo.get(f'/user/{_email}')

