#!/usr/bin/python3

import sys, getopt
from secretpy import alphabets


def usage():
    print("Usage:")
    print(sys.argv[0] + "[-h|--help] [(-i |--input=)<file>] [(-o |--output=)<file>] [(-s |--size=)<size>] [(-l |--lang=)(en|de)]")

def readfile(filename):
    output = None
    try:
        with open(filename) as f:
            output = f.read().splitlines()
    except IOError:
        print("IOError!!!")
        usage()
        sys.exit(3)
    return output

g_alphabet = alphabets.ENGLISH

def in_alphabet(variable):
    if (variable in g_alphabet):
        return True
    else:
        return False

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:s:l:", ["help", "input=", "output=", "size=", "lang="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    input_txt_file = 'input.txt'
    output_file = 'output.txt'
    sbstr_size = 2
    global g_alphabet
    for option, op_value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ('-o', '--output'):
            output_file = op_value
        elif option in ('-i', '--input'):
            input_txt_file = op_value
        elif option in ('-s', '--size'):
            sbstr_size = int(op_value)
        elif option in ('-l', '--lang'):
            if op_value == 'de':
                g_alphabet = alphabets.GERMAN
            elif op_value == 'en':
                g_alphabet = alphabets.ENGLISH
        else:
            assert False, "Unhandled option!"
    # finding frequencies from text file
    text = readfile(input_txt_file)
    freq = {}
    for line in text:
        line = line.lower()
        line = "".join(filter(in_alphabet, line))
        for i in range(len(line)-sbstr_size+1):
            sbstr = line[i:i+sbstr_size]
            if sbstr in freq:
                freq[sbstr] += 1
            else:
                freq[sbstr] = 1
    print(freq)
    file_out = open(output_file, encoding='utf-8', mode='w')
    for key in sorted(freq, key=freq.get, reverse=True):
        file_out.write(key + " " + str(freq[key]) + "\n")
    file_out.close()
    

if __name__ == "__main__":
    main()
