"""
H1B Salary Data
__version__ 0.1
"""
import datetime
import requests
import re


def default_year():
    """
    Set the default year to the previous year,
    because data for the current year is most probably unavailable.
    """
    return datetime.datetime.now().year - 1


class h1b:
    """

    """
    def __init__(self, company, year=None):
        self.company = company.lower()
        self.year = default_year() if year is None else year
        self.url = f"https://h1bdata.info/index.php?em={self.company}" +\
                   f"&year={self.year}"

    def raw_html(self):
        """This is return a string of the entire raw html data"""
        return requests.get("{}".format(self.url)).text

    def search_title(self, title):
        search = re.compile(title.upper())
        matches = search.finditer(self.raw_html())
        for match in matches:
            print(match)


if __name__ == "__main__":
    test = h1b("Google")
    test.search_title("software engineer")
