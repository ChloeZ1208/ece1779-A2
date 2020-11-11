from flask import render_template, redirect, url_for, request, g
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
import boto3
import mysql.connector
from manager import admin, config
#from celery.task import periodic_task

class AutoScalingForm(FlaskForm):
	grow_threshold = StringField('CPU Threshold for Growing the Worker Pool',
							validators=[DataRequired(message= u'Threshold can not be empty.')])
	shrink_threshold = StringField('CPU Threshold for shrinking the Worker Pool',
							validators=[DataRequired(message= u'Threshold can not be empty.')])
	expand_ratio = StringField('Expanding Ratio',
							validators=[DataRequired(message= u'Ratio can not be empty.')])
	shrink_ratio = StringField('Shrinking Ratio',
							validators=[DataRequired(message= u'Ratio can not be empty.')])
	submit = SubmitField('Submit')

'''
Functions for database
'''

@admin.route('/auto_scaling', methods=['GET', 'POST'])
def auto_scaling():
	form = AutoScalingForm()
	if form.is_submitted():
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
		"""

	return render_template('auto_scaling.html', form=form)

