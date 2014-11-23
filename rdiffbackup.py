"""Create and rdiff-backup of Dropbox and push it to Amazon S3"""

from subprocess import call

dir_name = 'tmp'
bucket_name = ''

dir_path = '' + dir_name
tmp_path = '/tmp/' + dir_name
s3remote = 's3://' + bucket_name

if __name__ == '__main__':
    # Dropbox stuff here
    call(['rdiff-backup', dir_path, tmp_path])
    call(['aws', 's3', 'cp', tmp_path, s3remote, '--recursive', '--quiet'])
    call(['rm', '-rf', tmp_path])
