from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

import datetime

# Create your models here.

class UserInfo(models.Model):
    """ Stores additional information for the user model """
    user       = models.OneToOneField(User, related_name="mhr_info")
    course     = models.CharField(max_length=30, blank=True, null=True)
    is_ta      = models.BooleanField(default=True)
    is_admin   = models.BooleanField(default=False)
    num_blocks = models.IntegerField(default=1)
    phone      = models.CharField(max_length=20, blank=True, null=True)

    def change_blocks(self, new_blocks):
        self.num_blocks = new_blocks
        self.save()

    def change_course(self, new_course):
        self.course = new_course
        self.save()

    def change_phone(self, new_phone):
        self.phone = new_phone
        self.save()

    def __str__(self):
        return self.user.username

class TimeTable(models.Model):
    """ The timtable itself """

    title = models.CharField(max_length=100)
    # When the timetable takes effect and ends
    start = models.DateField()
    end   = models.DateField()
    # Number of minutes per block
    interval = models.IntegerField(default=30)
    # Maximum TAs per slot
    max_per_slot = models.IntegerField(default=3)
    # For open enrollment, specify a datetime
    open_start = models.DateTimeField()
    open_end   = models.DateTimeField()

    def __str__(self):
        return self.title

class DayOfWeek(models.Model):
    """ One of the seven days a week. Generated when the timetable is created
        according to admin specification.
    """
    CHOICES = ( 
            ('SUN', 'Sunday'),
            ('MON', 'Monday'),
            ('TUE', 'Tuesday'),
            ('WED', 'Thursday'),
            ('THU', 'Frday'),
            ('SAT', 'Saturday'),
    )

    day_name  = models.CharField(choices=CHOICES, max_length=3)
    timetable = models.ForeignKey(TimeTable, related_name="dow")

    def __str__(self):
        return "{dow}: {timetable}".format(
                dow=self.day_name,
                timetable=self.timetable.title)

class TimeOfDay(models.Model):
    """ The time of the day. Linked to a day to allow variable hour ranges.
        Autogenerated with the timetable is created, according to admin
        specification.
    """
    # Of the form 2130, in 24 hour time
    timeblock = models.CharField(max_length=4)
    dow       = models.ForeignKey(DayOfWeek)

class TimeSlots(models.Model):
    """ An enrollment spot for a TA """
    ta   = models.ForeignKey(User, related_name="ta_timeslots")
    time_table = models.ForeignKey(TimeTable)
    # Store the data as day of week (dow) and time
    tod = models.ForeignKey(TimeOfDay, related_name="tod_timeslots")
