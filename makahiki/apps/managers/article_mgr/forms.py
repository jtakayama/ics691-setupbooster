from django.forms import ModelForm
from apps.managers.article_mgr.models import Article

class NewArticleForm(ModelForm):
    # It is expected that a views.py file that uses this form will provide default
    # values for revision, creationdate, lastedited, and lasteditedby.
    
    class Meta:
        model = Article
        fields = ('title', 'os', 'category', 'tags')