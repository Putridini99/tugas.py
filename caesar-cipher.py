#rumus enkripsi = (n - key) % 26
#rumus dekripsi = (n + key) % 26
#n = merupakan urutan dari abjad yang diinput 
#key = merupakan kunci dekripsi atau enkripsi
#26 =merupakan jumlah dari seluruh abjad
print(" Progam Enkripsi Caesar ")
abjad = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
#abjad berfungsi untuk menampung nilai abjad yang ada

#fungsi enkripsi dengan parameter abjad
def enkripsi(abjad):
    kalimat = input("Kalimat : ") #input kalimat yang akan di enkripsi
    key = int(input("Key : ")) #kunci untuk pergeseran abjad (enkripsi)

    kalimat = kalimat.upper() #kalimat di konversi ke huruf besar semua
    hasil = '' #membuat variable string untuk memuat hasil enkripsi

    for char in kalimat: #membuat perulangan untuk mengenkripsi kalimat
      if char in abjad: #abjad kalimat dipecah 1 1 dan di cek apakah terdapat dalam value abjad
        n = abjad.index(char) #jika ada maka nilai index dariabjad yang ditemukan disimpan dalam variable n
        encrypt = (n - key) % 26 #rumus enkripsi
        convert = abjad[encrypt] #konversi nilai string ke hasil enkripsi
        hasil = hasil + convert #membuat variable baru yang memuat hasil enkripsi
      else:
          hasil = hasil + ' ' #jika karakter yang dimasukkan bukan berasal dari abjad A - Z maka akan menjadi spasi

    print(f"Hasil : {hasil}") #hasil dari perulangan untuk enkripsi kalimat di tampilkan 

#fungsi dekripsi dengan parameter abjad
def dekripsi(abjad):
    kalimat = input("Kalimat Enkripsi : ")  #input kalimat yang akan di dekripsi
    key = int(input("Key : ")) #kunci untuk pergeseran abjad (dekripsi)

    kalimat = kalimat.upper() #kalimat di konversi ke huruf besar semua
    hasil = '' #membuat variable string untuk memuat hasil enkripsi

    for char in kalimat: #membuat perulangan untuk mengenkripsi kalimat
        if char in abjad: #abjad kalimat dipecah 1 1 dan di cek apakah terdapat dalam value abjad
          n = abjad.index(char) #jika ada maka nilai index dariabjad yang ditemukan disimpan dalam variable n
          encrypt = (n + key) % 26 #rumus dekripsi
          convert = abjad[encrypt] #konversi nilai string ke hasil dekripsi
          hasil = hasil + convert #membuat variable baru yang memuat hasil enkripsi
        else:
            hasil = hasil + ' '  #jika karakter yang dimasukkan bukan berasal dari abjad A - Z maka akan menjadi spasi

    print(f"Hasil : {hasil}") #hasil dari perulangan untuk enkripsi kalimat di tampilkan 

#menampilkan menu
pilihan = 'y' 

while (pilihan == 'y'): # membuat pilihan untuk melakukan enkripsi atau dekripsi
  print("Pilihan Menu : ")
  print("1. Enkripsi Data")
  print("2. Dekripsi Data")

  menu = input("Menu yang tersedia : ")

  if menu == '1':
    print("Menu Enkripsi Data") # memasukkan kalimat yang akan di enkripsi
    enkripsi(abjad) # memanggil fungsi Caesar_cipher untuk mengenkripsi kalimat
  elif menu == '2':
    print("Menu Dekripsi Data")  # memasukkan kalimat yang akan di enkripsi
    dekripsi(abjad) # memanggil fungsi Caesar_cipher untuk mendekripsi kalimat
    break 
  else:
    print("Menu tidak ditemukan") #jika memilih menu yang tidak ada di pilihan maka akan ditampilkan "menu tidak ditemukan" 

  pilihan = input("Apakah anda ingin melanjutkan ? (y/n) : ") #pilihan apakah ingin melanjutkan atau tidak,jika iya klik y jika tidak klik n
