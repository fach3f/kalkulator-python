print('Muchammad Fahrizal')                          #printout
print('152021005')                                   #printout
print('Kalkulator')                                  #printout
print('  1. Jumlah  [+]')                            #printout
print('  2. Kurang  [-]')                            #printout
print('  3. Kali    [*]')                            #printout
print('  4. Bagi    [/]')                            #printout

operasi = input('Pilih operasi (1/2/3/4): ')                     #inputan masuk ke variable operasi            
bilangan_1 = eval(input('Masukkan bilangan pertama: '))           #inputan masuk ke variable bilangan_1
bilangan_2 = eval(input('Masukkan bilangan kedua: '))               #inputan masuk ke variable bilangan_2

if operasi == '1':                                                         #jika user memasukan angka 1
  hasil = bilangan_1 + bilangan_2                                           #rumus operasi matematika penjumlahan        
  print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')        #hasil output
elif operasi == '2':                                                       #jika user memasukan angka 2        
  hasil = bilangan_1 - bilangan_2                                            #rumus operasi matematika pengurangan             
  print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')         #hasil output
elif operasi == '3':                                                        #jika user memasukan angka 3   
  hasil = bilangan_1 * bilangan_2                                            #rumus operasi matematika perkalian
  print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')        #hasil output
elif operasi == '4':                                                        #jika user memasukan angka 4   
  hasil = bilangan_1 / bilangan_2                                            #rumus operasi matematika pembagian
  print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')        #hasil output
else:
  print('Tidak valid')