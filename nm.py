""" Collection of modules that are useful for my
work at Northwestern Mutual.

Andrew Henning-Kolberg
2016-02-14
"""
# As functions get large, extract them to their own module.

## not mine
import datetime
import math
from tkinter import Tk
import sys
from nm_objectives import objectives
## /not mine

## mine
def debug_print(string):
    """ allow for turning debug effects on and off. probably can
    be a class eventually

    """
    print(string)
## try this import and print an error if it failes
try:
    from gross_net_calculator import gross_net_calculator as gnc
except (NameError, ModuleNotFoundError) as error:
    debug_print('module gross_net_calculator not found. Skipping this module.')
    pass
import nm_netx_cob
# /mine

### Done with imports. That's super messy.

def pension_est(top_salary, years_of_service):
    """ Returns an estimated Pension amount based on the formula
        Ballpark = Top Earnings Years * # of years of service * 0.011

        Uses floats
    """
    # Probably need to watch for floating point issues.
    return top_salary * years_of_service * 0.011


def ages(*birthyears):
    """ Takes a comma separated list of birthyears and returns their
        ages.
    """
    years = list()
    for year in birthyears:
        years.append(datetime.datetime.now().year - year)
    return years
    

def weeks_in_year(year):
    """ Given a year, returns the number of weeks per the iso calendar.
    Will always return 52 or 53
    """
    #TDD

    # creates a list of the iso week number for the last 7 days
    # in December of the current year. Takes the max of that and
    # that is how many weeks the current year has (52 or 53)

    return max([datetime.datetime.isocalendar(datetime.datetime(year, 12, x))[1] for x in range(31 - 7, 32)])

def per_week(goal, have, ):
    """
    Given a Goal of 'goal' units and a current 'have' amount,
    return the average weekly production needed to meet that goal by the
    end of the year, rounded to two decimal places.
    """
    # DONE: 53 week years
    # DONE: what value is returned during a partial week?
    # TODO: This appears affected by the time of the week the calculation
    #       is done. It assumes it's the end of the current week.
    #       I should probably add a flag to say how much of the current
    #       week is left to work into the calcuation.
    current_year = datetime.datetime.now().year
    weeks_in_current_year = weeks_in_year(current_year)

    return round((goal - have) / (weeks_in_current_year - datetime.datetime.isocalendar(
        datetime.datetime.now())[1]), 2)

def ci(P, r, n, t):
    """ "A = P(1 + r/n)**(nt)"
    P is principal
    r is interest rate
    n is number of times interest is compounded per year
    t is time in years
    return A, the amount
    """
    return P * (1 + (r / n)) ** (n * t)

def ci_list(P, r, n, t):
    """ "A = P(1 + r/n)**(nt)"
    P is principal
    r is interest rate (enter 8% as 0.08)
    n is number of times interest is compounded per year, as a list
    t is time in years
    return A, the amount
    """
    return_list = [P * (1 + (r / x)) ** (x * t) for x in n]
    
    return return_list

def ci_pert(P, r, t):
    """ "A = P*e**rt"
    P is principal
    r is interest rate
    t is time in years
    return A, the amount
    """
    return P * math.e ** (r * t)

def copy_to_clipboard(to_clipboard):
    """ Add whatever is passed to the clipboard.
    """
    rtk = Tk()
    rtk.withdraw()
    rtk.clipboard_clear()
    rtk.clipboard_append(to_clipboard)
    rtk.update() # now it stays on the clipboard after the window is closed
    rtk.destroy()

def c(to_clipboard):
    """ Add whatever is passed to the clipboard.
        (Short name version of copy_to_clipboard)
    """
    copy_to_clipboard(to_clipboard)


    
