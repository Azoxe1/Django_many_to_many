# Generated by Django 4.2.4 on 2023-08-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_scope_options_alter_tag_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='tags', to='articles.article'),
        ),
    ]
