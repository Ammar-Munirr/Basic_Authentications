from django.shortcuts import redirect


def redirect_api(request):
    return redirect('schema-swagger-ui')