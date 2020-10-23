from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context, loader
# Create your views here.

def index(request):
    data = {
        "name": "rock",
        "age": 25
    }
    data_1 = ["devops", "python"]
    # return HttpResponse("Hello World !!!")
    return JsonResponse(data_1, safe=False )

def index_template(request):
    # t = loader.get_template("test.html")
    # context = {"name": "hello reboot !!!"}
    # return HttpResponse(t.render(context, request))
    context = {"name": "reboot"}
    return render(request, "test.html", context )
