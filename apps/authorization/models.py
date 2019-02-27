import re

from django.db import models
from django.conf import settings

from common.fields import JsonListTextField
from orgs.mixins import OrgModelMixin


def default_rule_to_patterns_handler(rule):
    url = '/api/{app}/{version}/{resource}/'


class BaseRole(models.Model):
    name = models.SlugField(max_length=128, unique=True, allow_unicode=True)
    rules = models.ManyToManyField('Rule')
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=128, blank=True, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Role(OrgModelMixin, BaseRole):
    pass


class ClusterRole(BaseRole):
    pass


class Rule(models.Model):
    verbs = JsonListTextField()
    apps = JsonListTextField()
    resources = JsonListTextField()
    resources_ids = JsonListTextField()
    non_resource_urls = JsonListTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=128, blank=True, default='')

    def to_patterns(self):
        pass


class BaseRoleBinding(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    groups = models.ManyToManyField(settings.AUTH_GROUP_MODEL)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=128, blank=True, default='')

    class Meta:
        abstract = True


class RoleBinding(OrgModelMixin, BaseRoleBinding):
    pass


class ClusterRoleBinding(BaseRoleBinding):
    pass
