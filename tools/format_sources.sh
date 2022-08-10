#!/usr/bin/env bash
set -e

# Format Python sources using yapf.
find . -type f \! \( -name .git -prune \) \( -name "*.py" \) | while read FILE; do
  echo "[yapf] ${FILE}"
  yapf --in-place --style yapf "${FILE}"
done

# Format Java/JavaScript/JSON sources using clang-format.
find . -type f \! \( -name .git -prune \) \( -name "*.json" -o -name "*.js" \) | while read FILE; do
  echo "[clang-format] ${FILE}"
  clang-format -i "${FILE}"
done

# Format Markdown using mdformat.
find . -type f \! \( -name .git -prune \) \( -name "*.md" \) | while read FILE; do
  echo "[mdformat] ${FILE}"
  mdformat "${FILE}"
done

# Format YAML using yamlfmt.
find . -type f \! \( -name .git -prune \) \( -name "*.yaml" -o -name "*.yml" \) | while read FILE; do
  echo "[yamlfmt] ${FILE}"
  ./tools/yamlfmt.py -m 2 -s 4 -o 2 -p "${FILE}"
done
