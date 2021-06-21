from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import uuid


class UUIDPkFieldMixin(models.Model):
    id = models.UUIDField(primary_key=True, verbose_name=_('uuid'), default=uuid.uuid4,
                          editable=False, unique=True)

    class Meta:
        abstract = True

    @property
    def get_pk(self):
        return str(self.id)


class TimeManagerMixin(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True, )

    class Meta:
        abstract = True


class SetUpModel(TimeManagerMixin,
                 UUIDPkFieldMixin,
                 models.Model):
    class Meta:
        abstract = True


class ParanoiaQuerySet(QuerySet):
    """
    Prevents objects from being hard-deleted. Instead, sets the
    ``date_deleted``, effectively soft-deleting the object.
    """

    def delete(self):
        for obj in self:
            obj.deleted_at = timezone.now()
            obj.save()


class ParanoiaManager(models.Manager):
    """
    Only exposes objects that have NOT been soft-deleted.
    """

    def get_queryset(self):
        return ParanoiaQuerySet(self.model, using=self._db).filter(
            deleted_at__isnull=True)


class ParanoiaMixin(models.Model):
    class Meta:
        abstract = True

    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = models.Manager()
    objects_without_deleted = ParanoiaManager()

    def delete(self, **kwargs):
        self.deleted_at = timezone.now()
        self.save()

    @property
    def get_deleted_str(self):
        return ' - Deletado' if self.deleted_at else ''
