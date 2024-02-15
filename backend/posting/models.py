from django.db import models
from authentication.models import Employer

EMPLOYMENT_TYPES = [
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
]

EMPLOYMENT_ARRANGEMENTS = [
    ('Remote', 'Remote'),
    ('Hybrid', 'Hybrid'),
    ('On-site', 'On-site')
]


class Posting(models.Model):
    posting_id = models.AutoField(primary_key=True)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    min_salary = models.IntegerField(default=0)
    max_salary = models.IntegerField(default=1)
    job_description = models.CharField(max_length=400)
    qualifications = models.CharField(max_length=400)
    benefits = models.CharField(max_length=400)
    employment_type = models.CharField(max_length=12, choices=EMPLOYMENT_TYPES)
    employment_arrangement = models.CharField(max_length=10, choices=EMPLOYMENT_ARRANGEMENTS)

