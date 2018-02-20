""" Collection of modules that are useful for my
work at Northwestern Mutual.

Andrew Henning-Kolberg
2016-02-14
"""

import datetime
import math
from gross_net_calculator import gross_net_calculator as gnc

def per_week(goal, have):
    """ Given a Goal of 'goal' units and a current 'have' amount,
    return the average weekly production needed to meet that goal by the
    end of the year.

    Breaks if there are 53 weeks in the year.
    What happens during partial weeks?
    """
    #TODO: 53 week years
    #TODO: what value is returned during a partial week?
    # See per_week_mark2()
    
    return (goal - have) / (52 - datetime.datetime.isocalendar(
        datetime.datetime.now())[1])

def per_week_mark2(goal, have):
    """
    Not yet functional. This version will adjust with 53 week years.

    Given a Goal of 'goal' units and a current 'have' amount,
    return the average weekly production needed to meet that goal by the
    end of the year.

    Breaks if there are 53 weeks in the year.
    What happens during partial weeks?
    """
    #TODO: 53 week years
    #TODO: what value is returned during a partial week?
    current_year = datetime.datetime.now().year

    if datetime.datetime.isocalendar(datetime.datetime(2018, 12, 31))[0] 
    
    return (goal - have) / (52 - datetime.datetime.isocalendar(
        datetime.datetime.now())[1])

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
    r is interest rate
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
