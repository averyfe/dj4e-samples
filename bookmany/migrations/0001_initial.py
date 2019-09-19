# Generated by Django 2.1.7 on 2019-09-19 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Authored',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmany.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.ManyToManyField(through='bookmany.Authored', to='bookmany.Author')),
            ],
        ),
        migrations.AddField(
            model_name='authored',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmany.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(through='bookmany.Authored', to='bookmany.Book'),
        ),
    ]
