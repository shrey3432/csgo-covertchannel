import binascii
#reading the text file
f = open("/*.log", "r")
message = ""
message2 = ""
count = 0
covert = ""



while True:
    overt_msg = f.readline()
    if not overt_msg:
        break
    if "TERRORIST" in  overt_msg:
        if "killed" in overt_msg:
            message2 = overt_msg.split("\"")
            message = message2[4]
            print(message)
            if "64] with" in message:
                covert += "0"
            else:
                covert += "1"

print(covert)



f.close()

