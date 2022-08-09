from django.http import HttpResponse,JsonResponse
from evrekabackend.models import NavigationRecord,Bin
import datetime


def index(request):
    return HttpResponse("Merhaba dünya :)")

def results(request):
    get_results = NavigationRecord.objects.filter(datetime__gt=datetime.datetime.now() - datetime.timedelta(hours=48)).select_related("vehicle").values("latitude", "longitude", "vehicle__plate", "datetime")
    return JsonResponse(list(get_results),safe=False)

def results2(request):
    get_results = Bin.objects.all().values("collection__operation__name", "collection__frequency")
    return JsonResponse(list(get_results),safe=False)

