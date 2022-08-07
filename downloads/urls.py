from . import views
from django.urls import path, re_path

app_name = 'downloads'
urlpatterns = [
    re_path(r'latest/python2/?$', views.DownloadLatestPython2.as_view(), name='download_latest_python2'),
    re_path(
        r'latest/python3/with_binaries/?$',
        views.DownloadLatestPython3.as_view(),
        name='download_latest_python3_bin',
        kwargs={'with_binaries': True},
    ),
    re_path(r'latest/python3/?$', views.DownloadLatestPython3.as_view(), name='download_latest_python3'),
    re_path(
        r'latest/python(?P<major_version>3(?:\.\d+)?)/with_binaries/?$',
        views.DownloadLatestPython3.as_view(),
        name='download_latest_python3x_bin',
        kwargs={'with_binaries': True},
    ),
    re_path(
        r'latest/python(?P<major_version>3(?:\.\d+)?)/?$',
        views.DownloadLatestPython3.as_view(),
        name='download_latest_python3x_bin',
    ),
    path('operating-systems/', views.DownloadFullOSList.as_view(), name='download_full_os_list'),
    path('release/<slug:release_slug>/', views.DownloadReleaseDetail.as_view(), name='download_release_detail'),
    path('<slug:slug>/', views.DownloadOSList.as_view(), name='download_os_list'),
    path('', views.DownloadHome.as_view(), name='download'),
]
