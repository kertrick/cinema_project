from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True, null=True)
    duration = models.PositiveIntegerField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.title

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField()
    hall = models.CharField(max_length=20)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='tickets')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='tickets')
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Ticket {self.id} for {self.session.movie.title}"

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.position}"
