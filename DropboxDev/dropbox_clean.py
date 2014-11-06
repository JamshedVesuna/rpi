import dropbox
import json
#from time import strptime
from datetime import datetime, timedelta

app_key = ''
app_secret = ''

#TODO: Logging, time zones, auth handling, etc

class MediaCleaner:

        def __init__(self, access_token, path):
            if not access_token:
                self.access_token = self.get_access_token()
            else:
                self.access_token = access_token
            self.client = dropbox.client.DropboxClient(self.access_token)

        def get_access_token(self):
            flow = dropbox.client.DropboxOAuth2FlowNoRedirect(
                app_key, app_secret)
            authorize_url = flow.start()
            authorize_url = flow.start()
            print '1. Go to: ' + authorize_url
            print '2. Click "Allow" (you might have to log in first)'
            print '3. Copy the authorization code.'
            code = raw_input("Enter the authorization code here: ").strip()
            new_access_token, user_id = flow.finish(code)
            print 'Replace access_token with: ', new_access_token
            return new_access_token

        def upload(self):
            f = open('working-draft.txt', 'rb')
            response = self.client.put_file('/magnum-opus.jpg', f)
            print json.dumps(response, indent=4, separators=(',',':'))


        def get_contents(self, file_path):
            modified = self.client.metadata(file_path)
            contents = modified['contents']
            return contents

        def clean(self, contents, time_pin):
            backup_folder = self.get_backup_folder()
            #year = time_pin.year
            for media_file in contents:
                file_time = datetime.strptime(
                    (media_file['modified'].split("+")[0]),
                    '%a, %d %b %Y %H:%M:%S ')
                file_year = file_time.year
                if not self.dir_exists(backup_folder, str(file_year)):
                    self.client.file_create_folder(backup_folder+str(file_year))
                if file_time < time_pin:
                    old_path = media_file['path']
                    components = old_path.split('/')
                    file_name = components[len(components)-1]
                    self.client.file_move(
                        old_path,
                        ''.join(
                        [backup_folder, str(file_year), '/', file_name]))
                    print json.dumps(media_file, indent=4, separators=(',',':'))
                    print file_time

        def get_backup_folder(self):
            return '/Backup/Photos/'

        def dir_exists(self, path, directory):
            dir_metadata = self.client.metadata(path)
            for subdir in dir_metadata['contents']:
                if subdir['path'].lower() == (path + directory).lower():
                    return True
            return False


if __name__ == '__main__':
    access_token = ''
    path = '/Camera Uploads/'
    time_pin = datetime.now() - timedelta(hours=1)
    m = MediaCleaner(access_token, path)
    m.clean(m.get_contents(path), time_pin)
