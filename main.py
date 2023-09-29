import json

# Specify the input and output file names
input_file_name = "ChassisCAN1.dbc"
output_file_name = "CANoutput.json"

# Initialize empty lists to store the extracted data
extracted_data = []

# Initialize variables to hold message, sender_node, and signal information
message = None
sender_node = None
signal = None

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
                    "signal": signal
                })
            
            # Extract message and sender_node from the "BO_" line
            parts = line.split()
            if len(parts) >= 4:
                message = parts[1]+parts[2]
                sender_node = parts[5]
            
        elif line.startswith("SG_"):
            # Extract signal from the "SG_" line
            parts = line.split()
            if len(parts) >= 2:
                signal = parts[1]

# Add the last extracted data (if any) to the extracted_data list
if message and sender_node and signal:
    extracted_data.append({
        "message": message,
        "sender_node": sender_node,
        "signal": signal
    })

# Convert the extracted data to a JSON structure and write it to the output JSON file
with open(output_file_name, 'w') as output_file:
    json.dump(extracted_data, output_file, indent=2)

print(f"Extracted lines saved to {output_file_name}")
