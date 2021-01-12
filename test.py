from AES import AES_128, make_blocks, block_check

key = bytearray.fromhex("00112233445566778899aabbccddeeff")#.decode('ascii')
print(key)
#plaintext = "This is a super secret piece of infomation"

file  = input("Enter the file name: ")

aes = AES_128()
aes.key = key

try:
    if_ = open(file,'rb')
    data = if_.read()
    data = bytearray(data)
    if_.close()
except:
    print("Exception occured")

of = open("encrypted_"+file, 'wb')

data = make_blocks(block_check(data), 16)
#print(data)


print(len(data))
for i in data:
    #of.write(aes.encrypt(i))
    enc = aes.encrypt(i)
    of.write(bytearray(enc))
    #for d in enc:
    #print(d)
    #    of.write(bytearray(d))

of.close()

if_ = open("encrypted_"+file, 'rb')
of = open("decrypted_"+file, 'wb')

data = make_blocks(block_check(bytearray(if_.read())), 16)

for i in data[0:-1]:
    enc = aes.decrypt(i)

    of.write(bytearray(enc))

last = aes.decrypt(data[-1])
of.write(bytearray(last[0:last.index(126)]))

if_.close()
of.close()
