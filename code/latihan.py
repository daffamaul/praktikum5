data = ['a', 'b', 'c', 'd', 'e']

# akses list
# menampilkan data yang ke-3
print(data[2])
# output: c
# mengambil element ke-2 sammpai ke-4
print(data[1:4])
# output: ['b', 'c', 'd']
# mengambil nilai terakhir 
print(data[4])
# output: e

# ubah element list
# ubah elemen ke-4 dengan nilai lainnya
data[3] = "f"
print(data)
# output: ['a', 'b', 'c', 'f', 'e']
# ubah elemen ke-4 sampai dengan elemen terakhir
data[2:5] = ['g', 'h', 'i']
print(data)
# output: ['a', 'b', 'g', 'h', 'i']

# tambah element list
# ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
data1 = data[:3]
data2 = data[3:5]
print(data1, data2)
# output: ['a', 'b', 'g'] ['h', 'i']
# tambah list B (data2) dengan nilai integer
print(data2 + [1])
# output: ['h', 'i', 1] 
# tambah list B (data2) dengan tiga nilai
data2.extend([0.1, "hello", 'b'])
print(data2)
# output: ['h', 'i', 0.1, 'hello', 'b']
# menggabungkan kedua list
data = data1 + data2
print(data)
# output: ['a', 'b', 'g', 'h', 'i', 0.1, 'hello', 'b']

