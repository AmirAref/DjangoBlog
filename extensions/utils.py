from . import jalali

def jalali_convertor(gre_date):
    # convert month number to word
    month_words = ('فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند',)
    #  convert the gregorian date to jalali date
    jl_date = jalali.Gregorian(gre_date.year, gre_date.month, gre_date.day).persian_tuple()
    output = "{} {} {}، ساعت {}:{}".format(
        jl_date[2],
        month_words[jl_date[1] - 1], # index of month word
        jl_date[0],
        gre_date.hour,
        gre_date.minute,
    )
    
    return output