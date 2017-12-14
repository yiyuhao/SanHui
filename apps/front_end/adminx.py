import xadmin
from xadmin import views


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSetting:
    site_title = '三会村后台管理'
    site_footer = '假装是一个公司'
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
