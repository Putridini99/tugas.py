#rumus enkripsi = (n - key) % 26
#rumus dekripsi = (n + key) % 26
#n = merupakan urutan dari abjad yang diinput 
#key = merupakan kunci dekripsi atau enkripsi
#26 =merupakan jumlah dari seluruh abjad
print(" Progam Enkripsi Caesar ")
abjad = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

#fungsi enkripsi dengan parameter abjad
def enkripsi(abjad):
    kalimat = input("Kalimat yang di inginkan  : ") 
    key = int(input("Key : ")) 

    kalimat = kalimat.upper() 
    hasil = '' 

    for char in kalimat: 
      if char in abjad: 
        n = abjad.index(char)
        encrypt = (n - key) % 26 
        convert = abjad[encrypt] 
        hasil = hasil + convert 
      else:
          hasil = hasil + ' ' 

    print(f"Hasil : {hasil}") 

#fungsi dekripsi dengan parameter abjad
def dekripsi(abjad):
    kalimat = input("Kalimat yang di inginkan : ")  
    key = int(input("Key : ")) 

    kalimat = kalimat.upper() 
    hasil = '' 

    for char in kalimat: 
        if char in abjad: 
          n = abjad.index(char) 
          encrypt = (n + key) % 26 
          convert = abjad[encrypt] 
          hasil = hasil + convert 
        else:
            hasil = hasil + ' '  

    print(f"Hasil : {hasil}") 

#menampilkan menu
pilihan = 'y' 

while (pilihan == 'y'):
  print("Pilihan Menu : ")
  print("1. Enkripsi Data")
  print("2. Dekripsi Data")

  menu = input("Menu yang dipilih : ")

  if menu == '1':
    enkripsi(abjad) 
  elif menu == '2':
    dekripsi(abjad) 
    break 
  else:
    print("Menu tidak ditemukan") 

  pilihan = input("Apakah anda ingin melanjutkan ? (y/n) : ") 
