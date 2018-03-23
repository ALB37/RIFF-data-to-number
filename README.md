# RIFF-data-to-number

## About

The purpose of this python script is to return the first 128 values of the data portion of a given wav file. It will write the output to a new txt file. The form of the output is as a list, which can be used as data for various purposes. I built this to automate the creation of lists for input into a neural network for a project on which I am working. The output will thus be between 0 and 1. 

## Getting Started

To get started, fork/clone this repository. This was designed for use on a unix based environment, with a current version of Python 3 installed. To call this script from anywhere, 

`chmod -x riff-parse.py` 

and

`export PATH=$PATH:path/to/project/directory`

To run the script, it is expecting two command line arguments, the first of which is the wav file to read, and the second of which is the output file.

E.g.:

`riff-parse.py sample.wav output.txt`

## Credit

Created by Andrew Bloom