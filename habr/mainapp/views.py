from django.shortcuts import render


def index(request):
    """
    контроллер, возврящающий главную страницу со списком всех статей сайта
    """

    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)

