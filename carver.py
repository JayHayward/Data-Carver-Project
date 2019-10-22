# Jay Hayward
# CYBER 5830-013
# Project 2

from hashlib import md5
from _md5 import md5
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

    os.mkdir("hayward")  # make directory to put finished carved data

    find_carves_jpg(data)


def find_carves_jpg(data):  # carves = files I'm extracting
    # will likely find a lot of false positives due to frequency of magic number pattern
    name_c = 1  # name given to new carved file
    sof = data.find(jpg_mark[0])  #start of file
    while sof != -1:
        eof = data.find(jpg_mark[1], sof + 1)  # must find the eof at a position AFTER the sof
        while eof != -1:  # check the current sof with every eof
            carve = data[sof:eof]  # range of bytes in which the file is found
            with open("./hayward/" + str(name_c) + ".jpg", 'wb') as name_object:  #write files to folder
                print('found file')
                name_object.write(carve)

            eof = data.find(jpg_mark[1], eof + 1)  # update to next eof
        sof = data.find(jpg_mark[0], sof + 1)  # update to next sof


if __name__ == "__main__":
    main()
