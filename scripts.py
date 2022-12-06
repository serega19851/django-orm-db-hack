from datacenter.models import (
    Schoolkid,
    Mark,
    Chastisement,
    Lesson,
    Commendation
)
import random
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def fix_marks(schoolkid):
    return (
        Mark.objects.filter(
            schoolkid__full_name=schoolkid
        ).filter(points__lt=4).update(points=5)
    )


def remove_chastisements(schoolkid):
    return Chastisement.objects.filter(schoolkid__full_name=schoolkid).delete()


def create_commendation(schoolkid, subject):
    praise_texts = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Замечательно!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!"
    ]
    try:
        Schoolkid.objects.get(full_name__contains=schoolkid)
    except MultipleObjectsReturned:
        print("Schoolkid.MultipleObjectsReturned")
    except ObjectDoesNotExist:
        print("Schoolkid.DoesNotExist")
    else:
        commendation = Commendation.objects.create(
            text=random.choice(praise_texts),
            created=Lesson.objects.filter(
                subject__title=subject,
                year_of_study__contains=6,
                group_letter__contains="А"
            ).order_by('-subject').first().date,
            schoolkid=Schoolkid.objects.get(
                full_name__contains=schoolkid
            ),
            subject=Lesson.objects.filter(
                subject__title=subject,
                year_of_study__contains=6,
                group_letter__contains="А"
            ).order_by('-subject').first().subject,
            teacher=Lesson.objects.filter(
                subject__title=subject,
                year_of_study__contains=6,
                group_letter__contains="А"
            ).order_by('-subject').first().teacher
        )
        return commendation
