# huffman-by-python
This small python project was done for CS 320, Algorithms Theory and Practice.

## Objective

Learn how to implement the Huffman encoding algorithm.

## Instructions

You must use the heapq module from python to implement heap functions to create a Huffman code for text character encoding.

The heapq methods that you would be using are:

- heapify(): To create the heap
- heappop(): To extract minimum element from the heap
- heappush(): To insert the element after merging into the heap

Make a new file named huffman.py.

## Usage
When provided with an input file (in the same folder as huffman.py) named example.txt containing a message, a sample usage would be:
python3 huffman.py example.txt

When executed, the code will produce two new text files, example.txt_encoded, which contains the encoded message, and example.txt_encoded_decoded, which contains the decoded message.

## Further Details

We will test your code by calling the function named huffman_letter_codes_from_file_contents(file_name). It takes the name of a file as input and it returns a Huffman code for the letters in the file, in the form of a dict mapping from letters to a binary code as a string. Note that the return from huffman_letter_codes_from_file_contents is a dict from string to string. Since Python does not have a type for single characters, we represent them as strings of length one.

For example, when given the example text file provided (example.txt), the method huffman_letter_codes_from_file_contents might return the following dictionary:

{'H': '00000', 'u': '00001', 'W': '00010', '3': '00011', 'c': '00100', '0': '00101', 'd': '00110', 'S': '00111', 'C': '01000', '\n': '01001', 'm': '0101', '!': '01100', 'g': '01101', 'n': '0111',
    ' ': '100', 't': '1010', 'e': '1011', 's': '1100', 'i': '1101', '.': '11100', 'l': '11101', 'o': '11110', 'r': '111110', '2': '111111'}

Using these Huffman encodings, the file example.txt_encoded would contain:

000001011111011110111110100010000011110000011111111001011001100101000001001101011011110101100111001000001011010111101010111111101001101110010000100111100101010111010111011010110001001

Then decoding, we should recover the original message in example.txt. That is, the file example.txt_encoded_decoded would contain:

Hello CS 320 students. Winter is comming!

(That’s how they spell it in Westeros.)

## Testing

Testing your Huffman codes is not trivial. Python dictionaries don't have a guaranteed order of iteration, but you can compare two dictionaries for equality. However, a Huffman code for a given letter frequency is not unique. There are many Huffman codes for a given letter frequency that are all equally optimal, in terms of the compression they give.

## Prefix property

So, to determine if a Huffman code is correct, you should at least verify that it is a prefix code. A prefix code is a variable length encoding where no letter's code is a prefix of any other code. See the example above, the letter “e” was given code “000”. No other code begins with “000”, so it is not a prefix of any other code. This property is true for all the other codes too.

While you could verify this property by hand, it's more fun to see if files make a successful “round trip” through the encoding and decoding process. We have given you code to do this, and you can see above how to call it. After encoding and decoding an example file, you should be able to diff the original and the “_encoded_decoded”, and find no difference.

## Optimality of Compression

Huffman codes are optimal prefix codes for per-symbol encoding. Here our symbols are just letters. While there are many possible Huffman codes for given letter frequencies, they will all result in a minimal length of the encoded file.