from django.contrib.admin import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.forms.widgets import SelectMultiple
from django.test import TestCase, RequestFactory
from django.test.utils import override_settings

from testapp.models import ProductGroup


class MockSuperUser:
    def has_perm(self, perm):
        return True


@override_settings(ROOT_URLCONF='testapp.urls_admin')
class MFLFAdminTests(TestCase):

    def setUp(self):
        site = AdminSite()
        self.admin = ModelAdmin(ProductGroup, site)
        request_factory = RequestFactory()
        self.request = request_factory.get('/admin')
        self.request.user = MockSuperUser()

    def testFieldListWidget(self):
        form = self.admin.get_form(None)
        self.assertEqual(list(form.base_fields), ['title', 'fields'])
        self.assertEqual(type(form.base_fields['fields'].widget), SelectMultiple)
        self.assertEqual(form.base_fields['fields'].widget.choices, [
            ('id', 'ID'),
            ('title', 'Title'),
            ('description', 'Description'),
            ('price', 'Price'),
            ('creation_date', 'Creation date'),
            ('color', 'Color'),
            ('material', 'Material'),
            ('weight', 'Weight')
        ])
