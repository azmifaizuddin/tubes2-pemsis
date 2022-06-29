M = 100 # Batas Lintasan Makasimum
p = 0.3 # Probabilitas
v0 = 0  # Kecepatan Awal
N = 20  # Jumlah kendaraan
dt = 1  # Jarak Antar Waktu
vmax = 5    # Batas Kecepatan Maksimum
tmax = 1000 # Batas waktu untuk di iterasikan
t = 0       # Waktu Awal

arr_mobil = []  # list mobil
x0 = []   # posisi awal mobil
v = []         #list kecepatan masing masing mobil tiap detik
v = [0]*N       #inisiasi v0 tiap mobil = 0 
kepadatan_mobil = []  #kepadatan mobil pada selang x 80 & x90
t_kembali = []
t_kembali = [0]*N    # waktu dr tiap untuk kemabali posisi semula
total_putaran = []
total_putaran = [0]*N  # semua mobil melewati posisi awal
interval = [0]*20
warna = ['#898176', '#D36E70', '#18171C', '#382C1E', '#6D6552',
         '#F80000', '#B32821', '#4E5754', '#CAC4B0', '#31372B',
         '#354D73', '#633A34', '#898176', '#FF00FF', '#C1876B',
         '#C51D34','#F8F32B','#1C542D','#2A6478','#025669']