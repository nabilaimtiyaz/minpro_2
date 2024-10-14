from prettytable import PrettyTable

#List jadwal atlet dalam 1 minggu
jadwal_atlet = [
    [1, "Senin", "4-11-24", "Daya Tahan", "-"],
    [2, "Selasa", "5-11-24", "Kekuatan", "-"],
    [3, "Rabu", "6-11-24", "-", "REST"],
    [4, "Kamis", "7-11-24", "Kelenturan", "LIBUR"],
    [5, "Jumat", "8-11-24", "Fun Games", "-"],
    [6, "Sabtu", "9-11-24", "cross country", "-"],
    [7, "Minggu", "10-11-24", "-", "REST"]
]

#Dictionary dari nama atlet dan kata sandinya masing-masing, digunakan ketika login
nama_atlet = {
    "Lala": "111",
    "Mouzha": "222",
    "Zaskia": "333",
    "Hana": "444",
    "Carissa": "555"
}

#Fungsi untuk pelatih menambah jadwal (Create)
def tambah_jadwal():
    hari_latihan = input("\nMasukkan hari: ")
    tanggal_latihan = input("Masukkan tanggal (contoh: 4-11-24): ")
    program_latihan = input("Masukkan program: ")
    keterangan_latihan = input("Masukkan keterangan: ")
    for user in jadwal_atlet:
        if user[1] == hari_latihan:
            print('Jadwal sudah tersedia')
            break
    jadwal_baru = len( jadwal_atlet) + 1
    jadwal_atlet.append([jadwal_baru, hari_latihan, tanggal_latihan, program_latihan, keterangan_latihan])
    print('\nJadwal berhasil ditambahkan.')


#Fungsi untuk atlet menampilkan jadwal (Read)
def tampilkan_jadwal():
        table = PrettyTable()
        table.field_names = ["Nomor", "Hari","Tanggal","Program", "Keterangan"]
        for item in jadwal_atlet:
            table.add_row(item)
        print(table)

#Fungsi untuk pelatih meng-update jadwal (Update)
def update_jadwal():
    jadwal_latihan = input("\nMasukkan hari yang ingin Anda perbarui: ")
    for a in range(len(jadwal_atlet)):
        if jadwal_atlet[a][1] == jadwal_latihan:
            hari_baru = input("Masukkan hari baru:")
            tanggal_baru = input("Masukkan tanggal baru: ")
            program_baru = input("Masukkan program baru: ")
            keterangan_baru = input("Masukkan keterangan baru: ")
            jadwal_atlet[a][1] = hari_baru
            jadwal_atlet[a][2] = tanggal_baru
            jadwal_atlet[a][3] = program_baru
            jadwal_atlet[a][4] = keterangan_baru
            tampilkan_jadwal() 
            print("\n⋆. 𐙚 ˚ Jadwal latihan berhasil diupdate ⋆. 𐙚 ˚")
            break
    else:
        print("\nTidak valid! Mohon masukkan hari yang tersedia.")

#Fungsi untuk pelatih menghapus jadwal (Delete)
def hapus_jadwal():
    hapus = input("\nMasukkan jadwal yang ingin dihapus: ")
    for a, atlet in enumerate(jadwal_atlet):
        if atlet[1] == hapus:  
            del jadwal_atlet[a]
            print(f"\nData {hapus} berhasil dihapuskan.")
            tampilkan_jadwal()

#Fungsi untuk atlet mengkonfirmasi kehadiran
def konfirmasi_kehadiran():
    while True:
        konfirmasi = input("\nApakah Anda dapat menghadiri latihan? \n(Iya/Tidak): ").lower()
        if konfirmasi == "iya":
            print("\nSEMANGAT YAA LATIHANNYA (๑>◡<๑)")
            break
        elif konfirmasi == "tidak":
            print("\nTerima kasih sudah konfirmasi.")
            break
        else:
            print("\nTerjadi kesalahan.Silahkan input iya/tidak")
            konfirmasi_kehadiran()

        lanjut = input("\nApakah Anda ingin memulai dari awal lagi? \n(iya/tidak): ").lower()
        if lanjut == "iya":
            menu_atlet()
            break
        elif lanjut == "tidak":
            print("\n⋆⭒˚.⋆ Terima Kasih ⋆⭒˚.⋆")
            break
        else:
            print("\nTerjadi kesalahan.Silahkan input iya/tidak")
            konfirmasi_kehadiran()

#Fungsi Menu pelatih
def menu_pelatih():
    while True:
        pelatih = "Nia"
        kata_sandi = "2505"
        
        sebagai_pelatih = input("\nNama: Coach ")
        input_kata_sandi = input("Kata Sandi: ")
        
        if sebagai_pelatih == pelatih and input_kata_sandi == kata_sandi:
            print("\nSelamat Datang Coach!")
            print("\n===== MENU PELATIH =====")
            print("1. Tambah Jadwal")
            print("2. Tampilkan Jadwal")
            print("3. Update Jadwal")
            print("4. Hapus Jadwal")
            print("5. keluar")
            opsi = input("\nSilahkan pilih menu (1-5): ")

            if opsi == "1":
                tambah_jadwal()
            elif opsi == "2":
                tampilkan_jadwal()
            elif opsi == "3":
                update_jadwal()
            elif opsi == "4":
                hapus_jadwal()
            elif opsi == "5":
                print("\nMenu pelatih telah ditutup.")
                break
            else:
                print("Maaf, pilihan anda tidak ada didaftar. Silahkan masukkan kembali.")
        else:
            print("\nData Anda tidak valid. Silahkan coba kembali.")

#Fungsi Menu atlet
def menu_atlet():
        while True:
            nama = input("\nSilahkan Masukkan Nama: ")
            kata_sandi = input("Silahkan Masukkan Kata Sandi: ")
            if nama in nama_atlet and nama_atlet[nama] == kata_sandi:
                print("\n𓏲 ๋࣭  ࣪ ˖ Anda Berhasil Masuk 𓏲 ๋࣭  ࣪ ˖")
                print("\n===== MENU ATLET =====")
                print("1. Lihat Jadwal Latihan")
                print("2. Konfirmasi Kehadiran")
                print("3. Keluar")
                opsi = input("\nSilahkan pilih menu (1-3): ")
                
                if opsi == "1":
                    tampilkan_jadwal()
                    break
                elif opsi == "2":
                    konfirmasi_kehadiran()
                    break
                elif opsi == "3":
                    print("\nMenu atlet telah ditutup.")
                    break
                else:
                    print("\nPilihan anda tidak ada didaftar. Silahkan masukkan kembali.")
            else:
                print("\nData yang Anda masukkan tidak terdaftar, silahkan coba lagi.")

#Fungsi beranda aplikasi
def beranda():
    while True:
        print("====== FENCING TRAINING SCHEDULE =====")
        print("1. Pelatih")
        print("2. Atlet")

        opsi_peran = input("\nSilahkan pilih peran (1/2): ")

        if opsi_peran == "1":
            menu_pelatih()
            break
        elif opsi_peran == "2":
            menu_atlet()
            break
        else:
            print("Mohon masukkan pilihan yang benar.")

if __name__ == "__main__":
    beranda()