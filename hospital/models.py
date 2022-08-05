from django.db import models
from django.contrib.auth.models import User



centre=[('Centre Constantine','Centre Constantine'),
('centre Annaba','Centre Annaba'),
('Centre Alger','Centre Alger'),
('Centre Skikda','Centre Skikda'),
('Centre Batna','Centre Batna'),
('Centre oran','Centre oran'),
('Centre mila','Centre Mila')
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    centre= models.CharField(max_length=50,choices=centre,default='Constantine')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.centre)


class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)

class CentresOfVaccination(models.Model):
        centreId  =models.PositiveIntegerField(null=True)
        doctorNumber=models.PositiveIntegerField(null=True)
        Adresse=models.CharField(max_length=40,null=True)
    



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


class Test(models.Model):
    TYPE =(
      ('antigenic' , 'antigenic'),
      ('pcr' , 'pcr')
     
    )
    RESULT =(
      ('POSITIF' , 'POSITIF'),
      ('NEGATIF' , 'NEGATIF')
     
    )
          
    num_test =models.CharField(max_length=190,null=True)
    date = models.DateTimeField(auto_now_add=True , null = True)
    type = models.CharField(max_length=100 , null=True , choices=TYPE)
    resultat = models.CharField(max_length=100 , null=True , choices=RESULT)
    Patient = models.ForeignKey( Patient, null=True ,  on_delete= models.SET_NULL)  

class WilayaData(models.Model):
    wilaya = models.CharField(max_length=100)
    cas=models.IntegerField()  
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'virus Case wilaya'
    def __str__(self):
        return f'{self.wilaya}--{self.cas}'
class Vaccination(models.Model):
    CATEGORY = (
        ('Pfizer','Pfizer'),
        (' AstraZeneka ','AstraZeneka '),
        ('Spoutnik','Spoutnik')
    )
    vacc_id = models.CharField(max_length=190,null=True)
    date = models.DateTimeField(auto_now_add=True , null = True)
    marque =models.CharField(max_length=190,null=True , choices=CATEGORY)
    patient = models.ForeignKey(Patient , null=True ,  on_delete= models.SET_NULL)
    doctor = models.ForeignKey(Doctor , null=True ,  on_delete= models.SET_NULL)
    class Meta:
         db_table = ''
         managed = True
         verbose_name = 'Table vaccination'
         verbose_name_plural = 'Table vaccination'