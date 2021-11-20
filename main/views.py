from django.shortcuts import render

from .models import *

menu = ['Home', 'Books', 'Films', 'Games', 'Add recommendation']
# posts = [
#     {'title': 'Анна Каренина', 'content': '''Как и добрая половина рецензентов,
#     оставивших отзывы к этому изданию, "Анну Каренину" не брала в руки со школьных времен,
#     а тут прямо потянуло перечитать.''', 'image': 'main/images/1.jpg'},
#     {'title': 'Маттео Струкул: Соната разбитых сердец', 'content': '''Этим человеком восхищались даже заклятые враги:
#     они поражались и завидовали беспечной легкости,
#     с которой он подчинял жизнь своим желаниям,
#     вместо того чтобы самому подстраиваться под обстоятельства. ''',
#      'image': 'main/images/2.png'},
#     {'title': 'Великий гэтсби', 'content': '''"Бурные" двадцатые годы прошлого столетия…
#     Время шикарных вечеринок, "сухого закона" и "легких" денег…''',
#      'image': 'main/images/3.jpg'}
# ]
all_posts = Post.objects.all()
last_post = all_posts.last()
images = Image.objects.all()

def home(requests):

    return render(requests, 'main/index.html', {'title': 'Recommendation',
                                                'nav_buttons': menu,
                                                'posts': all_posts,
                                                'last_post': last_post,
                                                'image': images})


def post(requests):
    return render(requests, 'main/post.html', last_post)


def categories(requests):
    return render(requests, 'main/categories.html')
