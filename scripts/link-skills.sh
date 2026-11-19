#!/usr/bin/env bash
# Link the promoted catalog into one user-selected directory.
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd -P)
dest=${1:?Usage: link-skills.sh DESTINATION}
mkdir -p -- "$dest"
dest=$(cd "$dest" && pwd -P)
case "$dest/" in "$root/"*) echo "Choose a destination outside the checkout" >&2; exit 2;; esac
skills=("$root"/skills/{engineering,productivity}/*/SKILL.md)
for file in "${skills[@]}"; do
  src=${file%/SKILL.md}
  target="$dest/${src##*/}"
  if [[ -e "$target" || -L "$target" ]]; then
    [[ "$target" -ef "$src" ]] && continue
    echo "Conflict at $target. Existing entry preserved." >&2
    exit 1
  fi
done
for file in "${skills[@]}"; do
  src=${file%/SKILL.md}
  target="$dest/${src##*/}"
  [[ "$target" -ef "$src" ]] || ln -sT -- "$src" "$target"
done
