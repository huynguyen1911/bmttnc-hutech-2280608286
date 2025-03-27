from Crypto.Hash import SHA3_256

def sha3(messsage):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(messsage)
    return sha3_hash.digest()

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hash_text = sha3(text)
    
    print("Chuỗi văn bản đã nhập: ", text.decode('utf-8'))
    print("Giá trị hash SHA-3 của chuỗi văn bản là: ", hash_text.hex())
    
if __name__ == '__main__':
    main()