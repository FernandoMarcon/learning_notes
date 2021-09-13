'''
Calculate all N price-drop percentages for placing Safety Orders (SOs).
The percentage levels are based on a constant value (e.g. SO=2%), combined with a stepping factor that scale up the levels at each iteration:

FORMULA => SO + SO-STEP * PREVIOUS_%_DROP (or, if its the first: SO)
Ex: For SO = 2% and SO-STEP=1.1%, this would give:

SO(1): 2%           (only SO)
SO(2): 4,2%         (+step)
SO(3): 6.62%        (+step)
SO(4): 9.282%       (+step)
SO(5): 12.2102%     (+step)
SO(6): 15.43122%    (+step)
SO(7): 18.974342%   (+step)

This would cover a drop of 18.97% in the coin price.
'''

def SO(max_so=7,start_so=1,last_so=0,so=.02, so_step=1.1):
    if start_so == 1:
        last_so = so
    else:
        last_so = so + last_so*so_step

    if start_so < max_so:
        start_so+=1
        return SO(max_so=max_so,start_so=start_so,last_so=last_so)
    else:
        return last_so

def getSOperc(max_so=7):
    return [SO(i) for i in range(1,max_so+1)]
