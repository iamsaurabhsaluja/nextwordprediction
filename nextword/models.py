from django.db import models

class Links( models.Model ):
    link_id = models.AutoField( primary_key = True )
    key = models.CharField( max_length = 255, unique=True )
    link_url = models.CharField( max_length = 255, unique=True )
    page_data = models.CharField( max_length = 255, unique=True )
    updated_time = models.DateTimeField( auto_now = True )
    is_crawled = models.BooleanField( default = False )

class Status( models.Model ):
    link_id = models.ForeignKey( Links, on_delete=models.CASCADE )
    is_crawled = models.BooleanField( default = False )

class History( models.Model ):
    last_crawled_id = models.ForeignKey( Links, on_delete=models.CASCADE )

class LinksQueue( models.Model ):
    link_id = models.ForeignKey( Links, on_delete=models.CASCADE )
