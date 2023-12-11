from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='Make')
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name




# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    # car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100, default='Car')

    TOYOTA_CAMRY = 'toyota_camry'
    TOYOTA_COROLLA = 'toyota_corolla'
    TOYOTA_RAV4 = 'toyota_rav4'
    TOYOTA_PRIUS = 'toyota_prius'
    TOYOTA_HIGHLANDER = 'toyota_highlander'

    # Tesla Models
    TESLA_MODEL_S = 'tesla_model_s'
    TESLA_MODEL_3 = 'tesla_model_3'
    TESLA_MODEL_X = 'tesla_model_x'
    TESLA_MODEL_Y = 'tesla_model_y'

    # Audi Models
    AUDI_A4 = 'audi_a4'
    AUDI_A6 = 'audi_a6'
    AUDI_Q5 = 'audi_q5'
    AUDI_Q7 = 'audi_q7'
    AUDI_A3 = 'audi_a3'

    # SEDAN = 'Sedan'
    # SUV = 'SUV'
    # WAGON = 'Wagon'
    TYPES = [
       (TOYOTA_CAMRY, 'Toyota Camry'),
        (TOYOTA_COROLLA, 'Toyota Corolla'),
        (TOYOTA_RAV4, 'Toyota RAV4'),
        (TOYOTA_PRIUS, 'Toyota Prius'),
        (TOYOTA_HIGHLANDER, 'Toyota Highlander'),
        (TESLA_MODEL_S, 'Tesla Model S'),
        (TESLA_MODEL_3, 'Tesla Model 3'),
        (TESLA_MODEL_X, 'Tesla Model X'),
        (TESLA_MODEL_Y, 'Tesla Model Y'),
        (AUDI_A4, 'Audi A4'),
        (AUDI_A6, 'Audi A6'),
        (AUDI_Q5, 'Audi Q5'),
        (AUDI_Q7, 'Audi Q7'),
        (AUDI_A3, 'Audi A3'),
    ]
    
    type = models.CharField(
        null=False,
        max_length=50,
        choices=TYPES,
        default=TESLA_MODEL_3
    )

    # type = models.CharField(
    #     null=False,
    #     max_length=50,
    #     choices=TYPES,
    #     default=SEDAN
    # )
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # dealer_id = models.IntegerField(default=1)
    # name = models.CharField(max_length=100)

    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name     



# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name



# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership  = dealership #Id of dealership
        self.name = name #name of reviewer
        self.purchase = purchase #if they purchased
        self.review = review #text of review
        self.purchase_date = purchase_date #the purchase date
        self.car_make = car_make #car make
        self.car_model = car_model #car model
        self.car_year = car_year #car year
        self.sentiment = sentiment #sentiment of the review
        self.id = id #id of the review

    def __str__(self):
        return "Reviewer Name: " + self.name + \
            "Review: " + self.review

class ReviewPost:

    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)
