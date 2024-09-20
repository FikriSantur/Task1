import os
import gnupg

def sifrele_ve_coz(yol):
    # GPG ev dizinini belirleyin
    gpg_home = os.path.expanduser('~/.gnupg')

    # Eğer gpg_home dizini yoksa oluşturun
    if not os.path.exists(gpg_home):
        os.makedirs(gpg_home)

    # GPG binary yolunu belirtin
    gpg_binary = r'C:/Program Files (x86)/GnuPG/bin/gpg.exe'  # GPG binary yolunu burada belirtin

    # GPG nesnesini oluşturun
    gpg = gnupg.GPG(gnupghome=gpg_home, gpgbinary=gpg_binary)
    gpg.encoding = 'utf-8'

    # Yeni bir anahtar çifti oluşturun (eğer gerekli ise)
    input_data = gpg.gen_key_input(
        name_email='umutsantur51@gmail.com',  # Anahtarın e-posta adresi
        passphrase='mypassphrase',            # Anahtar için parola
        key_type='RSA',                       # Anahtar türü
        key_length=1024                       # Anahtar uzunluğu
    )

    # Anahtar çiftini oluşturun
    key = gpg.gen_key(input_data)

    # Genel anahtarı dışa aktarın ve bir dosyaya yazın
    public_key = gpg.export_keys(key.fingerprint)
    with open("public.txt", "w") as pf:
        pf.write(public_key)

    # Özel anahtarı dışa aktarın ve bir dosyaya yazın
    private_key = gpg.export_keys(key.fingerprint, True, passphrase="mypassphrase")
    with open("private.txt", "w") as prf:
        prf.write(private_key)

    # Anahtar oluşturma işleminin başarılı olduğunu belirtin
    print(f"Anahtar başarıyla oluşturuldu: {key}")

    # Giriş dosyasının yolunu belirleyin
    input_file = os.path.expanduser(yol)
    # Şifreli dosyanın yolunu belirleyin
    encrypted_file = os.path.expanduser('C:/Users/UmutFS/Desktop/sfirelenmis_mb100.bin')
    # Çözülmüş dosyanın yolunu belirleyin
    decrypted_file = os.path.expanduser('C:/Users/UmutFS/Desktop/desifrelenmis_mb100.bin')

    # Dosyayı oku ve şifrele
    with open(input_file, 'rb') as f:
        status = gpg.encrypt_file(
            f, recipients=['umutsantur51@gmail.com'], output=encrypted_file
        )

    # Şifreli dosyanın yolu
    print('Encrypted file:', encrypted_file)

    # Kullanıcıdan şifreyi al
    kullanici_girdisi = input("Dosya kitlendi, private key yolunu gir: ")

    # Şifreli dosyayı çöz
    with open(encrypted_file, 'rb') as f:
        status = gpg.decrypt_file(
            f, passphrase="mypassphrase", output=decrypted_file
        )
    
    # Şifre çözme işleminin sonucunu kontrol edin
    if status.ok:
        print('Dosya başarıyla çözüldü.')
        print('Decrypted file:', decrypted_file)
        return True
    else:
        print('Şifre çözme başarısız oldu.')
        return False
