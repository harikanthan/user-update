import click
import logging
from click_default_group import DefaultGroup
import yaml
import atexit
import umapi_client
import log_handler, umapi_connection
from umapi_client import IdentityTypes, UserAction
from util import CSVAdapter
import config.config_loader as config_loader

logHandler=None

@click.group(cls=DefaultGroup, default='update', default_if_no_args=True)
@click.version_option('1.2', '-v', '--version', message='%(prog)s %(version)s')
def main():
    pass

@main.command()
@click.help_option('-h', '--help')
@click.option('-c', '--config_filename',
              help="path to your main config file",
              type=str,
              nargs=1,
              metavar='path-to-file')
@click.option('-u', '--users_filename',
              help="filename of user file",
              type=str,
              nargs=1,
              metavar='path-to-file')
@click.option('-t', '--test-mode', default=False, is_flag=True,
              help='enable test mode (API calls do not execute changes on the Adobe side).')
def update(**kwargs):

    umapi, config = config_loader.ConfigLoader().load_config(**kwargs)

    logger = log_handler.getLogger()

    conn = umapi_connection.UmapiConnection().get_connection(logger, umapi, config)

    cols = ['Username', 'Email', 'New Email', 'New Username']

    actions = {}
    for user_rec in CSVAdapter.read_csv_rows(config.users_filename, recognized_column_names=cols):
        username, email, new_email, new_username, domain = \
            user_rec.get('Username'), user_rec.get('Email'), user_rec.get('New Email'),user_rec.get('New Username'), user_rec.get('Domain')
        if not username or not email:
            logger.warning("Skipping input record with missing Username and/or Email: %s" % user_rec)
            continue
        try:
            user = UserAction(id_type=IdentityTypes.federatedID, email=username)
            user.update(email=new_email, username=new_username)
            actions[email] = user
            # if kwargs["from_email"]
            #     user.update(username=username)
            #     actions[email] = user
            # else:
            #     user.update(username=email)
            #     actions[username] = user
            conn.execute_single(user)
        except Exception as e:
            logger.error("Error with: " + username + " ||| " + 'New Email: ' + new_email)

    conn.execute_queued()

    successes, failures = 0, 0
    for key, action in actions.items():
        if not action.execution_errors():
            successes += 1
        else:
            failures += 1
            logger.error("Conversion of %s failed: %s" % (key, action.execution_errors()))
    logger.info("Conversions attempted/succeeded/failed: %d/%d/%d" % (len(actions), successes, failures))

if __name__ == '__main__':
    main()