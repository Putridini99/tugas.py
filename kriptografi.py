print("......................+ Progam Enkripsi Caesar +......................")
abjad = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#fungsi enkripsi dengan parameter abjad
def enkripsi(abjad):
    str = input("String : ")
    key = int(input("Key : "))

    str = str.upper()
    hasil = ''

    for char in str:
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
    str = input("String Enkripsi : ")
    key = int(input("Key : "))

    str = str.upper()
    hasil = ''

    for char in str:
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
  print("3. Exit")

  menu = input("Menu yang tersedia : ")
  print("...................................")

  if menu == '1':
    print("Menu Enkripsi Data")
    enkripsi(abjad)
  elif menu == '2':
    print("Menu Dekripsi Data")
    dekripsi(abjad)
  elif menu == '3':
    print("Progam Selesai, terima kasih")
    break
  else:
    print("Menu tidak ditemukan")

  print("...................................")
  pilihan = input("Apakah anda ingin melanjutkan ? (y/n) : ")
  print("...................................")
