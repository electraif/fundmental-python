#tipe data skalar  =>  sederhana
anak1 = 'eko'
anak2 = 'telo'
anak3 = 'paijo'
anak4 = 'sukirno'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')

anak = ['eko', 'telo', 'paijo', 'sukirno']
print(anak)
anak.append('karto')
print(anak)

print('\nsapa anak')

print(f'hai {anak[1]}')

print('\nsapa semua anak')

for a in anak:
    print(f' hai {a}!')

print('\nsapa semua anak: cara ribet')

for a in range(0,len(anak)):
    print(f'{a+1}. hai {anak[a]}!')



