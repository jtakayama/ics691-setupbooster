"""Model for a wiki article."""

from django.db import models

OS_CHOICES = (
    ('LINUX', 'Linux'),
    ('MAC', 'Mac'),
    ('WINDOWS', 'Windows'),
    ('BSD', 'BSD'),
    ('OTHER UNIX', 'Other Unix'),
    ('IOS','iOS'),
    ('ANDROID', 'Android'),
    ('OTHER', 'Other'),
    ('MULTIPLATFORM', 'Multiplatform'),          
)

class Article(models.Model):
    title = models.CharField(max_length=250, help_text="The article title (up to 250 characters).<br/>")
    editors = models.TextField(help_text = "Comma-separated list of editors' usernames (e.g., Alice,Bob). Remember to add yourself.<br/>")
    # Targeted operating system
    os = models.CharField(max_length=100, choices=OS_CHOICES, help_text = "The OS this article will be written for.<br/>")
    category = models.CharField(max_length=250, help_text="The general subject of this article (e.g., Makahiki).<br/>")
    tags = models.TextField(help_text = "Comma-separated list of tags.")
    
    # The fields that must be determined by views.py, not the user
    revision = models.PositiveIntegerField()
    # article_file = models.FilePathField
    article_file = "Actual file creation not yet implemented."
    creationdate = models.DateField()
    lastedited = models.DateField()
    lasteditedby = models.CharField(max_length=250, help_text="The username of the last editor to work on the article.")
    
    # Pass in field values for a newly created article entry
    def saveNew(self, editor, revision_num, created, last_edit, last_edit_by):
        self.editors = editor
        self.revision = revision_num
        self.creationdate = created
        self.lastedited = last_edit
        self.lasteditedby = last_edit_by
        self.save()
    
    def __unicode__(self):
        return self.title
    
    def new_article(self):
        # unimplemented
        # open and write to some file
        return False
    
    # Check if a user can edit an article
    def is_editor(self, search_editor):
        editor = False
        for e in self.editors.split(','):
            if e == search_editor:
                editor = True
                break
        return editor
    
    # Appends the editor to the end of the string
    def add_editor(self, new_editor):
        self.editors += ("," + new_editor)
        return self.editors
    
    # Removes the editor from the comma-separated string 
    # and rebuilds the string
    def remove_editor(self, not_editor):
        all_editors = self.editors.split(',')
        remaining_editors = ""
        # Add the remaining editors back in.
        for e in all_editors:
            if e != not_editor:
                remaining_editors += (e + ',')
        # This is an implementation flaw, but I have not implemented
        # a system to let admins edit all articles yet.
        if remaining_editors.split(',').length == 0:
            return "You cannot remove the last editor from an article."
        else:
            self.editors = remaining_editors
            return remaining_editors
    
    # Check for a matching targeted pperating system
    def os_match(self, search_os):
        if self.os == search_os:
            return True
        else:
            return False
    
    # Check for a matching category
    def category_match(self, search_category):
        if self.category == search_category:
            return True
        else:
            return False
    
    # Check for a matching tag
    def tag_match(self, search_tag):
        is_tag_match = False
        for t in self.tags.split(','):
            if t == search_tag:
                is_tag_match = True
                break
        return is_tag_match
    
    # Appends the editor to the end of the string
    def add_tag(self, new_tag):
        self.tags += ("," + new_tag)
        return self.tags
    
    # Removes the tag from the comma-separated string 
    # and rebuilds the string
    def remove_tag(self, not_tag):
        all_tags = self.tags.split(',')
        remaining_tags = ""
        # Add the remaining tags back in.
        for t in all_tags:
            if t != not_tag:
                remaining_tags += (t + ',')
        if remaining_tags.split(',').length == 0:
            return "The article has no tags."
        else:
            self.tags = remaining_tags
            return remaining_tags
    
        