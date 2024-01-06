import json

def read_dict_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during reading: {e}")
        return None

def invert_dict(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if isinstance(value, list):
            for item in value:
                inverted_dict.setdefault(item, []).append(key)
        else:
            inverted_dict.setdefault(value, []).append(key)
    return inverted_dict

def write_dict_to_file(file_path, data_dict):
    try:
        with open(file_path, 'w') as file:
            json.dump(data_dict, file, indent=2)
    except PermissionError:
        print(f"Permission error: Unable to write to {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred during writing: {e}")

def main():
    input_file_path = 'C:\\Users\\Jack Mwisa\\Documents\\GitHub\\Folder\\Python-100-Days-of-code\\Day 6\\input_data.txt'

    output_file_path = 'output_data.txt'

    original_dict = read_dict_from_file(input_file_path)

    if original_dict:
        print("Original Dictionary:", original_dict)

        inverted_dict = invert_dict(original_dict)
        print("Inverted Dictionary:", inverted_dict)

        write_dict_to_file(output_file_path, inverted_dict)
    else:
        print("Error reading the original dictionary. Check the file and its format.")

if __name__ == "__main__":
    main()
