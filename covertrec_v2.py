import binascii
#reading the text file
f = open("/Users/shreyrandive/Downloads/CSGO_proofofconcept/project_logs/l192_168_001_151_27015_202110301246_001.txt", "r")

message2 = ""

while True:
    overt_msg = f.readline()
    if not overt_msg:
        break
    if "TERRORIST" in  overt_msg:
        if "killed" in overt_msg:
            if "<T>" in overt_msg:
                message2 += "0"
            if "<CT>" in overt_msg:
                message2 += "1"


print(message2)


f.close()

