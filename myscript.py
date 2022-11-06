import os
os.system("git bisect start c1a4be e4cfc6 --")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")