# Generated by Django 4.1.7 on 2023-03-31 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_staffmodel_is_staff_alter_blogmodel_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudymodel',
            name='short_description',
            field=models.TextField(default='Tincidunt donec vulputate ipsum erat urna auctor. Eget phasellus ideirs.adipiscing elit. Tincidunt donec vulputate ipsum erat urna auctor. '),
            preserve_default=False,
        ),
    ]
