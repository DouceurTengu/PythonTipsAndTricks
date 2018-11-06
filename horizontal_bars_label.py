'''
A small trivial project: Before the now famous Tableau and other tools such as Bokeh, sometimes you just 
wanted to have your negative numbers written in specific places on your bars to have a good looking graph.
'''

def horizontalBarLabels(ax,Type,name,listBars='',color1='white',color2='.3'):

    """
    For horizontal bar charts, this function automically writes the value on the end of the bar.

    :param ax: pointer to the axes on which to operate.
    :param Type: indicates the type of value to be written out.  Values for Type are either $ or %. If you
                 specify $, the output will be comma separated currency, e.g., $4,567  If you specify %,
                 values will be percentages with no decimals, e.g., 45%.  Percentages are automatically
                 multiplied by 100.
    :param name: not sure what this does
    :param listBars: again, not sure what this does
    :param color1: a hex color string for values written outside the bar
    :param color2: a hex color string for values that are written inside the bar
    :return: None
    """
    labels=ax.get_xticks()
    Max=labels.max()
    Min=labels.min()
    ix=0
    for p in ax.patches:
        l=p.get_x()+p.get_width()
        if not listBars:
            if p.get_x()<0:
                if (Type== '$') | (Type=='') :
                    val = Type + str(format(p.get_x(), ',.0f') )
                elif Type== '%':
                    val= str(format(p.get_x()*100, ',.0f')) + Type

            else:
                if (Type== '$') | (Type=='') :
                    val= Type  + str(format(l,',.0f'))
                elif Type == '%':
                    val= str(format(l*100,',.0f')) + Type
        else:
            #val= str(format(listBars[ix], ',.0f')+ name )
            val= listBars[ix]+ name
            ix+=1
        if p.get_x()==0: #bar goes to the right
            if l>Max*0.8: # write on the bar
                    ax.text(s=val,
                             x=l-Max/50,
                             y=p.get_y()+p.get_height()/2.,
                             va='center',
                             ha='right',
                             fontsize=9,
                             color=color1,
                             rotation=0)
            else: # write to the right of the bar
                    ax.text(s=val,
                             x=l+Max/50,
                             y=p.get_y()+p.get_height()/2.,
                             va   ='center',
                             ha='left',
                             fontsize=9,
                             color=color2,
                             rotation=0)
        elif p.get_x()<Min*0.8:
                ax.text(s=val,
                         x=p.get_x()-Min/50,
                         y=p.get_y()+p.get_height()/2.,
                         va='center',
                         ha='left',
                         fontsize=9,
                         color=color1,
                         rotation=0)
        else:
                ax.text(s=val,
                         x=p.get_x()-Max/50,
                         y=p.get_y()+p.get_height()/2.,
                         va='center',
                         ha='right',
                         fontsize=9,
                         color=color2,
                         rotation=0)
