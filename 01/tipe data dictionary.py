kamus = {}
kamus['anak'] = 'son'
kamus['ayah'] = 'father'
kamus['istri'] = 'wife'
kamus['ibu'] = 'mother'

print(kamus)

print(kamus['ayah'])
print(kamus['anak'])
print(kamus['ibu'])
print(kamus['istri'])

print('\n kebalikannya')
k = {}
k['son'] = 'anak'
k['mother'] = 'ibu'
k['father'] = 'ayah'
k['wife'] = 'istri'

print(k)
print(k['son'])
print(k['wife'])
print(k['father'])
print(k['mother'])

print(('\n data ini diberkan oleh server gojek,untuk memberi info driver di sekitar.'))
data_dari_gojek = {
    'tanggal' : '19-agustus-2021',
    'driver_list' : [{'nama' : 'eko', 'jarak' : 10},
                     {'nama' : 'telo', 'jarak' :  100 },
                     {'nama' : 'paijo', 'jarak' : 30},
                     {'nama' : 'sukirno', 'jarak' : 1000}]
}
print(data_dari_gojek)
print(f"\n driver disekitar sini {data_dari_gojek['driver_list']}")
print(f"driver 1. {data_dari_gojek['driver_list'][0]}")
print(f"driver 3. {data_dari_gojek['driver_list'][2]}")

print(f"\n driver terdekat 1. {data_dari_gojek['driver_list'][0]['jarak']} meter ")
print(f" driver terdekat 2. {data_dari_gojek['driver_list'][2]['jarak']} meter ")
print(f" driver terdekat 3. {data_dari_gojek['driver_list'][3]['jarak']} meter ")
print(f" driver terdekat 4. {data_dari_gojek['driver_list'][1]['jarak']} meter ")


