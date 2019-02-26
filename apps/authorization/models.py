from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.fields import JsonListTextField


class BaseRole(models.Model):
    name = models.SlugField(max_length=128, unique=True, allow_unicode=True)
    rules = models.ManyToManyField('Rule')
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=128, blank=True, default='')

    class Meta:
        abstract = True


class Role(BaseRole):
    org_id = models.CharField(max_length=36, blank=True, default='',
                              verbose_name=_("Organization"), db_index=True)


class ClusterRole(BaseRole):
    non_resource_urls = JsonListTextField()


class Rule(models.Model):
    VERBOSE_CHOICES = [
        ('list', 'List'),
        ('retrieve', 'Retrieve'),
        ('create', 'Create'),
        ('update', 'Update'),
        ('patch', 'PartialUpdate'),
        ('delete', 'Delete'),
    ]
    api_groups = JsonListTextField()
    resources = JsonListTextField()
    resourcesIDs = JsonListTextField()
    verbs = JsonListTextField()


class BaseRoleBinding(models.Model):

    class Meta:
        abstract = True


class RoleBinding(BaseRoleBinding):
    pass


class ClusterRoleBinding(BaseRoleBinding):
    pass
