arg="${1// /.*}"
dir="$2"
echo "<items>"
search="$(find "$dir" -follow -type f -not -name ".*" -not -path "*/.*" -not -name "_*" -not -path "*/_*" -not -name "LICENSE" -not -iname "readme.md")"
results="$(echo "$search" | egrep -i "$arg")"
# @todo : Search first line (subtitle) of file as well in a fast way
IFS=$'\n'
for i in $results; do
  title="$(basename "$i")"
  subtitle="$(head -1 "$i")"    
  echo "<item arg=\"$i\" type='file' valid='YES' uid=\"$i\"><title><![CDATA[$title]]></title><subtitle><![CDATA[$subtitle]]></subtitle></item>"
done
unset IFS
echo "</items>"
