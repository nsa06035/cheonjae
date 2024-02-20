# Generated by Django 5.0.2 on 2024-02-20 02:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=50)),
                ('bCreateDate', models.DateTimeField(auto_now_add=True)),
                ('coverImg', models.URLField(max_length=512)),
                ('copyR', models.CharField(max_length=30)),
                ('evalStart', models.IntegerField(default=0)),
                ('lastPage', models.IntegerField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savedAt', models.DateTimeField(auto_now_add=True)),
                ('drawSty', models.IntegerField(default=0)),
                ('diff', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'draft',
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowerName', models.CharField(max_length=50)),
                ('achieveCnt', models.IntegerField()),
                ('flowerImg', models.URLField(max_length=512)),
            ],
            options={
                'db_table': 'flower',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=100)),
                ('profImg', models.URLField(max_length=512)),
                ('seedCnt', models.IntegerField(default=10)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('createCnt', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introMode', models.BooleanField()),
                ('subject', models.CharField(max_length=100)),
                ('IntroContent', models.TextField()),
                ('draftId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.draft')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.members')),
            ],
            options={
                'db_table': 'intro',
            },
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followImg', models.URLField(max_length=512)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.members')),
            ],
            options={
                'db_table': 'follower',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedCap', models.CharField(max_length=512)),
                ('feedContent', models.TextField()),
                ('draftId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.draft')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.members')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='DraftPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageNum', models.IntegerField()),
                ('pageContent', models.TextField()),
                ('draftId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.draft')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.members')),
            ],
            options={
                'db_table': 'draftpage',
            },
        ),
        migrations.AddField(
            model_name='draft',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.members'),
        ),
        migrations.CreateModel(
            name='MyFlower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('getDate', models.DateField()),
                ('isActive', models.BooleanField()),
                ('flowerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.flower')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.members')),
            ],
            options={
                'db_table': 'myflower',
            },
        ),
        migrations.CreateModel(
            name='MyForest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.flower')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.members')),
            ],
            options={
                'db_table': 'myforest',
            },
        ),
        migrations.CreateModel(
            name='MyLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.books')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genius.members')),
            ],
            options={
                'db_table': 'mylibrary',
            },
        ),
    ]
