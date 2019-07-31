import yaml
import config.umapi_config as umapi_config
import config.user_config as user_config


class ConfigLoader:

    def load_config(self, **kwargs):
        with open(kwargs["config_filename"], "r") as f:
            config = yaml.load(f)
        umapi = self.get_umapi_config(config)
        user_configuration = self.get_user_config(config, kwargs["users_filename"])
        return umapi, user_configuration

    def get_user_config(self, config, users_filename):
        user_configuration = user_config.UserConfig.get_configuration()
        user_props = config["configuration"]
        user_configuration.id_type = user_props["id_type"]
        if  user_configuration.id_type is None:
            user_configuration.id_type = "Federated ID"
        user_configuration.logon_type = user_props["logon_type"]
        user_configuration.username_file = user_props["username_file"]
        if users_filename is not None:
            user_configuration.users_filename = users_filename
        return user_configuration

    def get_umapi_config(self, config):
        umapi = umapi_config.UmapiConfig.get_umapi_config()
        umapi_props = config["umapi"]
        umapi.org_id = umapi_props["org_id"]
        umapi.tech_acct_id = umapi_props["tech_acct_id"]
        umapi.api_key = umapi_props["api_key"]
        umapi.client_secret = umapi_props["client_secret"]
        umapi.private_key_file = umapi_props["private_key_file"]
        if 'host' in umapi_props:
            umapi.host = umapi_props["host"]
        else:
            umapi.host = "ims-na1.adobelogin.com"
        if 'ims_host' in umapi_props:
            umapi.ims_host = umapi_props["ims_host"]
        else:
            umapi.ims_host = "https://usermanagement.adobe.io/v2/usermanagement"
        return umapi
