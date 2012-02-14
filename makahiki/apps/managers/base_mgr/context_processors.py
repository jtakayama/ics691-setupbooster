""" It provides competition settings in the request context to be used within
 a template. It mainly retrieve the settings from settings files.
"""
from django.conf import settings
from managers.base_mgr import get_team_label, get_rounds_for_header, \
        get_current_round, get_current_round_info, in_competition
from managers.player_mgr.models import Profile
from managers.team_mgr.models import Team
from widgets.notifications import get_unread_notifications
from widgets.quests import get_quests


def competition(request):
    """Provides access to standard competition constants within a template."""
    user = request.user

    # Get user-specific information.
    team_count = Team.objects.count()
    overall_member_count = Profile.objects.count()
    team_member_count = None
    quests = None
    notifications = None

    if user.is_authenticated():
        quests = get_quests(user)
        notifications = get_unread_notifications(user, limit=3)
        if user.get_profile().team:
            team_member_count = user.get_profile().team.profile_set.count()

    # Get current round info.
    current_round = get_current_round() or "Overall"

    # Get Facebook info.
    try:
        facebook_app_id = settings.FACEBOOK_APP_ID
    except AttributeError:
        facebook_app_id = None

    return {
        "STATIC_URL": settings.STATIC_URL,
        "COMPETITION_NAME": settings.COMPETITION_NAME,
        "COMPETITION_POINT_NAME": settings.COMPETITION_POINT_NAME or "point",
        "CSS_THEME": settings.CSS_THEME,
        "THEME_NAME": settings.MAKAHIKI_THEME,
        "FLOOR_COUNT": team_count,
        "FLOOR_MEMBER_COUNT": team_member_count,
        "OVERALL_MEMBER_COUNT": overall_member_count,
        "ROUNDS": get_rounds_for_header(),
        "FLOOR_LABEL": get_team_label(),
        "CURRENT_ROUND": current_round,
        "CURRENT_ROUND_INFO": get_current_round_info(),
        "FACEBOOK_APP_ID": facebook_app_id,
        "QUESTS": quests,
        "NOTIFICATIONS": notifications,
        "IN_COMPETITION": in_competition(),
        "SPREADSHEETS": {
            "THIRTY_DAYS": settings.ENERGY_THIRTY_DAYS_URL,
            "ENERGY_GOAL": settings.ENERGY_GOAL_URL,
            "POWER": settings.POWER_GAUGE_URL,
            }
    }

