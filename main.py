import sys
import getopt
import cantools
import json
import os

def dbc_to_json(inputfile):
    try:
        # Load the CAN database file using cantools
        db = cantools.database.load_file(inputfile)

        # Create a list to store the messages
        messages_list = []

        # Iterate over messages and extract relevant information
        for message in db.messages:
            message_info = {
                "canId": message.frame_id,
                "pgn": message.frame_id,  # You may adjust this based on your needs
                "name": message.name,
                "isExtendedFrame": message.is_extended_frame,
                "dlc": message.length,
                "signals": []
            }

            # Iterate over signals in the message
            for signal in message.signals:
                signal_info = {
                    "name": signal.name,
                    "label": f"{message.name.lower()}.{signal.name.lower()}",
                    "startBit": signal.start,
                    "bitLength": signal.length,
                    "isLittleEndian": signal.byte_order == 'little_endian',
                    "isSigned": signal.is_signed,
                    "factor": signal.scale,
                    "offset": signal.offset,
                    "min": signal.minimum if signal.minimum is not None else 0,
                    "max": signal.maximum if signal.maximum is not None else 0,
                    "sourceUnit": signal.unit,
                    "dataType": "int",  # Assuming all signals are of integer data type
                    "comment": signal.comment
                }

                message_info["signals"].append(signal_info)

            messages_list.append(message_info)

        # Determine the output file name
        output_file = inputfile.replace('.dbc', '_output.json')  # Adjust the output file name as needed

        # Save the output as a JSON file
        with open(output_file, 'w') as outfile:
            json.dump(messages_list, outfile, indent=4)

        print(f"Conversion completed. Output saved to {output_file}")
    except cantools.database.exceptions.DecodeError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print('dbc2json.py -i <inputfile>')
        sys.exit(1)

    for opt, arg in opts:
        if opt == '-h':
            print('CAN_dbc2json.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    dbc_to_json(inputfile)

if __name__ == '__main__':
    main(sys.argv[1:])
