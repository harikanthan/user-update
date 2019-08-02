# user-update
Run user_update.py with below options to update the User Profile details in admin console. Email Id or User id of the user is used to update Email, Username, first name , last name and country

### Options

| Command  | Description  | Required | Default |
| ------------- | ------------- | ------------- | ------------- |
| -h, --help  | help (as generated by click)  |  n/a  |  n/a  |
| -c, --config-filename  | relative path to config file  | yes |  none  |
| -u, --users-filename   | relative path to user csv  | yes |  none  |
| -t, --test-mode    | test mode  | no |  false  |

### Files Required

1) xxxx-config.yml

```properties
umapi:
  org_id: '{Organization ID from Adobe I/O Console}'
  tech_acct_id: '{Technical account ID from Adobe I/O Console}'
  api_key: '{API Key (Client ID) from Adobe I/O Console}'
  client_secret: '{Client secret from Adobe I/O Console}'
  private_key_file: 'private.key file'
configuration:
  id_type: {id Type}
  logon_type: {logon type email/user id}
  username_file: {users list in csv file format with Username,Email,New Email,New Username}
```

2) user-export.csv
A csv file containg Username,Email,New Email,New Username, First Name,Last Name,Country Code

3) private.key