# Generated by Django 2.2.3 on 2019-07-17 15:11

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=45)),
                ('author_img', models.ImageField(upload_to='author_images')),
                ('author_description', models.TextField()),
                ('author_facebook', models.URLField(blank=True, null=True)),
                ('author_twitter', models.URLField(blank=True, null=True)),
                ('author_linkedin', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='post',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.AuthorProfile'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.AuthorProfile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images'),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.AuthorProfile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tags'),
        ),
    ]
