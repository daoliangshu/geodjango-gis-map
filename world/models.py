from django.contrib.gis.db import models
"""
class AirMeasurement(models.Model):
    
    wmoid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    air_quality_station = models.CharField(max_length=256)
    time_zone = models.CharField(max_length=256)
    country_code = models.CharField(max_length=256)
    sample = models.CharField(max_length=256)
    geom = models.PointField()

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'world'"""



class AirportModel(models.Model):
    scalerank = models.IntegerField()
    featurecla = models.CharField(max_length=80)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    abbrev = models.CharField(max_length=4)
    location = models.CharField(max_length=50)
    gps_code = models.CharField(max_length=254)
    iata_code = models.CharField(max_length=254)
    wikipedia = models.CharField(max_length=254)
    natlscale = models.FloatField()
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

class UrbanAreaModel(models.Model):
    scalerank = models.IntegerField()
    featurecla = models.CharField(max_length=50)
    area_sqkm = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    @property
    def prop_name(self):
        return "scalerank: "+ str(self.scalerank)

class WorldBorderModel(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    def get_name(self):
        return self.name

    def get_geom(self):
        return self.geom

    @property
    def prop_name(self):
        return self.name

class AdminBoundaryModel(models.Model):
    fid_ne_10m = models.IntegerField()
    scalerank = models.FloatField()
    featurecla = models.CharField(max_length=32)
    note_field = models.CharField(max_length=32)
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    adm0_usa = models.IntegerField()
    adm0_left = models.CharField(max_length=100)
    adm0_right = models.CharField(max_length=100)
    adm0_a3_l = models.CharField(max_length=3)
    adm0_a3_r = models.CharField(max_length=3)
    sov_a3_l = models.CharField(max_length=3)
    sov_a3_r = models.CharField(max_length=3)
    type = models.CharField(max_length=50)
    labelrank = models.IntegerField()
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    @property
    def prop_name(self):
        return self.name





"""
class WeatherStation(models.Model):

    wmoid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    geom = models.PointField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
        """



