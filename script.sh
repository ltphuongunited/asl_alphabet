#!/bin/bash

# Tạo thư mục cha mới
mkdir new_parent_directory

# Lặp qua tất cả các thư mục trong thư mục cha
for directory in asl_alphabet_train/*; do
    # Tạo thư mục con mới trong thư mục cha mới
    mkdir new_parent_directory/$(basename "$directory")

    # Lấy tất cả các file trong thư mục hiện tại
    files=($directory/*)

    # Đảo ngẫu nhiên danh sách các file
    shuf_files=($(shuf -e "${files[@]}"))

    # Tính toán số lượng file cần di chuyển vào thư mục mới
    num_files=$(( ${#shuf_files[@]} ))

    # Tính toán số lượng file cần di chuyển vào thư mục mới
    num_files_to_move=$(( $num_files * 2 / 10 ))

    # Tạo một số ngẫu nhiên từ 1 đến 10
    random_number=$((RANDOM%10+1))

    # Di chuyển các file vào thư mục mới hoặc thư mục hiện tại dựa trên số ngẫu nhiên
    if [[ "$random_number" -le 8 ]]; then
        for (( i=0; i<$num_files_to_move; i++ )); do
            mv "${shuf_files[$i]}" "new_parent_directory/$(basename "$directory")"
        done
        for (( i=$num_files_to_move; i<$num_files; i++ )); do
            mv "${shuf_files[$i]}" "$directory"
        done
    else
        for (( i=0; i<$num_files_to_move; i++ )); do
            mv "${shuf_files[$i]}" "$directory"
        done
        for (( i=$num_files_to_move; i<$num_files; i++ )); do
            mv "${shuf_files[$i]}" "new_parent_directory/$(basename "$directory")"
        done
    fi
done

