from django.db import models
from mongoengine import Document, EmbeddedDocument, fields


class Setting(Document):
    nama = fields.StringField(required=True)
    jenis_usaha = fields.StringField(required=True)
    logo = fields.StringField(required=True)
