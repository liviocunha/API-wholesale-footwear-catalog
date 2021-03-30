from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, help_text="Category of footwear.", verbose_name="Category")

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField(max_length=100, help_text="Collection.", verbose_name="Collection")

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=100, help_text="Status of sale.", verbose_name="Status")

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=100, help_text="Size grid.", verbose_name="Size")

    def __str__(self):
        return self.title


class Footwear(models.Model):
    code = models.CharField(max_length=100, help_text="Code of footwear.", verbose_name="Code")
    upper = models.CharField(max_length=100, help_text="Upper/Leather material of footwear.", verbose_name="Upper")
    name = models.CharField(max_length=100, help_text="Title of footwear", verbose_name="Title")
    outsole = models.CharField(max_length=100, help_text="Outsole material of footwear.", verbose_name="Outsole")
    lining = models.CharField(max_length=100, help_text="Lining material of footwear.", verbose_name="Lining")
    shoelaces = models.CharField(max_length=100, help_text="Shoelaces material of footwear.", verbose_name="Shoelaces")
    insole = models.CharField(max_length=100, help_text="Insole material of footwear.", verbose_name="Insole")
    abc_curve = models.CharField(max_length=1, help_text="ABC curve of footwear.", verbose_name="Curve")
    cost_price = models.FloatField(null=True, blank=True, verbose_name="USD $")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.code


class Photo(models.Model):
    code_footwear = models.ForeignKey(Footwear, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=100, help_text="Title of photo.", verbose_name="Title")
    url = models.URLField(max_length=200, help_text="URL of photo.", verbose_name="URL")
    thumb = models.URLField(max_length=200, help_text="URL thumb of photo.", verbose_name="Thumb")
    mime = models.CharField(max_length=100, help_text="Mime type of photo.", verbose_name="MIME")
    extension = models.CharField(max_length=10, help_text="Extension type of photo.", verbose_name="Extension")

    def __str__(self):
        return self.url
