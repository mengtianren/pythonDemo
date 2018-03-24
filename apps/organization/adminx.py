# _*_ coding:utf-8 _*_
import xadmin

from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):

    list_display = ['name', 'desc','add_time']
    search_fields = ['name', 'desc','add_time']
    list_filter = ['name', 'desc','add_time']


class CourseOrgAdmin(object):

    list_display = ['name', 'desc', 'click_nums','fav_nums','image','address','add_time']
    search_fields = ['name', 'desc', 'click_nums','fav_nums','image','address']
    list_filter = ['name', 'desc', 'click_nums','fav_nums','image','address','add_time']


class TeacherAdmin(object):

    list_display = [ 'name', 'work_years','work_company','work_position','points','click_nums','fav_nums']
    search_fields = [ 'name', 'work_years']
    list_filter = [ 'name', 'work_years','work_company','work_position','points','click_nums','fav_nums']




xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)