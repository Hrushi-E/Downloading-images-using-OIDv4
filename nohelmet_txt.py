import os

input_folder = "/content/NOH/content/OIDv4_ToolKit/NoHelmet"
#output_folder = "/content/NOH/content/OIDv4_ToolKit/NoHelmet"
#output_filename = "nohelmet_txt.py"

def replace_human_with_number(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if line.startswith("Human"):
            new_lines.append("1" + line[5:])
        else:
            new_lines.append(line)

    with open(filename, 'w') as file:
        file.writelines(new_lines)

# Process each txt file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_folder, filename)
        replace_human_with_number(input_file_path)
