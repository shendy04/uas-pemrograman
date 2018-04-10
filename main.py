import getpass

def login():
    print('==================================================')
    print('\n\t---Pilihan Utama---')
    print('\n\t1. Penilaian Mahasiswa')
    print('\n\t2. Pembayaran Mahasiswa')
    print('\n\t3. Kalkulator')

    pilih = input('\n\tSilahkan Pilih : ')
    if pilih == '1':
        from perhitungan.penilaian import tt
    elif pilih == '2':
        from perhitungan.pembayaran import pembayaran
    elif pilih == '3':
        from perhitungan.kalkulator import kalkulator
    else :
        exit
    tanya()

def tanya():
    tanya=input('\n\tKembali ke Pilihan Utama (y/n)? ')
    if tanya == 'y':
        login()
    elif tanya == 'n':
        exit
    else :
        print ('Pilihan yang Anda Masukkan Tidak Tersedia!')

user = input('\nUsername : ')
password = getpass.getpass()
print ('===================================================')

if user == 'sendi' and password == '112233':
    login()

else :
    print ('Maaf Username atau Password Salah!')
