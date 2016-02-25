#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

#modify file path here

INPUT_FILE = "D:\\Gdesign\\pku_training.utf8"
OUTPUT_FILE = "D:\\Gdesign\\pku_tagged.utf8"


def word_tagging():

    input_data = codecs.open(INPUT_FILE, 'r', 'utf-8')
    output_data = codecs.open(OUTPUT_FILE, 'w', 'utf-8')

    for line in input_data.readlines():
        words = line.strip().split()
        for word in words:
            length = len(word)
            if length == 1:
                output_data.write(word+'\tS\n')
            else:
                output_data.write(word[0]+'\tB\n')
                for char in word[1:length-1]:
                    output_data.write(char+'\tM\n')
                output_data.write(word[length-1]+'\tE\n')
        output_data.write("\n")

    output_data.close()
    input_data.close()

if __name__ == '__main__':

    print("Start Processing...")
    word_tagging()
    print("Process Complete!")
