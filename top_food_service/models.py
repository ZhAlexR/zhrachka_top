from django.db import models


class CheckType(models.TextChoices):
    KITCHEN = "KT", "kitchen"
    CLIENT = "CL", "client"


class CheckStatus(models.TextChoices):
    NEW = "NEW", "new"
    RENDERED = "RENDERED", "rendered"
    PRINTED = "PRINTED", "printed"


class Printer(models.Model):
    name = models.CharField(max_length=63)
    api_key = models.CharField(max_length=255, unique=True)
    check_type = models.CharField(choices=CheckType.choices, default=CheckType.KITCHEN)
    point_id = models.IntegerField()

    class Meta:
        default_related_name = "printers"

    def __str__(self):
        return self.name


class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField(choices=CheckType.choices, default=CheckType.KITCHEN)
    order = models.JSONField()
    status = models.CharField(choices=CheckStatus.choices, default=CheckStatus.NEW)
    pdf_file = models.FileField(upload_to="pdf/")

    class Meta:
        default_related_name = "checks"

    def __str__(self):
        return f"Check #{self.id}"