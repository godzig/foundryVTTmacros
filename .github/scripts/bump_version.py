import datetime

d = datetime.datetime.now(datetime.timezone.utc)
version = d.strftime('%Y.%j.%H%M%S')
print('::set-output name=version::v{}'.format(version))
