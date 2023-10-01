import json

# Specify the input and output file names
input_file_name = "ChassisCAN1.dbc"
output_file_name = "CANoutput.json"
skipped_file_name = "skipped.txt"

# Initialize a list to store the extracted data
extracted_data = []

# Initialize variables to hold the current message information and line counters
current_bo = None
bo_line_count = 0  # Counter for BO_ lines
sg_line_count = 0  # Counter for SG_ lines

# Initialize a list to store skipped lines
skipped_lines = []

# Open the input file for reading
with open(input_file_name, "r") as input_file:
    for line in input_file:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Process only lines that start with "BO_" or "SG_"
        if line.startswith(("BO_", "SG_")):
            if line.startswith("BO_"):
                bo_line_count += 1
                # Save the previous message if it exists
                if current_bo is not None:
                    extracted_data.append(current_bo)

                # Parse BO_ line to extract message information
                bo_parts = line.split()
                if len(bo_parts) >= 6:
                    current_bo = {
                        "BO": line,
                        "message": bo_parts[2],
                        "sender_node": bo_parts[5],
                        "SG": []
                    }
            elif current_bo is not None:
                sg_line_count += 1
                # Parse SG_ line to extract signal information and add it to the current message's "SG" list
                sg_parts = line.split()
                if len(sg_parts) >= 8:
                    current_bo["SG"].append({
                        "signal": line,
                        "signal_name": sg_parts[1],
                        "bit_position": sg_parts[3].split('|')[0],
                        "length_of_bit": sg_parts[3].split('|')[1].split('@')[0],
                        "factor": sg_parts[4].split(',')[0].strip('()'),
                        "offset": sg_parts[4].split(',')[1].strip('()'),
                        "min_value": sg_parts[5].split('|')[0].strip('[]'),
                        "max_value": sg_parts[5].split('|')[1].strip('[]'),
                        "unit": sg_parts[6].strip('"'),
                        "receiver_node": sg_parts[7]
                    })
            else:
                # Skip lines that start with "SG_" before encountering a "BO_" line
                skipped_lines.append(line)

# Add the last extracted BO_ (if any) to the extracted_data list
if current_bo is not None:
    extracted_data.append(current_bo)

# Convert the extracted data to a JSON structure and write it to the output JSON file
with open(output_file_name, 'w') as output_file:
    json.dump(extracted_data, output_file, indent=2)

print(f"Extracted lines saved to {output_file_name}")

# Check if all BO_ and SG_ lines are processed
with open(input_file_name, "r") as input_file:
    input_lines = [line.strip() for line in input_file if line.startswith(("BO_", "SG_"))]

if bo_line_count == len([line for line in input_lines if line.startswith("BO_")]) \
        and sg_line_count == len([line for line in input_lines if line.startswith("SG_")]):
    print("All lines starting with 'BO_' and 'SG_' are processed.")
else:
    print("Some lines starting with 'BO_' or 'SG_' are skipped during processing.")

# Write skipped lines to a "skipped.txt" file
if skipped_lines:
    with open(skipped_file_name, 'w') as skipped_file:
        for line in skipped_lines:
            skipped_file.write(line + '\n')

print(f"Skipped lines saved to {skipped_file_name}")
