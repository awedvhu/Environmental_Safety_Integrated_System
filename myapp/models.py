from django.db import models


# Create your models here.
class Department(models.Model):
    departmentID = models.AutoField(primary_key=True, unique=True)
    departmentName = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = "Department"


class Auth(models.Model):
    authID = models.AutoField(primary_key=True, unique=True)
    authName = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = "Auth"


class User(models.Model):
    UID = models.AutoField(primary_key=True, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, to_field="departmentName")
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE, to_field="authName")
    JID = models.CharField(max_length=15, unique=True)
    userName = models.CharField(max_length=10)
    gentle = models.CharField(max_length=2)
    phone = models.CharField(max_length=15, unique=True)
    gmail = models.EmailField(max_length=50, unique=True)
    accountName = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=50)
    accountEnable = models.BooleanField(max_length=1)

    class Meta:
        db_table = "User"


class Identify(models.Model):
    identifyID = models.AutoField(primary_key=True, unique=True)
    identifyName = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = "Identify"


class EventName(models.Model):
    eventNameID = models.AutoField(primary_key=True, unique=True)
    identify = models.ForeignKey(Identify, on_delete=models.CASCADE, to_field="identifyName")
    eventName = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = "Event_Name"


class Building(models.Model):
    buildingID = models.AutoField(primary_key=True, unique=True)
    buildingNumber = models.CharField(max_length=10, unique=True)
    buildingName = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = "Building"


class Room(models.Model):
    RoomID = models.AutoField(primary_key=True, unique=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, to_field="buildingName")
    roomNumber = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField()

    class Meta:
        db_table = "Room"


class Level(models.Model):
    levelID = models.AutoField(primary_key=True, unique=True)
    levelNumber = models.IntegerField(unique=True)
    numberOfPeople = models.IntegerField()

    class Meta:
        db_table = "Level"


class Device(models.Model):
    deviceID = models.AutoField(primary_key=True, unique=True)
    identify = models.ManyToManyField(Identify, through='DeviceFeature')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, to_field="roomNumber")
    deviceNumber = models.CharField(max_length=10, unique=True)
    deviceIP = models.CharField(max_length=20, unique=True)
    deviceState = models.CharField(max_length=10, default="未連線")
    deviceEnable = models.BooleanField()
    deviceCoordinate = models.CharField(max_length=50)
    devicePhoto = models.ImageField(blank=True, null=True)
    deviceNote = models.CharField(max_length=1000, blank=True)

    class Meta:
        db_table = "Device"


class DeviceFeature(models.Model):
    deviceFeatureID = models.AutoField(primary_key=True, unique=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, to_field="deviceNumber")
    identify = models.ForeignKey(Identify, on_delete=models.CASCADE, to_field="identifyName")
    deviceFeatureEnable = models.BooleanField()

    class Meta:
        db_table = "Device_Feature"


class YearlyDutyList(models.Model):
    yearlyDutyListID = models.AutoField(primary_key=True, unique=True)
    year = models.IntegerField(unique=True)

    class Meta:
        db_table = "Yearly_Duty_List"


class MonthlyDutyList(models.Model):
    monthlyDutyListID = models.AutoField(primary_key=True, unique=True)
    year = models.ForeignKey(YearlyDutyList, on_delete=models.CASCADE, to_field="year")
    month = models.IntegerField(unique=True)

    class Meta:
        db_table = "Monthly_Duty_List"


class DaylyDutyList(models.Model):
    daylyDutyListID = models.AutoField(primary_key=True, unique=True)
    month = models.ForeignKey(MonthlyDutyList, on_delete=models.CASCADE, to_field="month")
    UID = models.ManyToManyField(User, through='DutyList')
    building = models.ManyToManyField(Building, through='DutyList')
    day = models.IntegerField(unique=True)

    class Meta:
        db_table = "Dayly_Duty_List"


class YearlyTotalEvent(models.Model):
    yearlyTotalEventID = models.AutoField(primary_key=True, unique=True)
    year = models.IntegerField(unique=True)

    class Meta:
        db_table = "Yearly_Total_Event"


class MonthlyTotalEvent(models.Model):
    monthlyTotalEventID = models.AutoField(primary_key=True, unique=True)
    year = models.ForeignKey(YearlyTotalEvent, on_delete=models.CASCADE, to_field="year")
    month = models.IntegerField(unique=True)

    class Meta:
        db_table = "Monthly_Total_Event"


class DaylyTotalEvent(models.Model):
    daylyTotalEventID = models.AutoField(primary_key=True, unique=True)
    month = models.ForeignKey(MonthlyTotalEvent, on_delete=models.CASCADE, to_field="month")
    day = models.IntegerField(unique=True)

    class Meta:
        db_table = "Dayly_Total_Event"


class Event(models.Model):
    eventID = models.AutoField(primary_key=True, unique=True)
    PIC = models.ManyToManyField(User, through='EventPIC')
    eventName = models.ForeignKey(EventName, on_delete=models.CASCADE, to_field="eventName")
    device = models.ForeignKey(Device, on_delete=models.CASCADE, to_field="deviceNumber")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, to_field="levelNumber")
    day = models.ForeignKey(DaylyTotalEvent, on_delete=models.CASCADE, to_field="day")
    eventNumber = models.CharField(max_length=15, unique=True)
    eventState = models.CharField(max_length=10, default="未處理")
    eventTime = models.DateTimeField(auto_now_add=True)
    eventVideo = models.FileField(blank=True, null=True)
    eventCloseDate = models.DateTimeField(null=True)
    wrongReport = models.BooleanField(default=False)

    class Meta:
        db_table = "Event"


class DutyList(models.Model):
    dutyListID = models.AutoField(primary_key=True, unique=True)
    day = models.ForeignKey(DaylyDutyList, on_delete=models.CASCADE, to_field="day")
    UID = models.ForeignKey(User, on_delete=models.CASCADE)
    dealWithEvent = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                      to_field="eventNumber")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, to_field="buildingName")
    workTimeStart = models.TimeField()
    workTimeEnd = models.TimeField()

    class Meta:
        db_table = "Duty_List"


class EventPIC(models.Model):
    eventPICID = models.AutoField(primary_key=True, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, to_field="eventNumber")
    PIC = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Event_PIC"
