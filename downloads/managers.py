from django.db.models import Manager
from django.db.models.query import QuerySet


class ReleaseQuerySet(QuerySet):
    def published(self):
        return self.filter(is_published=True)

    def draft(self):
        return self.filter(is_published=False)

    def downloads(self):
        """ For the main downloads landing page """
        return self.select_related('release_page').filter(
            is_published=True,
            show_on_download_page=True,
            pre_release=False,
        ).order_by('-release_date')

    def python2(self):
        return self.filter(version=2, is_published=True)

    def python3(self):
        return self.filter(version=3, is_published=True)

    def latest_python2(self):
        return self.python2().filter(is_latest=True)

    def latest_python3(self, major_version='', *, with_binaries=True):
        if major_version and major_version != '3':
            qs = self.python3().filter(pre_release=False, name__startswith=f'Python {major_version}.')
            if not with_binaries:
                qs = qs.filter(releasefile__is_source=False)
            return qs.order_by('-release_date')[:1]
        else:
            return self.python3().filter(is_latest=True)

    def pre_release(self):
        return self.filter(pre_release=True)

    def released(self):
        return self.filter(is_published=True, pre_release=False)


class ReleaseManager(Manager.from_queryset(ReleaseQuerySet)):
    def latest_python2(self):
        qs = self.get_queryset().latest_python2()
        if qs:
            return qs[0]
        else:
            return None

    def latest_python3(self, major_version='', *, with_binaries=True):
        qs = self.get_queryset().latest_python3(
            major_version, with_binaries=with_binaries
        )
        if qs:
            return qs[0]
        else:
            return None
