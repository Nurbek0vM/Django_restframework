from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True, null=True, related_name="movies")

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    stars = models.IntegerField(
        verbose_name='Звезды',
        help_text='Рейтинг отзыва от 1 до 5',
        choices=[(i, i) for i in range(1, 6)],  # Ограничивает значение от 1 до 5
        default=1, )

    def __str__(self):
        return self.text