
import dropbox
import dropbox.files
import dropbox.exceptions
import logging
import os
import os.path
import sys

logging.basicConfig(level=logging.INFO)

def backup(dbx, file_name, remote_path = None, logger = None):
    """
    Backups a file into the dropbox folder.
    """

    path = remote_path if remote_path else '/';
    backup_file_name = os.path.join(path, file_name)

    with open(file_name, 'rb') as fd:

        if logger:
            logger.debug('Uploading %s to Dropbox as %s', file_name, backup_file_name)

        try:
            dbx.files_upload(fd.read(), backup_file_name, mode = dropbox.files.WriteMode('overwrite'))
        except dropbox.exceptions.ApiError as err:
            if err.error.is_path() and err.error.get_path().error.is_insufficient_space():
                if logger:
                    logger.error('Insufficient space')
            elif err.user_message_text:
                if logger:
                    logger.error('Dropbox error %s', err.user_message_text)
            else:
                if logger:
                    logger.error('Dropbox error %s', err)
            return False
        return True

if __name__ == '__main__':

    logger = logging.getLogger(__name__)
    token = os.getenv('DROPBOX_TOKEN', '')
    remote_path = os.getenv('DROPBOX_PATH', '/')

    if len(sys.argv) < 2:
        logger.error('At least one file name must be provided')
        sys.exit(1)

    if len(token) == 0:
        logger.error('The token hasn\'t been provided.')
        sys.exit(1)

    logger.debug("Creating a Dropbox object")
    dbx = dropbox.Dropbox(token)

    try:
        dbx.users_get_current_account()
    except dropbox.exceptions.AuthError as err:
        logger.error('Invalid access token')
        sys.exit(2)

    for file_name in sys.argv[1:]:
        res = backup(dbx, file_name, remote_path, logger)
        if not res:
            sys.exit(3)

