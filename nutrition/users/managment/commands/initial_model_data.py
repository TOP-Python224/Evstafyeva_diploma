from django.core.management import BaseCommand

from users.models import Activity

activities = [
    Activity(activity_name='Аквааэробика', burned_calories=8),
    Activity(activity_name='Бадминтон', burned_calories=4),
    Activity(activity_name='Баскетбол', burned_calories=5),
    Activity(activity_name='Бег', burned_calories=7),
    Activity(activity_name='Волейбол', burned_calories=4),
    Activity(activity_name='Гимнастика', burned_calories=2),
    Activity(activity_name='Дайвинг', burned_calories=5),
    Activity(activity_name='Езда на велосипеде', burned_calories=5),
    Activity(activity_name='Йога', burned_calories=6),
    Activity(activity_name='Кардиотренировка', burned_calories=8),
    Activity(activity_name='Катание на коньках', burned_calories=4),
    Activity(activity_name='Катание на роликах', burned_calories=4),
    Activity(activity_name='Плавание', burned_calories=5),
    Activity(activity_name='Растяжка', burned_calories=2),
    Activity(activity_name='Силовая тренировка', burned_calories=7),
    Activity(activity_name='Танцы', burned_calories=5),
    Activity(activity_name='Ходьба', burned_calories=4),
    Activity(activity_name='Ходьба на лыжах', burned_calories=7),
    Activity(activity_name='Футбол', burned_calories=6),
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for activity in activities:
            activity.save()
            activity.add()
        self.stdout.write('Data successfully inserted')


# authors = [
#     Author(first_name='Лоис', last_name='Буджолд'),
#     Author(first_name='Сергей', last_name='Лукьяненко'),
#     Author(first_name='Рэй', last_name='Брэдбери'),
# ]
# books = [
#     Book(title='Осколки чести', author=authors[0]),
#     Book(title='Барраяр', author_id=1),
#     Book(title='Спектр', author_id=2),
#     Book(title='Осенние визиты', author_id=2),
#     Book(title='Вино из одуванчиков', author=authors[2]),
#     Book(title='Электрическое тело, пою', author=authors[2]),
# ]
# publishers = [
#     Publisher(name='АСТ'),
#     Publisher(name='Эксмо'),
# ]


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         for author in authors:
#             author.save()
#         for book in books:
#             book.save()
#         for pub in publishers:
#             pub.save()
#
#         ast, eksmo = publishers
#
#         ast.authors.add(authors[1], authors[2])
#         ast.books.add(*books[3:])
#
#         eksmo.authors.add(authors[0], authors[1])
#         eksmo.books.add(*books[:3])
#
#         self.stdout.write('Data successfully inserted')


# (InteractiveConsole)
# >>>
# >>> from catalog.models import Author, Book, Publisher
# >>>
# >>> Author.objects
# <django.db.models.manager.Manager object at 0x0000027E83A1D3F0>
# >>>
# >>> Author.objects.all()
# <QuerySet [<Author: Лоис Буджолд>, <Author: Сергей Лукьяненко>, <Author: Рэй Брэдбери>]>
# >>>
# >>> Author.objects.filter(first_name='Лоис')
# <QuerySet [<Author: Лоис Буджолд>]>
# >>>
# >>> Author.objects.get(pk=1)
# <Author: Лоис Буджолд>
# >>>
# >>>
# >>> spectr = Book.objects.get(pk=3)
# >>>
# >>> spectr
# <Book: Спектр>
# >>>
# >>> spectr.author
# <Author: Сергей Лукьяненко>
# >>>
# >>> spectr.author_id
# 2
# >>>
# >>> Publisher.objects.all()
# <QuerySet [<Publisher: АСТ>, <Publisher: Эксмо>]>
# >>>
# >>> ast = Publisher.objects.all()[0]
# >>> ast
# <Publisher: АСТ>
# >>>
# >>> ast.authors
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x0000027E83A1EC50>
# >>>
# >>> ast.authors.all()
# <QuerySet [<Author: Сергей Лукьяненко>, <Author: Рэй Брэдбери>]>
# >>>
# >>> Publisher.objects.all()[1].authors.all()
# <QuerySet [<Author: Лоис Буджолд>, <Author: Сергей Лукьяненко>]>
# >>>
# >>> ast.books.all()
# <QuerySet [<Book: Осенние визиты>, <Book: Вино из одуванчиков>, <Book: Электрическое тело, пою>]>
# >>>
# >>> luc = Author.objects.get(pk=2)
# >>>
# >>> luc.book_set
# <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x0000027E838C3E20>
# >>>
# >>> luc.book_set.all()
# <QuerySet [<Book: Спектр>, <Book: Осенние визиты>]>
# >>>
