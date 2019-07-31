class UmapiConfig:

    def __init__(self, org_id, tech_acct_id, api_key, client_secret, private_key_file, host, ims_host):
        self._org_id = org_id
        self._tech_acct_id = tech_acct_id
        self._api_key = api_key
        self._client_secret = client_secret
        self._private_key_file = private_key_file
        self._host = host
        self._ims_host = ims_host

    @classmethod
    def get_umapi_config(cls, org_id=None, tech_acct_id=None, api_key=None, client_secret=None, private_key_file=None,
                         host=None, ims_host=None):
        return UmapiConfig(org_id, tech_acct_id, api_key, client_secret, private_key_file, host, ims_host)

    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        self._org_id = org_id

    @property
    def tech_acct_id(self):
        return self._tech_acct_id

    @tech_acct_id.setter
    def tech_acct_id(self, tech_acct_id):
        self._tech_acct_id = tech_acct_id

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key

    @property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        self._client_secret = client_secret

    @property
    def private_key_file(self):
        return self._private_key_file

    @private_key_file.setter
    def private_key_file(self, private_key_file):
        self._private_key_file = private_key_file

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def ims_host(self):
        return self._ims_host

    @ims_host.setter
    def ims_host(self, ims_host):
        self._ims_host = ims_host
