import zipfile
import sys

# might need a rework to more clearly convey what I want
usage_message = "Usage: zipcracker.py FILE.zip WORDLIST.txt"
if len(sys.argv) < 2:
    sys.exit(usage_message)

file_is_zip = sys.argv[1][-4:] == '.zip'
wordlist_is_txt = sys.argv[2][-4:] == '.txt'
if not file_is_zip or not wordlist_is_txt:
    sys.exit(usage_message)

def password_crack(zip_file, wordlist):
    with open(wordlist, 'rb') as file:
        line_number = 0
        for line in file:
            for word in line.split():
                line_number += 1
                try:
                    zip_object = zipfile.ZipFile(zip_file)
                    zip_object.extractall(pwd=word)
                    print("Password found at line", line_number)
                    print("Password is", word.decode())
                    return True
                except:
                    continue

    return False

zip_file = sys.argv[1]
wordlist = sys.argv[2]

if not password_crack(zip_file, wordlist):
    print("Password not found in file")
