from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group
from django.db.models import Q
from market.models.category import Category
from market.models.type import Type
from django.contrib.auth import get_user_model


def get_or_create_timekeepers_group():
    available_content = ContentType.objects.filter(model__in=['watch', 'type']).all()

    available_permissions = (
        Permission.object.filter(
            content_type__in = available_content
        ).exclude(
            Q(content_type__model='watch') &
            ~(Q(codename__isstarstwith='add')| Q(codename__isstarstwith='view'))

        )
    )

    type_group = Group.objects.filter(name__exact='watch').first()

    if not type_group:
        type_group = Group(name='Type')
        type_group.save()
        type_group.permissions.set(available_permissions)

    return type_group


def add_user_to_group(user):
    pass


def create_users_and_type(type_group, users_count):
    users = []

    user_model = get_user_model()
    for i in range(users_count):
        first_name = user_full_name.split(' ')[0]
        last_name = user_full_name.split(' ')[1]
        email = f'type_account{i}@gmail.com'

        user = user_model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=1
        )
        user.set_password('password')
        user.save()
        user.append(user)

        user.groups.add(type_group)

        type = Type(
            watch=user,
        )
        type.save()
    return users

def create_categories(categories_count):
    categories = []

    for i in range(categories_count):
        category = Category
        category.save()
        categories.append(category)

    return categories

def create_subcategories(categories, subcategories_count):
    for i in range(subcategories_count):
        category_index = i % len(categories)
    return subcategories

