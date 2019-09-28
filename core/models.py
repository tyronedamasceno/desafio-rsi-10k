from django.db import models


class Address(models.Model):
    street = models.CharField('Rua', max_length=255)
    number = models.IntegerField('Número')
    city = models.CharField('Cidade', max_length=255)
    neighborhood = models.CharField('Bairro', max_length=255)
    state = models.CharField('Estado', max_length=255)

    def __str__(self):
        return f'Endereço <Rua: {self.street}, Número: {self.number}>'


class User(models.Model):
    name = models.CharField('Nome', max_length=255)
    surname = models.CharField('Sobrenome', max_length=255)
    email = models.CharField('E-mail', max_length=255)
    birth_date = models.CharField('Data de Nascimento', max_length=10)
    cpf = models.BigIntegerField('CPF')
    password = models.CharField('Senha', max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name='Usuario'
    )
    friends = models.ManyToManyField("self", related_name='Amigos')

    def __str__(self):
        return f'Usuário <Nome: {self.name}, Email: {self.email}>'

    # class Meta:
    #     verbose_name = 'Usuário'
    #     verbose_name_plural = 'Usuários'
