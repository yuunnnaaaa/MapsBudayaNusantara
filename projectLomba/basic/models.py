from django.db import models
import datetime
import os

# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)

class PopupInfo(models.Model):
    nama_daerah = models.CharField(max_length=200, null=False, blank=False)
    desc = models.TextField(max_length=700, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=False)
    slug = models.CharField(max_length=100, null=False, blank=False)
    tarian = models.CharField(max_length=100, null=True, blank=True)
    baju_adat = models.CharField(max_length=100, null=True, blank=True)
    alat_musik = models.CharField(max_length=100, null=True, blank=True)
    link_ref = models.CharField(max_length=700, null=True, blank=True)
    latitude = models.FloatField(help_text="Koordinat latitude titik pemancar", null=True, blank=True)
    longitude = models.FloatField(help_text="Koordinat longitude titik pemancar", null=True, blank=True)
    
    def __str__(self):
        return self.nama_daerah
    
