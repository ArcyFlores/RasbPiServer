from django.db import models

# Create your models here.
# Create your models here.


class File(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=250)
    file_id = models.AutoField(primary_key=True)

    def delete(self):
        self.file.delete()
        super(File, self).delete()
