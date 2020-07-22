from up9lib import *


def authenticate(target_key, target):
        with open('data/auth_data.json') as fp:
            auth_data = json.load(fp)
        
        if target_key == 'TARGET_AUTHDETECTOR_STG_TESTR_IO':
            token = random.choice(auth_data['TARGET_AUTHDETECTOR_STG_TESTR_IO'])
            target.additional_headers({'Authorization': token})
        
        elif target_key == 'TARGET_TRCC_STG_TESTR_IO':
            token = random.choice(auth_data['TARGET_TRCC_STG_TESTR_IO'])
            target.additional_headers({'Authorization': token})
        
        else:
          pass
        


