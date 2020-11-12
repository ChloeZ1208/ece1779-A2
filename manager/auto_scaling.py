from flask import render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
import boto3
import mysql.connector
from manager import admin, check_cpu

class AutoScalingForm(FlaskForm):
	grow_threshold = IntegerField('CPU Threshold for Growing the Worker Pool',
							validators=[DataRequired(message= u'Threshold can not be empty.')])
	shrink_threshold = IntegerField('CPU Threshold for shrinking the Worker Pool',
							validators=[DataRequired(message= u'Threshold can not be empty.')])
	expand_ratio = FloatField('Expanding Ratio',
							validators=[DataRequired(message= u'Ratio can not be empty.')])
	shrink_ratio = FloatField('Shrinking Ratio',
							validators=[DataRequired(message= u'Ratio can not be empty.')])
	submit = SubmitField('Submit')

'''
Functions for database

def connect_to_database():
	return mysql.connector.connect(user=db_config['user'],
					password=db_config['password'],
					host=db_config['host'],
					database=db_config['database'])

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = connect_to_database()
	return db

@admin.teardown_appcontext
# this will execute every time when the context is closed
def teardown_db(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()
'''


'''
Functions for auto-scaling
'''
@admin.route('/auto_scaling', methods=['GET','POST'])
def auto_scaling():
	form = AutoScalingForm()
	if form.validate_on_submit():
		grow_threshold = form.grow_threshold.data
		shrink_threshold = form.shrink_threshold.data
		expand_ratio = form.expand_ratio.data
		shrink_ratio = form.shrink_ratio.data
		"""
		cnx = get_db()
        cursor = cnx.cursor()
        query = '''UPDATE policy
                   SET grow_th = %s,
                       shrink_th = %s,
                       expand_ratio = %s,
                       shrink_ratio = %s
                   WHERE id = 1
        '''
        cursor.execute(query, (growth_threshold,shrink_threshold,expand_ratio,shrink_ratio))
        cnx.commit()
		compare_cpu()
		"""
	return render_template('auto_scaling.html', form=form)


"""
def get_policy():
    cnx = get_db()
    cursor = cnx.cursor()
    query = '''SELECT * FROM policy'''
    cursor.execute(query)
    row = cursor.fetchone()
    return row
"""

