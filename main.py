import string
from barcode.writer import ImageWriter
from barcode import EAN13
from UC3MLogistics import OrderManager

#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3

def encode(word):
    "Encodes a string into the correct format"
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) + shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded

def decode(word):
    "Decodes a string into the correct format"
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) - shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded

def main():
    "Reads the Json file, checks the code and generates an image using the code if it is correct"
    mng = OrderManager()
    res = mng.readproductcodefromJSON("test.json")
    str_res = str(res)
    print(str_res)
    Encode_res = encode(str_res)
    print("Encoded Res "+ Encode_res)
    Decode_res = decode(Encode_res)
    print("Decoded Res: " + Decode_res)
    print("Codew: " + res.PRODUCT_CODE)
    with open("./barcodeEan13.jpg", 'wb') as f:
        iw = ImageWriter()
        EAN13(res.PRODUCT_CODE, writer=iw).write(f)


if __name__ == "__main__":
    main()
