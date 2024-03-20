#in progress


digital = int(input("Enter Digital to conv \n"))
type = input("Enter type digital -\n DEC,\n BIN \n HEX\n")



out = ""
#conv from bin
if type == "bin" or type == "BIN":
    pass

#conv from dex
elif type == "dec" or type == "DEC":
    hex_digital = digital 
    ## dec to bin
    while digital >= 1:
        out = out + str(digital%2)
        digital = int(digital/2)
   
    print(out[::-1])

    ## dec to hex
    while len(out)%4 == True:
        out = out + "0"
    out = out + "00"
    print(out)

#conv from hex
elif type == "hex" or type == "HEX":
    print("hex")
