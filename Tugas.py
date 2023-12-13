import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
hitung_peningkatan_gaji = lambda gaji: gaji * 0.05
for i, row in df.iterrows():
    df.at[i, 'Gaji_Setelah_Peningkatan'] = hitung_peningkatan_gaji(row['Gaji']) + row['Gaji']

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame Setelah diperbarui:")
print(df)

# Ringkasan
print("\nRingkasan Perubahan:")
for i, row in df.iterrows():
    print(f"Gaji {row['Nama']} sebelumnya: {row['Gaji']}, Gaji setelah peningkatan: {row['Gaji_Setelah_Peningkatan']}")

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
evaluasi_gaji_lebih_30 = lambda gaji: gaji * 1.02
for i, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[i, 'Gaji_Usia_Lebih_30Tahun'] = evaluasi_gaji_lebih_30(row['Gaji_Setelah_Peningkatan'])
    else:
        df.at[i, 'Gaji_Usia_Lebih_30Tahun'] = row['Gaji_Setelah_Peningkatan']

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("DataFrame Setelah diperbarui:")
print(df)

# Ringkasan
print("\nRingkasan Perubahan:")
for i, row in df.iterrows():
    print(f"Gaji {row['Nama']} sebelumnya: {row['Gaji_Setelah_Peningkatan']}, Gaji setelah peningkatan: {row['Gaji_Usia_Lebih_30Tahun']:.2f}")

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.