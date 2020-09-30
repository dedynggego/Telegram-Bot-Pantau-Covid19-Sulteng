import data

rs = data.rumahsakit()

def undata():
    nama = ''
    alamat = ''
    region = ''
    telp = ''

    for i in rs:
        nama = i[110]['name'] #mengambil data RS undata yang berada di index 110
        alamat = i[110]['address'] 
        region = i[110]['region'] 
        telp = i[110]['phone'] 

    data = "Nama: {}\n Alamat: {}\n Region: {}\n Telepon: {}\n".format(nama, alamat, region,telp)
    return data
    
def anutapura():
    nama = ''
    alamat = ''
    region = ''
    telp = ''

    for i in rs:
        nama = i[111]['name'] #mengambil data RS anutapura yang berada di index 111
        alamat = i[111]['address'] 
        region = i[111]['region'] 
        telp = i[111]['phone'] 

    data = "Nama: {}\n Alamat: {}\n Region: {}\n Telepon: {}\n".format(nama, alamat, region,telp)
    return data

def toli_toli():
    nama = ''
    alamat = ''
    region = ''
    telp = ''

    for i in rs:
        nama = i[112]['name'] #mengambil data RS toli-toli yang berada di index 112
        alamat = i[112]['address'] 
        region = i[112]['region'] 
        telp = i[112]['phone'] 

    data = "Nama: {}\n Alamat: {}\n Region: {}\n Telepon: {}\n".format(nama, alamat, region,telp)
    return data

def kolodale():
    nama = ''
    alamat = ''
    region = ''
    telp = ''

    for i in rs:
        nama = i[113]['name'] #mengambil data RS kolonodale yang berada di index 113
        alamat = i[113]['address'] 
        region = i[113]['region'] 
        telp = i[113]['phone'] 

    data = "Nama: {}\n Alamat: {}\n Region: {}\n Telepon: {}\n".format(nama, alamat, region,telp)
    return data

def banggai():
    nama = ''
    alamat = ''
    region = ''
    telp = ''

    for i in rs:
        nama = i[114]['name'] #mengambil data RS banggai yang berada di index 114
        alamat = i[114]['address'] 
        region = i[114]['region'] 
        telp = i[114]['phone'] 

    data = "Nama: {}\n Alamat: {}\n Region: {}\n Telepon: {}\n".format(nama, alamat, region,telp)
    return data