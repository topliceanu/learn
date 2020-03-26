# -*- coding: utf-8 -*-


def run_length_encode(data):
    """ Encodes the input data using the RLE method.

    See: https://en.wikipedia.org/wiki/Run-length_encoding

    Args:
        data: list, corresponding to the input data.

    Returns:
        list, result of the compression.
    """
    val = data[0]
    count = 1
    compressed_data = []

    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            compressed_data.extend([count, val])
            val = data[i]
            count = 1

    compressed_data.extend([count, val])
    return compressed_data

def run_length_decode(compressed_data):
    """ Decodes the input sequence using the RLE method.

    See: https://en.wikipedia.org/wiki/Run-length_encoding

    Args:
        data: list, format [number_of_letters, repeated_letter, ....]

    Returns:
        list, result of the decompression.
    """
    out = ''
    for i in range(0, len(compressed_data), 2):
        out += compressed_data[i+1] * compressed_data[i]
    return out

def lz77_encode(data, dictionary_buffer_size=12, preview_buffer_size=9):
    """ Encodes the input data using the LZF method or Sliding Window Compression.

    Invented by Abraham Lempel and Jacob Ziv in 1977.

    See: https://en.wikipedia.org/wiki/LZ77_and_LZ78#LZ78

    Args:
        data: list, of input characters/numbers/booleans/etc.
        dict_buffer_size: int, the size of the sliding window
        preview_buffer_size: int, the size of the text which can be potentially encoded.

    Returns:
        list, of tuples, of format (L, D, C), L - length, D - distance, C - value
    """
    # TODO make this work !!!
    def find_max_prefix(needle, haystack):
        haystack = ''.join(haystack)
        needle = ''.join(needle)

        if haystack == '' and len(needle) == 0:
            return (0, 0, needle)
        if len(needle) == 0:
            return (None, None, '')

        last = needle[-1]
        init = needle[:-1]
        haystack += init

        offset = haystack.find(needle)
        if offset != -1:
            return (len(haystack) - offset, len(needle), '')

        offset = haystack.find(init)
        return (len(haystack) - offset, len(init), last)


    encoded = []
    preview_buffer = []
    dictionary_buffer = []
    preview_buffer_index = 0

    for i in range(len(data)):
        # Maintain sliding windows for the two buffers.
        preview_buffer.append(data[i])
        if len(preview_buffer) > preview_buffer_size:
            head = preview_buffer[0]
            preview_buffer = preview_buffer[1:]
            dictionary_buffer.append(head)
        if len(dictionary_buffer) > dictionary_buffer_size:
            dictionary_buffer = dictionary_buffer[1:]

        # Find longest prefix in preview_buffer which is present in dictionary_buffer.
        (distance_back, length, new_letter) = find_max_prefix(preview_buffer, dictionary_buffer)
        if new_letter == '': # ie. perfect match.
            if i == len(data) - 1:
                encoded.append((distance_back, length, '$'))
            else:
                continue
        else:
            encoded.append((distance_back, length, new_letter))

def lz77_decode(compressed_data):
    """ Decodes the compressed data into the original form. """
    output = []
    index = 0

    for (distance_back, length, new_character) in compressed_data:
        for i in range(index-distance_back, index-distance_back+length):
            output.append(output[i])
        if new_character != '$':
            output.append(new_character)
        index = index + length + 1

    return output
