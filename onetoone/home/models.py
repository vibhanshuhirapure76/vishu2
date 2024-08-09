from django.db import models
class Trainer(models.Model):
    tname=models.CharField(max_length=20)
    language=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.tname+' '+self.language
class Student(models.Model):
    sname=models.CharField(max_length=30)
    branch=models.CharField(max_length=20)
    trainer=models.OneToOneField(Trainer,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.sname+' '+self.branch