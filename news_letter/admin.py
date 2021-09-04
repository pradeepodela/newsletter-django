from news_letter.models import Keyword, Tweet, TwitterHandle
from django.contrib import admin


admin.site.site_header = "News App"
admin.site.site_title = "News App"

# Register your models here.
admin.site.register(Keyword)
admin.site.register(TwitterHandle)
admin.site.register(Tweet)
