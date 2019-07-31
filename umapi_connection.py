import umapi_client
import yaml
import config.umapi_config as umapi_config
import config.user_config as user_config

class UmapiConnection:

    def get_connection(self, logger, umapi: umapi_config.UmapiConfig, user_configuration: user_config.UserConfig):

        if umapi.host is not None and umapi.ims_host is not None :
            conn = umapi_client.Connection(org_id=umapi.org_id,
                                           auth_dict=self.get_auth_dict(umapi.__dict__),
                                           test_mode=False,
                                           ims_host=umapi.ims_host,
                                           ims_endpoint_jwt='/ims/exchange/jwt',
                                           user_management_endpoint=umapi.host,
                                           logger=logger)
        else:
            conn = umapi_client.Connection(org_id=umapi.org_id,
                                           auth_dict=umapi,
                                           test_mode=False,
                                           ims_endpoint_jwt='/ims/exchange/jwt',
                                           logger=logger)

        return conn

    def get_auth_dict(self, auth_dict):
        corrected_dict = {k.replace("_", "", 1): v for k, v in auth_dict.items()}
        corrected_dict.__delitem__("ims_host")
        return corrected_dict