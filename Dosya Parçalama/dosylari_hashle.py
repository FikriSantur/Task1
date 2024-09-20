import hashlib

def dosya_hashle(dosya):
    with open(dosya,'rb') as f: # dosya_bölden gelen dosyayı okuma modunda açıyorum
        data = f.read() #içerisindeki verileri okuyup data değişkeninde binary olarak tutoyrum
    # Ayn ıveriyi aşağıda 3 farklı algoritmayla hashliyorum
    hash_md5 = hashlib.md5(data).hexdigest()
    hash_sha256 = hashlib.sha256(data).hexdigest()
    hash_sha512 = hashlib.sha512(data).hexdigest()

    # oluşan bu hashleri türüne göre txt açıp içlerine yazıyorum
    with open('md5.txt','a') as md5_file:
        md5_file.write(f"{hash_md5} {dosya}\n")
    with open('sha256.txt','a') as sha256_file:
        sha256_file.write(f"{hash_sha256} {dosya}\n")
    with open('sh512.txt','a') as sha512_file:
        sha512_file.write(f"{hash_sha512} {dosya}\n")
    