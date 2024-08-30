from django.db import models

class Task(models.Model):
    team_choices = (("WorkFlow Team", 'WorkFlow Team'), ("Software Team", 'Software Team'), ("Accounting Team", "Accounting Team"), ("Quality Assurance Team", "Quality Assurance Team"), ("Testing Team", "Testing Team"))
    status_choices = (('Not Been Started', 'Not Been Started'), ("In Progress", "In Progress"), ("Pending", "Pending"))

    id = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=100)
    dueDate = models.DateField()
    status = models.CharField(choices=status_choices, max_length = 40)
    team = models.CharField(choices=team_choices, max_length = 50)



    def __str__(self):
        return self.taskName

class Report(models.Model):

    id = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=100)
    report = models.CharField(max_length=1000)

    def __str__(self):
        return self.taskName