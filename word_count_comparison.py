import argparse
import re
from collections import Counter

def parse_args():
    parser = argparse.ArgumentParser(
        description='Compare word usage counts and total messages between sent and received text files.'
    )
    parser.add_argument(
        '--sent',
        default='sent.txt',
        help='Path to the file containing sent messages (default: sent.txt)'
    )
    parser.add_argument(
        '--received',
        default='received.txt',
        help='Path to the file containing received messages (default: received.txt)'
    )
    parser.add_argument(
        '--input',
        default='input_words.txt',
        help='Path to the file containing words to analyze (default: input_words.txt)'
    )
    return parser.parse_args()


def load_words(path):
    """
    Load a list of words from a file, one per line.
    Strips whitespace and ignores empty lines.
    Returns a list of lowercase words.
    """
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip()]


def count_words(text, words):
    """
    Count occurrences of each word in the given text.
    Splits on word boundaries and counts tokens case-insensitively.
    Returns a dict mapping each word to its count.
    """
    tokens = re.findall(r"\w+", text.lower())
    counter = Counter(tokens)
    return {word: counter.get(word, 0) for word in words}


def main():
    args = parse_args()

    # Load words to track
    words = load_words(args.input)
    if not words:
        print(f"No words found in '{args.input}'.")
        return

    # Read and count lines for sent messages
    try:
        with open(args.sent, 'r', encoding='utf-8') as f_sent:
            sent_lines = [line.rstrip('\n') for line in f_sent]
            sent_text = '\n'.join(sent_lines)
            sent_msg_count = len(sent_lines)
    except FileNotFoundError:
        print(f"Error: Sent file not found: {args.sent}")
        return

    # Read and count lines for received messages
    try:
        with open(args.received, 'r', encoding='utf-8') as f_recv:
            received_lines = [line.rstrip('\n') for line in f_recv]
            received_text = '\n'.join(received_lines)
            received_msg_count = len(received_lines)
    except FileNotFoundError:
        print(f"Error: Received file not found: {args.received}")
        return

    # Count word occurrences
    sent_counts = count_words(sent_text, words)
    received_counts = count_words(received_text, words)

    # Output summary of total messages
    print(f"{'Metric':<20}{'Sent':>10}{'Received':>10}")
    print('-' * 40)
    print(f"{'Total messages':<20}{sent_msg_count:>10}{received_msg_count:>10}")
    print()

    # Output the word counts table
    print(f"{'Word':<20}{'Sent':>10}{'Received':>10}")
    print('-' * 40)
    for word in words:
        print(f"{word:<20}{sent_counts[word]:>10}{received_counts[word]:>10}")

if __name__ == '__main__':
    main()
