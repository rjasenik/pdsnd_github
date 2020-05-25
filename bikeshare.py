import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello My Friend! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city which you want to explore from the list (chicago, new york city, washington):").lower()
    if city in CITY_DATA:
        print("Your choosen city is: " + city)
    else:
        while city not in CITY_DATA:
            print("There is no city with this name in the list, presss ENTER and try again!")
            city = input("Enter the city which you want to explore from the list (chicago, new york city, washington):").lower()
            print("Your choosen city is: " + city)       
      
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month=input("Enter your month from the list (all, january, february, ... , june):").lower()
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
     
    while month not in months:
            print("There is no month with this name in the list, presss ENTER and try again!")
            month=input("Enter your month from the list (all, january, february, ... , june):").lower()
                         
       
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day=input("Enter your day of week from the list (all, monday, tuesday, ... sunday):").lower()
    days=['all', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']
    while day not in days:
            print("There is no day with this name in the list, presss ENTER and try again!")
            day=input("Enter your day of week from the list (all, monday, tuesday, ... sunday):").lower()
    
                                
    print('Your selection is: City - {}, Month - {}, Day - {}'.format( city, month, day))                   
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
       months = ['all','january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month)
       df = df[df['month'] == month]
        
    if day != 'all':
       df = df[df['day'] == day.title()]
               
    
    
    return df

    print(load_data)    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('The most common month - {}'.format( most_common_month))
    

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week -  {}'.format(most_common_day_of_week))
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour - {}'.format(most_common_hour))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station  - {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station  - {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combination = df['combination'].mode()[0]
    print('The most frequent combination - {}'.format(most_common_combination))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time  - {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time  - {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender info in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth Year'].min()
        print('The earliest birth year  - {}'.format(earliest))
        most_recent = df['Birth Year'].max()
        print('The most recent birth year  - {}'.format(most_recent))
        most_common_birth = df['Birth Year'].mode()[0]
        print('The most common birth year  - {}'.format(most_common_birth))
    else:
        print("There is no birth year info in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    selection = input('Would you like to read some of the raw data? Yes/No: ').lower()
    selections = ['yes','no']
    while selection not in selections:
        print("It is not valid input, presss ENTER and try again!")
        selection = input('Would you like to read some of the raw data? Yes/No: ').lower()
    
    while True:
        if selection.lower() == 'yes':
            print(df.head())
            break
        else:
            break               
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
