# This function takes a list of columns from a pandas dataframe and converts them to datetime format
# filling missing values with 01-01-1970. You may choose whatever you want
def fixDate(df, list_dates=[]):

    list_date_default = ['my_date_column(s)'] # default list of columns

    list_date_to_fix = []

    if not list_dates:
        for col in df.columns:
            if col in list_date_default:
                list_date_to_fix.append(col)
        for date in list_date_to_fix:
            try:
                df[date].fillna('01JAN1970', inplace=True)
                df[date] = df[date].apply(lambda x: pd.to_datetime(x, format='%d%b%Y'))
            except:
                try:
                    df[date].replace('01JAN1970', '19700101', inplace=True)
                    df[date] = df[date].apply(lambda x: pd.to_datetime(x, format='%Y%m%d'))
                except:
                    df[date].replace('19700101', '1970-01-01', inplace=True)
                    df[date] = df[date].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d'))

    else:
        print 'list not empty'
        for date in list_dates:
            try:
                df[date].fillna('01JAN1970', inplace=True)
                df[date] = df[date].apply(lambda x: pd.to_datetime(x, format='%d%b%Y'))
            except:
                try:
                    df[date].replace('01JAN1970', '19700101', inplace=True)
                    df[date] = df[date].apply(lambda x: pd.to_datetime(x, format='%Y%m%d'))
                except:
                    df[date].replace('19700101', '1970-01-01', inplace=True)
                    df[date] = df[date].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
    return df
