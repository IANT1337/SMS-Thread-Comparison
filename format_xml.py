#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import argparse
import sys

def extract_messages(xml_file, sent_file, received_file):
    """
    Parse the SMS backup XML and write bodies of sent (type="2")
    and received (type="1") messages into separate files.
    """
    try:
        tree = ET.parse(xml_file)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}", file=sys.stderr)
        sys.exit(1)

    root = tree.getroot()
    with open(sent_file, 'w', encoding='utf-8') as sent_f, \
         open(received_file, 'w', encoding='utf-8') as recv_f:

        for sms in root.findall('sms'):
            body = sms.get('body', '').strip()
            msg_type = sms.get('type')
            if not body:
                continue  # skip empty bodies

            if msg_type == '2':
                sent_f.write(body + '\n')
            elif msg_type == '1':
                recv_f.write(body + '\n')
            # else: ignore other types

    print(f"Written sent messages to: {sent_file}")
    print(f"Written received messages to: {received_file}")

def main():
    parser = argparse.ArgumentParser(
        description='Extract SMS bodies into sent/received text files.')
    parser.add_argument('xml_file',
                        help='Path to the SMS XML backup file')
    parser.add_argument('--sent', '-s',
                        default='sent.txt',
                        help='Output file for sent messages (type=2)')
    parser.add_argument('--received', '-r',
                        default='received.txt',
                        help='Output file for received messages (type=1)')
    args = parser.parse_args()

    extract_messages(args.xml_file, args.sent, args.received)

if __name__ == '__main__':
    main()
