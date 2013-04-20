from django.db import models
from django.forms import ModelForm
from apps.managers.article_mgr.models import Article

class NewArticleForm(ModelForm):
    title = models.CharField(max_length=250, required=True, help_text="The article title (up to 250 characters).")
    editors = models.TextField(required=True, help_text = "Comma-separated list of editors (e.g., Alice,Bob)."),
    os = models.CharField(max_length=250, required=True, help_text = "The OS this article will be written for."),
    category = models.CharField(required=True, help_text="The general subject of this article (e.g., Makahiki."),
    tags = models.TextField(required=True, help_text = "Comma-separated list of tags.")
    # It is expected that a views.py file that uses this form will provide default
    # values for revision, creationdate, lastedited, and lasteditedby.
    
    class Meta:
        model = Article
        fields = ('title', 'editors', 'os', 'category', 'tags')
        