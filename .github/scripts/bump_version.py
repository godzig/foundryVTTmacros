import datetime
import json

MODULE_FILE = 'module.json'
VERSION_DATE_FORMAT = '%Y.%j.%H%M%S'

# Get version from current date.
now = datetime.datetime.now(datetime.timezone.utc)
version = now.strftime(VERSION_DATE_FORMAT)

# Update module.json with this version.
with open(MODULE_FILE, 'r+') as f:
  module = json.load(f)
  module['version'] = version
  f.seek(0)
  json.dump(module, f, indent=2)
  f.truncate()

# Store variable for github workflow.
print('::set-output name=version::v{}'.format(version))
