from django.core.management.base import BaseCommand
from market.management.helpers.utils import get_max_ids, create_category, create_subcategories
from market.management.helpers.utils import create_types


class Command(BaseCommand):
    help = 'Seed DB for market application.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--categories', '-cc',
            type=int,
            help='Number of categories to seed.',
            default=5
        )

        parser.add_argument(
            '--subcategories', '-sc',
            type=int,
            help='Number of subcategories to seed.',
            default=20
        )

        parser.add_argument(
            '--types', '-tc',
            type=int,
            help='Number of types to seed.',
            default=100
        )

    def handle(self, *args, **options):
        categories_count = options.get('categories')
        subcategories_count = options.get('subcategories')
        types_count = options.get( 'types' )
        category_max_id, subcategory_max_id , type_max_id = get_max_ids()

        # categories = []

        # for index in range(categories_count):
        # category = create_category(category_max_id, index)
        # categories.append(category)

        categories = [
            create_category(category_max_id, index)
            for index in range(categories_count)
        ]

        subcategories = create_subcategories(categories, subcategory_max_id, subcategories_count)
        types = create_types(subcategories, type_max_id, types_count)

        #subcategories = create_foreign_key_objects(Subcategory, categories, subcategory_max_id, subcategories_count)
        #watches = create_foreign_key_objects(Watch, subcategories, book_max_id, watches_count)
