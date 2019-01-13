from django.contrib.auth.models import User
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
class CoursewareChapter(models.Model):
    """
    Link One - one to CourseOverview
    """
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # department = models.CharField(max_length=100)
    # user_id =  models.IntegerField()
    user = models.ForeignKey(User)
    course = models.ForeignKey(CourseOverview)
    display_name = models.TextField(max_length=455)
    chapter_id = models.CharField(max_length=255)
    created_on =models.DateField()
    id=models.AutoField(primary_key=True)
    class Meta:
        db_table = "courseware_chapters"