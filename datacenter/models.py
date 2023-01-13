from django.db import models
from django.utils.timezone import localtime
from datetime import timedelta


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        return localtime(self.leaved_at)-localtime(self.entered_at)
            
    def format_duration(self, duration):
        total_seconds = timedelta.total_seconds(duration)
        total_hours = total_seconds / 3600
        total_minutes = (total_seconds % 3600) // 60
        return f'{round(total_hours)} hours {round(total_minutes)} mins'
          
    def is_visit_long(self, minutes):
        duration = self.get_duration()
        total_minutes = timedelta.total_seconds(duration)//60
        return total_minutes > minutes
