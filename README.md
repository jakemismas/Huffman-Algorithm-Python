# 🔐 Huffman Encoding and Decoding

This Python script demonstrates how to perform Huffman encoding and decoding on a given text file. Huffman coding is a lossless data compression algorithm that assigns shorter codes to more frequently occurring characters, and longer codes to less frequently occurring characters. This results in a compressed representation of the original text.

## 🌟 Features

- Calculate character frequencies in a given file
- Generate Huffman codes based on character frequencies
- Encode a text file using the generated Huffman codes
- Decode an encoded file back to its original form

## 📚 Requirements

- Python 3.6+ 🐍

## 🚀 Usage

You can run the script by executing the following command:

```
python huffman.py <input_file>
```

Replace `<input_file>` with the path to the text file you want to compress.

The script will generate an encoded file with the suffix `_encoded` and a decoded file with the suffix `_encoded_decoded`.

## 📖 Example

Suppose you have a text file named `example.txt`. You can run the script as follows:

```
python huffman.py example.txt
```

This will create two new files: `example.txt_encoded` (the encoded file) and `example.txt_encoded_decoded` (the decoded file). The decoded file should have the same content as the original `example.txt` file.

## 🛠️ Implementation Details

The script consists of several functions to perform Huffman encoding and decoding:

- `file_character_frequencies(file_name)`: Calculates character frequencies in a given file
- `huffman_letter_codes_from_file_contents(file_name)`: Generates Huffman codes for characters in a given file
- `encode_file_using_codes(file_name, letter_codes)`: Encodes a file using the provided Huffman codes
- `decode_file_using_codes(file_name_encoded, letter_codes)`: Decodes an encoded file using the provided Huffman codes

Additionally, there are some helper functions and a `PriorityTuple` class to assist in building the Huffman tree and managing the heap.

## 🌱 Possible Code Enhancements
Below are some possible enhancements that could be made to the code:

- Parallelization: Use parallel processing to encode and decode larger files more quickly. This could be achieved using Python's multiprocessing or concurrent.futures modules.

- Binary file handling: Modify the script to handle binary files, allowing compression and decompression of a wider range of file types.

- File size optimization: In the current implementation, the encoded file is saved as a text file with '0's and '1's. It can be further optimized by saving the encoded file as a binary file, where each group of 8 bits represents a byte.

- Performance metrics: Display performance metrics, such as compression ratio, encoding time, and decoding time, to provide users with feedback on the efficiency of the algorithm.

- Adaptive Huffman coding: Implement adaptive Huffman coding, which updates the tree dynamically as the data is being encoded or decoded. This would make the algorithm more efficient for compressing files with varying character distributions.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
