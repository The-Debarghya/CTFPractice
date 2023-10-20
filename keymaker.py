from Crypto.Cipher import AES

data = open("The-Keymaker.jpg", "rb").read()

def find_iv():
    begin = data.find(b'\xFF\xC0')
    iv_len = 16
    # skip marker and length
    end = begin + 4 + iv_len
    SOF0 = data[begin+4:end]
    return SOF0

def find_key():
    begin = data.find(b'\xFF\xDA')
    key_len = 32
    # skip marker
    end = begin + 2 + key_len
    SOS = data[begin+2:end]
    return SOS

key = find_key()
iv = find_iv()
#hint b'openssl enc -d -aes-256-cbc -iv SOF0 -K SOS -in flag.enc -out flag -base64\n\niv does not include the marker or length of SOF0\n\nkey does not include the S0S marker\n\n'
cipher =  b"\x9akZHx@\xb0\xafi,\xc7\xa9\xc8P\xe5\xdf\xb5\x13]\x04\xf4\x08\xc9mfN\xfe\xe0\xa6\x9a\xd6\xcb\xe8\xe6\xfa\x9b\xe8\x9b\x9c\xcdJ\x90\x18RX\x8b'\x18"
aes = AES.new(key, mode=AES.MODE_CBC, IV=iv)
dec = aes.decrypt(cipher)
print('flag', dec)
