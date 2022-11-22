data = [
	[],
	[],
	[
		[], [], []
	],
	[]
]
i = 0
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