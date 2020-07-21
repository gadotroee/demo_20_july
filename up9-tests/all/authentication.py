from up9lib import *


def authenticate(target_key, target):
        with open('data/auth_data.json') as fp:
            auth_data = json.load(fp)
        
        if target_key == 'TARGET_SOCKSHOP_HAIUT_DEV_SPYD_IO':
            token = random.choice(auth_data['TARGET_SOCKSHOP_HAIUT_DEV_SPYD_IO'])
            target.additional_headers({'Authorization': token})
        
        else:
          pass
        


