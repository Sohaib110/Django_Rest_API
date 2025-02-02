from django.http import HttpResponse, JsonResponse


def home_page(request):
    print('home_page')
    friends = ['John', 'Jane', 'Jack']
    return JsonResponse(friends, safe=False)  