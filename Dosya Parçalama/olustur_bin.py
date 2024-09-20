import os 

def olustur_100mb():
    toplam_boyut = 100*1024*1024 #100 mb lk bir dosya boyutu

    parca_boyut=1024*1024 #1 mb lık dosya bouyutu

    dosya_adi="mb100.bin" 

    dosya_yolu =os.path.join(os.getcwd(),dosya_adi) # mb100.bin adlı dosyanın dşnamik olarak dosya yolunu tuttum.
    with open ("mb100.bin","wb",) as f: # mb100 isimli dosyayı yazma ve binary modda açtım.
        for _ in range(toplam_boyut//parca_boyut): # toplam parça sayısı / parça boyutu yaparak oluşacak dosya sayını belirttim.
            byte_icerigi=os.urandom(parca_boyut) # her seferinde os den rparça boyutu kadar random binary değerler alarak bunları tuttum
            f.write(byte_icerigi)  #tuttuğum bu rastgele binary içeriklerini oluşan parça dosyaya yazdım
    return dosya_yolu

