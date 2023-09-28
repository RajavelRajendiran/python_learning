import json
# Specify the input and output file names
input_file_name = "ChassisCAN1.dbc"
output_file_name = "CANoutput.json"

# Open the input file for reading
with open(input_file_name, "r") as input_file:
    # Read all lines from the input file
    lines = input_file.readlines()

# Initialize an empty list to store the extracted data
extracted_data = []

# Iterate through the lines and extract the required from lines starting with "BO_"
for line in lines:
    if line.startswith("BO_"):
        extracted_text = line
        a = extracted_text.rindex(":")
        updated_text = line.strip()[3:a]  # Extract the required data
        extracted_data.append(updated_text)
# Convert the extracted lines to a JSON structure and write it to the output JSON file
with open(output_file_name, 'w') as output_file:
    json.dump(extracted_data, output_file, indent=2)

print(f"Extracted lines saved to {output_file_name}")
