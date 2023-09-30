import json

# Specify the input and output file names
input_file_name = "ChassisCAN1.dbc"
output_file_name = "CANoutput.json"

# Initialize empty lists to store the extracted data
extracted_data = []

# Initialize variables to hold message, sender_node, and signal information
current_bo = None
current_sg = None

# Open the input file for reading
with open(input_file_name, "r") as input_file:
    for line in input_file:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Skip lines that do not start with "BO_", "SG_", or other relevant prefixes
        if not line.startswith(("BO_", "SG_", "BA_DEF_REL_", "BA_REL_", "BA_DEF_DEF_REL_", "BU_SG_REL_", "BU_EV_REL_", "BU_BO_REL_")):
            continue

        if line.startswith("BO_"):
            # If a new BO_ line is encountered, add the previous BO_ dictionary to the data list
            if current_bo is not None:
                if current_sg is not None:
                    current_bo["SG"].append(current_sg)
                extracted_data.append(current_bo)
            bo_parts = line.strip().split()
            if len(bo_parts) >= 2:
                # Extract the current BO information
                current_bo = {
                    "BO": line.strip(),
                    "message": bo_parts[2],
                    "sender_node": bo_parts[5],
                    "SG": []
                }
            else:
                current_bo = None
        elif line.startswith("SG_"):
            if current_bo is not None:
                sg_parts = line.strip().split()
                if len(sg_parts) >= 2:
                    # Extract the SG information and add it to the current BO dictionary's SG list
                    current_sg = {
                        "signal": sg_parts[1]
                    }
                    current_bo["SG"].append(current_sg)

# Add the last extracted BO_ (if any) to the extracted_data list
if current_bo is not None:
    if current_sg is not None:
        current_bo["SG"].append(current_sg)
    extracted_data.append(current_bo)

# Convert the extracted data to a JSON structure and write it to the output JSON file
with open(output_file_name, 'w') as output_file:
    json.dump(extracted_data, output_file, indent=2)

print(f"Extracted lines saved to {output_file_name}")
