# Specify the input and output file names
input_file_name = "ChassisCAN1.dbc"
output_file_name = "CANoutput.dbc"

# Open the input file for reading
with open(input_file_name, "r") as input_file:
    # Read all lines from the input file
    lines = input_file.readlines()

# Initialize an empty list to store the extracted data
extracted_data = []

# Iterate through the lines and extract the required datafrom lines starting with "BO_"
for line in lines:
    if line.startswith("BO_"):
        extracted_text=line
        a=extracted_text.rindex(":")
        updated_text = line.strip()[3:a]  # Extract the required data after "BO_"
        extracted_data.append(updated_text)

# Open the output file for writing and write the extracted data to it
with open(output_file_name, "w") as output_file:
    for data in extracted_data:
        output_file.write(data + "\n")

# Print a confirmation message
print(f"Extracted and wrote to {output_file_name}:\n{extracted_data}")