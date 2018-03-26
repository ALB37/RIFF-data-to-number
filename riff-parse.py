#!/usr/bin/env python
import sys

WAV_HEADER = 44
SIXTEEN_BIT_SAMPLE = 2
NEGATIVE_OFFSET = 32768
MAX_VALUE = 65535

with open(sys.argv[1], "rb") as buf:
    header = buf.read(WAV_HEADER)
    string_to_write = "["
    i = 0
    while (i < 128):
        sample = buf.read(SIXTEEN_BIT_SAMPLE)
        current_sample = int.from_bytes(sample, byteorder='little', signed=True)
        current_sample += NEGATIVE_OFFSET
        current_sample /= MAX_VALUE
        string_to_write += str(current_sample)
        string_to_write += ", "
        i += 1

    string_to_write = string_to_write[:-2]
    string_to_write += "]"

with open(sys.argv[2], "w") as output:
    output.write(string_to_write)