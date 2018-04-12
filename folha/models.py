from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django import forms
from django_pandas.managers import DataFrameManager

EstCivil = (
    ('Casado', 'Casado'),
    ('Solteiro','Solteiro'),
    ('Divorciado', 'Divorciado'),
    ('Desquitado','Desquitado'),
    ('Viúvo', 'Viúvo'),
)


INSTRUCAO = (
    ('Analfabeto', 'Analfabeto'),
    ('Ensino Fundamental Incompleto','Ensino Fundamental Incompleto'),
    ('Ensino Fundamental Completo','Ensino Fundamental Completo'),
    ('Ensino Médio Incompleto','Ensino Médio Incompleto'),
    ('Ensino Médio Completo','Ensino Médio Completo'),
    ('Superior completo (ou Graduação)','Superior completo (ou Graduação)'),
    ('Pós-Graduação','Pós-Graduação'),
    ('Mestrado','Mestrado'),
    ('Doutorado','Doutorado'),
    ('PHD','PHD'),

)

PAGAMENTO = (
    ('MENSAL', 'MENSAL'),
    ('QUINZENAL','QUINZENAL'),
    ('SEMANAL','SEMANAL'),
)


TIPO_SALARIO = (
    ('MENSALISTA', 'MENSALISTA'),
    ('HORISTA','HORISTA'),
)



class employees(models.Model):
    nome = models.CharField(max_length=100,help_text='Nome completo do colaborador',blank=False)
    pai = models.CharField(max_length=100,help_text='Nome completo do pai do colaborador',blank=False)
    mae = models.CharField(max_length=100,help_text='Nome completo da mãe do colaborador',blank=False)
    carteira = models.CharField(max_length=100,help_text='Numero da carteira profissional seguido da série da mesma',blank=False)
    data_carteira = models.DateField(help_text='Data da carteira')
    reservista = models.CharField(max_length=100,help_text='Numero Reservista caso aplicável',blank=True)
    categoria = models.CharField(max_length=100,help_text='Qual a categoria',blank=True)
    titulo_eleitor = models.CharField(max_length=100,help_text='Titulo se aplicável',blank=True)
    exame_admissional = models.DateField(help_text='Data do exame admissional',blank=True,null=True)
    exame_medico_demissional = models.DateField(help_text='Data do exame demissional',blank=True,null=True)
    cart_identidade = models.CharField(max_length=10,help_text='No. Identidade',blank=False)
    emissao_identidade = models.DateField()
    Org_emissor = models.CharField(max_length=10,help_text='sigla do orgao emissor da carteira',blank=False)
    CPF = models.CharField(max_length=11,help_text='Numero sem pontos e traços com 11 digitos',blank=False)
    PIS = models.CharField(max_length=50,help_text='Numero sem pontos e traços',blank=False)
    Data_Cadastro_PIS = models.DateField()
    Sigla_Conselho_Regional = models.CharField(max_length=50,help_text='por exemplo: CRA, caso aplicavel. Para fins de contribuicao sindical',blank=True)
    Numero_Reg_Conselho = models.CharField(max_length=50,help_text='Caso aplicavel. Para fins de contribuicao sindical',blank=True)
    Regiao_Registro_Conselho = models.CharField(max_length=50,help_text='Caso aplicavel. Para fins de contribuicao sindical',blank=True)
    Data_Nascimento = models.DateField()
    Local_Nascimento = models.CharField(max_length=50,help_text='Município e Estado onde nasceu',blank=False)
    Estado_Civil = models.CharField(max_length=30, choices=EstCivil,help_text='Estado Civil colaborador',blank = False)
    Grau_Instrucao = models.CharField(max_length=50, choices=INSTRUCAO,help_text='Escolaridade do colaborador',blank = False)
    Nacionalidade = models.CharField(max_length=12, help_text='Brasileiro ou Estrangeiro',blank = False)
    Sexo = models.CharField(max_length=12, help_text='Masculino ou Feminino',blank = False)
    Cor = models.CharField(max_length=12, help_text='Cor de pele',blank = False)
    Altura = models.CharField(max_length=12, help_text='Altura',blank = False)
    Peso = models.CharField(max_length=12, help_text='Peso do colaborador',blank = False)
    Cabelos = models.CharField(max_length=12, help_text='Cor dos cabelos',blank = False)
    Olhos = models.CharField(max_length=12, help_text='Cor dos olhos',blank = False)
    Defeitos = models.CharField(max_length=12, help_text='Caso aplicavel',blank=True)
    Endereço = models.CharField(max_length=200, help_text='Rua e numero da casa ou apartamento',blank = False)
    Bairro = models.CharField(max_length=12, help_text='Bairro',blank = False)
    Cidade = models.CharField(max_length=12, help_text='Cidade', blank = False)
    Estado = models.CharField(max_length=12, help_text='Estado onde reside', blank = False)
    CEP = models.CharField(max_length=9, help_text='numeros com traço', blank = False)
    Registro_Geral = models.CharField(max_length=50, help_text='Caso seja estrangeiro Naturalizado', blank = True)
    Filhos = models.CharField(max_length=50, help_text='No caso de estrageniro, reponser Sim caso possua filhos brasileiros', blank = True)
    Data_Chegada_Brasil = models.DateField(blank = True,null=True)
    N_Carteira_Mod_19 = models.CharField(max_length=50, help_text='No caso de estrageiro, informar o numero', blank = True,null=True)
    Validade_Cart_Identidade_Estrangeiro = models.DateField(blank = True,null=True)
    Tipo_Visto_Estrageiro = models.CharField(max_length=50, help_text='No caso de estrangeiro informar o tipo de visto obtido', blank = True)
    Validade_Carteira_Trabalho = models.DateField(blank = True,null=True)
    Data_Admissao = models.DateField()
    Data_Opção_FGTS= models.DateField(blank = True,null=True, help_text='Mesma data da admissão')
    Forma_Pagamento= models.CharField(max_length=50, choices=PAGAMENTO, blank = False)
    Cargo_Atual= models.CharField(max_length=50, help_text='Cargo do colaborador', blank = False)
    Salario = models.FloatField()
    Tipo_Salario = models.CharField(max_length=50, choices = TIPO_SALARIO, blank = False)
    Local_Trabalho = models.CharField(max_length=50, help_text='Endereço completo do local de trabalho', blank = False)
    Membro_Cipa = models.CharField(max_length=50, help_text='Membro da Cipa? Sim ou Nao', blank = False)
    Dependendentes1 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Dependendentes2 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Dependendentes3 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Dependendentes4 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Dependendentes5 = models.CharField(max_length=200, help_text='Nome e Parentesco caso exista', blank = True)
    Salario_Familia = models.CharField(max_length=200, help_text='Preenchido posteriormente pela nossa equipe', blank = True)
    Imposto_Renda = models.CharField(max_length=200, help_text='Preenchido posteriormente pela nossa equipe', blank = True)
    Salario_Educacao = models.CharField(max_length=200, help_text='Preenchido posteriormente pela nossa equipe', blank = True)


    pdobjects = DataFrameManager()


    def __str__(self):
        return self.nome
