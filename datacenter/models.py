from django.db import models
from django.utils import timezone


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
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def get_duration(self):
        if self.leaved_at is None:
            return timezone.localtime() - self.entered_at
        return self.leaved_at - self.entered_at

    def is_long(self, minutes):
        return self.get_duration().total_seconds() > minutes * 60

    def format_duration(self):
        duration_seconds = self.get_duration().total_seconds()
        hours = duration_seconds // (60 * 60)
        if hours > 0: 
            minutes = duration_seconds // 60 % (hours * 60)
        else:
            minutes = duration_seconds // 60
        return '{:.0f}ч {:.0f}м'.format(hours, minutes)
