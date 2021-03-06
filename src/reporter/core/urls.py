# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('reporter.core.views',
    url(r'^$',
        view='index',
        name='index'),
    url(r'^home/$',
        view='home',
        name='home'),
    url(r'^(?P<pk>\d+)/xml/$',
        view='report_xml',
        name='report_xml'),
    url(r'^(?P<pk>\d+)/$',
        view='report_html',
        name='report_html'),
    url(r'^latest/$',
        view='report_latest',
        name='report_latest'),
    url(r'^rss/$',
        view='report_rss',
        name='report_rss'),
    url(r'^rss/(?P<name>[\w-]+)/$',
        view='report_rss_selectednode',
        name='report_rss_selectednode'),
)
