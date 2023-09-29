import json

# Specify the input and output file names
input_file_name = "ChassisCAN1.dbc"
output_file_name = "Canoutput.json"

# Initialize empty lists to store the extracted data
extracted_data = []

# Initialize variables to hold message, sender_node, and signal information
message = None
sender_node = None
signal = None
bit_position = None
length_of_bit = None
factor = None
offset = None
min_value = None
max_value = None
unit = None
receiver_node = None

# Open the input file for reading
with open(input_file_name, "r") as input_file:
    for line in input_file:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Skip lines that do not start with "BO_" or "SG_"
        if not line.startswith(("BO_", "SG_")):
            continue

        if line.startswith("BO_"):
            # If there's already data from a previous "BO_" line, append it to the extracted data
            if message and sender_node and signal:
                extracted_data.append({
                    "message": message,
                    "sender_node": sender_node,
                    "signal": signal,
                    "bit_position": bit_position,
                    "length_of_bit": length_of_bit,
                    "factor": factor,
                    "offset": offset,
                    "min_value": min_value,
                    "max_value": max_value,
                    "unit": unit,
                    "receiver_node": receiver_node
                })

            # Extract message and sender_node from the "BO_" line
            parts = line.split()
            if len(parts) >= 4:
                message = parts[1] + parts[2]
                sender_node = parts[5]

        elif line.startswith("SG_"):
            # Extract signal from the "SG_" line
            parts = line.split()
            if len(parts) >= 7:
                signal = parts[1]
                bit_position_and_length_of_bit = parts[2]  # 15|1@0+
                factor_and_offset = parts[3]  # (1,0)
                min_max_values = parts[4]  # [0|1]
                unit = parts[5]  # ""
                receiver_node = parts[6]  # VDDM

                # Split bit_position_and_length into subparts
                subparts_bit_position = bit_position_and_length_of_bit.split('|')
                if len(subparts_bit_position) == 2:
                    bit_position = subparts_bit_position[0]
                    length_of_bit = subparts_bit_position[1]

                # Split factor_and_offset into subparts
                subparts_factor_offset = factor_and_offset.strip('()').split(',')
                if len(subparts_factor_offset) == 2:
                    factor = subparts_factor_offset[0]
                    offset = subparts_factor_offset[1]

                # Split min_max_values into subparts
                subparts_min_max = min_max_values.strip('[]').split('|')
                if len(subparts_min_max) == 2:
                    min_value = subparts_min_max[0]
                    max_value = subparts_min_max[1]

# Add the last extracted data (if any) to the extracted_data list
if message and sender_node and signal:
    extracted_data.append({
        "message": message,
        "sender_node": sender_node,
        "signal": signal,
        "bit_position": bit_position,
        "length_of_bit": length_of_bit,
        "factor": factor,
        "offset": offset,
        "min_value": min_value,
        "max_value": max_value,
        "unit": unit,
        "receiver_node": receiver_node
    })

# Convert the extracted data to a JSON structure and write it to the output JSON file
with open(output_file_name, 'w') as output_file:
    json.dump(extracted_data, output_file, indent=2)

print(f"Extracted lines saved to {output_file_name}")
