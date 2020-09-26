import csv

#maxarray=100

#Funsgi-F01 Load File
def load() :
    # input nama file
    a=input("Masukkan nama File User: ")
    b=input("Masukkan nama File Daftar Wahana: ")
    c=input("Masukkan nama File Pembelian Tiket: ")
    d=input("Masukkan nama File Penggunaan Tiket: ")
    e=input("Masukkan nama File Kepemilikan Tiket: ")
    f=input("Masukkan nama File Refund: ")
    g=input("Masukkan nama File Kritik dan Saran: ")
    
    #membuka dan membaca file
    DataUser = open(a,"r")
    DataWahana = open(b,"r")
    DataPembelian = open(c,"r")
    DataPenggunaan = open(d,"r")
    DataKepemilikan = open(e,"r")
    DataRefund = open(f,"r")
    DataKritikSaran = open(g,"r")
    DataKehilangan = open("kehilangan.csv", 'r')
    
    readerUser = csv.reader(DataUser,delimiter=",")
    readerWahana = csv.reader(DataWahana,delimiter=",")
    readerPembelian = csv.reader(DataPembelian,delimiter=",")
    readerPenggunaan = csv.reader(DataPenggunaan,delimiter=",")
    readerKepemilikan = csv.reader(DataKepemilikan,delimiter=",")
    readerRefund = csv.reader(DataRefund,delimiter=",")
    readerKritikSaran = csv.reader(DataKritikSaran,delimiter=",")
    readerKehilangan = csv.reader(DataKehilangan,delimiter=",")
    
    #mencetak 8 jenis array
    arrayUser = [["" for j in range(8)] for i in range (100)]
    i = 0
    for row in readerUser:
        RekUser = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        arrayUser[i] = RekUser
        i += 1
    
    # LoadWahana
    arrayWahana = [["" for j in range(5)] for i in range (100)]
    i = 0
    for row in readerWahana:
        RekWahana = (row[0],row[1],row[2],row[3],row[4])
        arrayWahana[i] = RekWahana
        i += 1
    
    # LoadPembelianTiket
    arrayPembelian = [["" for j in range(4)] for i in range (100)]
    i = 0
    for row in readerPembelian:
        RekPembelian = (row[0],row[1],row[2],row[3])
        arrayPembelian[i] = RekPembelian
        i += 1
    
    # LoadPenggunaanTiket
    arrayPenggunaan = [["" for j in range(4)] for i in range (100)]
    i = 0
    for row in readerPenggunaan:
        RekPenggunaan = (row[0],row[1],row[2],row[3])
        arrayPenggunaan[i] = RekPenggunaan
        i += 1
    
    # LoadKepemilikanTiket
    arrayKepemilikan = [["" for j in range(3)] for i in range (100)]
    i = 0
    for row in readerKepemilikan:
        RekKepemilikan = (row[0],row[1],row[2])
        arrayKepemilikan[i] = RekKepemilikan
        i += 1
    
    # LoadRefund
    arrayRefund = [["" for j in range(4)] for i in range (100)]
    i = 0
    for row in readerRefund:
        RekRefund = (row[0],row[1],row[2],row[3])
        arrayRefund[i] = RekRefund
        i += 1
    
    # LoadKritikSaran
    arrayKritikSaran = [["" for j in range(4)] for i in range (100)]
    i = 0
    for row in readerKritikSaran:
        RekKritikSaran = (row[0],row[1],row[2],row[3])
        arrayKritikSaran[i] = RekKritikSaran
        i += 1
        
    # LoadKehilangan
    arrayKehilangan = [["" for i in range(4)] for i in range(100)]
    i=0
    for row in readerKehilangan:
        rekKehilangan = (row[0],row[1],row[2],row[3])
        arrayKehilangan[i] = rekKehilangan
        i+=1
    
    DataUser.close()
    DataWahana.close()
    DataPembelian.close()
    DataKepemilikan.close()
    DataPenggunaan.close()
    DataRefund.close()
    DataKritikSaran.close()
    DataKehilangan.close()
    
    print()
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")
    return (arrayUser,arrayWahana,arrayPembelian,arrayPenggunaan,arrayKepemilikan,arrayRefund,arrayKritikSaran,arrayKehilangan)

#Fungsi F02 - Login User
def login(arrayUser):
    #membuat inisialisasi
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    found = False
    case=False
    emas=False
    
    #mengecek apakah username dan password sesuai dengan yang ada di dalam array
    for i in range(100):
        if username == arrayUser[i][3] and password == arrayUser[i][4]:
            found = True
            role = arrayUser[i][5]
            nama = arrayUser[i][0]
            if arrayUser[i][7] == "yes":
                emas=True
            break
    
    if found:
        print()
        print("Selamat bersenang-senang, "+nama)
        case=True
    else:
        print()
        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
        role = ""
        username = ""
    return username,role,case,emas
            
#Fungsi F03 - Save File
def savefile(arrayUser,arrayWahana,arrayPembelian,arrayPenggunaan,arrayKepemilikan,arrayRefund,arrayKritikSaran):
    #input nama file
    a=input("Masukkan nama File User: ")
    b=input("Masukkan nama File Daftar Wahana: ")
    c=input("Masukkan nama File Pembelian Tiket: ")
    d=input("Masukkan nama File Penggunaan Tiket: ")
    e=input("Masukkan nama File Kepemilikan Tiket: ")
    f=input("Masukkan nama File Refund: ")
    g=input("Masukkan nama File Kritik dan Saran: ")
    
    # membuka dan meng-convert data dari array ke file
    DataUser = open(a,"w",newline='')
    DataWahana = open(b,"w",newline='')
    DataPembelian = open(c,"w",newline='')
    DataPenggunaan = open(d,"w",newline='')
    DataKepemilikan = open(e,"w",newline='')
    DataRefund = open(f,"w",newline='')
    DataKritikSaran = open(g,"w",newline='')
    
    writerUser = csv.writer(DataUser)
    writerWahana = csv.writer(DataWahana)
    writerPembelian = csv.writer(DataPembelian)
    writerPenggunaan = csv.writer(DataPenggunaan)
    writerKepemilikan = csv.writer(DataKepemilikan)
    writerRefund = csv.writer(DataRefund)
    writerKritikSaran = csv.writer(DataKritikSaran)
    
    for i in range(100):
        writerUser.writerow(arrayUser[i])
        writerWahana.writerow(arrayWahana[i])
        writerPembelian.writerow(arrayPembelian[i])
        writerPenggunaan.writerow(arrayPenggunaan[i])
        writerKepemilikan.writerow(arrayKepemilikan[i])
        writerRefund.writerow(arrayRefund[i])
        writerKritikSaran.writerow(arrayKritikSaran[i])
    
    print("Data berhasil disimpan!")
    return
    
#Fungsi F04 - Sign Up User
def sign_up(arrayUser):
#    Nama,Tanggal_Lahir,Tinggi_Badan,Username,Password,Role,Saldo,GoldenACC
    nama = input("Masukkan nama pemain: ")
    tanggal_lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    tinggi = input("Masukkan tinggi badan pemain (cm): ")
    uname = input("Masukkan username pemain: ")
    password = input("Masukkan password pemain: ")
    
    for i in range(100):
        if arrayUser[i][0] == "" :
            arrayUser[i] = (nama,tanggal_lahir,tinggi,uname,password,"Pemain","0","No")
            print("Selamat menjadi pemain, "+str(nama)+". Selamat bermain.")
            break
    return arrayUser
        

#Fungsi F05 - Pencarian Pemain
def cari_pemain() :
    #format tipe bentukan -> <Nama,Tanggal_lahir,Tinggi_Badan,Username,Password,Role,Saldo>
    #Buka file csv dan menyiapkan reader
    DataPemain = open("user.csv" , 'r')
    readerUser = csv.reader(DataPemain,delimiter=',')
    
    #inisialisasi
    pencarian_username = input("Masukkan username: ")
    NamaPemain = "."
    TinggiPemain = "."
    TanggalLahir = "."
    found=False
    
    #pencarian username dalam array user
    for row in readerUser:
        RekUSER=(row[0],row[1],row[2],row[3],row[4],row[5],(row[6]),row[7])
        if  pencarian_username == RekUSER[3] :
            found=True
            NamaPemain = RekUSER[0]
            TinggiPemain = RekUSER[2]
            TanggalLahir = RekUSER[1]
            break
    
    if not(found):
        print("Pemain Tidak Ditemukan!")
    else : #found = True
        print("Nama Pemain:",NamaPemain)
        print("Tinggi Pemain:",TinggiPemain, "cm")
        print("Tanggal Lahir Pemain:",TanggalLahir)
    DataPemain.close()
    return
    
#Fungsi F06 - Pencarian Wahana 
def cari():
    #format tipe bentukan -> <ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi>
    #definisi untuk row batasan umur = anak-anak(1),dewasa(2),semuaumur(3)
    #definisi untuk batasan tinggi badan = lebihdari170(1),tanpabatasan(2)
    
    #membuka file csv dan menyiapkan reader
    DataWahana = open("wahana.csv" , 'r')
    readerWahana = csv.reader(DataWahana,delimiter=',')
    
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    
    #input variabel batasan_umur dan batasan_tinggi serta memvalidasinya
    batasan_umur = int(input("Batasan umur pemain: "))
    while batasan_umur < 1 or batasan_umur > 3 :
        print("Batasan umur tidak valid")
        batasan_umur = int(input("Batasan umur pemain: "))
    batasan_tinggi = int(input("Batasan tinggi badan: "))
    while batasan_tinggi < 1 or batasan_tinggi > 2 :
        print("Batasan tinggi badan tidak valid")
        batasan_tinggi = int(input("Batasan tinggi badan: "))
    
    print()
    print("Hasil pencarian:")
    
    adaWahana=0 #deklarasi jumlah wahana yang akan ada di output
    umur=""
    tinggi=""
    
    if batasan_umur == 1 :
        umur = "anak-anak"
    elif batasan_umur == 2 :
        umur = "dewasa"
    else : #batasan_umur == 3
        umur = "semua umur"
    
    if batasan_tinggi == 1 :
        tinggi = ">=170"
    else : #batasan_tinggi == 2 :
        tinggi = "tidak ada"
    
    for row in readerWahana :
        RekWAHANA = (row[0],row[1],(row[2]),(row[3]),(row[4]))
        if umur==RekWAHANA[3] and tinggi==RekWAHANA[4]:
            print(RekWAHANA[0],"|",RekWAHANA[1],"|",RekWAHANA[2])
            adaWahana += 1
    
    if adaWahana == 0 : #khusus apabila tidak ada wahana yg sesuai dengan kriteria
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.")
    DataWahana.close()
    return

#Fungsi F-07 - Pembelian Tiket
def umur(tanggalLahir, Tanggal):
    tahun=0
    
    tahun1 = ""
    for i in range(6,10):
        tahun1 += tanggalLahir[i]
    bulan1 = ""
    for i in range(3,5):
        bulan1 += tanggalLahir[i]
    hari1 = ""
    for i in range(2):
        hari1 += tanggalLahir[i]
    
    tahun2 = ""
    for i in range(6,10):
        tahun2 += Tanggal[i]
    bulan2 = ""
    for i in range(3,5):
        bulan2 += Tanggal[i]
    hari2 = ""
    for i in range(2):
        hari2 += Tanggal[i]
    
    if int(hari2)-int(hari1) < 0 :
        bulan2 = int(bulan2)-1
    if int(bulan2)-int(bulan1) < 0 :
        tahun2 = int(tahun2)-1
    tahun = int(tahun2)-int(tahun1)
    return tahun

def beli(username,arrayUser,arrayWahana,arrayPembelian,arrayKepemilikan,emas) :
    id_wahana = input("Masukkan ID Wahana: ")
    Tanggal = input("Masukkan tanggal hari ini: ")
    Tiket = int(input("Jumlah tiket yang dibeli: "))
    rekamanPembelian = (username,Tanggal,id_wahana,Tiket)
    
    case1 = False #ga sesuai kriteria
    case2 = False #uang ga cukup
    namaWahana=""
    hargaWahana = 0
    tahun=0
    batasanTinggi = False
    tinggi=0
    saldo=0
    sisaSaldo=0
    banyakTiket=0
    umurUser="semua umur"
    
    for i in range(100):
        if id_wahana == arrayWahana[i][0]:
            namaWahana = arrayWahana[i][1]
            if not(emas):
                hargaWahana = float(arrayWahana[i][2])*Tiket
            else: #emas=True
                hargaWahana = float(arrayWahana[i][2])*Tiket*0.5
            if arrayWahana[i][4] == ">=170":
                batasanTinggi = True
            break
    
    for i in range(100):
        if arrayUser[i][3] == username :
            tanggalLahir = arrayUser[i][1]
            tahun = umur(tanggalLahir, Tanggal)
            if tahun >=17:
                umurUser = "dewasa"
            else: # tahun <17
                umurUser = "anak-anak"
            tinggi = arrayUser[i][2]
            saldo = arrayUser[i][6]
            break
                
    for i in range(100):
        if id_wahana == arrayWahana[i][0]:
            if (umurUser=="dewasa" and arrayWahana[i][3] == "anak-anak") or (umurUser=="anak-anak" and arrayWahana[i][3] == "dewasa") or (int(tinggi)<170 and batasanTinggi):
                case1=True
            if float(saldo)<float(hargaWahana):
                case2=True
    
    if not(case1) and not(case2):
        #Username,Tanggal_Pembelian,ID_Wahana,Jumlah_Tiket
        print("Selamat bersenang-senang di "+str(namaWahana)+".")
        for i in range(100):
            if arrayPembelian[i][0] == "" :
                arrayPembelian[i] = rekamanPembelian
                break
        
        for i in range(100):
            if username == arrayUser[i][3]:
                sisaSaldo = float(saldo)-float(hargaWahana)
                arrayUser[i]= (arrayUser[i][0],arrayUser[i][1],arrayUser[i][2],arrayUser[i][3],
                         arrayUser[i][4],arrayUser[i][5],sisaSaldo,arrayUser[i][7])
                break
        
        for i in range(100):
            if username == arrayKepemilikan[i][0] and id_wahana == arrayKepemilikan[i][1]:
                banyakTiket = int(Tiket)+int(arrayKepemilikan[i][2])
                arrayKepemilikan[i] = (arrayKepemilikan[i][0],arrayKepemilikan[i][1],banyakTiket)
                break
            if arrayKepemilikan[i][0] == "" :
                arrayKepemilikan[i] = (username, id_wahana, Tiket)
                break
    
    if case1:
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
        print("Silakan menggunakan wahana lain yang tersedia.")
        
    if case2:
        print("Saldo Anda tidak cukup")
        print("Silakan mengisi saldo Anda")
    
#    print(arrayUser)
#    print(arrayKepemilikan)
#    print(arrayPembelian)
    return arrayUser,arrayPembelian,arrayKepemilikan

    

#Fungsi F-08 - Menggunakan Tiket
def main(arrayKepemilikan,arrayPenggunaan,username):
    #format tipe bentukan penggunaan tiket -> 
    #<Username,Tanggal_Penggunaan,ID_Wahana,Jumlah_Tiket>
    #format tipe bentukan kepemilikan tiket ->
    #<Username,ID_Wahana,Jumlah_Tiket>
    
    #baca masukan dan bentuk menjadi tuple
    id_wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jumlah_tiket = int(input("Jumlah tiket yang digunakan: "))
    rekamanPenggunaan = (username,tanggal,id_wahana,jumlah_tiket)
    
    found=False
    sisaTiket = 0        
        
    for i in range(100):
        if username == arrayKepemilikan[i][0] and id_wahana == arrayKepemilikan[i][1] and int(jumlah_tiket)<=int(arrayKepemilikan[i][2]):
            found=True
            sisaTiket =int (arrayKepemilikan[i][2]) - int(jumlah_tiket)
            break
    
    if found:
        for i in range(100):
            if arrayPenggunaan[i][0] == "" :
                arrayPenggunaan[i] = rekamanPenggunaan
                break

        for i in range(100):
            if arrayKepemilikan[i][0] == username and arrayKepemilikan[i][1] == id_wahana :
                arrayKepemilikan[i] = (username,id_wahana,sisaTiket)
        
        print("Terima kasih telah bermain")
        
    else:
        print("Tiket anda tidak valid dalam sistem kami")
   
    return arrayKepemilikan,arrayPenggunaan
    
#Fungsi F-09 - Refund
def refund(arrayUser,arrayWahana,arrayKepemilikan,arrayRefund,username):
    #butuh csv user, kepemilikan,wahana ,dan refund
    #tuple user <Nama,Tanggal_Lahir,Tinggi_Badan,Username,Password,Role,Saldo,GoldenAcc>
    #tuple kepemilikan <Username,ID_Wahana,Jumlah_Tiket>
    #tuple refund <Username,tanggalrefund(kalo jadi),ID_Wahana,Jumlah_Tiket>
    #tuple wahana <ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi>
    
    #harga tiket yg direfund memiliki harga 50% dari harga sebelumnya
    id_wahana=input("Masukkan ID wahana: ")
    tanggal=input("Masukkan Tanggal Refund: ")
    jumlah_tiket=int(input("Jumlah tiket yang di-refund: "))
    rekamanRefund=(username,tanggal,id_wahana,jumlah_tiket)
    
    found=False
    sisaTiket = 0
    saldoPenambahan = 0

    for i in range(100):
        if (username==arrayKepemilikan[i][0]) and (id_wahana==arrayKepemilikan[i][1]) and (jumlah_tiket <= int(arrayKepemilikan[i][2])):
            found = True
            sisaTiket = int(arrayKepemilikan[i][2]) - int(jumlah_tiket)
            
            for i in range(100):
                if id_wahana == arrayWahana[i][0] :
                    saldoPenambahan = 0.5*float(arrayWahana[i][2])*int(jumlah_tiket)
                    break
            for i in range(100):
                if username == arrayUser[i][3]:
                    saldoPenambahan = float(arrayUser[i][6]) + saldoPenambahan
                    break
    
    
    if found :
        print("Uang refund sudah kami berikan pada akun Anda.")
        for i in range(100):
            if arrayRefund[i][0] == "" :
                arrayRefund[i] = rekamanRefund
                break

        for i in range(100):
            if username == arrayKepemilikan[i][0] and id_wahana == arrayKepemilikan[i][1]:
                arrayKepemilikan[i] = (username,id_wahana,sisaTiket)
        
        for i in range(100):
            if username == arrayUser[i][3] :
                arrayUser[i] = (arrayUser[i][0],arrayUser[i][1],arrayUser[i][2],arrayUser[i][3],
                         arrayUser[i][4],arrayUser[i][5],saldoPenambahan,arrayUser[i][7])
    
    else:
        print("Anda tidak memiliki tiket terkait")

#    print(arrayUser)
#    print(arrayKepemilikan)
#    print(arrayRefund)
    return arrayUser,arrayKepemilikan,arrayRefund


#F10 - Membuat Kritik Saran
def kritik_saran(arrayKritikSaran,username) :
    ID_Wahana = input("Masukkan ID wahana: ")
    Tanggal = input("Masukkan tanggal pelaporan: ")
    Kritik = input("Kritik/saran Anda: ")
    rekamanKritik = (username,Tanggal,ID_Wahana,Kritik)
    
    for i in range(100):
        if arrayKritikSaran[i][0] == "" :
            arrayKritikSaran[i] = rekamanKritik
            print("Kritik dan Saran Anda kami terima.")
            break

    return arrayKritikSaran

#F11- Melihat Kritik Saran
#Admin dapat melihat kritik dan saran yang dimasukkan oleh pemain. 
#Diurutkan berdasarkan ID 
#Wahana secara alfabetis.
#Format: ID Wahana | Tanggal Pelaporan | Username Pemain | Isi kritik dan saran
def lihat_saran():
    #baca file
    file_kritik = open("kritiksaran.csv" , 'r')
    readerKritik = csv.reader(file_kritik,delimiter=',')
    
    #inisiasi
    jmlbaris=0
    Isi_Kritik=[0 for i in range(100)]
    
    #membaca data
    for row in readerKritik:
        Isi_Kritik[jmlbaris]=(row[0],row[1],row[2],row[3])
        if Isi_Kritik[jmlbaris] == ("","","",""):
            break
        jmlbaris+=1
        

    ID_Wahana = [0 for i in range (jmlbaris)]
    Tanggal = [0 for i in range (jmlbaris)]
    Username = [0 for i in range (jmlbaris)]
    Isi = [0 for i in range (jmlbaris)]
    found=False

    #membaca data sesuai klasifikasi
    for i in range (jmlbaris):
        ID_Wahana[i] = Isi_Kritik[i][2]
        Tanggal[i] = Isi_Kritik[i][1]
        Username[i] = Isi_Kritik[i][0]
        Isi[i]= Isi_Kritik[i][3]
    
    #apabila kritik ada
    if jmlbaris>0:
        found=True

    #keluaran
    print("Kritik dan saran:")
    #kasus kosong
    if not(found):
        print("Tidak Ditemukan Kritik dan Saran!")
    else :
        #mengurutkan sesuai alfabetis 
        for Pass in range (1,(jmlbaris-1)):
            Imin=Pass
            for i in range ((Pass+1),jmlbaris):
                if ID_Wahana[Imin]>ID_Wahana[i]:
                    Imin=i
            
                Temp=ID_Wahana[Imin]
                Temp1=Tanggal[Imin]
                Temp2=Username[Imin]
                Temp3=Isi[Imin]

                ID_Wahana[Imin]=ID_Wahana[Pass]
                Tanggal[Imin]=Tanggal[Pass]
                Username[Imin]=Username[Pass]
                Isi[Imin]=Isi[Pass]

                ID_Wahana[Pass]=Temp
                Tanggal[Pass]=Temp1
                Username[Pass]=Temp2
                Isi[Pass]=Temp3
        #keluaran yang alfabetis
        for i in range (1,jmlbaris):
            print(ID_Wahana[i]+' | '+Tanggal[i]+' | '+Username[i]+' | '+Isi[i]) 
    file_kritik.close()
    return

#F12- Menambahkan Wahana Baru   
#Admin dapat menambahkan wahana baru ke dalam manajemen wahana.
#Dapat diasumsikan semua masukan valid.
def tambah(arrayWahana):
    print("Masukkan Informasi Wahana yang ditambahkan: ")
    
    #menerima masukan wahana baru
    ID_Wahana = input("Masukkan ID Wahana: ")
    Nama_Wahana = input("Masukkan Nama Wahana: ")
    Harga = input("Masukkan Harga Tiket: ")
    Umur = input("Batasan umur: ")
    Tinggi = input("Batasan tinggi badan : ")

    #array baru setelah penambahan
    for i in range(100):
        if arrayWahana[i][0] == "" :
            arrayWahana[i] = (ID_Wahana,Nama_Wahana,Harga,Umur,Tinggi)
            print("Info wahana telah ditambahkan!")
            break
    return arrayWahana

#F13 - Top Up Saldo
def top_up(arrayUser):
    username = input("Masukkan username: ")
    saldo = input("Masukkan saldo yang di-top up: ")

    Found = True
    TotalSaldo = 0
    nama = "fulan"

    for i in range(100):
        if username == arrayUser[i][3]:
            Found = True
            nama = arrayUser[i][0]
            TotalSaldo = float(saldo) + float(arrayUser[i][6])
            arrayUser[i] = (arrayUser[i][0],arrayUser[i][1],arrayUser[i][2],arrayUser[i][3],
                     arrayUser[i][4],arrayUser[i][5],TotalSaldo,arrayUser[i][7])
            break

    if Found:
        print("Top up berhasil. Saldo " + nama + " bertambah menjadi " + str(round(TotalSaldo)))
    return arrayUser

#F14- Melihat Riwayat Penggunaan Wahana
#Admin bisa melihat riwayat penggunaan wahana.
#Format: Tanggal_Bermain | Username Pengguna | Jumlah Tiket
def riwayat():
    #baca file
    file_riwayat = open("penggunaan.csv",'r')
    readerRiwayat = csv.reader(file_riwayat,delimiter=',')

    #inisiasi
    Tanggal_Bermain = "."
    Username = "."
    Jumlah_Tiket = "."

    #baca masukan
    ID_Wahana= input("Masukkan ID Wahana: ")
    print("Riwayat:")

    found = False

    #proses
    for riwayat in readerRiwayat:
        Cek_Riwayat=(riwayat[0],riwayat[1],riwayat[2],riwayat[3])
        #pengecekan ID_Wahana
        if(ID_Wahana==Cek_Riwayat[2]):
            Tanggal_Bermain=Cek_Riwayat[1]
            Username=Cek_Riwayat[0]
            Jumlah_Tiket=Cek_Riwayat[3]
            found=True
            #output
            print(Tanggal_Bermain," | ", Username," | ",Jumlah_Tiket)

    if not (found):
        print("Wahana belum pernah dipakai")

    file_riwayat.close()
    return

#F15- Melihat Jumlah Tiket Pemain
#Admin bisa melihat jumlah tiket yang dimiliki pemain.
#Format: ID_Wahana | Nama_Wahana | Jumlah Tiket
def CariWahana (ID_Wahana):
    file_wahana = open("wahana.csv" , 'r')
    readerWahana = csv.reader(file_wahana,delimiter=',')
    for wahana in readerWahana:
        CekWahana=(wahana[0],wahana[1],wahana[2],wahana[3],wahana[4])
        if(ID_Wahana==CekWahana[0]):
            return(CekWahana[1])
    file_wahana.close()

def tiket():
    #baca file
    file_tiket = open("kepemilikan.csv" , 'r')
    readerTiket = csv.reader(file_tiket,delimiter=',')

    #inisiasi
    ID_Wahana = "."
    Jumlah_Tiket = "."
    Nama_Wahana = "."

    #baca masukan
    uname=input("Masukkan username: ")
    print("Riwayat:")

    #proses
    found=False
    for tiket in readerTiket:
        Cek_Tiket=(tiket[0],tiket[1],tiket[2])
        if(uname==Cek_Tiket[0]):
            ID_Wahana=Cek_Tiket[1]
            Jumlah_Tiket=Cek_Tiket[2]
            Nama_Wahana=CariWahana(ID_Wahana)
            print(ID_Wahana," | ", Nama_Wahana,"| ",Jumlah_Tiket)
            found=True
    
    if not(found):
        print("Tidak ada riwayat penggunaan")

    file_tiket.close()

# Fungsi F-16 - Exit
def keluar():
    pilihan=input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
    if pilihan == 'Y' :
        savefile(arrayUser,arrayWahana,arrayPembelian,arrayPenggunaan,arrayKepemilikan,arrayRefund,arrayKritikSaran)
        return
    else:
        return

# Fungsi B-02 - Golden Account
# Spek = fungsi ini mengharuskan pemain membayar 100.000 untuk mendapatkan akses gold acc. Pemain
#        gold acc akan mendapat keuntungan dapat membeli tiket bermain dengan setengah harga.
def golden(arrayUser):
    found=False
    sisaSaldo = 0
    uname = input("Masukkan username yang ingin di-upgrade: ")
    for i in range(100):
        if uname == arrayUser[i][3] and arrayUser[i][7]=="no":
            sisaSaldo = float(arrayUser[i][6])
            sisaSaldo -= 100000
            arrayUser[i] = arrayUser[i] = (arrayUser[i][0],arrayUser[i][1],arrayUser[i][2],arrayUser[i][3],
                         arrayUser[i][4],arrayUser[i][5],sisaSaldo,"yes")
            print("Akun Anda telah diupgrade.")
            found=True
        elif uname == arrayUser[i][3] and arrayUser[i][7]=="yes":
            found=True
            print("Akun Anda sudah memiliki akses Gold.")
    if not(found):
        print("Input username salah!")
    return arrayUser

# Fungsi B03 – Best Wahana
# Mahasiswa diminta untuk memberikan daftar 3 wahana terbaik berdasarkan jumlah tiket yang 
# terjual pada pemain untuk bermain di wahana terkait.
# Format: Rank | ID Wahana | Nama Wahana | Jumlah Tiket Terjual
def best_wahana():
    Username = ["" for j in range(100)]
    Tanggal = ["" for j in range(100)]
    ID = ["" for j in range(100)]
    Jumlah = ["" for j in range(100)]
    t=1
    for j in range (1,100):
        Username[j]=arrayPembelian[j][0]
        Tanggal[j]=arrayPembelian[j][1]
        ID[j]=arrayPembelian[j][2]
        Jumlah[j]=arrayPembelian[j][3]
        if (Username[j]!=''):
            t+=1

    for Pass in range (2,t):
        Imin=Pass
        Temp=Username[Imin]
        Temp1=Tanggal[Imin]
        Temp2=ID[Imin]
        Temp3=Jumlah[Imin]

        j=Imin-1
        while((Temp2<ID[j]) and (j>1)):
            Username[j+1]=Username[j]
            Tanggal[j+1]=Tanggal[j]
            ID[j+1]=ID[j]
            Jumlah[j+1]=Jumlah[j]
            j-=1

        if(Temp2>=ID[j]):
            Username[j+1]=Temp
            Tanggal[j+1]=Temp1
            ID[j+1]=Temp2
            Jumlah[j+1]=Temp3
        else:
            Username[j+1]=Username[j]
            Tanggal[j+1]=Tanggal[j]
            ID[j+1]=ID[j]
            Jumlah[j+1]=Jumlah[j]

            Username[j]=Temp
            Tanggal[j]=Temp1
            ID[j]=Temp2
            Jumlah[j]=Temp3

    j=1
    k=0
    ID_2 =['' for k in range(100)]
    Jumlah_2=[0 for k in range(100)]
    while (j<t):
        Sum=0
        Current=ID[j]
        while(ID[j]==Current):  
            Sum += int(Jumlah[j])
            j+=1
        ID_2[k]=Current
        Jumlah_2[k]=Sum
        k+=1

    for Pass2 in range (1,100):
        Imin=Pass2
        Temp=ID_2[Imin]
        Temp1=Jumlah_2[Imin]

        m=Imin-1
        while((Temp1>Jumlah_2[m]) and (m>0)):
            Jumlah_2[m+1]=Jumlah_2[m]
            ID_2[m+1]=ID_2[m]
            m-=1
        if(Temp1<=Jumlah_2[m]):
            ID_2[m+1]=Temp
            Jumlah_2[m+1]=Temp1
        else:
            ID_2[m+1]=ID_2[m]
            Jumlah_2[m+1]=Jumlah_2[m]

            ID_2[m]=Temp
            Jumlah_2[m]=Temp1

    for a in range (3):
        Nama_Wahana=CariWahana(ID_2[a])
        print((a+1),' | ',ID_2[a],' | ',Nama_Wahana,' | ',Jumlah_2[a])  

# Fungsi B-04 - Laporan Kehilangan Tiket
def kehilangan(arrayKepemilikan,arrayKehilangan):
    uname = input("Masukkan username: ")
    tanggal_hilang = input("Tanggal kehilangan tiket: ")
    id_wahana = input("ID wahana: ")
    jumlah_tiket = int(input("Jumlah tiket yang dihilangkan: "))
    rekamanKehilangan = (uname,tanggal_hilang,id_wahana,jumlah_tiket)
    
    for i in range(100):
        if arrayKehilangan[i][0] == "" :
            arrayKehilangan[i] = rekamanKehilangan
            break
    
    for i in range(100):
        if arrayKepemilikan[i][0]==uname and arrayKepemilikan[i][1]==id_wahana :
            jumlah_tiket=int(arrayKepemilikan[i][2])-jumlah_tiket
            arrayKepemilikan[i]=(uname,id_wahana,jumlah_tiket)
    print("Laporan kehilangan tiket Anda telah direkam.")
    return arrayKepemilikan,arrayKehilangan
    
#ALGORITMA UTAMA
struktur = load()
arrayUser = struktur[0]
arrayWahana = struktur[1]
arrayPembelian = struktur[2]
arrayPenggunaan = struktur[3]
arrayKepemilikan = struktur[4]
arrayRefund = struktur[5]
arrayKritikSaran = struktur[6]
arrayKehilangan = struktur[7]

role = ""
while role!= "Admin" and role!="Pemain":
    masuk = login(arrayUser)
    username = ""
    role = ""
    username = masuk[0]
    role = masuk[1]
    case = masuk[2] #melihat apakah input username dan password salah atau benar. benar -> case=True
    emas = masuk[3] #boolean

if case :
    menu=""
else: #case = False
    menu = "$ exit"
while menu != "$ exit" :
    if role == "Admin":
        print()
        print("Menu Admin:")
        print("1. SignUp Pemain, $ signup")
        print("2. Pencarian Pemain, $ cari_pemain")
        print("3. Melihat Kritik dan Saran, $ lihat_laporan")
        print("4. Menambahkan Wahana Baru, $ tambah_wahana")
        print("5. Top Up Saldo, $ topup")
        print("6. Melihat Riwayat Pengguna Wahana, $ riwayat_wahana")
        print("7. Melihat Jumlah Tiket Pemain, $ tiket_pemain")
        print("8. Akses Golden Account, $ upgrade_gold")
        print("9. Best Wahana, $ best_wahana")
        print("10. Exit, $ exit")
        print("contoh input -> $ topup")
        menu = input()
        if menu == ("$ signup"):
            sign_up(arrayUser)
        elif menu == ("$ cari_pemain"):
            cari_pemain()
        elif menu == ("$ lihat_laporan"):
            lihat_saran()
        elif menu == ("$ tambah_wahana"):
            tambah(arrayWahana)
        elif menu == ("$ topup"):
            top_up(arrayUser)
        elif menu == ("$ riwayat_wahana"):
            riwayat()
        elif menu == ("$ tiket_pemain"):
            tiket()
        elif menu == ("$ exit"):
            keluar()
            pilihan=input("Apakah Anda ingin melakukan login kembali? (Y/N): " )
            if pilihan == 'Y':
                menu = ""
                role = ""
                while role!= "Admin" and role!="Pemain":
                    masuk = login(arrayUser)
                    username = ""
                    role = ""
                    username = masuk[0]
                    role = masuk[1]
                    case = masuk[2] #melihat apakah input username dan password salah atau benar. benar -> case=True
                    emas = masuk[3] #boolean
        elif menu == ("$ save"):
            savefile(arrayUser,arrayWahana,arrayPembelian,arrayPenggunaan,arrayKepemilikan,arrayRefund,arrayKritikSaran)
        elif menu == ("$ upgrade_gold"):
            golden(arrayUser)
        elif menu == ("$ best_wahana"):
            best_wahana()
   
    elif role == "Pemain":
        print()
        print("Menu Pemain:")
        print("1. Pencarian Wahana, $ cari")
        print("2. Pembelian Tiket, $ beli_tiket")
        print("3. Menggunakan Tiket, $ main")
        print("4. Refund Tiket, $ refund")
        print("5. Menulis Kritik dan Saran, $ kritik_saran")
        print("6. Laporan Kehilangan Tiket, $ tiket_hilang")
        print("7. Best Wahana, $ best_wahana")
        print("8. Exit, $ exit")
        print("contoh input -> $ refund")
        menu = input()
        if menu == ("$ cari"):
            cari()
        elif menu == ("$ beli_tiket"):
            beli(username,arrayUser,arrayWahana,arrayPembelian,arrayKepemilikan,emas)
        elif menu == ("$ main"):
            main(arrayKepemilikan,arrayPenggunaan,username)
        elif menu == ("$ refund"):
            refund(arrayUser,arrayWahana,arrayKepemilikan,arrayRefund,username)
        elif menu == ("$ kritik_saran"):
            kritik_saran(arrayKritikSaran,username)
        elif menu == ("$ exit"):
            keluar()
            pilihan=input("Apakah Anda ingin melakukan login kembali? (Y/N): " )
            if pilihan == 'Y':
                menu = ""
                role = ""
                while role!= "Admin" and role!="Pemain":
                    masuk = login(arrayUser)
                    username = ""
                    role = ""
                    username = masuk[0]
                    role = masuk[1]
                    case = masuk[2] #melihat apakah input username dan password salah atau benar. benar -> case=True
                    emas = masuk[3] #boolean
        elif menu == ("$ save"):
            savefile(arrayUser,arrayWahana,arrayPembelian,arrayPenggunaan,arrayKepemilikan,arrayRefund,arrayKritikSaran)
        elif menu == ("$ tiket_hilang"):
            kehilangan(arrayKepemilikan,arrayKehilangan)
        elif menu == ("$ best_wahana"):
            best_wahana()
