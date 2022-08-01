#!/usr/bin/env python3

import random
import glob
import sys
import json
import string
import pathlib

# Arbitrary author ID, not sure if necessary.
AUTHOR_ID = 'h3vjdsNcTNpDAKxr'

# Source macro scripts.
SOURCE_PATH = 'scripts'

# Output db file.
OUTPUT_DB = 'packs/macros.db'

def GenerateId():
  """ Returns a 16 character ID for database entries. """
  size = 16
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  return ''.join(random.choice(chars) for _ in range(size))

def main(unused_argv):
  with pathlib.Path(OUTPUT_DB).open("w", encoding="UTF-8") as macros_db:
    for filename in pathlib.Path(SOURCE_PATH).glob('*.js'):
      entry = {}
      entry['_id'] = GenerateId()
      entry['name'] = filename.with_suffix('').name.replace('_', ' ')
      entry['type'] = 'script'
      entry['author'] = AUTHOR_ID
      entry['img'] = 'icons/svg/dice-target.svg'
      entry['scope'] = 'global'
      entry['command'] = filename.read_text()
      entry['folder'] = None
      entry['sort'] = 0
      entry['permission'] = {}
      entry['permission']['default'] = 0
      entry['permission'][AUTHOR_ID] = 3
      entry['flags'] = {}
      json.dump(entry, macros_db)
      macros_db.write('\n')

if __name__ == "__main__":
  main(sys.argv[1:])
