from django.db import models


class Organization(models.Model):
    name = models.CharField(verbose_name="NAME", max_length=100)


class Person(models.Model):
    name = models.CharField(verbose_name="full name", max_length=100)
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)
    married = models.BooleanField(verbose_name="married", default=False)


class Bulk(models.Model):
        title = models.CharField(max_length=200)
        category = models.CharField(max_length=11)
        details = models.TextField()
        reseller = models.CharField(max_length=11)
        reseller_mob = models.IntegerField(max_length=11)
        storages = models.CharField(max_length=11)
        products = models.CharField(max_length=11)
        start_time = models.DateTimeField()
        dead_time = models.DateTimeField()
        arrived_time = models.CharField(max_length=100, null=True)
        status = models.IntegerField(max_length=11)
        location = models.CharField(max_length=100)
        receive_mode = models.IntegerField(max_length=11, default=2)
        seq = models.IntegerField(max_length=11, default=0)
        card_title = models.CharField(max_length=100)
        card_desc = models.CharField(max_length=255)
        card_icon = models.ImageField(upload_to='images/card_icon/%Y/%m/%d', blank=True)
        create_time = models.DateTimeField(auto_now=True)
        volume = models.CharField(max_length=200)


#class Order(models.Model):
#	id = models.CharField(max_length=200, primary_key=True)
#	user = models.ForeignKey('User')
#	bulk = models.ForeignKey('Bulk')
#	receive_mode = models.IntegerField(max_length=11, default=2)
#	storage = models.ForeignKey('Storage', null=True)
#	receive_name = models.CharField(max_length=200, null=True, blank=True)
#	receive_mob = models.CharField(max_length=20, null=True, blank=True)
#	receive_address = models.TextField(null=True, blank=True)
#	status = models.IntegerField(max_length=11)
#	freight = models.IntegerField(max_length=11)
#	total_fee = models.IntegerField(max_length=11)
#	seq = models.IntegerField(max_length=11, default=0)
#	create_time = models.DateTimeField(auto_now=True)
#	obtain_name = models.CharField(max_length=100, null=True, blank=True)
#	obtain_mob = models.CharField(max_length=20, null=True, blank=True)
#	is_delete = models.BooleanField(default=False)
#	comments = models.TextField(null=True, blank=True)
