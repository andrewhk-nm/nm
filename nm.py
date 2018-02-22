""" Collection of modules that are useful for my
work at Northwestern Mutual.

Andrew Henning-Kolberg
2016-02-14
"""

import datetime
import math
from gross_net_calculator import gross_net_calculator as gnc
from operator import itemgetter

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

def weeks_in_year(year):
    """ Given a year, returns the number of weeks per the iso calendar.
    Will always return 52 or 53
    """
    #TDD

    return max([datetime.datetime.isocalendar(datetime.datetime(year, 12, x))[1] for x in range(31 - 7, 32)])

def per_week_mark2(goal, have):
    """
    Not yet functional. This version will adjust with 53 week years.

    Given a Goal of 'goal' units and a current 'have' amount,
    return the average weekly production needed to meet that goal by the
    end of the year.

    Breaks if there are 53 weeks in the year.
    What happens during partial weeks?
    """
    pass
    #TODO: 53 week years
    #TODO: what value is returned during a partial week?
    current_year = datetime.datetime.now().year
    # creates a list of the iso week number for the last 7 days
    # in December of the current year. Taxes the max of that and
    # that is how many weeks the current year has (52 or 53)
    weeks_in_current_year = weeks_in_year(current_year)
    
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

def objectives(autosave_to_clipboard=False, retirement_age=None, min_rating=0, budget=None):
    """ Given number values, spit out the objectives in order.

    TODO: params.
        autosave_to_clipboard=False,
            This will copy the results to the clipboard
        retirement_age=None,
            This will add the "retire by age __. text"
        min_rating=0
            This will not print anything below (or should it be at or below?) min_rating
        budget=None
            This will do the "Allocate ___ per month toward attaining these objectives." statement
    """
    # 2018-02-21 Doesn't really work at all.
    # 2018-02-22 Sorting isn't working at all, I must be doing something wrong
    # 2018-02-22 Sorting is working!
    # TODO: put it on the clipboard automatically
    # TODO: I think entry should be a space separated string instead.
    objectives = ["Funding your children's education.",
                  "Funding a comfortable retirement.",
                  "Providing for your family in the event of death.",
                  "Providing for you and your family in the event of a disability.",
                  "Providing for long-term care needs.",
                  "Properly addressing your estate settlement needs.",
                  "Evaluating your investment portfolio.",
                  ]

    order = list()
    for obj in objectives:
        r = int(input('{}: '.format(obj)))
        order.append((r, obj))
    order = sorted(order, key=itemgetter(0), reverse=True)

    # print the results for easy copy/paste
    print('\nVVV Printing in order VVV\n')
    for _, obj in order:
        print(obj)
    print('\n^^^ Printed in order ^^^')
    return order
