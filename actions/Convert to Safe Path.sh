# Replace spaces with underscores and make it all lowercase
pbpaste | tr ' ' '_' | awk '{print tolower($0)}' | pbcopy
echo "Spaces removed and lowercased in clipboard"
