#!/bin/bash

FOLDER_PATH="/path/to/your/folder"

txt_files=("$FOLDER_PATH"/*.txt)

if [ ${#txt_files[@]} -gt 0 ]; then
  selected_file="${txt_files[RANDOM % ${#txt_files[@]}]}"
  cat "$selected_file"
fi
