import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_lv2.settings')

import django
django.setup()

from faker import Faker
fakegen = Faker()

from lv2_app.models import User
def populate(N=5):
    for _ in range(N):
        fn = fakegen.first_name()
        ln = fakegen.last_name()
        em = fakegen.email()

        users = User.objects.get_or_create(first_name=fn, last_name=ln, email=em)

if __name__=='__main__':
    print('start populating')
    populate(20)
    print('done')