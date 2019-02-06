# H1B SALARIES DATA VIEWER
This is a simple web scraping app that takes data from the https://h1bdata.info/index.php website.

The purpose of this app is to find the minimum, maximum, average, and most common annual salaries given by a company for a specific job title in the United States to Foreigners.

This maybe able to help you understand the current market rate and also help during your salary negotiations.


## Requirements
This works on all OS.
You only need to install Python 3.6 or above.
Libraries used in the app are built-in, therefore, no other installations are required.


## Installation guidelines for Mac OS X
If you have brew already installed, in terminal, key:
brew install python


### Installation guidelines for other OS
I won't include it here, please refer to python homepage for help.
https://www.python.org/

Then check the python version in the terminal:
python --version


## Run app
Key the following in the terminal to run app:
python run.py

## Usage example
* Company name: google
* Job Title name: software engineer
* Set year as most recent [y/n]? y

The annual salary for Software Engineers at Google in the year 2018:
 - Min is $86,540, Average is $141,742, Max is $331,000
 - Median salary is $138,000
 - The most common salary given is $120,000
 - The standard deviation is 23078
