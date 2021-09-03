from django.db import models

# Create your models here.
from Production.models import BPRLog
from Products.models import Products


#   ------------------ Non Conformance  ------------------


class NCCategory(models.Model):
    category = models.CharField(max_length=30)
    subCategory = models.CharField(max_length=30)

    REQUIRED = ['category', 'subCategory']

    def __str__(self):
        return self.id


class NCR(models.Model):
    date = models.DateField(auto_now=True)
    NCRNo = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, default="OPEN")
    originator = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    sourceOfIdentification = models.CharField(max_length=30)
    refNo = models.CharField(max_length=30)
    natureOfNC = models.CharField(max_length=30)
    gradeOfNC = models.CharField(max_length=30)
    NCCategory = models.ForeignKey(NCCategory, on_delete=models.CASCADE, related_name="cat")
    batchNo = models.ForeignKey(BPRLog, on_delete=models.CASCADE, related_name="BNo")
    descriptionOFNonConformance = models.CharField(max_length=100)
    solutionOfCurrentProblem = models.CharField(max_length=30)
    immediateAction = models.CharField(max_length=30)
    isActionTaken = models.BooleanField()
    actionDate = models.DateField()
    verifiedBy = models.CharField(max_length=30)
    isLimitAction = models.BooleanField()
    rootCause = models.CharField(max_length=100, null=True, blank=True)
    proposedCorrectiveAction = models.CharField(max_length=100, null=True, blank=True)
    actionTaken = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.NCRNo
