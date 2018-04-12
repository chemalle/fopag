# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-12 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo do colaborador', max_length=100)),
                ('pai', models.CharField(help_text='Nome completo do pai do colaborador', max_length=100)),
                ('mae', models.CharField(help_text='Nome completo da mãe do colaborador', max_length=100)),
                ('carteira', models.CharField(help_text='Numero da carteira profissional seguido da série da mesma', max_length=100)),
                ('data_carteira', models.DateField(help_text='Data da carteira inseria Mes,Dia e Ano, exemplo 12/23/1973')),
                ('reservista', models.CharField(blank=True, help_text='Numero Reservista caso aplicável', max_length=100)),
                ('categoria', models.CharField(blank=True, help_text='Qual a categoria', max_length=100)),
                ('titulo_eleitor', models.CharField(blank=True, help_text='Titulo se aplicável', max_length=100)),
                ('exame_admissional', models.CharField(blank=True, help_text='Exame', max_length=10)),
                ('exame_medico', models.CharField(blank=True, help_text='Exame medico', max_length=10)),
                ('cart_identidade', models.CharField(help_text='No. Identidade', max_length=10)),
                ('emissao_identidade', models.DateField()),
                ('Org_emissor', models.CharField(help_text='sigla do orgao emissor da carteira', max_length=10)),
                ('CPF', models.CharField(help_text='Numero sem pontos e traços com 11 digitos', max_length=11)),
                ('PIS', models.CharField(help_text='Numero sem pontos e traços', max_length=50)),
                ('Data_Cadastro_PIS', models.DateField()),
                ('Sigla_Conselho_Regional', models.CharField(blank=True, help_text='por exemplo: CRA, caso aplicavel. Para fins de contribuicao sindical', max_length=50)),
                ('Numero_Reg_Conselho', models.CharField(blank=True, help_text='Caso aplicavel. Para fins de contribuicao sindical', max_length=50)),
                ('Regiao_Registro_Conselho', models.CharField(blank=True, help_text='Caso aplicavel. Para fins de contribuicao sindical', max_length=50)),
                ('Data_Nascimento', models.DateField()),
                ('Local_Nascimento', models.CharField(help_text='Município e Estado onde nasceu', max_length=50)),
                ('Estado_Civil', models.CharField(choices=[('Casado', 'Casado'), ('Solteiro', 'Solteiro'), ('Divorciado', 'Divorciado'), ('Desquitado', 'Desquitado'), ('Viúvo', 'Viúvo')], help_text='Estado Civil colaborador', max_length=30)),
                ('Grau_Instrucao', models.CharField(choices=[('Analfabeto', 'Analfabeto'), ('Ensino Fundamental Incompleto', 'Ensino Fundamental Incompleto'), ('Ensino Fundamental Completo', 'Ensino Fundamental Completo'), ('Ensino Médio Incompleto', 'Ensino Médio Incompleto'), ('Ensino Médio Completo', 'Ensino Médio Completo'), ('Superior completo (ou Graduação)', 'Superior completo (ou Graduação)'), ('Pós-Graduação', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'), ('PHD', 'PHD')], help_text='Escolaridade do colaborador', max_length=30)),
                ('Nacionalidade', models.CharField(help_text='Brasileiro ou Estrangeiro', max_length=12)),
                ('Sexo', models.CharField(help_text='Masculino ou Feminino', max_length=12)),
                ('Cor', models.CharField(help_text='Cor de pele', max_length=12)),
                ('Altura', models.CharField(help_text='Altura', max_length=12)),
                ('Peso', models.CharField(help_text='Peso do colaborador', max_length=12)),
                ('Cabelos', models.CharField(help_text='Cor dos cabelos', max_length=12)),
                ('Olhos', models.CharField(help_text='Cor dos olhos', max_length=12)),
                ('Defeitos', models.CharField(blank=True, help_text='Caso aplicavel', max_length=12)),
                ('Endereço', models.CharField(help_text='Rua e numero da casa ou apartamento', max_length=200)),
                ('Bairro', models.CharField(help_text='Bairro', max_length=12)),
                ('Cidade', models.CharField(help_text='Cidade', max_length=12)),
                ('Estado', models.CharField(help_text='Estado onde reside', max_length=12)),
                ('CEP', models.CharField(help_text='numeros com traço', max_length=9)),
                ('Registro_Geral', models.CharField(blank=True, help_text='Caso seja estrangeiro Naturalizado', max_length=50)),
                ('Filhos', models.CharField(blank=True, help_text='No caso de estrageniro, reponser Sim caso possua filhos brasileiros', max_length=50)),
                ('Data_Chegada_Brasil', models.DateField(blank=True, null=True)),
                ('N_Carteira_Mod_19', models.CharField(blank=True, help_text='No caso de estrageiro, informar o numero', max_length=50, null=True)),
                ('Validade_Cart_Identidade_Estrangeiro', models.DateField(blank=True, null=True)),
                ('Tipo_Visto_Estrageiro', models.CharField(blank=True, help_text='No caso de estrangeiro informar o tipo de visto obtido', max_length=50)),
                ('Validade_Carteira_Trabalho', models.DateField(blank=True, null=True)),
                ('Data_Admissao', models.DateField()),
                ('Data_Opção_FGTS', models.DateField(blank=True, help_text='Mesma data da admissão', null=True)),
                ('Forma_Pagamento', models.CharField(choices=[('MENSAL', 'MENSAL'), ('QUINZENAL', 'QUINZENAL'), ('SEMANAL', 'SEMANAL')], max_length=50)),
                ('Cargo_Atual', models.CharField(help_text='Cargo do colaborador', max_length=50)),
                ('Salario', models.FloatField()),
                ('Tipo_Salario', models.CharField(choices=[('MENSALISTA', 'MENSALISTA'), ('HORISTA', 'HORISTA')], max_length=50)),
                ('Local_Trabalho', models.CharField(help_text='Endereço completo do local de trabalho', max_length=50)),
                ('Membro_Cipa', models.CharField(help_text='Membro da Cipa? Sim ou Nao', max_length=50)),
                ('Dependendentes1', models.CharField(blank=True, help_text='Nome e Parentesco caso exista', max_length=200)),
                ('Dependendentes2', models.CharField(blank=True, help_text='Nome e Parentesco caso exista', max_length=200)),
                ('Dependendentes3', models.CharField(blank=True, help_text='Nome e Parentesco caso exista', max_length=200)),
                ('Dependendentes4', models.CharField(blank=True, help_text='Nome e Parentesco caso exista', max_length=200)),
                ('Dependendentes5', models.CharField(blank=True, help_text='Nome e Parentesco caso exista', max_length=200)),
                ('Salario_Familia', models.CharField(blank=True, help_text='Preenchido posteriormente pela nossa equipe', max_length=200)),
                ('Imposto_Renda', models.CharField(blank=True, help_text='Preenchido posteriormente pela nossa equipe', max_length=200)),
                ('Salario_Educacao', models.CharField(blank=True, help_text='Preenchido posteriormente pela nossa equipe', max_length=200)),
            ],
            managers=[
                ('pdobjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
