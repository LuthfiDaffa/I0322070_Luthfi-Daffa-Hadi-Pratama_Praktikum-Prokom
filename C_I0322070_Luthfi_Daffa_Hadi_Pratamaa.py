# no 2 aplikasi penjualan rumah
# report 1 yang harus dibuat
utang = float(input('Masukkan jumlah utangnya '))
bunga = float(input('Masukkan suku bunga tahunannya '))
lama_pinjaman = float(input('Masukkan lama pinjaman dalam tahunnya '))

# Perhitungan Report 1
cicilan_pokok_bulanan = utang / lama_pinjaman
cicilan_bunga_bulanan = (bunga * utang * lama_pinjaman) / (lama_pinjaman * 12)
total_cicilan_setiap_bulan = cicilan_pokok_bulanan + cicilan_bunga_bulanan

# Output Report 1
print('Cicilan pokok bulanannya = ', cicilan_pokok_bulanan)
print('Cicilan bunga bulanannya = ', cicilan_bunga_bulanan)
print('Total cicilan setiap bulannya = ', total_cicilan_setiap_bulan)

# report 2 yang harus dibuat: total pembayaran pertama yang harus disiapkan calon pembeli
harga_rumah = float(input('Masukkan harga rumah: '))
cicilan_bulanan_pertama = float(input('Masukkan cicilan bulanan pertama: '))
biaya_notaris = 2000000
print('biaya notarisnya adalah =', biaya_notaris)
biaya_provisi = 1500000
print('biaya provinsinya adalah =', biaya_provisi)
pajak_pembelian = float(input('Masukkan pajak pembelian: '))
PNBP = 650000
print('biaya PNBPnya adalah =', PNBP)
biaya_balik_nama = 1500000
print('biaya balik namanya adalah =', biaya_balik_nama)

# Perhitungan report 2
uang_muka = harga_rumah - (cicilan_bulanan_pertama + biaya_notaris + biaya_provisi + pajak_pembelian + PNBP + biaya_balik_nama)
total_pembayaran_pertama = harga_rumah































