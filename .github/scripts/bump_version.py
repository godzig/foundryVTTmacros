
major = None
minor = None
patch = None

with open('VERSION', 'r') as f:
  major, minor, patch = [int(x) for x in f.read().strip().split('.')]

# Arbitrary increment process.

patch = patch + 1

if patch > 20:
  patch = 0
  minor = minor + 1

if minor > 20:
  minor = 0
  major = major + 1

version = '{}.{}.{}'.format(major,minor,patch)
with open('VERSION', 'w') as f:
  f.write(version)

print('::set-output name=version::{}'.format(version))
