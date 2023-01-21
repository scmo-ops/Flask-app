import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' # the value of the secret key is that it has two terms. 



    # Using the principle of separation of concers, it was decided to separate  the config argument into a separate file, so we are storing config into a class