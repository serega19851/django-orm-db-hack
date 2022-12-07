from datacenter.models import (
    Schoolkid,
    Mark,
    Chastisement,
    Lesson,
    Commendation
)
import random
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

PRAISE_TEXTS = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Замечательно!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!"
]


def fix_marks(schoolkid):
    return Mark.objects.filter(
        schoolkid__full_name=schoolkid
    ).filter(points__lt=4).update(points=5)


def remove_chastisements(schoolkid):
    return Chastisement.objects.filter(schoolkid__full_name=schoolkid).delete()


def create_commendation(schoolkid, subject):
    subjected = Lesson.objects.filter(
        subject__title=subject
    ).order_by('-subject').first()
    school_kid = Schoolkid.objects.get(full_name__contains=schoolkid)
    try:
        school_kid
    except Schoolkid.ObjectsReturned:
        raise MultipleObjectsReturned(
            'Найдено несколько учеников, уточните ФИО'
        )
    except Schoolkid.DoesNotExist:
        raise ObjectDoesNotExist("Ученика не существует")
    else:
        commendation = Commendation.objects.create(
            text=random.choice(PRAISE_TEXTS),
            created=subjected.date,
            schoolkid=school_kid,
            subject=subjected.subject,
            teacher=subjected.teacher
        )
        return commendation
