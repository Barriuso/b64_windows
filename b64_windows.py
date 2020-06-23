#Convertir archivos a base64 con el formato de windows
import readline
import base64
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Convert file to base64 as Windows likes')
    parser.add_argument('-o', '--output', dest='output', type=str, required=False, help='Output File')
    parser.add_argument('-f', '--file', dest='infile', type=str, required=False, help='File to convert')
    return parser.parse_args()

def load_shellcode(filePath):
    try:
        with open(filePath, 'r') as file:
            file_shellcode = file.read()
            file_shellcode = file_shellcode.strip()
            #print ("Fichero ",file_shellcode)
            return file_shellcode
    except:
        print((" [!] WARNING: path not found"))
        return None

    if len(file_shellcode) == 0:
        print(" [!] WARNING: File is empty", )
        return None

if __name__ == '__main__':
    args = get_args()
    if (args.infile == None):
        readline.set_completer_delims(' \t\n=')
        readline.parse_and_bind("tab: complete")
        filePath = input("Tab complete a file: ")
        payload = load_shellcode(filePath)
    else:
        load_shellcode(args.infile)

    output = "powershell -enc " + base64.b64encode(payload.encode('utf16')[2:]).decode()
    if (args.output == None):
        print (output)
    else:
        try:
            with open(args.ouput, 'a') as file:
                file.write(output)

        except:
            print((" [!] WARNING: Error with the outpout file"))
