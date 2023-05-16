from django.db import models

# Create your models here.
class createSellers(models.Model):
    fullname=models.CharField(max_length=500)
    adress=models.CharField(max_length=500)
    phonenum=models.CharField(max_length=15)
    def __str__(self):
        return self.fullname
    

types=('Bosh kiyimlar','Bosh kiyimlar'),("ko'ylaklar","ko'ylaklar"),("Etiklar va qo'nji kalta etiklar","Etiklar va qo'nji kalta etiklar"),("Shimlar va jinsilar","Shimlar va jinsilar"), ('Tufli va mokasinlar','Tufli va mokasinlar'),('Futbolkalar va maykalar','Futbolkalar va maykalar'),('Sport kiyimlari','Sport kiyimlari'),('Jemperlar va sviterlar','Jemperlar va sviterlar'),('Ustki kiyimlar','Ustki kiyimlar'),("Kostyumlar va to'plamlar","Kostyumlar va to'plamlar"),('Pidjaklar va jiletlari','Pidjaklar va jiletlari'),('Krossovkalar va kedalar',' Krossovkalar va kedalar')
# offers=('none','hech qaysi'),('5%','5%'),('10%','10%'),('15%','15%'),('20%','20%'),('30%','30%'),('40%','40%'),('50%','50%'),
class CreateProduct(models.Model):
    name=models.CharField(max_length=400)
    price=models.CharField(max_length=100)
    full_detail=models.TextField()
    # offer=models.CharField(max_length=12, choices=offers, default="none")
    images=models.ImageField(upload_to ='uploads/')
    producttype=models.CharField(choices=types, max_length=200, default='nomalum')
    seller=models.ForeignKey(createSellers,on_delete=models.CASCADE, default=5)
    # offered = models.CharField(max_length=200,blank=True,default=None, null=True)
   
    def __str__(self):
        return self.name
    
            


    