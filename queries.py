from django.db.models import Count, Q, Max

from models import Author, Book, Sales

task_1 = Book.objects.filter(publish_date__year__gt=2000).count()
task_2 = Book.objects.exclude(name__icontains="a").values("authors__name")
task_3_1_1 = Book.objects.order_by("publish_date").last()
task_3_1_2 = Book.objects.latest("publish_date")
task_3_2_1 = Book.objects.order_by("publish_date").first()
task_3_2_2 = Book.objects.earliest("publish_date")
task_4 = Author.objects.annotate(Count("books"))
task_5 = Author.objects.alias(Count("books")).filter(books__gt=5)
task_6 = Book.objects.values("publish_date", "name").distinct("publish_date")
task_7 = Book.objects.values("publisher__name")
task_8 = Author.objects.values(
    "books__name",
    "books__authors__name",
    "books__publisher_name",
    "books__publish_date",
)
task_9 = Author.objects.raw("SELECT * FROM orm_author")
task_10 = Book.objects.filter(id=100).exists()
task_11 = Book.objects.filter(
    Q(authors__birth_day__year__range=(1500, 1600))
    | Q(authors__birth_day__year__range=(1700, 1800))
)
task_12 = Book.objects.get_or_create(
    name="Эйвыйцйвйцвцй",
    defaults={"publisher_id": 1, "publish_date": "2020-02-02", "price": 470},
)
task_13 = Book.objects.bulk_create(
    [
        Book(name="One", publisher_id=1, publish_date="2020-02-02", price=470),
        Book(name="Two", publisher_id=1, publish_date="2020-02-02", price=470),
        Book(name="Three", publisher_id=1, publish_date="2020-02-02", price=470),
        Book(name="Four", publisher_id=1, publish_date="2020-02-02", price=470),
        Book(name="Five", publisher_id=1, publish_date="2020-02-02", price=470),
    ]
)
task_14 = Author.objects.values("birth_day").earliest("birth_day")
task_15 = Book.objects.filter(price=Book.objects.aggregate(max=Max("price"))["max"])
task_16 = Book.objects.filter(
    price__gt=Sales.objects.get(date="2002-02-20").total_sold_usd
)
