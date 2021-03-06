# Generated by Django 2.1.5 on 2019-03-18 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('waste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='JourneyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('departure_from', models.CharField(max_length=20, verbose_name='From')),
                ('departure_to', models.CharField(max_length=20, verbose_name='To')),
                ('distance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LogisticsPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.LogisticsPlan')),
            ],
        ),
        migrations.CreateModel(
            name='LogistsPlanApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval', models.BooleanField()),
                ('approved_by', models.CharField(max_length=30)),
                ('comments', models.TextField()),
                ('date_of_approval', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WasteCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField()),
                ('journey_management_form', models.FileField(upload_to='')),
                ('risk_assessment', models.FileField(upload_to='')),
                ('driving_permit', models.FileField(upload_to='')),
                ('fitness_certificate', models.FileField(upload_to='')),
                ('vehicle_and_inspection_form', models.FileField(upload_to='')),
                ('journey_risk_assessment', models.FileField(upload_to='')),
                ('journey_emergency_reponse_plan', models.FileField(upload_to='')),
                ('truck_nema_licence', models.FileField(upload_to='')),
                ('date_of_approval', models.DateTimeField(auto_now=True)),
                ('journey_plan', models.ManyToManyField(to='logistics.JourneyPlan')),
            ],
        ),
        migrations.CreateModel(
            name='WasteInspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval', models.BooleanField()),
                ('journey_management_form', models.FileField(upload_to='')),
                ('driving_permit', models.FileField(upload_to='')),
                ('fitness_certificate', models.FileField(upload_to='')),
                ('vehicle_and_inspection_form', models.FileField(upload_to='')),
                ('journey_risk_assessment', models.FileField(upload_to='')),
                ('journey_emergency_reponse_plan', models.FileField(upload_to='')),
                ('truck_nema_licence', models.FileField(upload_to='')),
                ('date_of_approval', models.DateTimeField(auto_now=True)),
                ('journey_plan', models.ManyToManyField(to='logistics.JourneyPlan')),
            ],
        ),
        migrations.AddField(
            model_name='logisticsplan',
            name='waste_collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.WasteCollection'),
        ),
        migrations.AddField(
            model_name='logisticsplan',
            name='waste_inspection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.WasteInspection'),
        ),
        migrations.AddField(
            model_name='logisticsplan',
            name='waste_tracking_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.ServiceInstruction'),
        ),
        migrations.AddField(
            model_name='collectionservice',
            name='journey_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.JourneyPlan'),
        ),
        migrations.AddField(
            model_name='collectionservice',
            name='vessel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.Vessel'),
        ),
    ]
