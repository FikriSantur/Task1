from dosylari_hashle import dosya_hashle
def dosya_bol(dosya):
    boyut=1*1024*1024 # 1mb lık dosya büyüklüğü
    with open(dosya,"rb") as f:
        count=0
        while True:
            parca_dosya_icerigi = f.read(boyut) #sürekli boyut kadar veri okuyarak sıradaki boyutluk veriye geçer
            if not parca_dosya_icerigi: # okunacak içerik yoksa döngüden çıkar
                break
            else:
                count+=1
                parca_dosya_adi = f"{dosya}_part{count}" #yeni olusturulan dosya adı için format
                with open(parca_dosya_adi,"wb") as fp: #her dönfüde olusturulan dosya yazma binary modunda create edilir 
                    fp.write(parca_dosya_icerigi) # create edilen bu dosyaya 1 mb lık parça içeriği yazılır
                dosya_hashle(parca_dosya_adi) # oluşan her 1mb lık parça haslenmek için fonksiyona gönderilir 
                print(f"Created {parca_dosya_adi}") # oluşturulan 1mb lık dosya uzantısı ekrana bastılır 
        

