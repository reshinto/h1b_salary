"""
H1B Salary Data
__version__ 0.1
"""
import datetime
import requests
import re
import statistics as stat


class H1b_database:
    """H1B salary database"""

    def __init__(self, company, job_title, year=None):
        # ensures company name is all in lowercase and capitalized for display
        self.company = company.lower().capitalize()
        # ensures each word is capitalized for display
        self.title = job_title.title()
        # used for url searches only
        self._title = "+".join(self.title.split()).lower()
        self.year = self.default_year() if year is None else year
        # lower() is used to ensure company name is in lowercase during search
        self.url = rf"https://h1bdata.info/index.php?em=" +\
                   rf"{self.company.lower()}&job={self._title}&city=" +\
                   rf"&year={self.year}"
        # calculate one time and store value for easy reference
        self.salaries = self.get_salaries()

    @staticmethod
    def default_year():
        """
        This will set the default year to the previous year,
        because data for the current year is most probably unavailable
        """
        return datetime.datetime.now().year - 1

    def raw_html(self):
        """This will return a string of the entire raw html data"""
        return requests.get(f"{self.url}").text

    def get_salaries(self):
        salary_list = []
        # used for regex when searching
        tempTitle = r"\+".join(self.title.split()).upper()
        search = re.compile(rf'{tempTitle}'
                            r'[ 0-9.<a-z=~"->&;A-Z]+\$?[0-9]+,[0-9]+')
        matches = search.finditer(self.raw_html())  # get search results
        if matches is not None:
            for match in matches:
                string = match.group(0)  # extract string from search result
                index = string.find("$")  # find salary that starts with $ sign
                if index == -1:
                    # find salary when $ is unavailable
                    index = string.find("<td>") + 3
                # extract salary and remove the , sign
                salary = int(string[index+1:].replace(",", ""))
                salary_list.append(salary)
            salary_list.sort()
        else:
            print("No salary data available!")
        return salary_list

    def min_salary(self):
        """Find the lowest salary"""
        return min(self.salaries)

    def max_salary(self):
        """Find the highest salary"""
        return max(self.salaries)

    def avg_salary(self):
        """Find average salary"""
        return round(stat.mean(self.salaries))

    def median_salary(self):
        """Find the median salary"""
        return round(stat.median(self.salaries))

    def salary_stdev(self):
        """Find the salary standard deviation"""
        return round(stat.stdev(self.salaries))

    def salary_mode(self):
        """Find the most common given salary"""
        try:
            return stat.mode(self.salaries)
        except stat.StatisticsError:
            return "unavailable because multiple modes exists"
