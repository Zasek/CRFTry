#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

INPUT_FILE = "D:\\Gdesign\\pku_test_fin.utf8"
OUTPUT_FILE = "D:\\Gdesign\\pku_test_done.utf8"

def translate():

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILE, 'w', 'utf-8')

    for line in input_data.readlines():

        if len(line) < 4:
            output_data.write('\n')
        else:
            ch_tag = line.strip().split('\t')
            char = ch_tag[0]
            tag = ch_tag[2]

            if tag == 'B':
                output_data.write(' '+char)
            if tag == 'M':
                output_data.write(char)
            if tag == 'E':
                output_data.write(char+' ')
            if tag == 'S':
                output_data.write(' '+char+' ')
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    translate()
