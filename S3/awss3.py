import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

aws_access_key = ''
aws_secret_key = ''
bucket = ''
path = ''
file_name = ''

#TODO: Logging, auth handling

class AwsS3:

        def __init__(self, aws_access_key, aws_secret_key, path):
            self.access_key = aws_access_key
            self.secret_key = aws_secret_key
            self.client = S3Connection(self.access_key, self.secret_key)

        def create_bucket(self, bucket_name):
            try:
                new_bucket = self.client.create_bucket(bucket_name)
                return new_bucket
            except boto.exception.S3CreateError:
                print 'The bucket name "' + bucket_name + '" is already taken.'
                print 'Please choose a unique bucket name'

        def get_bucket(self, bucket_name):
            try:
                return self.client.get_bucket(bucket_name)
            except boto.exception.S3ResponseError as e:
                print 'Bucket "' + bucket_name + '" does not exist.'

        def list_buckets(self):
            return self.client.get_all_buckets()

        def upload(self, file_path, file_name, bucket_name):
            k = Key(bucket_name)
            k.key = file_name
            k.set_contents_from_filename(file_path)

if __name__ == '__main__':
    #time_pin = datetime.now() - timedelta(hours=1)
    if not aws_access_key or not aws_secret_key:
        print 'Please provide your aws_access_key and aws_secret_key'
    if not path:
        print 'Please provide a path'
    if not bucket:
        print 'Please provide a bucket'
    else:
        client = AwsS3(aws_access_key, aws_secret_key, path)
        aws_bucket = client.get_bucket(bucket)
        if aws_bucket is None:
            aws_bucket = client.create_bucket(bucket)
        if aws_bucket is None:
            print "Try picking a bucket from the list below:"
            print client.list_buckets()
            print "Aborting"
        else:
            client.upload(path + file_name, file_name, aws_bucket)
