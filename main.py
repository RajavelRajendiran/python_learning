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
# Initialize variables to hold the message ID and message name
message = None
sender_node = None

# Iterate through the lines and extract the required from lines starting with "BO_"
for line in lines:
    if line.startswith("BO_"):
 # If there's already data from a previous "BO_" line, append it to the extracted data
     if message and sender_node:
       extracted_data.append({"message": message, "sender_node": sender_node})
     extracted_text = line
     a = extracted_text.rindex(":")
     b=(2+extracted_text.rindex("8 "))
     message = line.strip()[3:a]  # Extract required data after "BO_"
     sender_node = line.strip()[b:]  # Extract required data after "BO_"
if message and sender_node:
    extracted_data.append({"message": message, "sender_node": sender_node})
# Convert the extracted lines to a JSON structure and write it to the output JSON file
with open(output_file_name, 'w') as output_file:
    json.dump(extracted_data, output_file, indent=2)

print(f"Extracted lines saved to {output_file_name}")
