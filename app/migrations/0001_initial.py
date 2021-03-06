# Generated by Django 2.2.11 on 2020-03-20 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_line', models.TextField(blank=True, null=True)),
                ('second_line', models.TextField(blank=True, null=True)),
                ('first_book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='first_line', to='app.Book')),
                ('second_book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='second_line', to='app.Book')),
            ],
        ),
    ]
