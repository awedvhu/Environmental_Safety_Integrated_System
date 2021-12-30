from django.db import models


# Create your models here.
class Department(models.Model):
    departmentID = models.AutoField(primary_key=True, unique=True)
    departmentName = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self

    class Meta:
        db_table = "Department"


class Auth(models.Model):
    authID = models.AutoField(primary_key=True, unique=True)
    authName = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self

    class Meta:
        db_table = "Auth"


class User(models.Model):
    UID = models.AutoField(primary_key=True, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
    JID = models.CharField(max_length=15, unique=True)
    userName = models.CharField(max_length=10)
    gentle = models.CharField(max_length=2)
    phone = models.CharField(max_length=15, unique=True)
    gmail = models.EmailField(max_length=50, unique=True)
    accountName = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=50)
    accountEnable = models.BooleanField(max_length=1)

    def __str__(self):
        return self

    class Meta:
        db_table = "User"


class Identify(models.Model):
    identifyID = models.AutoField(primary_key=True, unique=True)
    identifyName = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self

    class Meta:
        db_table = "Identify"


class EventName(models.Model):
    eventNameID = models.AutoField(primary_key=True, unique=True)
    identify = models.ForeignKey(Identify, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self

    class Meta:
        db_table = "Event_Name"


class Building(models.Model):
    buildingID = models.AutoField(primary_key=True, unique=True)
    buildingNumber = models.CharField(max_length=10, unique=True)
    buildingName = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self

    class Meta:
        db_table = "Building"


class Room(models.Model):
    RoomID = models.AutoField(primary_key=True, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    roomNumber = models.CharField(max_length=10)
    floor = models.IntegerField()

    def __str__(self):
        return self

    class Meta:
        db_table = "Room"


class Level(models.Model):
    levelID = models.AutoField(primary_key=True, unique=True)
    levelNumber = models.IntegerField(unique=True)
    numberOfPeople = models.IntegerField()

    def __str__(self):
        return self

    class Meta:
        db_table = "Level"


class Device(models.Model):
    deviceID = models.AutoField(primary_key=True, unique=True)
    identify = models.ManyToManyField(Identify, through='DeviceFeature')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    deviceNumber = models.CharField(max_length=10, unique=True)
    deviceIP = models.CharField(max_length=20, unique=True)
    deviceState = models.CharField(max_length=10)
    deviceEnable = models.BooleanField()
    deviceCoordinate = models.CharField(max_length=50)
    devicePhoto = models.ImageField()
    deviceNote = models.CharField(max_length=1000)

    def __str__(self):
        return self

    class Meta:
        db_table = "Device"


class DeviceFeature(models.Model):
    deviceFeatureID = models.AutoField(primary_key=True, unique=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    identify = models.ForeignKey(Identify, on_delete=models.CASCADE)
    deviceFeatureEnable = models.BooleanField()

    def __str__(self):
        return self

    class Meta:
        db_table = "Device_Feature"


class Event(models.Model):
    eventID = models.AutoField(primary_key=True, unique=True)
    PIC = models.ManyToManyField(User, through='EventPIC')
    eventName = models.ForeignKey(EventName, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    eventNumber = models.CharField(max_length=15, unique=True)
    eventState = models.CharField(max_length=10)
    eventTime = models.DateTimeField(auto_now_add=True)
    eventVideo = models.FileField()
    eventCloseDate = models.DateTimeField(null=True)

    def __str__(self):
        return self

    class Meta:
        db_table = "Event"


class EventPIC(models.Model):
    EventPICID = models.AutoField(primary_key=True, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    PIC = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self

    class Meta:
        db_table = "Event_PIC"
