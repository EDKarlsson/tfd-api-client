#!/usr/bin/env bash

get_files() {
    # files=(ls $1/*)
    files=($(find $1 -type f -print))
}

diff_file() {
    out_dir=./out/python-client
    filename=$1
    new_file_dir=$(dirname $(echo $filename | sed 's/out\/python-client\///'))
    new_file=$(basename $filename)
    old_file=$(find $new_file_dir \( -path ./out -prune -o -path ./scripts -prune \) -o  -name $new_file -print -maxdepth 1)
    echo "File: $filename"
    echo "    new: $new_file_dir/$new_file"
    echo "    old: $old_file"
    if ! diff -q ./$filename $old_file > /dev/null 2>&1; then
        
    # if cmp -s ./$filename $old_file; then
        echo "    ===> differs"
        # lines=$(diff -u $filename $old_file$ | diffstat)
        diff -u $filename $old_file | diffstat

        # echo "         lines: $lines"
    fi
}

get_files out/python-client
for f in ${files[@]}; do
    if [ -f "$f" ]; then
        # echo "File: $f"
        diff_file $f

    fi
done