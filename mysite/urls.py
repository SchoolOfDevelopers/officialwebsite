from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from mysite.views import Index,ContactUs
from .views import InternshipApplyView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='welcome.html'),name='welcome'),
    url(r'^home$', Index.as_view(), name='index'),
    url(r'^Contact$', ContactUs.as_view(), name='contact'),
    url(r'^Internship$', InternshipApplyView.as_view(),name='internship'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Training$', TemplateView.as_view(template_name='courses/ittraining.html'),name='training'),
    url(r'^Training/Foundation/C$', TemplateView.as_view(template_name='courses/C.html'), name='cprogramming'),
    url(r"^Training/Foundation/C\+\+$", TemplateView.as_view(template_name='courses/C++ .html'), name='cplusplus'),
    url(r"^Training/Foundation/CoreJava$", TemplateView.as_view(template_name='courses/corejava.html'), name='corejava'),
    url(r"^Training/Advanced/Oracle$", TemplateView.as_view(template_name='courses/oracle.html'), name='oracle'),
    url(r"^Training/Advanced/Webdesign$", TemplateView.as_view(template_name='courses/webdesigning.html'), name='webdesign'),
    url(r"^Training/Advanced/SEO$", TemplateView.as_view(template_name='courses/seo.html'), name='seo'),
    url(r"^Training/Advanced/android$", TemplateView.as_view(template_name='courses/android.html'), name='android'),
    url(r'Success$', TemplateView.as_view(template_name='enquiry_success.html'), name='Success'),
)