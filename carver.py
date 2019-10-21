# Jay Hayward
# CYBER 5830-013
# Project 2

from hashlib import md5
import sys
import binascii
import os

jpg_mark = (b'\xFF\xD8', b'\xFF\xD9')  # sof and eof markers for jpg
png_mark = (b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A', b'\x49\x45\x4E\x44\xAE\x42\x60\x82')  # sof and eof markers for png
pdf_mark = (b'\x25\x50\x44\x46', b'\x25\x25\x45\x4F\x46')  # sof and eof markers for pdf

def main():

    infile = sys.argv[1]
    # infile = './carve.lab'
    with open(infile, 'rb') as f_obj:  # open stream in binary to read, put in object
        data = f_obj.read()

    # os.mkdir("hayward")  # make directory to put finished carved data

    #test data dump
    print(data[:50])

    #test offset find
    print(hex(data.find(jpg_mark[0])))
    print(hex(data.find(jpg_mark[1])))


if __name__ == "__main__":
    main()
