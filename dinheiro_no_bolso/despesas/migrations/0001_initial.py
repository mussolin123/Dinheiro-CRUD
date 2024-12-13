# Generated by Django 5.1.4 on 2024-12-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('Água', 'Água'), ('Luz', 'Luz'), ('Aluguel', 'Aluguel'), ('IPVA', 'IPVA'), ('IPTU', 'IPTU'), ('Mercado', 'Mercado'), ('Farmácia', 'Farmácia'), ('Lazer', 'Lazer'), ('Esportes', 'Esportes'), ('Contas Diversas', 'Contas Diversas')], max_length=20)),
                ('data', models.DateField(auto_now_add=True)),
                ('valor', models.FloatField()),
                ('status_pago', models.BooleanField(default=False)),
            ],
        ),
    ]