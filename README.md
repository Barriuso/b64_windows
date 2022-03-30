# Base64 as Windows

Encoded file as Windows likes Base64(UTF-16LE). This is designed to encode code or command and then be executed.
````
$ python b64_windows.py whoami
powershell -enc dwBoAG8AYQBtAGkA

$ cat my_file
whoami

$ python b64_windows.py -f my_file -o my_file_b64

$ cat my_file_b64
powershell -enc dwBoAG8AYQBtAGkA

````
