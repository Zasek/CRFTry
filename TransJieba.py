#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILE = "D:\\Gdesign\\jiebares.utf8"
OUTPUT_FILE = "D:\\Gdesign\\jieba_fin.utf8"


def translate():
    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILE, 'w', 'utf-8')

    for line in input_data.readlines():

        for word in line.strip():
            word = word.strip()
            if word != '/':
                output_data.write(word)
            else:
                output_data.write("  ")

        output_data.write("\n")

    input_data.close()
    output_data.close()

if __name__ == '__main__':
    translate()
