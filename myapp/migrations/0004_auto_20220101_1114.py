# Generated by Django 3.2.10 on 2022-01-01 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_event_eventclosedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaylyDutyList',
            fields=[
                ('daylyDutyListID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('day', models.IntegerField()),
            ],
            options={
                'db_table': 'Dayly_Duty_List',
            },
        ),
        migrations.CreateModel(
            name='YearlyDutyList',
            fields=[
                ('yearlyDutyListID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'Yearly_Duty_List',
            },
        ),
        migrations.CreateModel(
            name='YearlyTotalEvent',
            fields=[
                ('yearlyTotalEventID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'Yearln_Total_Event',
            },
        ),
        migrations.RenameField(
            model_name='eventpic',
            old_name='EventPICID',
            new_name='eventPICID',
        ),
        migrations.CreateModel(
            name='MonthlyTotalEvent',
            fields=[
                ('monthlyTotalEventID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('month', models.IntegerField()),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.yearlytotalevent')),
            ],
            options={
                'db_table': 'Monthln_Total_Event',
            },
        ),
        migrations.CreateModel(
            name='MonthlyDutyList',
            fields=[
                ('monthlyDutyListID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('month', models.IntegerField()),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.yearlydutylist')),
            ],
            options={
                'db_table': 'Monthly_Duty_List',
            },
        ),
        migrations.CreateModel(
            name='DutyList',
            fields=[
                ('dutyListID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('workTimeStart', models.TimeField()),
                ('wrokTimeEnd', models.TimeField()),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.building')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.daylydutylist')),
                ('dearWithEvent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.event')),
            ],
            options={
                'db_table': 'Duty_List',
            },
        ),
        migrations.CreateModel(
            name='DaylyTotalEvent',
            fields=[
                ('daylyTotalEventID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('day', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.event')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.monthlytotalevent')),
            ],
            options={
                'db_table': 'Dayln_Total_Event',
            },
        ),
        migrations.AddField(
            model_name='daylydutylist',
            name='UID',
            field=models.ManyToManyField(through='myapp.DutyList', to='myapp.User'),
        ),
        migrations.AddField(
            model_name='daylydutylist',
            name='building',
            field=models.ManyToManyField(through='myapp.DutyList', to='myapp.Building'),
        ),
        migrations.AddField(
            model_name='daylydutylist',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.monthlydutylist'),
        ),
    ]