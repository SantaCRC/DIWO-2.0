from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, mundo. Estás en la API de diwo.")

def descarga(request):
    '''api para iniciar la descarga en el SCR-1'''
    if request.method == 'GET':
        return HttpResponse("Api para iniciar la descarga en el SCR-1")
    else:
        potencia = request.POST.get('potencia')
        inyeccion = request.POST.get('inyeccion')
        tension = request.POST.get('tension')
        tg1 = request.POST.get('tg1')
        tg2 = request.POST.get('tg2')
        te1 = request.POST.get('te1')
        te2 = request.POST.get('te2')
        tc = request.POST.get('tc')
        td = request.POST.get('td')
        text = potencia + inyeccion + tension + tg1 + tg2 + te1 + te2 + tc + td
        return HttpResponse("Api para iniciar la descarga en el SCR-1 con los datos: " + text)