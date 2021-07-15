import sys

sensorInput = "$GPGGA,134658.00,5106.9792,N,11402.3003,W,2,09,1.0,1048.47,M,-16.27,M,08,AAAA*60"
lista = sensorInput.split(   ","  )
utcDecoter = lista
hr = lista[1][:2]
min =  lista[1][2:4]
sec = lista[1][4:6]
lista[1] = f'hr: {hr}, min: {min}, sec: {sec}'
if __name__ == "__main__":
    print("GPS ACTIVITY")

    ##Convertir inputs en la lists##
    print("Header config:", lista[0])
    print("utc:",lista[1] )
    print("Latitud: ", lista[2], "Latitud_dir:", lista[3])
    print("Longitud:", lista[4], "Longitud_dir:",lista[5])
    print("Quality indicator:", lista[6])

    gps = {"HeaderConfig":lista[0], "UTC":lista[1],"Latitud": f'{lista[2]} {lista[3]}' ,"Longitud": f'{lista[4]} {lista[5]}' }
    print(gps['Latitud'])
    # sensorFixed  = ",".join(gps)
    # print(sensorFixed)

