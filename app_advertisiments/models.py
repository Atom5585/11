from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model

User= get_user_model()
class Advertisiment(models.Model):
    title = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=3)
    auction = models.BooleanField("Торг", help_text="укажите, если возможен торг")
    create_at = models.DateTimeField(auto_now_add=True)
    update_add = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE)
    image = models.ImageField("изображение", upload_to="advertisiments/")

    @admin.display(description="дата создания")
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", created_time
            )
        return self.create_at.strftime("%d:%m:%Y")

    @admin.display(description="дата обновления")
    def update_date(self):
        if self.update_add.date() == timezone.now().date():
            updated_time = self.create_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: blue;'>Сегодня в {}</span>", updated_time
            )
        return self.update_add.strftime("%d:%m:%Y")

    @admin.display(description="уменьшение")
    def minimage(self):
        if self.image:
            return format_html("<img src='{}' width='50'/>".format(self.image.url))
        return "-"

    class Meta:
        db_table = "advertisiments"
        verbose_name = "App_Advertisiments"
        verbose_name_plural = "Объявления"
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

