from h1b import H1b_database


def addComma(integer):
    """
    Add a comma after every 3 integers from right to left
    """
    strList = list(str(integer))
    if len(strList) > 3:
        for i in range(len(strList)-3, -1, -3):
            strList.insert(i, ",")
    if strList[0] == ",":
        strList.pop(0)
    finalStr = "".join(strList)
    return finalStr


def menu():
    company = input("Company name: ")
    job_title = input("Job Title name: ")
    default_year = input("Set year as most recent [y/n]? ").lower()
    year = int(input("Year: ")) if default_year == "n" else None
    # year = None if default_year == "y" else int(input("Year: "))
    data = H1b_database(company, job_title, year)
    # let x be the average salary to test conditions
    x = data.salary_mode()
    avgSalary = "$" + addComma(x) if type(x) == int else data.salary_mode()
    print(f"\nThe annual salary for {data.title}s at {data.company}"
          f" in the year {data.year}:"
          f"\n - Min is ${addComma(data.min_salary())}, "
          f"Average is ${addComma(data.avg_salary())},"
          f" Max is ${addComma(data.max_salary())}")
    print(f" - Median salary is ${addComma(data.median_salary())}")
    print(" - The most common salary given is "
          f"{avgSalary}")
    print(f" - The standard deviation is {data.salary_stdev()}")
