import itertools
import string
# Password Cracking Function by Resul Ucar
# To decrease the scope of the brute force and crack faster
# you can use string.ascii_letters 
charset = string.ascii_letters + string.digits + string.punctuation

#Enter desired password to crack
pas = "aabb"

#iterates through the charset until the test word matches the password
for pwd in itertools.product(charset, repeat=4):
    test = ''.join(pwd)
    print("%s" % (test))
    if test == pas:
        print("Password Found!: %s" % (test))
        break