#input
n = float(input("angka berapa ? :"))

satuan = ['', 'satu', 'dua', 'tiga', 'empat','lima', 'enam', 'tujuh', 'delapan', 'sembilan']


def terbilang(n):
    #koma
    if n%1>0:
        x=str(n)
        find = x.find(".")
        BelakangKoma = find+1
        hasilKoma = []
        hasilDepan=[]

        for v in x[0:find]:
            hasilDepan.append(v)

        for i in x[BelakangKoma:]:
            hasilKoma.append(i)

        PenggabunganDepanKoma="".join(hasilDepan)
        convertD=int(PenggabunganDepanKoma)
            
        PenggabunganKoma = "".join(hasilKoma)
        ConvertK=int(PenggabunganKoma)

        return terbilang (convertD) + " koma " + terbilang(ConvertK)
    
    #Satuan
    elif n < 10 :
        return satuan[int(n)]
    
    #Milyaran
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + " milyar " + terbilang(n % 1_000_000_000) 
    #jutaan
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + " juta " + terbilang(n % 1_000_000) 

    
    #ribuan
    elif n >= 1000:
        if n // 1000 == 1:
            return "seribu " + terbilang (n % 1000) 
        else:
            return terbilang(n // 1000) + " ribu " + terbilang (n % 1000) 
    
    #ratusan
    elif n >= 100 :
        if n // 100 == 1:
            return "seratus " + terbilang(n % 100) 
        else:
            return terbilang(n // 100) + " ratus " + terbilang(n % 100) 

    #puluhan
    elif n >= 20 :
        return terbilang(n // 10) + " puluh " + terbilang(n % 10) 

    #belasan
    elif n >= 10:
        if n == 10:
            return "sepuluh"
        elif n == 11:
            return "sebelas"
        else:
            return terbilang(n % 10) + " belas"

# test
if n % 1 > 0:
    print (f'{n} = {terbilang(n)}')
else:
    print (f'{int(n)} = {terbilang(n)}')
    