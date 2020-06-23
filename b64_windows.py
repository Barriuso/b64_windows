#!/usr/bin/env python3
#Convertir archivos a base64 con el formato de windows
import readline
import base64
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(description='Convert file to base64 as Windows likes')
    parser.add_argument('-o', '--output', dest='output', type=str, required=False, help='Output File')
    parser.add_argument('-f', '--file', dest='file', type=str, required=False, help='File to convert')
    return parser.parse_args()

def load_file(filePath):
    try:
        with open(filePath, 'r') as file:
            file = file.read()
            file = file.strip()
            #print ("Fichero ",file)
            return file
    except:
        print((" [!] WARNING: path not found"))
        exit()

    if len(file) == 0:
        print(" [!] WARNING: File is empty", )
        exit()

if __name__ == '__main__':

    if len(sys.argv) == 2:
        output = "powershell -enc " + base64.b64encode(sys.argv[1].encode('utf16')[2:]).decode()
        print (output)
        exit()
    else:
        args = get_args()

    if (args.file == None):
        readline.set_completer_delims(' \t\n=')
        readline.parse_and_bind("tab: complete")
        filePath = input("Tab complete a file: ")
        payload = load_file(filePath)
    else:
        payload = load_file(args.file)

    if (args.output == None):
        output = "powershell -enc " + base64.b64encode(payload.encode('utf16')[2:]).decode()
        print (output)
    else:
        output = "powershell -enc " + base64.b64encode(payload.encode('utf16')[2:]).decode()
        try:
            with open(args.output, 'w') as file:
                file.write(output)

        except:
            print((" [!] WARNING: Error with the outpout file"))
