from django.db import models

# def get_internal(name):
#     ans = ""
#     for char in name:
#         if (char>=48 & char<= 58) | (char>=65 & char<=90) | (char >= 97 & char<=122):
#             ans+=char
#     return ans

class Subject(models.Model):
    name = models.CharField(max_length=30)
    internal = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    internal = models.CharField(max_length=30, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class URL(models.Model):
    description = models.CharField(max_length=50)
    url = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.description