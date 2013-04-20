"""Provides the view for the Create Article widget."""

import datetime
from apps.managers.article_mgr.forms import NewArticleForm

def supply(request, page_name):
    """ supply view_objects for widget rendering."""
    _ = page_name
    profile = request.user.get_profile()
    
    if request.method =='POST':
        # Set the defaults for a new article
        form = NewArticleForm(request.POST)
        new_article = form.save(commit=False)
        new_article.saveNew(0, datetime.datetime.now(), datetime.datetime.now(), profile.name)
    else:
        # Unbound form
        form = NewArticleForm()

    return {
        "form": form,
    }
