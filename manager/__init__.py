from flask import Flask

admin = Flask(__name__)
admin.config['SECRET_KEY'] = 'Hard to guess!'

from manager import main
from manager import worker
#from manager import autoscaling