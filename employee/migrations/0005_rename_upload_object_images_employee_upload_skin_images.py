# Generated by Django 3.2.6 on 2021-09-22 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_rename_upload_leaf_image_employee_upload_object_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='UPLOAD_OBJECT_IMAGES',
            new_name='UPLOAD_SKIN_IMAGES',
        ),
    ]