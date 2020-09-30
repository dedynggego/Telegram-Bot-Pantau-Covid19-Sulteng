import requests

def indo1():
    url = 'https://apicovid19indonesia-v2.vercel.app/api/indonesia/more'
    result = requests.get(url).json()
    indo = [result]
    return indo
def prov():
    url = 'https://apicovid19indonesia-v2.vercel.app/api/indonesia/provinsi/more'
    result = requests.get(url).json()
    prov = result[32]
    prov_st = [prov]
    return prov_st

def rumahsakit():
    url = 'https://dekontaminasi.com/api/id/covid19/hospitals'
    rs = requests.get(url).json()
    rs = [rs]
    # harian_positif = harian_list[0]
    return rs

def detail():
    api_url = 'https://data.covid19.go.id/public/api/prov.json'
    result = requests.get(api_url).json()
    prov = result['list_data']
    detail_res = prov[32]
    ambil_detal = [detail_res]
    ambil_detal = ambil_detal[0]
    ambil_detal = ambil_detal['kelompok_umur']
    ambil_detal = ambil_detal
    return ambil_detal

# det = rumahsakit()
# for i in det:
#     print(i[110])



