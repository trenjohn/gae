# Put here your models or extend User model from bp_includes/models.py

from google.appengine.ext import ndb

class Game(ndb.Model):
    #user = ndb.ReferenceProperty(Account)
    numberPlayers = ndb.IntegerProperty()
    entryFee = ndb.FloatProperty()
    usersSignedUp = ndb.JsonProperty()
    usersSignedUpCount = ndb.ComputedProperty(self lambda: self.len(usersSignedUp))
    #PrizeStructure (Model w/ variety of types)
    #StartTime
    #Duration
    #EndTime
    #GameResultKey (ForeignKey) - 1 to 1
