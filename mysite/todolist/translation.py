from modeltranslation.translator import TranslationOptions,register
from .models import *
@register(Task)
class TaskTranslationOptions(TranslationOptions):
    fields = ['title','description']