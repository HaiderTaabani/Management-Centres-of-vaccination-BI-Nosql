from django.contrib import admin
from .models import  CentresOfVaccination, Doctor,Patient,Appointment,PatientDischargeDetails, Test, Vaccination, WilayaData
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)


admin.site.register(Test)

admin.site.register(WilayaData)

admin.site.register(Vaccination)
admin.site.register(CentresOfVaccination)
