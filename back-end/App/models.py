# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Schoolprocess(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sum = models.CharField(db_column='Sum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ti = models.CharField(db_column='TI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    im = models.CharField(db_column='IM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    im1 = models.CharField(db_column='IM1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    im2 = models.CharField(db_column='IM2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    im3 = models.CharField(db_column='IM3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    im4 = models.CharField(db_column='IM4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    im5 = models.CharField(db_column='IM5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    to = models.CharField(db_column='TO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    to1 = models.CharField(db_column='TO1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    to2 = models.CharField(db_column='TO2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    to3 = models.CharField(db_column='TO3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    to4 = models.CharField(db_column='TO4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    to5 = models.CharField(db_column='TO5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rs = models.CharField(db_column='RS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rs1 = models.CharField(db_column='RS1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rs2 = models.CharField(db_column='RS2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sr = models.CharField(db_column='SR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schoolprocess'

class Userinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'

class Image(models.Model):
    name = models.CharField(max_length=200)
    image_file = models.ImageField(upload_to='image/')
