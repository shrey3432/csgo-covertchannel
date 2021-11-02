import binascii
#reading the text file
f = open("/Users/shreyrandive/Downloads/CSGO_proofofconcept/project_logs/l192_168_001_151_27015_202110301233_001.log", "r")
g = open("/Users/shreyrandive/Downloads/CSGO_proofofconcept/project_logs/l192_168_001_151_27015_202110301246_001.txt", "w")
message = ""
message2 = ""
count = 0

secret = "0110100001100101011011000110110001101111"


p =len(secret)

while True:
    overt_msg = f.readline()
    if not overt_msg:
        break
    if "TERRORIST" in  overt_msg:
        if "killed" in overt_msg:
            message2 = overt_msg.split("\"")
            if count >= p:
                break
            if secret[count] == "0":
                message2[3]=message2[3][:-4]+"<T>"
            message2 = ' '.join(message2)
            count += 1
            g.write(message2)

    else:
        g.write(overt_msg)


if p > count:
    print("Encoding not possible")
else:
    print("Encoded Message Successfully")

g.close()
f.close()

