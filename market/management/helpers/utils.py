from market.models.category import Category, Subcategory
from django.db.models import Max
from market.models.type import Type

def get_max_ids():
    all_categories = Category.objects.all()
    category_max_id = all_categories.aggregate(Max('id'))['id__max'] if len(all_categories)>0 else 0

    all_subcategories = Subcategory.objects.all()
    subcategory_max_id = all_subcategories.aggregate(Max('id'))['id__max'] if len(all_subcategories)>0 else 0

    all_types = Type.objects.all()
    type_max_id = all_types.aggregate( Max('id'))['id__max'] if len(all_types)>0 else 0

    return category_max_id, subcategory_max_id, type_max_id

def create_category(category_max_id,index):
    category = Category(name=f'Command Category {category_max_id + 1 + index}')
    category.save()

    return category

def create_subcategories(categories, subcategory_max_id, subcategories_count):
    subcategories = []
    subcategory_index = 0
    category_index = 0
    categories_count = len(categories)

    while subcategory_index < subcategories_count:
        if category_index >= categories_count:
            category_index = 0

        current_category = categories[category_index]

        subcategory = Subcategory(
            name=f'Command Subcategory {subcategory_max_id + 1 + subcategory_index}',
            category=current_category)
        subcategory.save()
        subcategories.append(subcategory)

        subcategory_index += 1
        category_index += 1

    return subcategories

def create_types(subcategories, type_max_id, types_count):
    types = []
    type_index = 0
    subcategory_index = 0
    subcategories_count = len(subcategories)

    while type_index < types_count:
        if subcategory_index >= subcategories_count:
            subcategory_index = 0

        current_subcategory = subcategories[subcategory_index]

        type = Type(
            name=f'{type_max_id + 1 + type_index}',
            case_material=f'{type_max_id + 1 + type_index}',
            bracelet_material=f'{type_max_id + 1 + type_index}',
            caliber=f'{type_max_id + 1 + type_index}',
            gender=f'{type_max_id + 1 + type_index}',
            subcategory=current_subcategory)
        type.save()
        types.append(type)

        type_index += 1
        subcategory_index += 1

    return types


