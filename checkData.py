
import os
import shutil

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def process_data(data_lines):
    entries = [line.strip().split(": ") for line in data_lines if line.strip()]
    cleaned_entries = remove_repeated_entries([(range_, id_) for range_, id_ in entries if id_ != "brak"])
    return cleaned_entries

def remove_repeated_entries(entries):
    seen = set()
    cleaned_entries = []
    for range_, id_ in entries:
        if id_ not in seen:
            seen.add(id_)
            cleaned_entries.append((range_, id_))
    return cleaned_entries

def save_data_to_file(cleaned_entries, output_file_path):
    with open(output_file_path, 'w') as file:
        for range_, id_ in cleaned_entries:
            file.write(f'{range_} : {id_}\n')


def read_and_process_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    ranges = []
    for line in lines:
        range_str, _ = line.strip().split(": ")
        start, end = map(int, range_str.split('-'))
        ranges.extend(range(start, end + 1))
    return ranges

def copy_and_rename_images(image_ranges, source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    image_number = 1
    for image_id in image_ranges:
        source_image_path = os.path.join(source_dir, f'LDRAW_file-{image_id:04d}.png')
        target_image_path = os.path.join(target_dir, f'{image_number}.png')
        
        if os.path.exists(source_image_path):
            shutil.copy(source_image_path, target_image_path)
            print(f'Zdjęcie {source_image_path} zostało skopiowane jako {target_image_path}')
            image_number += 1


def main():
    input_file_path = 'lego_id.txt'  # Zastąp ścieżką do twojego pliku wejściowego
    output_file_path = 'lego_fixed_id.txt'  # Zastąp ścieżką do pliku wyjściowego
    source_dir = 'LDRAW_file-glExport'   # Katalog źródłowy ze zdjęciami
    target_dir = 'Dataset\images'                # Katalog docelowy dla zdjęć

    data_lines = read_data_from_file(input_file_path)
    cleaned_entries = process_data(data_lines)
    save_data_to_file(cleaned_entries, output_file_path)
    print(f"Dane zostały zapisane w pliku: {output_file_path}")
    image_ranges = read_and_process_data(output_file_path)
    copy_and_rename_images(image_ranges, source_dir, target_dir)

if __name__ == "__main__":
    main()
