"""Provides the view for the Create Article widget."""

import datetime
from apps.managers.article_mgr.models import NewArticleForm

def supply(request, page_name):
    """ supply view_objects for widget rendering."""
    _ = page_name
    profile = request.user.get_profile()
    
    if request.method =='POST':
        # Set the defaults for a new article
        form = NewArticleForm(request.POST)
        new_article = form.save(commit=False)
        new_article.revision = 0
        new_article.creationdate = datetime.datetime.now()
        new_article.lastedited = datetime.datetime.now()
        new_article.lasteditedby = profile.name
        new_article.save()
    else:
        form = NewArticleForm()

    return {
        "form": form,
    }
