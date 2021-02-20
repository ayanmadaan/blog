# Generated by Django 3.1.3 on 2020-12-06 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('caption', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('imgg', models.ImageField(default='default1.jpg', upload_to='posts_media')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userreg.profile')),
            ],
        ),
    ]
