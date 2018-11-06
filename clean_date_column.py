def fast_to_datetime(date_field, datetime_format):
    """
    converts a date from string to date, using the provided datetime_format
    :param date_field: field with date as a string
    :param datetime_format: date format such as:
        - datetime_format_csv = '%Y-%m-%d'
        - datetime_format_claims = '%d%b%Y'
        - datetime_format_episodes = '%Y%m%d'
    :return:
    """
    dates = {date: pd.to_datetime(date, format=datetime_format) for date in date_field.unique()}
    return date_field.map(dates)

def clean_dates(df, date_nan, datetime_format, date_field_list):
    """
    This is a simple date cleaner to fill df dates with default NULL date, and fix date format
    :param df: dataframe to clean
    :param date_nan: Default string date to use where dates are NULL. Must be in the same format as datetime_format e.g
        - date_nan_csv = '1970-01-01'
        - date_nan_claims = '01JAN1970'
        - date_nan_episodes = '19700101'
    :param date_field_list: List of date fields to clean up
    :param datetime_format:  date format such as:
        - datetime_format_csv = '%Y-%m-%d'
        - datetime_format_claims = '%d%b%Y'
        - datetime_format_episodes = '%Y%m%d'
    :return: changed df input
    """
    for date_field in date_field_list:
        if date_field in df.columns:
            try:
                df[date_field].fillna(date_nan, inplace=True)
                df[date_field] = fast_to_datetime(df[date_field], datetime_format)
            except:
                df[date_field].replace(date_nan, '01JAN1970', inplace=True)
                df[date_field] = fast_to_datetime(df[date_field], '%d%b%Y')
        else:
            print "  - Skipping {}. Not in Data Frame".format(date_field)
            print df.dtypes
