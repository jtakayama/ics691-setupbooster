"""Celery Task definitions."""

from celery.task import task
import datetime
from apps.managers.challenge_mgr import challenge_mgr
from apps.widgets.resource_goal import resource_goal


@task
def check_energy_goal():
    """check the energy goal for all teams and update energy baseline"""
    today = datetime.datetime.today()
    print '****** Processing check_energy_goal and update baseline for %s *******\n' % today

    challenge_mgr.init()
    today = today.date()
    resource_goal.check_resource_goals("energy", today)

    # update the baseline
    resource_goal.update_resource_baseline("energy", today, 2)


@task
def check_water_goal():
    """check the water goal for all teams and update energy baseline"""
    today = datetime.datetime.today()
    print '****** Processing check_water_goal and update baseline for %s *******\n' % today

    challenge_mgr.init()
    today = today.date()
    resource_goal.check_resource_goals("water", today)

    # update the baseline
    resource_goal.update_resource_baseline("water", today, 2)
