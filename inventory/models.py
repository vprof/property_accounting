from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)                 # Назва матеріальних активів
    type = models.CharField(max_length=55, blank=True, null=True)  # Тип матеріальних активів
    unitOfMeasurement = models.CharField(
        max_length=23, 
        default='шт.', 
        null=True, 
        blank=True
    )                                                      # Одиниця виміру
    inventoryNumber = models.FloatField(null=True, blank=True)    # Інвентарний номер
    category = models.CharField(max_length=55, blank=True, null=True)  # Категорія
    initialCost = models.FloatField(null=True, blank=True)          # Початкова вартість
    factoryNumber = models.CharField(max_length=55, blank=True, null=True)  # Заводський номер
    clas = models.CharField(max_length=55, blank=True, null=True)     # Клас матеріальних активів
    series = models.CharField(max_length=50, blank=True, null=True)          # Серія
    expirationDate = models.DateField(null=True, blank=True)         # Дата закінчення терміну експлуатації
    releaseDate = models.DateField(null=True, blank=True)            # Дата випуску

    class Meta:
            db_table = 'items'
            managed = False 
            indexes = [
                models.Index(fields=['name'], name='ix_items_name'),
            ]

    def __str__(self):
        return self.name

class Unit(models.Model):
    unit = models.CharField(max_length=100)                # Одиниця
    for_print = models.CharField(max_length=128, null=True, blank=True)  # Поле для друку
    location = models.CharField(max_length=50, null=True, blank=True)    # Локація

    class Meta:
        db_table = 'units'         # Вказуємо ім'я таблиці в базі даних
        managed = False            # Django не буде керувати цією таблицею
        indexes = [
            models.Index(fields=['unit'], name='ix_units_unit'),
        ]

    def __str__(self):
        return self.unit

class Balance(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)            # Зовнішній ключ до Unit
    party = models.DateTimeField()                                      # Дата партії
    item = models.ForeignKey(Item, on_delete=models.CASCADE)   # Зовнішній ключ до Item
    series = models.CharField(max_length=50, null=True, blank=True)     # Серія
    amount = models.DecimalField(max_digits=18, decimal_places=2)       # Кількість
    reserved = models.DecimalField(max_digits=18, decimal_places=2)     # Зарезервовано
    available = models.DecimalField(max_digits=18, decimal_places=2, editable=False, blank=True)  # Доступно
    price = models.DecimalField(max_digits=19, decimal_places=4)        # Ціна
    sum = models.DecimalField(max_digits=19, decimal_places=4, editable=False, blank=True)        # Сума

    class Meta:
        db_table = 'balances'       # Вказуємо назву таблиці
        managed = False             # Django не створює та не змінює таблицю

    def __str__(self):
        return f"Balance ID {self.id} - Item {self.item.name}"

class Rank(models.Model):
    rank = models.CharField(max_length=50, unique=True)  # Ранг, унікальний індекс забезпечується `unique=True`

    class Meta:
        db_table = 'ranks'    # Вказуємо, що ця модель відповідає таблиці ranks у базі даних
        managed = False       # Django не керуватиме цією таблицею
        indexes = [
            models.Index(fields=['rank'], name='ix_ranks_rank'),
        ]

    def __str__(self):
        return self.rank

class Position(models.Model):
    position = models.CharField(max_length=50)  # Назва посади

    class Meta:
        db_table = 'positions'   # Вказуємо, що ця модель відповідає таблиці positions у базі даних
        managed = False          # Django не буде керувати цією таблицею

    def __str__(self):
        return self.position

class ResponsiblePerson(models.Model):
    name = models.CharField(max_length=50)                   # Ім'я відповідальної особи
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE)  # Зовнішній ключ до Rank
    position = models.ForeignKey('Position', on_delete=models.CASCADE)  # Зовнішній ключ до Position
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)          # Зовнішній ключ до Unit
    status = models.CharField(max_length=50, null=True, blank=True)     # Статус (може бути пустим)

    class Meta:
        db_table = 'responsiblePersons'   # Вказуємо ім'я таблиці у базі даних
        managed = False                   # Django не створюватиме і не змінюватиме цю таблицю
        indexes = [
            models.Index(fields=['name'], name='index_responsiblePersons_name', include=['position', 'rank', 'unit', 'status']),
        ]

    def __str__(self):
        return self.name

class TypeOfDocument(models.Model):
    docType = models.CharField(max_length=50)  # Тип документа

    class Meta:
        db_table = 'typesOfDocuments'  # Вказуємо, що ця модель відповідає таблиці typesOfDocuments
        managed = False                # Django не керуватиме цією таблицею

    def __str__(self):
        return self.doc_type

class Document(models.Model):
    type = models.ForeignKey('TypeOfDocument', on_delete=models.CASCADE)          # Тип документа
    number = models.IntegerField()                                                # Номер документа
    date = models.DateTimeField()                                                 # Дата документа
    unitSender = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name='sent_documents')      # Відправник
    unitReceiver = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name='received_documents')  # Отримувач
    status = models.CharField(max_length=20)                                      # Статус документа
    personSender = models.ForeignKey('ResponsiblePerson', on_delete=models.CASCADE, related_name='sent_by')  # Відправник
    personReceiver = models.ForeignKey('ResponsiblePerson', on_delete=models.CASCADE, related_name='received_by')  # Отримувач
    docName = models.CharField(max_length=255, editable=False)                   # Назва документа, автоматично оновлюється тригером

    class Meta:
        db_table = 'documents'    # Назва таблиці у базі даних
        managed = False           # Django не керуватиме цією таблицею

    def __str__(self):
        return f"{self.doc_name} (№{self.number})"

class Supplier(models.Model):
    supplier = models.CharField(max_length=50, unique=True)  # Назва постачальника
    city = models.CharField(max_length=50, null=True, blank=True)      # Місто
    phone = models.CharField(max_length=50, null=True, blank=True)     # Телефон
    email = models.EmailField(max_length=50, null=True, blank=True)    # Email
    manager = models.CharField(max_length=50, null=True, blank=True)   # Менеджер

    class Meta:
        db_table = 'suppliers'  # Вказуємо назву таблиці в базі даних
        managed = False         # Django не керуватиме цією таблицею
        indexes = [
            models.Index(fields=['supplier'], name='ix_suppliers_supplier'),
        ]

    def __str__(self):
        return self.supplier

class MedUser(models.Model):
    id = models.IntegerField(primary_key=True)                    # Первинний ключ без автоматичного збільшення
    medUser = models.CharField(max_length=50)                    # Ім'я користувача
    salt = models.CharField(max_length=50)                        # Сіль для хешування пароля
    hashedPassword = models.TextField()                          # Хешований пароль
    role = models.CharField(max_length=20)                        # Роль користувача

    class Meta:
        db_table = 'med_users'  # Назва таблиці у базі даних
        managed = False         # Django не керуватиме цією таблицею

    def __str__(self):
        return f"{self.med_user} ({self.role})"

class Transaction(models.Model):
    document = models.ForeignKey('Document', on_delete=models.CASCADE)           # Зовнішній ключ до документа
    party = models.DateTimeField()                                               # Дата транзакції
    sender = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name='sent_transactions')      # Відправник
    receiver = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name='received_transactions')  # Отримувач
    item = models.ForeignKey('Item', on_delete=models.CASCADE)           # Товар
    amount = models.DecimalField(max_digits=18, decimal_places=2)                # Кількість
    price = models.DecimalField(max_digits=19, decimal_places=4)                 # Ціна за одиницю
    sum = models.DecimalField(max_digits=19, decimal_places=4, editable=False, blank=True)  # Сума, обчислюється базою даних
    source = models.CharField(max_length=20)                                     # Джерело транзакції
    type = models.IntegerField()                                                 # Тип транзакції

    class Meta:
        db_table = 'transaction'    # Назва таблиці у базі даних
        managed = False              # Django не керуватиме цією таблицею

    def __str__(self):
        return f"Transaction ID {self.id} - Document {self.document.id}"