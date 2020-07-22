from up9lib import *


def authenticate(target_key, target):
        if target_key == 'TARGET_TRDEMO_STG_TESTR_IO':
            # endpoint 2
            resp = target.get('/login')
            resp.assert_status_code(200)
        
        else:
          pass
        


