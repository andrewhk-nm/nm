""" Collection of modules that are useful for my
work at Northwestern Mutual.

Andrew Henning-Kolberg
2016-02-14
"""

## not mine
import datetime
import math
from operator import itemgetter
from tkinter import Tk
import sys
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

def ages(*birthyears):
    """ Takes a comma separated list of birthyears and returns their
        ages.
    """
    years = list()
    for year in birthyears:
        years.append(datetime.datetime.now().year - year)
    return years
    

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
    This version will adjust with 53 week years.

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
    # in December of the current year. Takes the max of that and
    # that is how many weeks the current year has (52 or 53)
    weeks_in_current_year = weeks_in_year(current_year)
    
    return (goal - have) / (weeks_in_current_year - datetime.datetime.isocalendar(
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

def objectives(input_str=None,
               input_str_sep=' ',
               input_list=None,
               retirement_age=None,
               r=None,
               min_rating=0,
               budget=None,
               b=None,
               copy_output_to_clipboard=True,
               *args,
               ):
    """ Given number values, spit out the objectives in order.
    TODO: Command Line Args
    TODO: params.
        input_str
            use input_str or input_list, not both.
            if not None, use this as a list of inputs instead of asking for each
            one. There are 7 objectives by default.
            use form '1 2 3 4 5 6 7 8 9' by default
        input_str_sep
            the separator that input_str.split() will pass to sep=.
        input_list
            use input_str or input_list, not both.
            if not None, use this as a list of inputs instead of asking for each
            one. There are 7 objectives by default.
        retirement_age=None, (short name: r=None)
            String. This will add the "retire by age __. text"
            r overrides retirement_age, if both are passed.
        min_rating=0
            This will not print anything below (or should it be at or below?) min_rating
        budget=None, (short name: b=None)
            This will do the "Allocate ___ per month toward attaining these objectives." statement
            b overrides budget, if both are passed.
        copy_output_to_clipboard=True
            replace the clipboard contents with this output
        *args
            Any strings passed will be added as objectives.
    """
    # 2018-02-21 Doesn't really work at all.
    # 2018-02-22 Sorting isn't working at all, I must be doing something wrong
    # 2018-02-22 Sorting is working!
    # 2018-02-22 put it on the clipboard automatically
    # 2018-02-22 I think entry should be a space separated string instead.
    objectives = ["Funding your children's education.",
                  "Funding a comfortable retirement.",
                  "Providing for your family in the event of death.",
                  "Providing for you and your family in the event of a disability.",
                  "Providing for long-term care needs.",
                  "Properly addressing your estate settlement needs.",
                  "Evaluating your investment portfolio.",
                  ]
    
    # Change/add objectives based on the parameters given
    if r:
        retirement_age = r
    if retirement_age:
        objectives[1] = "Funding a comfortable retirement by age {}".format(retirement_age)

    if input_str:
        # if an input string was passed, split it and override
        # any input_list that may have been passed
        input_list = input_str.split(sep=input_str_sep)

    order = list()
    if not input_list:
        # if there's nothing passed as a prefilled input list, ask question
        # by question.
        for obj in objectives:
            r = int(input('{}: '.format(obj)))
            order.append((r, obj))
    elif input_list:
        # this is a list of the answers. put them together in a tuple
        for r, obj in enumerate(objectives):
            order.append((input_list[r], obj))
    order = sorted(order, key=itemgetter(0), reverse=True)

    # Add the budget line as the last item if a budget is given
    if b:
        budget = b
    if budget:
        order.append((len(order), "Allocate ${} per month toward attaining these objectives.".format(budget)))

    # copy the output to the clipboard, if the option is enabled
    if copy_output_to_clipboard:
        rtk = Tk()
        rtk.withdraw()
        rtk.clipboard_clear()

    # print the results for easy copy/paste
    print('\nVVV Printing in order VVV\n')
    last_element = len(order)
    c = 1
    for _, obj in order:
        print(obj)
        if copy_output_to_clipboard:
            rtk.clipboard_append(obj)
        if c < last_element:
            #debug_print('c={} last_element={}'.format(c, last_element))
            rtk.clipboard_append('\n')
            c += 1
            
    print('\n^^^ Printed in order ^^^\n')

    # print clipboard contents
    #print('printing clipboard={}'.format(rtk.clipboard

    if copy_output_to_clipboard:
        debug_print('Printing clipboard contents:\n{}'.format(rtk.selection_get(selection="CLIPBOARD")))
        rtk.update() # now it stays on the clipboard after the window is closed
        rtk.destroy()
        print('\nOutput copied to clipboard.')



    #return order

def _process_args():
    """
    # NAME
    #   nm.py
    # SYNTAX
    #   nm.py [[--objectives_ranks] [-o]] <'space separated string of ranks'>
    #   nm.py [[--retirement_age] [-r]] <string age>
    #   nm.py [[--minimum_rank] [-m]] <string minimum printable rank>
    #   nm.py [[--budget] [-b]] <string monthly_budget>
    #   nm.py [[--no_clipboard] [-n]]
    #
    # Only the objectives() module is currently supported at the commandline
    """
    # TODO: Copying to the clipboard doesn't work when I run this from
    #       the command line
    #   Get contents of clipboard: result = r.selection_get(selection = "CLIPBOARD")
    # don't pass thru the module name
    arg_list = sys.argv[1:]
    # reverse the list so it pops in order
    arg_list.reverse()
    # Initialize the variables that will be passed as parameters
    objectives_ranks = None
    retirement_age = None
    minimum_rank = None
    budget = None
    use_clipboard = True
    while arg_list:
        # cycle through each arg and process as appropriate
        # remove them from arg_list as you go
        arg = arg_list.pop()
        debug_print('popped arg={}'.format(arg))
        # parser for the objective ranks
        if arg == '--objectives_ranks' or arg == '-o':
            # expect a single string of numbers to follow this arg
            # currently only supports a single space separated string
            arg = arg_list.pop()
            objectives_ranks = arg.split()
            # clear the arg before continuing
            arg = None
        elif arg == '--retirement_age' or arg == '-r':
            # expect a single string representing the age or ages of
            # retirement
            # e.g. -r 65
            #      -r 65/62
            #       the second option would be for a couple
            arg = arg_list.pop()
            retirement_age = arg
            # clear the arg before continuing
            arg = None
        elif arg == '--minimum_rank' or arg == '-m':
            # expect a single number representing the minimum rank to print
            arg = arg_list.pop()
            minimum_rank = int(arg)
            # clear the arg before continuing
            arg = None
        elif arg == '--budget' or arg == '-b':
            # expect a single number representing the budget available
            arg = arg_list.pop()
            budget = arg
            # clear the arg before continuing
            arg = None
        elif arg == '--no_clipboard' or arg == '-n':
            # no other things expected
            # if this is passed, don't copy to the clipboard
            use_clipboard = False
        elif arg == '--help' or arg == '-h' or arg == 'help' or arg == '?':
            print(_process_args.__doc__)
        else:
            # If it gets here, it's an unrecognized arguement.
            # print it and quit
            # TODO: Definite my own exception to say this.
            raise ValueError('Argument or option not found: {}\npassed argv={}'.format(arg, sys.argv))
            
    debug_print('done popping')

    # run the appropriate function with the passed options
    objectives(input_list=objectives_ranks,
               retirement_age=retirement_age,
               min_rating=minimum_rank,
               budget=budget,
               copy_output_to_clipboard=use_clipboard,
               )
    
if __name__ == '__main__':
    # Process the args through here
    
    debug_print('passed args={}'.format(sys.argv[0:]))

    _process_args()
    
