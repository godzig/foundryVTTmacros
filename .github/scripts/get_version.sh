#!/bin/bash -l
set -euo pipefail

echo ::set-output name=version::"$(date +%Y%m%d%H%M%S)"
