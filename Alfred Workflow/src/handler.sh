cd "$(dirname "$1")"
if [[ "$1" == *".sh" ]]; then
    sh "$1"
  elif [[ "$1" == *".applescript" ]]; then
    osascript "$1"
  elif [[ "$1" == *".rb" ]]; then
    ruby "$1"
  elif [[ "$1" == *".py" ]]; then
    python "$1"
  elif [[ "$1" == *".php" ]]; then
  php "$1"
  else
    "./$1"
fi