class UserConfig:

    def __init__(self, id_type, logon_type, users_filename):
        self._id_type = id_type
        self._logon_type = logon_type
        self._users_filename = users_filename

    @classmethod
    def get_configuration(cls, id_type=None, logon_type=None, username_file=None):
        return UserConfig(id_type, logon_type, username_file)

    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        self._id_type = id_type

    @property
    def logon_type(self):
        return self._logon_type

    @logon_type.setter
    def logon_type(self, logon_type):
        self._logon_type = logon_type

    @property
    def users_filename(self):
        return self._users_filename

    @users_filename.setter
    def users_filename(self, users_filename):
        self._users_filename = users_filename