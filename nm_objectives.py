from tkinter import Tk
from operator import itemgetter

def objectives(input_str=None,
               input_str_sep=' ',
               input_list=None,
               retirement_age=None,
               r=None,
               min_rating_to_show=4,
               m=None,
               budget=None,
               b=None,
               copy_output_to_clipboard=True,
               *args,
               ):
    """ Given number values, spit out the objectives in order.

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
        min_rating_to_show=4, (short name: m=None)
            This will not print anything below (or should it be at or below?)
            min_rating. a value passed to the short name overrides the
            long name.
        budget=None, (short name: b=None)
            This will do the "Allocate ___ per month toward attaining these objectives." statement
            b overrides budget, if both are passed.
        copy_output_to_clipboard=True
            replace the clipboard contents with this output
        *args
            Any strings passed will be added as objectives.
    """
    # DONE: Command Line Args
    # DONE: params.
    # 2018-02-21 Doesn't really work at all.
    # 2018-02-22 Sorting isn't working at all, I must be doing something wrong
    # 2018-02-22 Sorting is working!
    # 2018-02-22 put it on the clipboard automatically
    # 2018-02-22 I think entry should be a space separated string instead.
    # 2018-03-08 TODO: Custom texts
    #            TODO: Separate objectives list data into an external file
    # 2018-03-09 TODO: Rich formatting for the clipboard
    # 2018-03-23 TODO: Round the budget number to a whole dollar amount
    #                  (the input supported math, so $500/12mo should be int
    #            TODO: Make the output format better when pasting into word.
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
        objectives[1] = "Funding a comfortable retirement by age {}.".format(retirement_age)
    # minimum rating
    if m:
        min_rating_to_show = m

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
            order.append((int(input_list[r]), obj))
    order = sorted(order, key=itemgetter(0), reverse=True)

    # Add the budget line as the last item if a budget is given.
    # This line doesn't actually get sorted, and shouldn't be
    # left off no matter the rating, so giving the a rating of 999.
    if b:
        budget = b
    if budget:
        order.append((999, "Allocate ${} per month toward attaining these objectives.".format(budget)))

    # copy the output to the clipboard, if the option is enabled
    if copy_output_to_clipboard:
        rtk = Tk()
        rtk.withdraw()
        rtk.clipboard_clear()

    # print the results for easy copy/paste
    # I think this is just visual clutter
##    print('\nVVV Printing in order VVV\n')
    last_element = len(order)
    c = 1
    for rating, obj in order:
        if rating >= min_rating_to_show:
            print(obj)
            if copy_output_to_clipboard:
                rtk.clipboard_append(obj)
            if c < last_element:
                #debug_print('c={} last_element={}'.format(c, last_element))
                rtk.clipboard_append('\n')
                c += 1

    # I think this is just visual clutter       
##    print('\n^^^ Printed in order ^^^\n')

    if copy_output_to_clipboard:
##        debug_print('**Printing clipboard contents:\n\n{}'.format(rtk.selection_get(selection="CLIPBOARD")))
        rtk.update() # now it stays on the clipboard after the window is closed
        rtk.destroy()
        print('\nOutput copied to clipboard.')

    # Return the ordered list of tuples, showing rating and text.
    return order

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

    # Process the arguements, if there are any
    if len(sys.argv) > 1:
        _process_args()
