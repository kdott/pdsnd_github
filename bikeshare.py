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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for any of these three cities in the United States (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
  
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n')
    if city.lower() in CITY_DATA:
            #obtains city name to analyze data.
            city = CITY_DATA[city.lower()]
    else:
            # prints when unable to get city name.
            print("Sorry we were not able to get the name of the city to analyze data, Please input either chicago, new york city or washington.\n")

    # obtains data specific for an entered month within the dictionary for; all months, january to june
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all month': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month to view its data, begining from January to June")
        print("\nAccepted input:\nFull month name; not case sensitive (e.g. january or JANUARY).\nFull month name in title case (e.g. April).")
        print("\n(You may also opt to view data for all months, please type 'all month' or 'All' or 'ALL' for that.)")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid input. Please try again.")
            print("\nRestarting")

    print(f"\nYou have chosen {month.title()} as your month.")


    # gets user input for day of week (all, monday, tuesday, ... sunday)
    DAILY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAILY_DATA:
        print("\nPlease enter the day to view its data, starting from monday to sunday")
        print("\n(You can enter all day to view the data of the entire week)")
        day = input().lower()
     
    #loops when unable to get a valid day entry
        if day not in DAILY_DATA:
            print("\nInvalid entry. Please enter a valid day.")
            print("\nRestarting...")
            
    print(f"\nYou have chosen {day.title()} as your day.")
    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
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
    #Loads city specific data
    print("\nLoading...")
    df = pd.read_csv(city)

    #Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Uses mode() to find the most popular month
    popular_month = df['month'].mode()[0]

    print(f"Most Popular Month (1 = January,...,6 = June): {popular_month}")

    #Uses mode() to find the most popular day
    popular_day = df['day_of_week'].mode()[0]

    print(f"\nMost Popular Day: {popular_day}")

    #Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    #Uses mode() to find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print(f"\nMost Popular Start Hour: {popular_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Uses mode() to find the most common start station
    common_start_station = df['Start Station'].mode()[0]

    print(f"The most commonly used start station: {common_start_station}")

    #Uses mode() to find the most common end station
    common_end_station = df['End Station'].mode()[0]

    print(f"\nThe most commonly used end station: {common_end_station}")

    #merges two colums in the df
    #Assigns the result to a new column 'Start To End'
    #mode() is used to determine the most common combination
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print(f"\nThe most frequent combination of trips are from {combo}.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displays total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # displays mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displays counts of user types
    count_of_user_types = df['User Type'].value_counts()
    print("The number of user type is: \n" + str(count_of_user_types))


    #Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")


    #Displays earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        rdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
