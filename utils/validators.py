from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class CPFValidator(object):
    def __call__(self, cpf):
        cpf = cpf.replace("-", "")
        cpf = cpf.replace(".", "")

        if (not cpf) or (len(cpf) < 11):
            raise ValidationError(_('CPF invalido'))

        if cpf == len(cpf) * cpf[0]:
            raise ValidationError(_('CPF invalido'))

        inteiros = list(map(int, cpf))
        novo = inteiros[:9]
        while len(novo) < 11:
            r = sum([(len(novo) + 1 - i) * v for i, v in enumerate(novo)]) % 11
            if r > 1:
                f = 11 - r
            else:
                f = 0
            novo.append(f)

        if not bool(novo == inteiros):
            raise ValidationError(_('CPF invalido'))


@deconstructible
class PorcentagemValidator():
    def __call__(self, fio2):
        try:
            if not (0 <= fio2 <= 100):
                raise ValidationError(f'{fio2} deve estar entre 0 e 100', params={'fio2': fio2})
        except TypeError:
            raise ValidationError(f'{fio2} deve ser um número', params={'fio2': fio2})


@deconstructible
class IntPositivoValidator():
    def __call__(self, int):
        try:
            if not int >= 0:
                raise ValidationError(f'{int} deve ser maior do que 0', params={'int': int})
        except TypeError:
            raise ValidationError(f'{int} deve ser um número', params={'int': int})
