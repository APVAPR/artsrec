from django.shortcuts import render

menu = ['Home', 'Books', 'Films', 'Games']
posts = [
    {'title': 'Анна Каренина', 'content': '''Как и добрая половина рецензентов, 
    оставивших отзывы к этому изданию, "Анну Каренину" не брала в руки со школьных времен, 
    а тут прямо потянуло перечитать.''', 'image': 'main/images/1.jpg'},
    {'title': 'Маттео Струкул: Соната разбитых сердец', 'content': '''Этим человеком восхищались даже заклятые враги: 
    они поражались и завидовали беспечной легкости, 
    с которой он подчинял жизнь своим желаниям, 
    вместо того чтобы самому подстраиваться под обстоятельства. ''',
     'image': 'main/images/2.png'},
    {'title': 'Великий гэтсби', 'content': '''"Бурные" двадцатые годы прошлого столетия…
    Время шикарных вечеринок, "сухого закона" и "легких" денег…''',
     'image': 'main/images/3.jpg'}
]


def home(requests):
    return render(requests, 'main/index.html', {'title': 'Recommendation', 'nav_buttons': menu, 'posts': posts})


def categories(requests):
    return render(requests, 'main/categories.html')
