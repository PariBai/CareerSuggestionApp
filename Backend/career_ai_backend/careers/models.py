from mongoengine import Document, StringField, ListField, DateTimeField
from datetime import datetime


class Suggestion(Document):
    name = StringField()
    age = StringField()
    skills = ListField(StringField())
    interests = ListField(StringField())
    goals = StringField()
    suggested_careers = ListField(StringField())
    reasoning = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
