import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAY_OF_WEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('\n')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("Select a city to review - Choices include: chicago, new york city, or washington: ").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("That's not a valid choice.  Please enter a valid city.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("What month would you like to review - Choices include: all, january, february, march, april, may, june: ").lower()
      if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        print("That's not a valid choice.  Please enter a valid month.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("What day's info would you like to review - Choices include: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday: ").lower()
      if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print("That's not a valid choice.  Please enter a valid day.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file for city selected
    df = pd.read_csv(CITY_DATA[city])

    # conversion of start time in csf to datetime
    df ['Start Time'] = pd.to_datetime(df['Start Time'])

    # pull out month and day of the week from start time
    df ['month'] = df['Start Time'].dt.month
    df ['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if needed
    if month != 'all':
         month = month.index(month) + 1

         # filter by month to get new dataframe
         df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to get new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Starting_Station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is:', Starting_Station)

    # TO DO: display most commonly used end station
    Ending_Station = df['End Station'].value_counts().idxmax()
    print('\nThe most commonly used end station is:', Ending_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_of_Stations = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most commonly used combination of starting station and ending station trip is:', Starting_Station, " & ", Ending_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('The total travel time is:', Total_Travel_Time/(60*60*24), " days")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The average travel time is:', Mean_Travel_Time/60, " minutes")
    
    # TO DO: display shortest travel time
    Short_Travel_Time = df['Trip Duration'].min()
    print('The shortest travel time is:', Short_Travel_Time, " seconds")
    
    # TO DO: display longest travel time
    Long_Travel_Time = df['Trip Duration'].max()
    print('The longest travel time is:', Long_Travel_Time/60, " minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('All user types include:\n', user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender types include:\n', gender_types)
    except KeyError:
      print("\nGender types include:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nThe earliest birth year is:', Earliest_Year)
    except KeyError:
      print("\nThe earliest birth year is:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nThe most recent birth year is:', Most_Recent_Year)
    except KeyError:
      print("\nThe most recent birth year is:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nThe most common birth year is:', Most_Common_Year)
    except KeyError:
      print("\nThe most recent birth year is:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    '''Function displays 5 lines of data if user says yes to viewing data.
    After displaying 5 lines, asks user if they want 5 more and continues until they answer no.'''
    
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nDo you want to see 5 rows of trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("That is not a valid input. Please type 'yes' or 'no'.")
    if display.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nDo you want to see 5 more rows of trip data?'
                                     'Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("That is not a valid input. Please type 'yes' or 'no'.")
            if display_more.lower() == 'yes':
                 head += 5
                 tail += 5
                 print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()