from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_api_permutive_com(unittest.TestCase):
  @json_dataset('data/test_30_post_param_batch_events.json')
  @clear_session({'spanId': 30})
  def test_30_post_param_batch_events(self, data_row):
    param, k, k2, param2, = data_row

    # endpoint 21
    www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
    resp = www_ynet_co_il.get('/home/%s' % (param,))
    resp.assert_status_code(200)

    # endpoint 29
    qstr = '?' + urlencode([('k', k)])
    api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
    resp = api_permutive_com.post('/graphql' + qstr, data=None)
    resp.assert_status_code(200)

    # endpoint 30
    qstr = '?' + urlencode([('enrich', 'false'), ('k', k2)])
    resp = api_permutive_com.post('/%s/batch/events' % (param2,) + qstr, data=None)
    resp.assert_status_code(200)

  @json_dataset('data/test_31_post_param_events.json')
  @clear_session({'spanId': 31})
  def test_31_post_param_events(self, data_row):
    k, param, = data_row

    # endpoint 31
    qstr = '?' + urlencode([('enrich', 'false'), ('k', k)])
    api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
    resp = api_permutive_com.post('/%s/events' % (param,) + qstr, data=None)
    resp.assert_status_code(201)

  @json_dataset('data/test_32_get_param_geoip.json')
  @clear_session({'spanId': 32})
  def test_32_get_param_geoip(self, data_row):
    k, param, = data_row

    # endpoint 32
    qstr = '?' + urlencode([('k', k)])
    api_permutive_com = get_http_target('TARGET_API_PERMUTIVE_COM', authenticate)
    resp = api_permutive_com.get('/%s/geoip' % (param,) + qstr)
    resp.assert_status_code(200)

@data_driven_tests
class Tests_backend_upapi_net(unittest.TestCase):
  @json_dataset('data/test_46_get_pv.json')
  @clear_session({'spanId': 46})
  def test_46_get_pv(self, data_row):
    cv, pid, sid, w, = data_row

    # endpoint 46
    qstr = '?' + urlencode([('br', 'chrome'), ('cv', cv), ('pid', pid), ('r', 'false'), ('sid', sid), ('upapi', 'true'), ('w', w)])
    backend_upapi_net = get_http_target('TARGET_BACKEND_UPAPI_NET', authenticate)
    resp = backend_upapi_net.get('/pv' + qstr)
    resp.assert_status_code(200)

@data_driven_tests
class Tests_cdn_firstimpression_io(unittest.TestCase):
  @json_dataset('data/test_49_get_delivery_lg_php.json')
  @clear_session({'spanId': 49})
  def test_49_get_delivery_lg_php(self, data_row):
    param, bannerid, campaignid, cb, ficb, zoneid, = data_row

    # endpoint 21
    www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
    resp = www_ynet_co_il.get('/home/%s' % (param,))
    resp.assert_status_code(200)
    referer = cssselect(resp, 'html head link[href] @href')
    loc = cssselect(resp, 'div#hdr_main_links ul.hdr_bananas.ghcite li.hdr_isr.hdr_abr a[href] @href')

    # endpoint 49
    qstr = '?' + urlencode([('bannerid', bannerid), ('campaignid', campaignid), ('cb', cb), ('ficb', ficb), ('loc', loc), ('referer', referer), ('zoneid', zoneid)])
    cdn_firstimpression_io = get_http_target('TARGET_CDN_FIRSTIMPRESSION_IO', authenticate)
    resp = cdn_firstimpression_io.get('/delivery/lg.php' + qstr)
    resp.assert_status_code(200)

@data_driven_tests
class Tests_subscription_omnithrottle_com(unittest.TestCase):
  @json_dataset('data/test_58_get_index_php.json')
  @clear_session({'spanId': 58})
  def test_58_get_index_php(self, data_row):
    p_CID, p_uid, rm, = data_row

    # endpoint 58
    qstr = '?' + urlencode([('p_CID', p_CID), ('p_uid', p_uid), ('rm', rm)])
    subscription_omnithrottle_com = get_http_target('TARGET_SUBSCRIPTION_OMNITHROTTLE_COM', authenticate)
    resp = subscription_omnithrottle_com.get('/index.php' + qstr)
    resp.assert_status_code(200)

@data_driven_tests
class Tests_trdemo_stg_testr_io(unittest.TestCase):
  @clear_session({'spanId': 1})
  def test_1_get_(self):
    # endpoint 1
    trdemo_stg_testr_io = get_http_target('TARGET_TRDEMO_STG_TESTR_IO', authenticate)
    resp = trdemo_stg_testr_io.get('/')
    resp.assert_status_code(200)

  @clear_session({'spanId': 2})
  def test_2_get_login(self):
    # endpoint 2
    trdemo_stg_testr_io = get_http_target('TARGET_TRDEMO_STG_TESTR_IO', dummy_auth)
    resp = trdemo_stg_testr_io.get('/login')
    resp.assert_status_code(200)

  @json_dataset('data/test_3_post_login.json')
  @clear_session({'spanId': 3})
  def test_3_post_login(self, data_row):
    user, = data_row

    # endpoint 3
    trdemo_stg_testr_io = get_http_target('TARGET_TRDEMO_STG_TESTR_IO', dummy_auth)
    resp = trdemo_stg_testr_io.post('/login', data=[('user', user)])
    resp.assert_status_code(302)

@data_driven_tests
class Tests_www_google_co_il(unittest.TestCase):
  @clear_session({'spanId': 15})
  def test_15_get_domainless_read(self):
    # endpoint 15
    qstr = '?' + urlencode([('igu', '1')])
    www_google_co_il = get_http_target('TARGET_WWW_GOOGLE_CO_IL', authenticate)
    resp = www_google_co_il.get('/domainless/read' + qstr)
    resp.assert_status_code(200)

@data_driven_tests
class Tests_www_skyscanner_co_il(unittest.TestCase):
  @clear_session({'spanId': 75})
  def test_75_get_dataservices_culture_cldr_href_en_us_il_usd(self):
    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    url = url_part(cssselect(resp, 'html head link[href] @href'), '/4')

    # endpoint 75
    resp = www_skyscanner_co_il.get('/dataservices/culture/cldr/%s/en-us/il/usd' % (url,))
    resp.assert_status_code(200)

  @clear_session({'spanId': 76})
  def test_76_get_g_culture_data_service_dataservices_culture_cldr_href_en_us_il_gbp(self):
    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    url = url_part(cssselect(resp, 'html head link[href] @href'), '/4')

    # endpoint 76
    resp = www_skyscanner_co_il.get('/g/culture-data-service/dataservices/culture/cldr/%s/en-us/il/gbp' % (url,))
    resp.assert_status_code(200)

  @json_dataset('data/test_78_post_g_delivery_service_api_v3_request.json')
  @clear_session({'spanId': 78})
  def test_78_post_g_delivery_service_api_v3_request(self, data_row):
    traveller_context, adslot_bdbd9c3f, cabin_class, daylight_savings_offset_mins, daylight_savings_offset_mins2, display_height, display_width, duration, ga_cid, itinerary_type, _platform, pqs_house_ad, request_id, timezone_offset_mins, timezone_offset_mins2, unix_time_millis, unix_time_millis2, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    _locale = url_part(cssselect(resp, 'div#footer-flags-root div ul li a[href] @href'), '?locale')
    currency = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.culture.currency')
    location_id = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.flightSearch.origin.airportId')
    location_name = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.flightSearch.origin.name')
    location_name1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.flightSearch.origin.cityName')
    browser_name = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.device.browserName')

    # endpoint 74
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net'), ('traveller_context', traveller_context)])
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(302)
    utid = get_data_from_cookie('traveller_context')

    # endpoint 78
    with open('data/payload_for_www_skyscanner_co_il_endp78.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.id_placements.adslot-bdbd9c3f', adslot_bdbd9c3f)
    apply_into_json(json_payload, '$.id_placements.pqs-house-ad', pqs_house_ad)
    apply_into_json(json_payload, '$.targeting.cabin_class', cabin_class)
    apply_into_json(json_payload, '$.targeting.culture_settings.currency', currency)
    apply_into_json(json_payload, '$.targeting.culture_settings.locale', _locale)
    apply_into_json(json_payload, '$.targeting.duration', duration)
    apply_into_json(json_payload, '$.targeting.itinerary_type', itinerary_type)
    apply_into_json(json_payload, '$.targeting.origin.airport.location_attribute.location_id', location_id)
    apply_into_json(json_payload, '$.targeting.origin.airport.location_attribute.location_name', location_name)
    apply_into_json(json_payload, '$.targeting.origin.city.location_attribute.location_name', location_name1)
    apply_into_json(json_payload, '$.targeting.search_end_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins)
    apply_into_json(json_payload, '$.targeting.search_end_timestamp.timezone_offset_mins', timezone_offset_mins)
    apply_into_json(json_payload, '$.targeting.search_end_timestamp.unix_time_millis', unix_time_millis)
    apply_into_json(json_payload, '$.targeting.search_start_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins2)
    apply_into_json(json_payload, '$.targeting.search_start_timestamp.timezone_offset_mins', timezone_offset_mins2)
    apply_into_json(json_payload, '$.targeting.search_start_timestamp.unix_time_millis', unix_time_millis2)
    apply_into_json(json_payload, '$.user_features.client.browser_name', browser_name)
    apply_into_json(json_payload, '$.user_features.client.display_height', display_height)
    apply_into_json(json_payload, '$.user_features.client.display_width', display_width)
    apply_into_json(json_payload, '$.user_features.ga_cid', ga_cid)
    apply_into_json(json_payload, '$.user_features.platform', _platform)
    apply_into_json(json_payload, '$.user_features.request_id', request_id)
    apply_into_json(json_payload, '$.user_features.utid', utid)
    resp = www_skyscanner_co_il.post('/g/delivery-service/api/v3/request', json=json_payload)
    resp.assert_status_code(200)

  @json_dataset('data/test_79_get_g_shelfservice_dataservices_browse_v3_inspirationshelfweb_IL_param1_locale_routes_airportId_param2_param3_param4_.json')
  @clear_session({'spanId': 79})
  def test_79_get_g_shelfservice_dataservices_browse_v3_inspirationshelfweb_IL_param1_locale_routes_airportId_param2_param3_param4_(self, data_row):
    apikey, minDestinations, param, param2, param3, param4, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    url = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.flightSearch.origin.airportId')
    url1 = url_part(cssselect(resp, 'div#footer-flags-root div ul li a[href] @href'), '?locale')

    # endpoint 79
    qstr = '?' + urlencode([('apikey', apikey), ('include', 'image;countryInfo;directness'), ('minDestinations', minDestinations), ('profile', 'minimalcityrollupwithnamesv2')])
    resp = www_skyscanner_co_il.get('/g/shelfservice/dataservices/browse/v3/inspirationshelfweb/IL/%s/%s/routes/%s/%s/%s/%s/' % (param, url1, url, param2, param3, param4,) + qstr)
    resp.assert_status_code(200)

  @json_dataset('data/test_81_post_slipstream_grp_v1_custom_env_analyticsPageName_FlightsHomePageLoaded_blackbird_FlightsHomePageLoaded.json')
  @clear_session({'spanId': 81})
  def test_81_post_slipstream_grp_v1_custom_env_analyticsPageName_FlightsHomePageLoaded_blackbird_FlightsHomePageLoaded(self, data_row):
    traveller_context, param, param2, accept_language, daylight_savings_offset_mins, device_guid, guid, timezone_offset_mins, user_agent, user_preferences_guid, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    accept_language_first_lang = url_part(cssselect(resp, 'div#footer-flags-root div ul li a[href] @href'), '?locale')
    url = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.microsite.name')

    # endpoint 74
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net'), ('traveller_context', traveller_context)])
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(302)
    experiment_allocation_id = get_data_from_cookie('experiment_allocation_id')
    utid = get_data_from_cookie('traveller_context')

    # endpoint 92
    qstr = '?' + urlencode([('adults', '1'), ('adultsv2', '1'), ('cabinclass', 'economy'), ('children', '0'), ('childrenv2', ''), ('inboundaltsenabled', 'false'), ('infants', '0'), ('outboundaltsenabled', 'false'), ('preferdirects', 'false'), ('ref', 'home'), ('rtn', '1')])
    resp = www_skyscanner_co_il.get('/transport/flights-from/tlv/%s/%s/' % (param, param2,) + qstr)
    resp.assert_status_code(200)
    url1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.config.env')

    # endpoint 81
    with open('data/payload_for_www_skyscanner_co_il_endp81.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.accept_language', accept_language)
    apply_into_json(json_payload, '$.accept_language_first_lang', accept_language_first_lang)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    apply_into_json(json_payload, '$.header.user_agent', user_agent)
    apply_into_json(json_payload, '$.header.user_preferences_guid', user_preferences_guid)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/FlightsHomePageLoaded/blackbird.FlightsHomePageLoaded' % (url1, url,), json=json_payload)
    resp.assert_status_code(200)

  @json_dataset('data/test_82_post_slipstream_grp_v1_custom_env_analyticsPageName_InspirationShelfLoaded_param.json')
  @clear_session({'spanId': 82})
  def test_82_post_slipstream_grp_v1_custom_env_analyticsPageName_InspirationShelfLoaded_param(self, data_row):
    traveller_context, param, param2, daylight_savings_offset_mins, device_guid, guid, location_attribute_encoding, location_id, panel_types, param3, timezone_offset_mins, user_agent, user_preferences_guid, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    url = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.microsite.name')
    sequence_number = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.mobile-link div.alternative-link[data-index] @data-index')
    shelf_number = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.timeline-head div.header-wrapper div.alternative-link[data-index] @data-index')
    browse_funnel_version = url_part(cssselect(resp, 'div#pagewrap div.inspiration-shelves-wrapper div.inspiration-wrap link[href] @href'), '/4')

    # endpoint 74
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net'), ('traveller_context', traveller_context)])
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(302)
    experiment_allocation_id = get_data_from_cookie('experiment_allocation_id')
    utid = get_data_from_cookie('traveller_context')

    # endpoint 92
    qstr = '?' + urlencode([('adults', '1'), ('adultsv2', '1'), ('cabinclass', 'economy'), ('children', '0'), ('childrenv2', ''), ('inboundaltsenabled', 'false'), ('infants', '0'), ('outboundaltsenabled', 'false'), ('preferdirects', 'false'), ('ref', 'home'), ('rtn', '1')])
    resp = www_skyscanner_co_il.get('/transport/flights-from/tlv/%s/%s/' % (param, param2,) + qstr)
    resp.assert_status_code(200)
    url1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.config.env')

    # endpoint 82
    with open('data/payload_for_www_skyscanner_co_il_endp82.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.common_properties.browse_funnel_version', browse_funnel_version)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    apply_into_json(json_payload, '$.header.user_agent', user_agent)
    apply_into_json(json_payload, '$.header.user_preferences_guid', user_preferences_guid)
    apply_into_json(json_payload, '$.origin.location_attribute.location_attribute_encoding', location_attribute_encoding)
    apply_into_json(json_payload, '$.origin.location_attribute.location_id', location_id)
    apply_into_json(json_payload, '$.panel_types.[*]', panel_types)
    apply_into_json(json_payload, '$.shelf_number', shelf_number)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/InspirationShelfLoaded/%s' % (url1, url, param3,), json=json_payload)
    resp.assert_status_code(200)

  @json_dataset('data/test_83_post_slipstream_grp_v1_custom_env_analyticsPageName_TldRedirect_blackbird_TldRedirect.json')
  @clear_session({'spanId': 83})
  def test_83_post_slipstream_grp_v1_custom_env_analyticsPageName_TldRedirect_blackbird_TldRedirect(self, data_row):
    traveller_context, param, param2, daylight_savings_offset_mins, device_guid, guid, timezone_offset_mins, user_agent, user_preferences_guid, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    sequence_number = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.timeline-head div.header-wrapper div.alternative-link[data-index] @data-index')
    url = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.microsite.name')

    # endpoint 74
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net'), ('traveller_context', traveller_context)])
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(302)
    experiment_allocation_id = get_data_from_cookie('experiment_allocation_id')
    utid = get_data_from_cookie('traveller_context')

    # endpoint 92
    qstr = '?' + urlencode([('adults', '1'), ('adultsv2', '1'), ('cabinclass', 'economy'), ('children', '0'), ('childrenv2', ''), ('inboundaltsenabled', 'false'), ('infants', '0'), ('outboundaltsenabled', 'false'), ('preferdirects', 'false'), ('ref', 'home'), ('rtn', '1')])
    resp = www_skyscanner_co_il.get('/transport/flights-from/tlv/%s/%s/' % (param, param2,) + qstr)
    resp.assert_status_code(200)
    url1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.config.env')

    # endpoint 83
    with open('data/payload_for_www_skyscanner_co_il_endp83.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    apply_into_json(json_payload, '$.header.user_agent', user_agent)
    apply_into_json(json_payload, '$.header.user_preferences_guid', user_preferences_guid)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/TldRedirect/blackbird.TldRedirect' % (url1, url,), json=json_payload)
    resp.assert_status_code(200)

  @json_dataset('data/test_84_post_slipstream_grp_v1_custom_env_analyticsPageName_funnel_events_clients_Acquisition.json')
  @clear_session({'spanId': 84})
  def test_84_post_slipstream_grp_v1_custom_env_analyticsPageName_funnel_events_clients_Acquisition(self, data_row):
    traveller_context, param, param2, acquisition_type, daylight_savings_offset_mins, device_guid, guid, referral_url, timezone_offset_mins, user_agent_string, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    sequence_number = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.timeline-head div.header-wrapper div.alternative-link[data-index] @data-index')
    url = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.microsite.name')

    # endpoint 74
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net'), ('traveller_context', traveller_context)])
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(302)
    experiment_allocation_id = get_data_from_cookie('experiment_allocation_id')
    utid = get_data_from_cookie('traveller_context')

    # endpoint 92
    qstr = '?' + urlencode([('adults', '1'), ('adultsv2', '1'), ('cabinclass', 'economy'), ('children', '0'), ('childrenv2', ''), ('inboundaltsenabled', 'false'), ('infants', '0'), ('outboundaltsenabled', 'false'), ('preferdirects', 'false'), ('ref', 'home'), ('rtn', '1')])
    resp = www_skyscanner_co_il.get('/transport/flights-from/tlv/%s/%s/' % (param, param2,) + qstr)
    resp.assert_status_code(200)
    url1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.config.env')

    # endpoint 84
    with open('data/payload_for_www_skyscanner_co_il_endp84.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.acquisition_type', acquisition_type)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    apply_into_json(json_payload, '$.referral_url', referral_url)
    apply_into_json(json_payload, '$.user_agent_string', user_agent_string)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/funnel_events/clients.Acquisition' % (url1, url,), json=json_payload)
    resp.assert_status_code(200)

  @json_dataset('data/test_86_post_slipstream_grp_v1_custom_env_analyticsPageName_funnel_events_clients_UserPreferences.json')
  @clear_session({'spanId': 86})
  def test_86_post_slipstream_grp_v1_custom_env_analyticsPageName_funnel_events_clients_UserPreferences(self, data_row):
    traveller_context, param, param2, currency, daylight_savings_offset_mins, device_guid, guid, is_gdpr_initialised, timezone_offset_mins, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    sequence_number = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.mobile-link div.alternative-link[data-index] @data-index')
    url = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.microsite.name')
    gdpr_cookie_version = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.timeline-head div.header-wrapper div.alternative-link[data-index] @data-index')
    _locale = url_part(cssselect(resp, 'div#footer-flags-root div ul li a[href] @href'), '?locale')

    # endpoint 74
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net'), ('traveller_context', traveller_context)])
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(302)
    experiment_allocation_id = get_data_from_cookie('experiment_allocation_id')
    utid = get_data_from_cookie('traveller_context')

    # endpoint 92
    qstr = '?' + urlencode([('adults', '1'), ('adultsv2', '1'), ('cabinclass', 'economy'), ('children', '0'), ('childrenv2', ''), ('inboundaltsenabled', 'false'), ('infants', '0'), ('outboundaltsenabled', 'false'), ('preferdirects', 'false'), ('ref', 'home'), ('rtn', '1')])
    resp = www_skyscanner_co_il.get('/transport/flights-from/tlv/%s/%s/' % (param, param2,) + qstr)
    resp.assert_status_code(200)
    url1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.config.env')

    # endpoint 86
    with open('data/payload_for_www_skyscanner_co_il_endp86.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.currency', currency)
    apply_into_json(json_payload, '$.gdpr_cookie_version', gdpr_cookie_version)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    apply_into_json(json_payload, '$.is_gdpr_initialised', is_gdpr_initialised)
    apply_into_json(json_payload, '$.locale', _locale)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/funnel_events/clients.UserPreferences' % (url1, url,), json=json_payload)
    resp.assert_status_code(200)

  @json_dataset('data/test_88_post_slipstream_grp_v1_custom_env_analyticsPageName_PageLoaded_browse_view_page_PageLoaded.json')
  @clear_session({'spanId': 88})
  def test_88_post_slipstream_grp_v1_custom_env_analyticsPageName_PageLoaded_browse_view_page_PageLoaded(self, data_row):
    traveller_context, param, param2, daylight_savings_offset_mins, device_guid, guid, sequence_number, timezone_offset_mins, user_agent, user_preferences_guid, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    url = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.microsite.name')

    # endpoint 74
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net'), ('traveller_context', traveller_context)])
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(302)
    experiment_allocation_id = get_data_from_cookie('experiment_allocation_id')
    utid = get_data_from_cookie('traveller_context')

    # endpoint 92
    qstr = '?' + urlencode([('adults', '1'), ('adultsv2', '1'), ('cabinclass', 'economy'), ('children', '0'), ('childrenv2', ''), ('inboundaltsenabled', 'false'), ('infants', '0'), ('outboundaltsenabled', 'false'), ('preferdirects', 'false'), ('ref', 'home'), ('rtn', '1')])
    resp = www_skyscanner_co_il.get('/transport/flights-from/tlv/%s/%s/' % (param, param2,) + qstr)
    resp.assert_status_code(200)
    url1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.config.env')

    # endpoint 88
    with open('data/payload_for_www_skyscanner_co_il_endp88.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    apply_into_json(json_payload, '$.header.user_agent', user_agent)
    apply_into_json(json_payload, '$.header.user_preferences_guid', user_preferences_guid)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/PageLoaded/browse_view_page.PageLoaded' % (url1, url,), json=json_payload)
    resp.assert_status_code(200)

  @json_dataset('data/test_89_post_slipstream_grp_v1_custom_env_analyticsPageName_funnel_events_clients_Search.json')
  @clear_session({'spanId': 89})
  def test_89_post_slipstream_grp_v1_custom_env_analyticsPageName_funnel_events_clients_Search(self, data_row):
    traveller_context, param, param2, business_domain, cabin_class, date_time_kind, date_time_kind2, daylight_savings_offset_mins, device_guid, group_model, guid, location_attribute_encoding, location_attribute_encoding2, location_attribute_encoding3, location_attribute_encoding4, location_attribute_encoding5, location_attribute_encoding6, location_id, location_id2, location_id3, sequence_number, timezone_offset_mins, unix_time_millis, unix_time_millis2, unix_time_millis3, unix_time_millis4, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    url = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.microsite.name')
    date_time_kind3 = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.timeline-head div.header-wrapper div.alternative-link[data-index] @data-index')

    # endpoint 74
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net'), ('traveller_context', traveller_context)])
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(302)
    experiment_allocation_id = get_data_from_cookie('experiment_allocation_id')
    utid = get_data_from_cookie('traveller_context')

    # endpoint 92
    qstr = '?' + urlencode([('adults', '1'), ('adultsv2', '1'), ('cabinclass', 'economy'), ('children', '0'), ('childrenv2', ''), ('inboundaltsenabled', 'false'), ('infants', '0'), ('outboundaltsenabled', 'false'), ('preferdirects', 'false'), ('ref', 'home'), ('rtn', '1')])
    resp = www_skyscanner_co_il.get('/transport/flights-from/tlv/%s/%s/' % (param, param2,) + qstr)
    resp.assert_status_code(200)
    url1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.config.env')

    # endpoint 89
    with open('data/payload_for_www_skyscanner_co_il_endp89.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.business_domain', business_domain)
    apply_into_json(json_payload, '$.destination.location_attribute.location_attribute_encoding', location_attribute_encoding)
    apply_into_json(json_payload, '$.end_date.date_time_kind', date_time_kind3)
    apply_into_json(json_payload, '$.end_date.unix_time_millis', unix_time_millis)
    apply_into_json(json_payload, '$.flight_search.cabin_class', cabin_class)
    apply_into_json(json_payload, '$.flight_search.passenger_group.group_model', group_model)
    apply_into_json(json_payload, '$.flight_search.return.leg1.date.date_time_kind', date_time_kind)
    apply_into_json(json_payload, '$.flight_search.return.leg1.date.unix_time_millis', unix_time_millis2)
    apply_into_json(json_payload, '$.flight_search.return.leg1.destination.location_attribute.location_attribute_encoding', location_attribute_encoding2)
    apply_into_json(json_payload, '$.flight_search.return.leg1.origin.location_attribute.location_attribute_encoding', location_attribute_encoding3)
    apply_into_json(json_payload, '$.flight_search.return.leg1.origin.location_attribute.location_id', location_id)
    apply_into_json(json_payload, '$.flight_search.return.leg2.date.date_time_kind', date_time_kind2)
    apply_into_json(json_payload, '$.flight_search.return.leg2.date.unix_time_millis', unix_time_millis3)
    apply_into_json(json_payload, '$.flight_search.return.leg2.destination.location_attribute.location_attribute_encoding', location_attribute_encoding4)
    apply_into_json(json_payload, '$.flight_search.return.leg2.destination.location_attribute.location_id', location_id2)
    apply_into_json(json_payload, '$.flight_search.return.leg2.origin.location_attribute.location_attribute_encoding', location_attribute_encoding5)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    apply_into_json(json_payload, '$.origin.location_attribute.location_attribute_encoding', location_attribute_encoding6)
    apply_into_json(json_payload, '$.origin.location_attribute.location_id', location_id3)
    apply_into_json(json_payload, '$.start_date.date_time_kind', date_time_kind3)
    apply_into_json(json_payload, '$.start_date.unix_time_millis', unix_time_millis4)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/funnel_events/clients.Search' % (url1, url,), json=json_payload)
    resp.assert_status_code(200)

  @json_dataset('data/test_90_post_slipstream_grp_v1_custom_env_js_tag_manager_funnel_events_funnel_eventId.json')
  @clear_session({'spanId': 90})
  def test_90_post_slipstream_grp_v1_custom_env_js_tag_manager_funnel_events_funnel_eventId(self, data_row):
    traveller_context, param, param2, action_type, cabin_class, daylight_savings_offset_mins, destination_iata_code, device_guid, guid, nearby_alts, origin_iata_code, param3, sequence_number, timezone_offset_mins, trip_type, unix_time_millis, user_agent, user_preferences_guid, daylight_savings_offset_mins2, device_guid2, guid2, sequence_number2, timezone_offset_mins2, daylight_savings_offset_mins3, device_guid3, guid3, name, sequence_number3, timezone_offset_mins3, variant, daylight_savings_offset_mins4, device_guid4, funnel_eventId, guid4, page, timezone_offset_mins4, user_agent2, user_preferences_guid2, = data_row

    # endpoint 73
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net')])
    www_skyscanner_co_il = get_http_target('TARGET_WWW_SKYSCANNER_CO_IL', authenticate)
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(200)
    sequence_number4 = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.timeline-head div.header-wrapper div.alternative-link[data-index] @data-index')
    url = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.microsite.name')
    url1 = url_part(cssselect(resp, 'html head link[href] @href'), '/4')
    is_prefer_directs = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.featureTests.*')
    leg_count = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.timeline-head div.header-wrapper div.alternative-link[data-index] @data-index')
    version = cssselect(resp, 'div#timeline-outer div.wrap.clearfix div.inspiration-timeline ul.timeline li.timeline__block div.mobile-link div.alternative-link[data-index] @data-index')

    # endpoint 77
    resp = www_skyscanner_co_il.get('/g/culture-data-service/dataservices/culture/cldr/%s/en-us/il/usd' % (url1,))
    resp.assert_status_code(200)
    children = jsonpath(resp, '$.supplemental.weekData.daysOfWeekUnordered.[*].index')

    # endpoint 74
    qstr = '?' + urlencode([('previousCultureSource', 'COOKIE'), ('redirectedFrom', 'www.skyscanner.net'), ('traveller_context', traveller_context)])
    resp = www_skyscanner_co_il.get('/' + qstr)
    resp.assert_status_code(302)
    name1 = get_data_from_header(resp, 'location')
    referrer_url = get_data_from_header(resp, 'location')
    experiment_allocation_id = get_data_from_cookie('experiment_allocation_id')
    utid = get_data_from_cookie('traveller_context')

    # endpoint 92
    qstr = '?' + urlencode([('adults', '1'), ('adultsv2', '1'), ('cabinclass', 'economy'), ('children', '0'), ('childrenv2', ''), ('inboundaltsenabled', 'false'), ('infants', '0'), ('outboundaltsenabled', 'false'), ('preferdirects', 'false'), ('ref', 'home'), ('rtn', '1')])
    resp = www_skyscanner_co_il.get('/transport/flights-from/tlv/%s/%s/' % (param, param2,) + qstr)
    resp.assert_status_code(200)
    url2 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.config.env')
    experiment_allocation_id1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.experimentAllocationId')
    utid1 = jsonpath(cssselect(resp, 'script#trackolding-sync[data-data] @data-data'), '$.userInfo.utid')

    # endpoint 80
    with open('data/payload_for_www_skyscanner_co_il_endp80.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.action_type', action_type)
    apply_into_json(json_payload, '$.cabin_class', cabin_class)
    apply_into_json(json_payload, '$.children', children)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    apply_into_json(json_payload, '$.header.user_agent', user_agent)
    apply_into_json(json_payload, '$.header.user_preferences_guid', user_preferences_guid)
    apply_into_json(json_payload, '$.is_prefer_directs', is_prefer_directs)
    apply_into_json(json_payload, '$.leg_count', leg_count)
    apply_into_json(json_payload, '$.nearby_alts', nearby_alts)
    apply_into_json(json_payload, '$.trip_legs.[*].departure_timestamp.unix_time_millis', unix_time_millis)
    apply_into_json(json_payload, '$.trip_legs.[*].destination_iata_code', destination_iata_code)
    apply_into_json(json_payload, '$.trip_legs.[*].origin_iata_code', origin_iata_code)
    apply_into_json(json_payload, '$.trip_type', trip_type)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/Action/%s' % (url2, url, param3,), json=json_payload)
    resp.assert_status_code(200)

    # endpoint 87
    with open('data/payload_for_www_skyscanner_co_il_endp87.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins2)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins2)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid2)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid2)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number2)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    apply_into_json(json_payload, '$.name', name1)
    apply_into_json(json_payload, '$.referrer_url', referrer_url)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/funnel_events/clients.View' % (url2, url,), json=json_payload)
    resp.assert_status_code(200)

    # endpoint 85
    with open('data/payload_for_www_skyscanner_co_il_endp85.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.experiments.[*].name', name)
    apply_into_json(json_payload, '$.experiments.[*].variant', variant)
    apply_into_json(json_payload, '$.experiments.[*].version', version)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins3)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins3)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid3)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id)
    apply_into_json(json_payload, '$.header.guid', guid3)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number3)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/%s/funnel_events/clients.ExperimentAllocation' % (url2, url,), json=json_payload)
    resp.assert_status_code(200)

    # endpoint 91
    resp = www_skyscanner_co_il.post('/slipstream/view', data=None)
    resp.assert_status_code(200)

    # endpoint 90
    with open('data/payload_for_www_skyscanner_co_il_endp90.json', 'r') as json_payload_file:
        json_payload = json.load(json_payload_file)
    apply_into_json(json_payload, '$.header.client_timestamp.daylight_savings_offset_mins', daylight_savings_offset_mins4)
    apply_into_json(json_payload, '$.header.client_timestamp.timezone_offset_mins', timezone_offset_mins4)
    apply_into_json(json_payload, '$.header.client_timestamp.unix_time_millis', int(time.time()))
    apply_into_json(json_payload, '$.header.device_guid', device_guid4)
    apply_into_json(json_payload, '$.header.experiment_allocation_id', experiment_allocation_id1)
    apply_into_json(json_payload, '$.header.guid', guid4)
    apply_into_json(json_payload, '$.header.sequence_number', sequence_number4)
    apply_into_json(json_payload, '$.header.traveller_identity.utid', utid1)
    apply_into_json(json_payload, '$.header.user_agent', user_agent2)
    apply_into_json(json_payload, '$.header.user_preferences_guid', user_preferences_guid2)
    apply_into_json(json_payload, '$.page', page)
    resp = www_skyscanner_co_il.post('/slipstream/grp/v1/custom/%s/js-tag-manager/funnel_events/%s' % (url2, funnel_eventId,), json=json_payload)
    resp.assert_status_code(200)

@data_driven_tests
class Tests_www_skyscanner_net(unittest.TestCase):
  @json_dataset('data/test_96_get_g_param_api_v1_alternatives.json')
  @clear_session({'spanId': 96})
  def test_96_get_g_param_api_v1_alternatives(self, data_row):
    cd, param, = data_row

    # endpoint 96
    qstr = '?' + urlencode([('destination_code', 'NYCA'), ('origin_code', 'TELA'), ('size', cd)])
    www_skyscanner_net = get_http_target('TARGET_WWW_SKYSCANNER_NET', authenticate)
    resp = www_skyscanner_net.get('/g/%s/api/v1/alternatives' % (param,) + qstr)
    resp.assert_status_code(200)

@data_driven_tests
class Tests_www_walla_co_il(unittest.TestCase):
  @clear_session({'spanId': 61})
  def test_61_get_(self):
    # endpoint 61
    www_walla_co_il = get_http_target('TARGET_WWW_WALLA_CO_IL', authenticate)
    resp = www_walla_co_il.get('/')
    resp.assert_status_code(200)

@data_driven_tests
class Tests_www_ynet_co_il(unittest.TestCase):
  @json_dataset('data/test_16_get_Cmn_App_Video_CmmAppVideoApi_Js_cmmappvideoapi_jId.json')
  @clear_session({'spanId': 16})
  def test_16_get_Cmn_App_Video_CmmAppVideoApi_Js_cmmappvideoapi_jId(self, data_row):
    cmmappvideoapi_jId, = data_row

    # endpoint 16
    www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
    resp = www_ynet_co_il.get('/Cmn/App/Video/CmmAppVideoApi_Js/%s' % (cmmappvideoapi_jId,))
    resp.assert_status_code(200)

  @json_dataset('data/test_17_get_Cmn_App_Video_CmmAppVideoApi_Js_Content_param.json')
  @clear_session({'spanId': 17})
  def test_17_get_Cmn_App_Video_CmmAppVideoApi_Js_Content_param(self, data_row):
    param, = data_row

    # endpoint 17
    www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
    resp = www_ynet_co_il.get('/Cmn/App/Video/CmmAppVideoApi_Js_Content/%s' % (param,))
    resp.assert_status_code(200)

  @json_dataset('data/test_18_get_param1_Comp_Ticker_Dhtml_Flash_Ticker_param2.json')
  @clear_session({'spanId': 18})
  def test_18_get_param1_Comp_Ticker_Dhtml_Flash_Ticker_param2(self, data_row):
    param, param2, = data_row

    # endpoint 18
    qstr = '?' + urlencode([('js', '1')])
    www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
    resp = www_ynet_co_il.get('/%s/Comp/Ticker/Dhtml_Flash_Ticker/%s' % (param, param2,) + qstr)
    resp.assert_status_code(200)

  @json_dataset('data/test_19_get_param1_Comp_Ticker_JS_Ticker_Data_param2.json')
  @clear_session({'spanId': 19})
  def test_19_get_param1_Comp_Ticker_JS_Ticker_Data_param2(self, data_row):
    param, param2, = data_row

    # endpoint 19
    www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
    resp = www_ynet_co_il.get('/%s/Comp/Ticker/JS_Ticker_Data/%s' % (param, param2,))
    resp.assert_status_code(200)

  @json_dataset('data/test_20_get_YediothPortal_param1_Comp_Teaser_MarketSchedual_New_CdaMarketSchedualIframe_New_param2.json')
  @clear_session({'spanId': 20})
  def test_20_get_YediothPortal_param1_Comp_Teaser_MarketSchedual_New_CdaMarketSchedualIframe_New_param2(self, data_row):
    param, param2, = data_row

    # endpoint 20
    www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
    resp = www_ynet_co_il.get('/YediothPortal/%s/Comp/Teaser/MarketSchedual_New/CdaMarketSchedualIframe_New/%s' % (param, param2,))
    resp.assert_status_code(200)

  @json_dataset('data/test_22_get_ticker_flash_breakingnews_html.json')
  @clear_session({'spanId': 22})
  def test_22_get_ticker_flash_breakingnews_html(self, data_row):
    content_id, = data_row

    # endpoint 22
    qstr = '?' + urlencode([('content_id', content_id)])
    www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
    resp = www_ynet_co_il.get('/ticker/flash/breakingnews.html' + qstr)
    resp.assert_status_code(200)

@data_driven_tests
class Tests_z_ynet_co_il(unittest.TestCase):
  @clear_session({'spanId': 24})
  def test_24_get_fast_ResFrame_default_aspx(self):
    # endpoint 24
    qstr = '?' + urlencode([('d', 'today')])
    z_ynet_co_il = get_http_target('TARGET_Z_YNET_CO_IL', authenticate)
    resp = z_ynet_co_il.get('/fast/ResFrame/default.aspx' + qstr)
    resp.assert_status_code(200)

  @json_dataset('data/test_25_get_fast_content_param_coronavirus_coronaviruId.json')
  @clear_session({'spanId': 25})
  def test_25_get_fast_content_param_coronavirus_coronaviruId(self, data_row):
    coronaviruId, param, = data_row

    # endpoint 25
    z_ynet_co_il = get_http_target('TARGET_Z_YNET_CO_IL', authenticate)
    resp = z_ynet_co_il.get('/fast/content/%s/coronavirus/%s' % (param, coronaviruId,))
    resp.assert_status_code(200)

  @clear_session({'spanId': 26})
  def test_26_get_long_content_links_sportSideIframe_(self):
    # endpoint 26
    z_ynet_co_il = get_http_target('TARGET_Z_YNET_CO_IL', authenticate)
    resp = z_ynet_co_il.get('/long/content/links/sportSideIframe/')
    resp.assert_status_code(200)

  @json_dataset('data/test_27_get_mShort_commerce_href_YnetShopsIframe.json')
  @clear_session({'spanId': 27})
  def test_27_get_mShort_commerce_href_YnetShopsIframe(self, data_row):
    param, = data_row

    # endpoint 21
    www_ynet_co_il = get_http_target('TARGET_WWW_YNET_CO_IL', authenticate)
    resp = www_ynet_co_il.get('/home/%s' % (param,))
    resp.assert_status_code(200)
    url = url_part(cssselect(resp, 'article#F_Content div.block.B6 div.block.B6 div.area.footer.ghcite div.new_homepage_footer_background div.new_homepage_footer_part_one div.new_homepage_footer_about div.footer_column.clearfix div ul li a[href] @href'), '/3')

    # endpoint 27
    z_ynet_co_il = get_http_target('TARGET_Z_YNET_CO_IL', authenticate)
    resp = z_ynet_co_il.get('/mShort/commerce/%s/YnetShopsIframe' % (url,))
    resp.assert_status_code(200)

  @json_dataset('data/test_28_get_short_commerce_param_SportTable_.json')
  @clear_session({'spanId': 28})
  def test_28_get_short_commerce_param_SportTable_(self, data_row):
    param, = data_row

    # endpoint 28
    z_ynet_co_il = get_http_target('TARGET_Z_YNET_CO_IL', authenticate)
    resp = z_ynet_co_il.get('/short/commerce/%s/SportTable/' % (param,))
    resp.assert_status_code(200)

