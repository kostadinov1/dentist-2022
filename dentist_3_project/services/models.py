from django.db import models


class Service(models.Model):
    CATEGORIES = (('1', 'Preventative'),
                  ('2', 'Restorative'),
                  ('3', 'Cosmetic'),)

    treatment = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    duration = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.treatment}'


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


'''
 --- TREATMENTS ---
COSMETIC:
    Teeth whitening treatment, cleanings
    crowns,
    teeth shaping
    tooth bonding
    veneers
    gum contouring

DIAGNOSTIC AND PREVENTATIVE: 
    sealants 
    fluoride treatments
    oral exams
    
RESTORATIVE:
    installing dental implants,
    bridges,  Braces
    dentures, inlays, onlays, 
    Cavity fillings
    Wisdom teeth removal
    Gum disease treatment 
    tooth extractions
'''