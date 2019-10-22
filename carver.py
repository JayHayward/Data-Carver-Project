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
    find_carves_png(data)
    find_carves_pdf(data)


def find_carves_jpg(data):  # carves = files I'm extracting
    # will likely find a lot of false positives due to frequency of magic number pattern
    ctype = 'JPG'  # type of carved file
    clen = 0  # length of carved file
    name_c = 1  # name given to new carved file
    sof = data.find(jpg_mark[0])  #start of file
    while sof != -1:
        eof = data.find(jpg_mark[1], sof + 1)  # must find the eof at a position AFTER the sof
        while eof != -1:  # check the current sof with every eof
            carve = data[sof:eof]  # range of bytes in which the file is found
            with open("./hayward/" + str(name_c) + ".jpg", 'wb') as name_object:  #write files to folder
                name_object.write(carve)

            with open("./hayward/hashes.txt", 'a+') as hash_object:  # write hashes to file
                hash_object.write(str(name_c) + ".jpg" + ": " + md5(carve).hexdigest() + "\n")

            name_c += 1
            clen = eof - sof
            s_offset = hex(sof)  # take the hex value of the decimal sof offset
            e_offset = hex(eof)  # take the hex value of the decimal eof offset
            print("found a {} file at offsets {} and {} with size of {} bytes".format(ctype,s_offset,e_offset,clen))
            eof = data.find(jpg_mark[1], eof + 1)  # update to next eof
        sof = data.find(jpg_mark[0], sof + 1)  # update to next sof


def find_carves_png(data):  # carves = files I'm extracting
    ctype = 'PNG'  # type of carved file
    clen = 0  # length of carved file
    name_c = 1  # name given to new carved file
    sof = data.find(png_mark[0])
    while sof != -1:
        eof = data.find(png_mark[1], sof + 1)  # must find the eof at a position AFTER the sof
        while eof != -1:  # check the current sof with every eof
            carve = data[sof:eof]  # range of bytes in which the file is found
            with open("./hayward/" + str(name_c) + ".png", 'wb') as name_object:  #write files to folder
                name_object.write(carve)

            with open("./hayward/hashes.txt", 'a+') as hash_object:  # write hashes to file
                hash_object.write(str(name_c) + ".png" + ": " + md5(carve).hexdigest() + "\n")

            name_c += 1
            clen = eof - sof
            s_offset = hex(sof)  # take the hex value of the decimal sof offset
            e_offset = hex(eof)  # take the hex value of the decimal eof offset
            print("found a {} file at offsets {} and {} with size of {} bytes".format(ctype,s_offset,e_offset,clen))
            eof = data.find(png_mark[1], eof + 1)  # update to next eof
        sof = data.find(png_mark[0], sof + 1)  # update to next sof


def find_carves_pdf(data):  # carves = files I'm extracting
    ctype = 'PDF'  # type of carved file
    clen = 0  # length of carved file
    name_c = 1  # name given to new carved file
    sof = data.find(pdf_mark[0])
    while sof != -1:
        eof = data.find(pdf_mark[1], sof + 1)  # must find the eof at a position AFTER the sof
        while eof != -1:  # check the current sof with every eof
            carve = data[sof:eof]  # range of bytes in which the file is found
            with open("./hayward/" + str(name_c) + ".pdf", 'wb') as name_object:  #write files to folder
                name_object.write(carve)

            with open("./hayward/hashes.txt", 'a+') as hash_object:  # write hashes to file
                hash_object.write(str(name_c) + ".pdf" + ": " + md5(carve).hexdigest() + "\n")

            name_c += 1
            clen = eof - sof
            s_offset = hex(sof)  # take the hex value of the decimal sof offset
            e_offset = hex(eof)  # take the hex value of the decimal eof offset
            print("found a {} file at offsets {} and {} with size of {} bytes".format(ctype,s_offset,e_offset,clen))
            eof = data.find(pdf_mark[1], eof + 1)  # update to next eof
        sof = data.find(pdf_mark[0], sof + 1)  # update to next sof


if __name__ == "__main__":
    main()
