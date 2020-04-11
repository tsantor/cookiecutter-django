# from django import forms

# # https://www.caktusgroup.com/blog/2018/06/18/make-all-your-django-forms-better/


# class BaseForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('label_suffix', '')
#         super().__init__(*args, **kwargs)

#     def disable_fields(self, field_names=[]):
#         """Disable group of fields."""
#         for f in field_names:
#             self.fields[f].disabled = True
#         return fields


# # def _disable_fields(self, field_names=[]):
# #     """Disable group of fields."""
# #     for f in field_names:
# #         self.fields[f].disabled = True
# #     return fields

# # forms.BaseForm.add_to_class('disable_fields', _disable_fields)
# forms.BaseForm = BaseForm
