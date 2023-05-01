import sys
import heapq
from collections import Counter
from contextlib import contextmanager

# Context manager for opening and closing files
@contextmanager
def open_file(file_name, mode='r'):
    f = open(file_name, mode)
    try:
        yield f
    finally:
        f.close()

# Calculate character frequencies in a file
def file_character_frequencies(file_name):
    with open_file(file_name, 'r') as f:
        text = f.read()
    return Counter(text)

# PriorityTuple class for sorting based on the first item
class PriorityTuple(tuple):
    def __lt__(self, other):
        return self[0] < other[0]

# Convert frequencies to a heap
def to_heap(freqs):
    freqs = sorted(freqs.items())
    return [PriorityTuple((freq, (char, ''))) for freq, char in freqs]

# Update node codes with '0' or '1'
def update_node_code(nodes, LR):
    for node in nodes:
        node[1] = LR + node[1]
    return nodes

# Build Huffman tree from the heap
def build_tree(heap):
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        update_node_code(left[1:], '0')
        update_node_code(right[1:], '1')

        heapq.heappush(heap, PriorityTuple((left[0] + right[0], left[1:] + right[1:])))

    return heap[0][1:]

# Generate Huffman codes from character frequencies
def huffman_codes_from_frequencies(freqs):
    heap = to_heap(freqs)
    tree = build_tree(heap)
    return {char: code for char, code in tree}

# Main function to generate Huffman codes from a file
def huffman_letter_codes_from_file_contents(file_name):
    freqs = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freqs)

# Encode a file using the given Huffman codes
def encode_file_using_codes(file_name, letter_codes):
    with open_file(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open_file(file_name_encoded, 'w') as fout:
        fout.write(''.join(letter_codes[c] for c in contents))
    print("Wrote encoded text to {}".format(file_name_encoded))

# Decode an encoded file using the given Huffman codes
def decode_file_using_codes(file_name_encoded, letter_codes):
    with open_file(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open_file(file_name_encoded_decoded, 'w') as fout:
        partial_code = ""
        for c in contents:
            partial_code += c
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))

def main():
    frequencies = file_character_frequencies(sys.argv[1])
    codes = huffman_codes_from_frequencies(frequencies)

    encode_file_using_codes(sys.argv[1], codes)
    decode_file_using_codes(sys.argv[1]+'_encoded', codes)

if __name__ == '__main__':
    main()
