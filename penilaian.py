import texttable as tt
import getpass


def menu():
    print ("=======================================")
    print ("\n\t---Pilihan---")
    print ("\t1. Penilaian Mahasiswa")
    print ("\t2. Pembayaran Mahasiswa")

    pilih = input ("\n\tSilahkan Pilih : ")
    if pilih == "1" :
        nilai_mahasiswa ()
    elif pilih == "2" :
        pembayaran()
    else :
        exit
    tanya()

def tanya ():
    tanya = input ("\n\tKembali ke Menu (y/t)?")
    if tanya == "y" :
        menu ()
    if tanya == "t" :
        exit
    else :
        print ("\n\tSalah Input.......!!!")

def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []

    x = [[]]

    jawab = "y"

    tab = tt.Texttable()

    while (jawab == 'y'):
        nama.append(input("Masukkan Nama: "))
        nim.append(input("Masukkan Nim: "))
        tugas = int(input("Nilai Tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("Nilai UTS: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("Nilai UAS: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("Tambah data [y/n]?  ")


    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['l','l','l','r','r','r','r'])
    tab.header(['No','Nama','Nim','Nilai Tugas', 'Nilai UTS', 'Nilai UAS','Nilai Akhir'])
    print (tab.draw())

nilai_mahasiswa()
