import json

# Specify the input JSON file name
input_json_file = "CANoutput.json"
output_dbs_file = "Reversed_Can.dbc"

# Load the JSON data
with open(input_json_file, 'r') as json_file:
    extracted_data = json.load(json_file)

# Function to convert extracted data back to DBS format
def data_to_dbs(data):
    dbs_lines = []

    for message in data:
        dbs_lines.append(f"BO_ {message['message']} {message['sender_node']}:{len(message['SG'])}")

        for signal in message['SG']:
            dbs_lines.append(f" SG_ {signal['signal_name']} : {signal['bit_position']}|{signal['length_of_bit']}@{signal['factor']},{signal['offset']} [{signal['min_value']}|{signal['max_value']}] \"{signal['unit']}\" {signal['receiver_node']}")

    return dbs_lines
# Generate DBS content
dbs_content = data_to_dbs(extracted_data)

# Write the DBS content to the output file
with open(output_dbs_file, 'w') as dbs_file:
    dbs_file.write('\n'.join(dbs_content))

print(f"Reversed data saved to {output_dbs_file}")
