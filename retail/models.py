from django.db import models


class RetailChain(models.Model):
    LEVEL_ZERO = 0
    LEVEL_FIRST = 1
    LEVEL_SECOND = 2
    LEVEL = [
        (LEVEL_ZERO, 'завод'),
        (LEVEL_FIRST, 'розничная сеть'),
        (LEVEL_SECOND, 'индивидуальный предприниматель'),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name='название звена сети'
    )
    email = models.EmailField(
        verbose_name='email'
    )
    country = models.CharField(
        max_length=100,
        verbose_name='страна'
    )
    city = models.CharField(
        max_length=100,
        verbose_name='город'
    )
    street = models.CharField(
        max_length=100,
        verbose_name='улица'
    )
    house_number = models.IntegerField(
        verbose_name='номер дома'
    )
    chain_level = models.IntegerField(
        choices=LEVEL,
        verbose_name='уровень сети'
    )
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='поставщик'
    )
    debt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name='задолженность перед поставщиком, руб.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'


class Product(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='название продукта'
    )
    product_model = models.CharField(
        max_length=250,
        verbose_name='модель продукта'
    )
    release_date = models.DateField(
        verbose_name='дата выхода продукта'
    )
    retail_chain = models.ForeignKey(
        RetailChain,
        on_delete=models.CASCADE,
        verbose_name='поставщик'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
