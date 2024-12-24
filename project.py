import mysql.connector
import time
import pyfiglet
import os
import colorama
from colorama import Fore, Style, init
from tabulate import tabulate
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.progress import Progress
from rich import print as rprint
from datetime import datetime


# Membuat Koneksi antara python ke MySQL
def connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='idea_distro',
    )

# Membuat Animasi Login
console = Console()
init()
def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art_idea = pyfiglet.figlet_format("IDEA", font="Doom")
    ascii_art_distro = pyfiglet.figlet_format("DISTRO", font="Doom")

    terminal_width = os.get_terminal_size().columns

    def print_centered(text):
        lines = text.split('\n')
        for line in lines:
            print(line.center(terminal_width))

    print(Fore.BLUE + Style.BRIGHT)
    print_centered(ascii_art_idea)
    print(Fore.RED + Style.BRIGHT)
    print_centered(ascii_art_distro)
    print(Style.RESET_ALL)

def animasi_login():
    console.print("[bold magenta] Program Is Being Processed, Please Wait...[/bold magenta]")
    
    # Menambahkan efek loading yang lebih kreatif
    loading_chars = ["🔄", "⏳", "✨", "🚀", "🔄"]
    loading_messages = [
        "[cyan]Initializing...[/cyan]",
    ]
    
    for i in range(2):  # Memperpanjang durasi loading
        for index, char in enumerate(loading_chars):
            console.print(f"[cyan]{char} {loading_messages[index % len(loading_messages)]}", end="\r")
            time.sleep(0.5)

    # Menambahkan pesan selamat datang setelah loading selesai
    console.print("\n[bold green]DONE!!![/bold green]")
    console.print("[bold yellow]Welcome to the IDEA DISTRO Aplication![/bold yellow]")

def show_barang(connection):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM barang"
        cursor.execute(sql)
        result = cursor.fetchall()
        table = Table(title="Daftar Barang")
        table.add_column("ID", justify="center")
        table.add_column("Nama", justify="center")
        table.add_column("Type", justify="center")
        table.add_column("Stock", justify="center")
        table.add_column("Harga", justify="center")

        for barang in result:  # Menggunakan result yang benar
            stock = barang[4]  # Menggunakan indeks untuk mengakses kolom Stock (indeks 4)
            if stock < 5:
                stock_str = f"[red]{stock}[/red]"       
            elif 5 <= stock <= 10:
                stock_str = f"[yellow]{stock}[/yellow]"  
            else:
                stock_str = f"[green]{stock}[/green]"   

            table.add_row(
                str(barang[0]),  # ID_Barang (indeks 0)
                barang[1],       # Nama_Barang (indeks 1)
                barang[2],       # Type_Barang (indeks 2)
                stock_str,  
                f"{barang[3]:,}"  # Harga (indeks 3), format harga dengan pemisah ribuan
            )

        console.print(table)  # Menampilkan tabel

def show_TShirt(connection):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM barang WHERE Type_Barang = 'T-Shirt'"
        cursor.execute(sql)
        result = cursor.fetchall()
        table = Table(title="Daftar Barang")
        table.add_column("ID", justify="center")
        table.add_column("Nama", justify="center")
        table.add_column("Type", justify="center")
        table.add_column("Stock", justify="center")
        table.add_column("Harga", justify="center")

        for barang in result:  # Menggunakan result yang benar
            stock = barang[4]  # Menggunakan indeks untuk mengakses kolom Stock (indeks 4)
            if stock < 5:
                stock_str = f"[red]{stock}[/red]"       
            elif 5 <= stock <= 10:
                stock_str = f"[yellow]{stock}[/yellow]"  
            else:
                stock_str = f"[green]{stock}[/green]"   

            table.add_row(
                str(barang[0]),  # ID_Barang (indeks 0)
                barang[1],       # Nama_Barang (indeks 1)
                barang[2],       # Type_Barang (indeks 2)
                stock_str,  
                f"{barang[3]:,}"  # Harga (indeks 3), format harga dengan pemisah ribuan
            )
        
        console.print(table)

def show_outterwear(connection):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM barang WHERE Type_Barang = 'Outterwear'"
        cursor.execute(sql)
        result = cursor.fetchall()
        table = Table(title="Daftar Barang")
        table.add_column("ID", justify="center")
        table.add_column("Nama", justify="center")
        table.add_column("Type", justify="center")
        table.add_column("Stock", justify="center")
        table.add_column("Harga", justify="center")

        for barang in result:  # Menggunakan result yang benar
            stock = barang[4]  # Menggunakan indeks untuk mengakses kolom Stock (indeks 4)
            if stock < 5:
                stock_str = f"[red]{stock}[/red]"       
            elif 5 <= stock <= 10:
                stock_str = f"[yellow]{stock}[/yellow]"  
            else:
                stock_str = f"[green]{stock}[/green]"   

            table.add_row(
                str(barang[0]),  # ID_Barang (indeks 0)
                barang[1],       # Nama_Barang (indeks 1)
                barang[2],       # Type_Barang (indeks 2)
                stock_str,  
                f"{barang[3]:,}"  # Harga (indeks 3), format harga dengan pemisah ribuan
            )
        
        console.print(table)

def show_bottoms(connection):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM barang WHERE Type_Barang = 'Bottoms'"
        cursor.execute(sql)
        result = cursor.fetchall()
        table = Table(title="Daftar Barang")
        table.add_column("ID", justify="center")
        table.add_column("Nama", justify="center")
        table.add_column("Type", justify="center")
        table.add_column("Stock", justify="center")
        table.add_column("Harga", justify="center")

        for barang in result:  # Menggunakan result yang benar
            stock = barang[4]  # Menggunakan indeks untuk mengakses kolom Stock (indeks 4)
            if stock < 5:
                stock_str = f"[red]{stock}[/red]"       
            elif 5 <= stock <= 10:
                stock_str = f"[yellow]{stock}[/yellow]"  
            else:
                stock_str = f"[green]{stock}[/green]"   

            table.add_row(
                str(barang[0]),  # ID_Barang (indeks 0)
                barang[1],       # Nama_Barang (indeks 1)
                barang[2],       # Type_Barang (indeks 2)
                stock_str,  
                f"{barang[3]:,}"  # Harga (indeks 3), format harga dengan pemisah ribuan
            )
        
        console.print(table)

def show_accessories(connection):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM barang WHERE Type_Barang = 'Accessories'"
        cursor.execute(sql)
        result = cursor.fetchall()
        table = Table(title="Daftar Barang")
        table.add_column("ID", justify="center")
        table.add_column("Nama", justify="center")
        table.add_column("Type", justify="center")
        table.add_column("Stock", justify="center")
        table.add_column("Harga", justify="center")

        for barang in result:  # Menggunakan result yang benar
            stock = barang[4]  # Menggunakan indeks untuk mengakses kolom Stock (indeks 4)
            if stock < 5:
                stock_str = f"[red]{stock}[/red]"       
            elif 5 <= stock <= 10:
                stock_str = f"[yellow]{stock}[/yellow]"  
            else:
                stock_str = f"[green]{stock}[/green]"   

            table.add_row(
                str(barang[0]),  # ID_Barang (indeks 0)
                barang[1],       # Nama_Barang (indeks 1)
                barang[2],       # Type_Barang (indeks 2)
                stock_str,  
                f"{barang[3]:,}"  # Harga (indeks 3), format harga dengan pemisah ribuan
            )
        
        console.print(table)

def insert_barang(connection):
    cursor = connection.cursor()
    id_barang = (input("Masukkan ID Barang : "))
    nama_barang = input("Masukkan Nama Barang : ")
    type_barang = input("Masukkan Type Barang : ")
    harga = int(input("Masukkan Harga Barang : "))
    stock = int(input("Masukkan Stock Barang : "))

    sql = ("INSERT INTO barang (ID_Barang, Nama_Barang, Type_Barang, Harga, Stock) VALUES (%s,%s,%s,%s,%s)")
    cursor.execute(sql, (id_barang, nama_barang, type_barang, harga, stock))
    connection.commit()
    print("Data Berhasil Ditambahkan")

def update_barang(connection):
    cursor = connection.cursor()
    id_barang = input("Masukkan ID Barang yang ingin diupdate : ")
    
    # Mengambil data barang yang ada untuk ditampilkan
    cursor.execute("SELECT * FROM barang WHERE ID_Barang = %s", (id_barang,))
    result = cursor.fetchone()
    
    if result is None:
        print("ID Barang tidak ditemukan.")
        return
    
    # Menampilkan data barang yang ada
    print("Data Barang Saat Ini:")
    print(f"ID Barang: {result[0]}")
    print(f"Nama Barang: {result[1]}")
    print(f"Type Barang: {result[2]}")
    print(f"Harga: {result[3]}")
    print(f"Stock: {result[4]}")
    
    # Mengambil input baru dari pengguna
    nama_barang = input("Masukkan Nama Barang yang ingin diupdate (tekan enter untuk tidak mengubah) : ")
    type_barang = input("Masukkan Type Barang Baru (tekan enter untuk tidak mengubah) : ")
    harga = input("Masukkan Harga Barang Baru (tekan enter untuk tidak mengubah) : ")
    stock = input("Masukkan Stock Barang Baru (tekan enter untuk tidak mengubah) : ")

    # Membuat pernyataan SQL untuk update
    updates = []
    params = []

    if nama_barang:
        updates.append("Nama_Barang = %s")
        params.append(nama_barang)

    if type_barang:
        updates.append("Type_Barang = %s")
        params.append(type_barang)

    if harga:
        try:
            params.append(int(harga))  # Pastikan harga adalah integer
            updates.append("Harga = %s")
        except ValueError:
            print("Harga harus berupa angka.")
            return

    if stock:
        try:
            params.append(int(stock))  # Pastikan stock adalah integer
            updates.append("Stock = %s")
        except ValueError:
            print("Stock harus berupa angka.")
            return

    # Menambahkan ID_Barang ke parameter
    params.append(id_barang)

    if not updates:
        print("Tidak ada data yang diubah.")
        return

    # Menyusun pernyataan SQL akhir
    sql = "UPDATE barang SET " + ", ".join(updates) + " WHERE ID_Barang = %s"

    # Menjalankan pernyataan SQL
    cursor.execute(sql, params)
    connection.commit()
    print("Data Berhasil Diupdate")

def hapus_barang(connection):
    cursor = connection.cursor()
    id_barang = input("Masukkan ID Barang yang ingin dihapus : ")
    sql = ("DELETE FROM barang WHERE ID_Barang = %s")
    cursor.execute(sql, (id_barang,))
    connection.commit()
    print("Data Berhasil Dihapus")

def search_barang(connection):
    cursor = connection.cursor()
    keyword = input("Masukkan Keyword Pencarian : ")
    sql = "SELECT * FROM barang WHERE Nama_Barang LIKE %s OR Type_Barang LIKE %s"
    cursor.execute(sql, ("%" + keyword + "%", "%" + keyword + "%"))
    result = cursor.fetchall()
    
    if cursor.rowcount <= 0:
        console.print("Tidak ada data yang tersedia", style="bold red")
    else:
        table = Table(title="Hasil Pencarian Barang")
        table.add_column("ID", justify="center")
        table.add_column("Nama", justify="center")
        table.add_column("Type", justify="center")
        table.add_column("Stock", justify="center")
        table.add_column("Harga", justify="center")

        for barang in result:
            stock = barang[4]  # Menggunakan indeks untuk mengakses kolom Stock (indeks 4)
            if stock < 5:
                stock_str = f"[red]{stock}[/red]"       
            elif 5 <= stock <= 10:
                stock_str = f"[yellow]{stock}[/yellow]"  
            else:
                stock_str = f"[green]{stock}[/green]"   

            table.add_row(
                str(barang[0]),  # ID_Barang (indeks 0)
                barang[1],       # Nama_Barang (indeks 1)
                barang[2],       # Type_Barang (indeks 2)
                stock_str,  
                f"{barang[3]:,}"  # Harga (indeks 3), format harga dengan pemisah ribuan
            )
        
        console.print(table)

def insert_pegawai(connection):
    cursor = connection.cursor()
    id_pegawai = input("Masukkan ID Pegawai : ")
    nama_pegawai = input("Masukkan Nama Pegawai : ")
    alamat = input("Masukkan Alamat Pegawai : ")
    no_tlp = input("Masukkan No Telepon Pegawai : ")

    sql = ("INSERT INTO pegawai (ID_Pegawai, Nama_Pegawai, Alamat, No_Tlp) VALUES (%s, %s, %s, %s)")
    cursor.execute(sql, (id_pegawai, nama_pegawai, alamat, no_tlp))
    connection.commit()
    print("Data Berhasil Ditambahkan")

def show_pegawai(connection):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM pegawai"
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount <= 0:
            console.print("Tidak ada data yang tersedia", style="bold red")
        else:
            headers = ["ID_Pegawai", "Nama_Pegawai", "Alamat", "No.Tlp"]
            print(tabulate(result, tablefmt="fancy_grid", headers=headers, colalign=["center"]))

def hapus_pegawai(connection):
    cursor = connection.cursor()
    id_pegawai = int(input("Masukkan ID Pegawai yang ingin dihapus : "))
    sql = ("DELETE FROM pegawai WHERE ID_Pegawai = %s")
    cursor.execute(sql, (id_pegawai,))
    connection.commit()
    print("Data Berhasil Dihapus")

def update_pegawai(connection):
    cursor = connection.cursor()
    id_pegawai = input("Masukkan ID Pegawai yang ingin diupdate : ")
    
    # Mengambil data pegawai yang ada untuk ditampilkan
    cursor.execute("SELECT * FROM pegawai WHERE ID_Pegawai = %s", (id_pegawai,))
    result = cursor.fetchone()
    
    if result is None:
        print("ID Pegawai tidak ditemukan.")
        return
    
    # Menampilkan data pegawai yang ada
    print("Data Pegawai Saat Ini:")
    print(f"ID Pegawai: {result[0]}")
    print(f"Nama Pegawai: {result[1]}")
    print(f"Alamat: {result[2]}")
    print(f"No Telepon: {result[3]}")
    
    # Mengambil input baru dari pengguna
    nama_pegawai = input("Masukkan Nama Pegawai yang ingin diupdate (tekan enter untuk tidak mengubah) : ")
    alamat = input("Masukkan Alamat Pegawai Baru (tekan enter untuk tidak mengubah) : ")
    no_tlp = input("Masukkan No Telepon Pegawai Baru (tekan enter untuk tidak mengubah) : ")

    # Membuat pernyataan SQL untuk update
    updates = []
    params = []

    if nama_pegawai:
        updates.append("Nama_Pegawai = %s")
        params.append(nama_pegawai)
    if alamat:
        updates.append("Alamat = %s")
        params.append(alamat)
    if no_tlp:
        updates.append("No_Tlp = %s")
        params.append(no_tlp)

    # Menambahkan ID_Pegawai ke parameter
    params.append(id_pegawai)

    if not updates:
        print("Tidak ada data yang diubah.")
        return

    # Menyusun pernyataan SQL akhir
    sql = "UPDATE pegawai SET " + ", ".join(updates) + " WHERE ID_Pegawai = %s"

    # Menjalankan pernyataan SQL
    cursor.execute(sql, params)
    connection.commit()
    print("Data Pegawai Berhasil Diupdate")

def transaksi(connection):
    cursor = connection.cursor()
    
    # Menampilkan daftar barang untuk memilih
    show_barang(connection)
    
    id_transaksi = input("Masukkan ID Transaksi : ")
    id_barang = input("Masukkan ID Barang yang dibeli: ")
    jumlah = int(input("Masukkan Jumlah yang dibeli: "))
    
    # Mengambil harga dan stok barang berdasarkan ID
    cursor.execute("SELECT Type_Barang, Nama_Barang, Harga, Stock FROM barang WHERE ID_Barang = %s", (id_barang,))
    result = cursor.fetchone()
    
    if result is None:
        console.print("ID Barang tidak ditemukan.", style="bold red")
        return
    
    type_barang, nama_barang, harga, stock = result
    
    if jumlah > stock:
        console.print("Jumlah yang dibeli melebihi stok yang tersedia.", style="bold red")
        return
    
    total_harga = harga * jumlah
    
    # Menyimpan transaksi ke dalam tabel transaksi
    sql = "INSERT INTO transaksi (ID_Transaksi, ID_Barang, Jumlah, Harga_Satuan, Total_Harga) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (id_transaksi, id_barang, jumlah, harga, total_harga))
    
    # Mengupdate stok barang
    new_stock = stock - jumlah
    sql_update = "UPDATE barang SET Stock = %s WHERE ID_Barang = %s"
    cursor.execute(sql_update, (new_stock, id_barang))
    
    connection.commit()
    
    console = Console()

    struk_data = [
        ["ID Transaksi", id_transaksi],
        ["ID Barang", id_barang],
        ["Nama Barang", nama_barang],
        ["Type Barang", type_barang],
        ["Jumlah", jumlah],
        ["Harga Satuan", harga],
        ["Total Harga", total_harga],  
    ]
    
    
    struk_panel = Panel.fit(
        tabulate(struk_data, headers=["Detail", "Informasi"], tablefmt="simple"),
        title="RECEIPT",
        border_style="blue",
        padding=(1, 2)
    )
    
    console.print(struk_panel)

def tampilkan_riwayat(connection):
    cursor = connection.cursor()
    sql = "SELECT t.ID_Transaksi, t.ID_Barang, b.Nama_Barang, t.Jumlah, t.Harga_Satuan, t.Total_Harga, t.Tanggal FROM transaksi t JOIN barang b ON t.ID_Barang = b.ID_Barang"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if cursor.rowcount <= 0:
        console.print("Tidak ada riwayat transaksi yang tersedia.", style="bold red")
    else:
        headers = ["ID Transaksi", "ID Barang", "Nama Barang", "Jumlah", "Harga Satuan", "Total Harga", "Tanggal"]
        print(tabulate(result, headers=headers, tablefmt="fancy_grid", stralign="center"))

def show_menu(connection):
    while True:
        text1 = "[bold red] 1. [/bold red][cyan] Barang [/cyan]"
        text2 = "[bold red] 2. [/bold red][cyan] Pegawai [/cyan]"
        text3 = "[bold red] 3. [/bold red][cyan] Pembelian [/cyan]"
        text4 = "[bold red] 4. [/bold red][cyan] Transaksi [/cyan]"
        text5 = "[bold red] 0. [/bold red][cyan] Exit Program [/cyan]"

        rprint(Panel(
        f"{text1}\n{text2}\n{text3}\n{text4}\n{text5}",
        expand=False,
        title="[magenta]Daftar Menu Utama[/magenta]",
        border_style="none",
        padding=(1, 2)
    ))

        menu = input("{}>{} Masukkan Pilihan Menu : ".format(Fore.MAGENTA, Style.RESET_ALL))

        if menu == "1":
            while True:
                text1 = "[bold red] 1. [/bold red][cyan] Tambah Barang[/cyan]"
                text2 = "[bold red] 2. [/bold red][cyan] Lihat Barang[/cyan]"
                text3 = "[bold red] 3. [/bold red][cyan] Update Barang[/cyan]"
                text4 = "[bold red] 4. [/bold red][cyan] Hapus Barang[/cyan]"
                text5 = "[bold red] 5. [/bold red][cyan] Cari Barang [/cyan]"
                text6 = "[bold red] 0. [/bold red][cyan] Kembali Ke Menu Utama[/cyan]"

                rprint(Panel(
                    f"{text1}\n{text2}\n{text3}\n{text4}\n{text5}\n{text6}",
                    expand=False,
                    title="[magenta]Daftar Menu Barang[/magenta]",
                    border_style="none",
                    padding=(1, 2)  # Add some padding for better appearance
                ))
                
                submenu = input("{}>{} Masukkan Pilihan Menu : ".format(Fore.MAGENTA, Style.RESET_ALL))

                if submenu == "1":
                    insert_barang(connection)
                    show_barang(connection)
                    while True:
                        tanya = input("Apakah ingin menambahkan data lain? (y/{}n{})".format(Fore.RED, Style.RESET_ALL))
                        if tanya == "y":
                            insert_barang(connection)
                        elif tanya == "n":
                            break
                
                elif submenu == "2":
                    while True:
                        
                        text1 = "[bold red] 1. [/bold red][cyan] T-Shirt [/cyan]"
                        text2 = "[bold red] 2. [/bold red][cyan] Outterwear [/cyan]"
                        text3 = "[bold red] 3. [/bold red][cyan] Bottoms [/cyan]"
                        text4 = "[bold red] 4. [/bold red][cyan] Accessories [/cyan]"
                        text5 = "[bold red] 5. [/bold red][cyan] Lihat Semua Barang [/cyan]"
                        text6 = "[bold red] 0. [/bold red][cyan] Kembali Ke Menu Utama [/cyan]"

                        rprint(Panel(
                        f"{text1}\n{text2}\n{text3}\n{text4}\n{text5}\n{text6}",
                        expand=False,
                        title="[magenta]Daftar Type Barang[/magenta]",
                        border_style="none",
                        padding=(1, 2)  # Add some padding for better appearance
                        ))

                        tanya = input("{}>{}Pilihlah Type Barang Yang Ingin Dilihat : ".format(Fore.MAGENTA, Style.RESET_ALL))
                        if tanya == "1":
                            show_TShirt(connection)
                        elif tanya == "2":
                            show_outterwear(connection)
                        elif tanya == "3":
                            show_bottoms(connection)
                        elif tanya == "4":
                            show_accessories(connection)
                        elif tanya == "5":
                            show_barang(connection)
                        elif tanya == "0":
                            break

                elif submenu == "3":
                    show_barang(connection)
                    update_barang(connection)
                    while True:
                        tanya = input("Apakah ingin mengupdate data lain? (y/{}n{})".format(Fore.RED, Style.RESET_ALL))
                        if tanya == "y":
                            update_barang(connection)
                        elif tanya == "n":
                            break
                    
                elif submenu == "4":
                    show_barang(connection)
                    hapus_barang(connection)

                elif submenu == "5":
                    search_barang(connection)

                elif submenu == "0":
                    break

                else :
                    print("Masukkan Angka Yang Sesuai Boy!")
                    time.sleep(2)

        elif menu == "2":
            while True:
                text1 = "[bold red] 1. [/bold red][cyan] Tambah Pegawai [/cyan]" # insert_pegawai
                text2 = "[bold red] 2. [/bold red][cyan] Lihat Data Pegawai [/cyan]" # show_pegawai
                text3 = "[bold red] 3. [/bold red][cyan] Update Data Pegawai [/cyan]" # update_pegawai
                text4 = "[bold red] 4. [/bold red][cyan] Pecat Pegawai [/cyan]" # hapus_pegawai  
                text5 = "[bold red] 0. [/bold red][cyan] Kembali Ke Menu Utama [/cyan]"

                rprint(Panel(
                    f"{text1}\n{text2}\n{text3}\n{text4}\n{text5}",
                    expand=False,
                    title="[magenta]Daftar Menu Pegawai[/magenta]",
                    border_style="none",
                    padding=(1, 2)  # Add some padding for better appearance
                ))

                submenupegawai = input("{}>{} Masukkan Pilihan Menu : ".format(Fore.MAGENTA, Style.RESET_ALL))

                if submenupegawai == "1":
                    insert_pegawai(connection)
                elif submenupegawai == "2":
                    show_pegawai(connection)
                elif submenupegawai == "3":
                    update_pegawai(connection)
                elif submenupegawai == "4":
                    hapus_pegawai(connection)
                elif submenupegawai == "0":
                    break
        
        elif menu == "3":
            while True:
                transaksi(connection)
                break
            print("{}TERIMA KASH SUDAH BERBELANJA DI TOKO KAMI!!!! {}".format(Fore.MAGENTA, Style.RESET_ALL))
        
        elif menu == "4":
            tampilkan_riwayat(connection)
            keluar = input("Klik {}x{} untuk keluar dari Riwayat transaksi : ".format(Fore.RED, Style.RESET_ALL))
            
        elif menu == "0":
            print("{}TERIMA KASH SUDAH BERKUNJUNG KE TOKO KAMI!!!! {}".format(Fore.RED, Style.RESET_ALL))
            break
            

if __name__ == "__main__":
    conn = connection()
    try:
        welcome()
        animasi_login()
        show_menu(conn)
    finally:
        conn.close()