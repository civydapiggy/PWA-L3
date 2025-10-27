from django.db import models

# Category Model
class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"  # nicer label in admin

    def __str__(self):
        return self.title


# Product Model
class Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField()  # keep as-is; you can make it unique later if you use it in URLs
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'   # handy reverse access: category.products.all()
    )
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()
    featured = models.BooleanField(default=False)  # ✅ used to filter homepage

    def __str__(self):
        return self.name