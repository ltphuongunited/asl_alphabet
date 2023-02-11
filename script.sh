#!/bin/bash

# Get a list of all directories
dirs=$(ls -d */)

# Loop through each directory
for dir in $dirs; do
  # Change into the directory
  cd "$dir"

  # Get a list of all files
  files=$(ls -1)

  # Counter for keeping track of the number of files processed
  counter=0

  # Loop through each file
  for file in $files; do
    # Increment the counter
    counter=$((counter + 1))

    # Check if the counter is a multiple of 15
    if [ $((counter % 15)) -eq 0 ]; then
      # Keep the file
      continue
    fi

    # Delete the file
    rm "$file"
  done

  # Change back to the parent directory
  cd ..
done

