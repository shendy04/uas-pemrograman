def kalkulator():
    print('\n\t====================================')
    print('\tProgram Kalkulator Sederhana')
    print('\t========================================')
    print('\t1.Penjumlahan')
    print('\t2.pengurangan')
    print('\t3.Pembagian')
    print('\t4.Perkalian')
    print('============================================')
    print('')
    
    pil = input('Masukan pilihan:')
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil=='4':
        kali()
    else:
        print ('Maaf,input yang anda masukan salah')
        print ('Coba ulangi kembali')
        tanya()
def tambah():
    print('1. penjumlahan')
    a= int (input('Masukan nilai x= '))
    b= int (input('Masukan nilai y= '))
    c= a+b
    print ('tx+y=',c)
    tanya ()
def kurang():
    print('2.pengurangan')
    a= int (input('Masukan nilai x= '))
    b= int (input('Masukan nilai y= '))
    c= a-b
    print ('tx-y=',c)
    tanya ()
def bagi ():
    print('3.bagi')
    a= int (input('Masukan nilai x= '))
    b= int (input('Masukan nilai y= '))
    c= a/b
    print ('\tx/y=',c)
    tanya ()
def kali():
    print('4.perkalian')
    a= int (input('Masukan nilai x= '))
    b= int (input('Masukan nilai y= '))
    c=a*b
    print ('\tx*y=',c)
    tanya()

def tanya ():
    tanya = input('\nKembali ke menu kalkulator (y/t)?')
    if tanya== 'y':
         kalkulator()
    elif tanya == 't':
         exit
    else:
        print ('\n\Salah input ,,,,,,,,,,,,,,!!!')

kalkulator()
