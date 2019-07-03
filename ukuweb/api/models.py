# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from form_manager.models import UserProfile
import datetime


class Interviewed(models.Model):
    alias = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def complete_name(self):
        if self.name and self.last_name:
            return "{} - {} {}".format(self.alias, self.name, self.last_name)
        if self.name:
            return "{} - {}".format(self.alias, self.name)
        return self.alias


class FormDataManager(models.Manager):
    def create(self, form):
        """
        form = {
            "codigoPlantilla": "formularioPrueba",
            "coordenadas": null,
            "data": [],
            "fechaAcceso": "22/01/2019",
            "fechaCreacion": "22/01/2019",
            "fechaGuardado": "22/01/2019",
            "gps": false,
            "motivo": "No puedo",
            "usuario": {"username": "user example"}
        }
        """
        access_date = datetime.datetime.strptime(
            " ".join(form.get("fechaAcceso").split(" ")[:5]), "%a %b %d %Y %H:%M:%S"
        )
        created_date = datetime.datetime.strptime(
            " ".join(form.get("fechaCreacion").split(" ")[:5]), "%a %b %d %Y %H:%M:%S"
        )
        send_date = datetime.datetime.strptime(
            " ".join(form.get("fechaGuardado").split(" ")[:5]), "%a %b %d %Y %H:%M:%S"
        )
        form_data = self.model(
            type=form.get("codigoPlantilla"),
            coordinates=form.get("coordenadas", None),
            data=form.get("data"),
            access_date=access_date,
            created_date=created_date,
            send_date=send_date,
            include_gps=form.get("gps"),
            reason=form.get("motivo", None),
        )
        user = form.get("usuario", None)
        if user:
            user = UserProfile.objects.get(uid=user.get("uid"))
            form_data.user = user
        return form_data


class FormData(models.Model):
    type = models.CharField(max_length=500, blank=True)
    coordinates = models.CharField(max_length=100, null=True)
    data = models.TextField()
    access_date = models.DateField(null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)
    send_date = models.DateField(null=True, blank=True)
    include_gps = models.BooleanField(default=False)
    reason = models.TextField(null=True, blank=True)
    objects = FormDataManager()
    user = models.ForeignKey(UserProfile, null=True)
    interviewed = models.ForeignKey(Interviewed, null=True)

    def to_dict(self):
        return {
            "codigoPlantilla": self.type if self.type else "",
            "coordenadas": self.coordinates if self.coordinates else "",
            "data": self.data,
            "fechaAcceso": self.access_date,
            "fechaCreacion": self.created_date,
            "fechaGuardado": self.send_date,
            "gps": self.include_gps,
            "motivo": self.reason if self.reason else "",
            "usuario": self.user.uid if self.user else "",
        }
