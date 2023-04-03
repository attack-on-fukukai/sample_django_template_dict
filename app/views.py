from django.shortcuts import render


def index(request):

    dict_data = {
        'key1': 'spam',
        'key2': 'ham',
    }

    target_key = 'key1'

    context = {
        'dict_data': dict_data,
        'target_key': target_key,
    }

    return render(request, 'index.html', context)
