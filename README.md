# Flowchart Program
![flowchart](/gambar/2.png)
> **Flowchart** adalah sebuah rancangan sebelum tahap coding yang biasanya disebut pada tahap ini adalah tahap pra-code, membuat alur program yang akan diimplementasikan kedalam program dengan menggunakan bahasa program yang dibutuhkan.

# Penjelasan Code 
## Tahap Deklarasi
```python
data = [
	[],
	[],
	[
		[], [], []
	],
	[]
]
i = 0
```
> Di atas adalah tipe data array kosong yang berdimensi untuk menyimpan sebuah inputan dari user dan 'i' menunjukkan tipe data integer yang berisi nilai 0

## Tahap Logika Program
```python
while True:
	nama = input('nama = ')
	data[0].append(nama)
	nim = int(input('nim = '))
	data[1].append(nim)
	nilaiTugas = int(input('nilai tugas = '))
	data[2][0].append(nilaiTugas)
	nilaiUts = int(input('nilai UTS = '))
	data[2][1].append(nilaiUts)
	nilaiUas = int(input('nilai uas = '))
	data[2][2].append(nilaiUas)
	nilaiAkhir = (nilaiTugas * .3) + (nilaiUts * .35) + (nilaiUas * .35)
	data[3].append(nilaiAkhir)
```
> Pada tahap ini, user diminta untuk menginput yang diinginkan oleh program dan program akan menyimpan inputan tersebut ke dalam array yang sudah disediakan, array tersebut sudah diberi indeks (daftar) untuk menyimpan data secara mudah

```python
	user = (' ')
	while user != 'y' and user != 'n':
		user = input('Tambah data [y/n] = ')
		i += 1
	if user ==  'n':
    print("+----+---------------------+-----------------+-------+-------+-------+---------------+")
		print("| No | Nama                | NIM             | Tugas | UTS   | UAS   | Nilai Akhir   |")
		print("+----+---------------------+-----------------+-------+-------+-------+---------------+")
		for n in range(i):
			print("|", n+1, " |", data[0][n+1-1], "\t   |", data[1][n+1-1], "\t     |", data[2][0][n+1-1], "   |", data[2][1][n+1-1], "   |", data[2][2][n-1+1], "   |",  data[3][n-1+1],"\t     |" )	
		print("+----+---------------------+-----------------+-------+-------+-------+---------------+")
		break
```
> Pada tahap selanjutnya, user diminta, apakah ada penambahan data? Jika ada, maka user diminta untuk menginputkan data kembali. Jika tidak, maka data yang sudah diinputkan akan ditampilkan pada user, tampilan tersebut di bawah ini.
![output](/gambar/1.png)
