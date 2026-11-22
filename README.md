# Django model field list field

[![Test status](https://github.com/andreynovikov/django-mflf/actions/workflows/test.yaml/badge.svg)](https://github.com/andreynovikov/django-mflf/actions/workflows/test.yaml)
[![GitHub release](https://img.shields.io/github/release/andreynovikov/django-mflf.svg)](https://github.com/andreynovikov/django-mflf/releases/latest)
[![PyPI release](https://img.shields.io/pypi/v/django-mflf.svg)](https://pypi.org/project/django-mflf/)
[![Python version](https://img.shields.io/pypi/pyversions/django-mflf.svg)](https://pypi.org/project/django-mflf/)
[![GitHub issues](https://img.shields.io/github/issues/andreynovikov/django-mflf.svg)](https://github.com/andreynovikov/django-mflf/issues)
[![GitHub license](https://img.shields.io/github/license/andreynovikov/django-mflf.svg)](LICENSE)

This is a Django model field that provides a list of some other model's fields. Fields can be multi-selected and "under the hood" are stored as a comma-separated string. Also package provides simple form field with the same capabilities.

## Requirements

* Python 3.10+
* Django 5.2+ (5.2, 6.0 and 6.1 are tested)

## Installation

Install ```django-mflf``` using pip:

```shell
pip install django-mflf
```

Add ```model_field_list``` to ```INSTALLED_APPS```. Example:

```python
INSTALLED_APPS = (
    ...
    'model_field_list',
    ...
)
```

## Example usage

Model field:

```python
from model_field_list import ModelFieldListField

class ProductKind(models.Model):
    name = models.CharField(max_length=100)
    comparison = ModelFieldListField('comparison criteria', source_model=Product)
```

If referenced model has many fields it would be useful to use ```FilteredSelectMultiple``` in Django admin:

```python
from django.contrib.admin.widgets import FilteredSelectMultiple

class ProductKindAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            # different widget label is intentional
            'comparison': FilteredSelectMultiple('product properties', False)
        }
```

Simple form field:

```python
from django.contrib.admin.widgets import FilteredSelectMultiple
from model_field_list import ModelFieldListFormField

class ProductExportForm(ExportForm):
    export_fields = ModelFieldListFormField(source_model=Product, label='Export fields',
                                            widget=FilteredSelectMultiple('свойства товара', False))
```

## Limitations

- All model fields are listed, no option to filter them in any way.
- Field order can't be customized - they are sorted by the order of their definition in a model.

## Upgrading to 1.0

* Python 3.10+ and Django 5.2+ are required.
* ```ModelFieldListFormField``` takes ```source_model``` as a required keyword argument.

## Development

Tests are run with [tox](https://tox.wiki/) against all supported Python and Django versions:

```shell
pip install tox
tox                             # all available Python versions
tox -e py313-django61           # particular environment
python tests/runtests.py        # current virtual environment
```

To release a new version, update ```version``` in ```pyproject.toml```, commit the change and push a tag
with the same version:

```shell
git tag v1.0.0
git push origin v1.0.0
```

GitHub workflow runs the tests, publishes the package to TestPyPI and PyPI and creates GitHub release.
