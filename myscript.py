import os
os.system("git bisect start c1a4be0 e4cfc6f")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")