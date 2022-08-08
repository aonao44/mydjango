# Generated by Django 4.0.2 on 2022-08-01 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('naonao_blog', '0004_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='NAME')),
                ('text', models.TextField(verbose_name='TEXT')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='CREATE')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naonao_blog.post', verbose_name='POST')),
            ],
        ),
    ]
