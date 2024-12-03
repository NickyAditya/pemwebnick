#Nicky aditya bagus
#152023065
#BB
data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },

    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },

    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },

    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },

    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
}

print(f"Semua Data Panen Setiap Lokasi")
for i,j in data_panen.items():
    print(f"{i}{j}")

print(f"\nHasil Panen Jagung Lokasi 2")
print(f"Hasil Jagung : ",data_panen['lokasi2']['hasil_panen']['jagung'])

print(f"\nNama Lokasi Panen 3")
print(f"Nama Lokasi 3 : ",data_panen['lokasi3']['nama_lokasi'])

hasil_padi = {}
hasil_kedelai = {}
for i,j in data_panen.items():
    hasil_padi[i] = j['hasil_panen']['padi']
    hasil_kedelai[i] = j['hasil_panen']['kedelai']
print("\nJumlah Hasil Panen Padi Setiap Lokasi:",hasil_padi)
print("Jumlah Hasil Panen Kedelai Setiap Lokasi:",hasil_kedelai)

print("\nStatus Setiap Lokasi")
for i,j in data_panen.items():
    padi = j['hasil_panen']['padi']
    jagung = j['hasil_panen']['jagung']
    lokasi = j['nama_lokasi']
    if padi > 1300 or jagung > 800:
        print(f"{lokasi}: Memerlukan Perhatian Khusus")
    else:
        print(f"{lokasi}: Dalam kondisi Baik")