
if [ -z $1 ]; then
  echo "Usage: remote_file_to_clipboard.sh <user@remote_host> <path_to_the_file>"
  exit 1
fi

if [ -z $2 ]; then
  echo "Usage: remote_file_to_clipboard.sh <user@remote_host> <path_to_the_file>"
  exit 1
fi


ssh $1 "cat $2" | pbcopy
