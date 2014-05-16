dir="$2"
echo "<items>"
IFS=$'\n'
for i in $(find "$dir" -follow -type f -not -name ".*" -not -path "*/.*" -not -name "LICENSE" -not -name "readme.md"); do
  title="$(basename "$i")"
  subtitle="$(head -1 "$i")"

  # If the argument is empy (show all), or if the argument is in the title or subitle, show them. Spaces in arguments are '.*' in RegEx.
  if [[ "$1" == "" || "$(echo "$title" | egrep -ic "${1// /.*}")" != "0" || "$(echo "$subtitle" | egrep -ic "${1// /.*}")" != "0" ]]; then
    echo "<item arg=\"$i\" type='file' valid='YES' uid=\"$i\"><title><![CDATA[$title]]></title><subtitle><![CDATA[$subtitle]]></subtitle></item>"
  fi
done
unset IFS
echo "</items>"
