#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Provides the view of the widget."""


def supply(request, page_name):
    """ supply view_objects for widget rendering."""
    _ = request
    _ = page_name

    # Ratings system not yet implemented
    default_rating = u'\x2606\x2606\x2606\x2606\x2606'
    default_numeric_rating = 100

    return {
	"starstring": convert_numeric(default_numeric_rating),
        "rating": str(default_numeric_rating) + " %"
    }

def convert_numeric(numeric_rating):
    """Convert a numeric rating (out of 100%) to a star value"""
    star_rating = ""
    if numeric_rating < 40:
        star_rating = u'\u2606\u2605\u2605\u2605\u2605'
    elif numeric_rating >= 40 and numeric_rating <= 60:
        star_rating = u'\u2606\u2606\u2605\u2605\u2605'
    elif numeric_rating >= 60 and numeric_rating < 80:
        star_rating = u'\u2606\u2606\u2606\u2605\u2605'
    elif numeric_rating >= 80 and numeric_rating < 90:
        star_rating = u'\u2606\u2606\u2606\u2606\u2605'
    elif numeric_rating >= 90:
        star_rating = u'\u2606\u2606\u2606\u2606\u2606'
    return star_rating
