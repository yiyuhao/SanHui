import xadmin
from xadmin import views

from .models import Village


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '三会村数据管理'
    site_footer = '假装是一个公司'
    menu_style = 'accordion'


class VillageAdmin(object):
    list_display = ('name', 'people_nums', 'add_time')
    search_fields = ('name', 'people_nums')
    list_filter = list_display

xadmin.site.register(Village, VillageAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)