def pembayaran () :
    print ("\n========================================")
    nama = input ("\nMasukkan Nama : ")
    nim = input ("\nMasukkan NIM : ")
    semester = input ("\nMasukkan Semester : ")
    print ("\n\t---Pilihan Pembayaran---")
    print ("\t1. Pembayaran SPP")
    print ("\t2. Pembayaran UTS")
    print ("\t3. Pembayaran UAS")
    print ("\t4. Pembayaran SPP & UTS")
    print ("\t5. Pembayaran SPP & UAS")
    pilih = input ("\n\tSilahkan Pilih : ")
    if pilih == "1" :
        spp ()
    elif pilih == "2" :
        uts ()
    elif pilih == "3" :
        uas ()
    elif pilih == "4" :
        spp_uts ()
    elif pilih == "5" :
        spp_uas ()
    else :
        exit
        tanya ()
def spp() :
    bulan = int(input("\n\tjumlah bulan yang dibayar = "))
    bulan = float(bulan)
    total = 1000000 * bulan
    print ("=============================================")
    print ("\ttotal yang harus dibayar Rp. 1000000 *" ,bulan, " = Rp. ", total)

def uas() :
    matkul_uas = int(input("\n\tjumlah mata kuliah = "))
    matkul_uas = float(matkul_uas)
    total = 100000 * matkul_uas
    print ("=============================================")
    print ("\ttotal yang harus dibayar Rp. 100000 * ",matkul_uas," = Rp. ",total)

def uts():
    matkul_uts = int(input("\n\tjumlah mata kuliah = "))
    matkul_uts = float(matkul_uts)
    total = 100000 * matkul_uts
    print ("============================================")
    print ("\ttotal yang harus dibayar Rp. 100000 * ",matkul_uts," = Rp. ",total)

def spp_uas() :
    bulan = int(input("\n\tjumlah bulan yang dibayar = "))
    matkul = int(input("\n\jumlah mata kuliah = "))
    matkul =float(matkul)
    bulan =float(bulan)
    total_spp = 1000000 * bulan
    byr_uas = 100000 * matkul
    total = total_spp + byr_uas + 10000
    print ("\ttotal bayar spp Rp. 1000000 * ",bulan," = Rp. ", total_spp)
    print ("\ttotal bayar uas Rp. 10000 * ",matkul," = Rp. ", byr_uas)
    print ("\tbiaya tambahan server sebesar Rp. 10000")
    print ("===========================================")
    print ("\ttotal yang harus dibayar", total)

def spp_uts() :
    bulan = int(input("\n\tjumlah bulan yang dibayar = "))
    matkul = int(input("\n\tjumlah mata kuliah = "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 1000000 * bulan
    byr_uts = 100000 * matkul
    total = total_spp + byr_uts + 10000
    print ("\ttotal bayar spp Rp. 1000000 * ",bulan," = Rp. ", total_spp)
    print ("\ttotal bayar uts Rp. 100000 * ",matkul," = Rp. ", byr_uts)
    print ("\tbiaya tambahan server sebesar Rp. 10000")
    print ("==========================================")
    print ("\ttotal yang harus dibayar", total)

pembayaran()
