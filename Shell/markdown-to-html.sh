#!/bin/sh
# 
# Uses pandoc and in-place sed to format markdown text as HTML, with LaTeX math
# handled by MathJax.
#
# Specify output file location with `-o <output_path>`. 
# If unspecified, default to creating the HTML document in the same directory
# as the original markdown document. 

SUBJECT=markdown-to-html-converter
VERSION=0.0.1
USAGE="Usage: ./markdown-to-html.sh -hv args"

# --- Option processing --------------------------------------------
if [ $# == 0 ] ; then
    echo $USAGE
    exit 1;
fi

while getopts ":vho:" optname
  do
    case "$optname" in
      "v")
        echo "Version $VERSION"
        exit 0;
        ;;
      "h")
        echo $USAGE
        exit 0;
        ;;
      "?")
        echo "Unknown option $OPTARG"
        exit 0;
        ;;
      "o")
        OUTPUT_PATH=${OPTARG}
        ;;
      ":")
        echo "No argument value for option $OPTARG"
        exit 0;
        ;;
      *)
        echo "Unknown error while processing options"
        exit 0;
        ;;
    esac
  done

shift $(($OPTIND - 1))
FILEPATH=$1
SED_HTML_REGEX='s/src="\/\/\(cdn\.mathjax\.org[^\"]*"\)/src="https:\/\/\1/'
# -----------------------------------------------------------------

LOCK_FILE=/tmp/${SUBJECT}.lock

if [ -f "$LOCK_FILE" ]; then
echo "Script is already running"
exit
fi

# -----------------------------------------------------------------
trap "rm -f $LOCK_FILE" EXIT
touch $LOCK_FILE 

# -----------------------------------------------------------------
#  SCRIPT LOGIC GOES HERE
# -----------------------------------------------------------------

if [ -e "$FILEPATH" ]; then
  # Get file's name, directory, and extension
  BASENAME=$(basename "${FILEPATH}")
  EXT="${BASENAME##*.}"
  FILENAME="${BASENAME%.*}"
  DIR=$(dirname "${FILEPATH}")
  

  echo $OUTPUT_PATH  
  # Check if output path is unset
  if [ -z ${OUTPUT_PATH+x} ]; then 
    OUTPUT_PATH="${DIR}/${FILENAME}.html"
  fi

  echo "Saving results at ${OUTPUT_PATH}"
  echo "Performing pandoc processing..."
  pandoc -s $FILEPATH -o $OUTPUT_PATH --mathjax
  echo "Replacing buggy HTML..."
  sed -i '' $SED_HTML_REGEX $OUTPUT_PATH
  echo "Done!"
fi




