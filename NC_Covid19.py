import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

def getCountyData(county):
    print(county)
    url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
    col_list = ["date","county","state","cases","deaths"]
    df = pd.read_csv(url,sep=",",usecols=col_list, index_col=False)

    data = df[(df["county"] == str(county)) & (df["state"] == "North Carolina")]
    data = data.reset_index()
    data = data.drop(['index'],axis=1)
    x_value_date = ["2020-10-28", "2020-10-29", "2020-10-30"," 2020-10-31",
                    "2020-11-01", "2020-11-02", "2020-11-03", "2020-11-04",
                    "2020-11-05", "2020-11-06"]

    #data.reset_index(drop=True, inplace=True)
    x = [0,1,2,3,4,5,6,7,8,9]
    #x_value = [data["date"].tail(10)]
    y_value = data["cases"].tail(10)
    total_deaths_to_date = data["deaths"].tail(10)
    total_cases_to_date = data[["date","cases"]].tail(10)

    # Create 2x2 sub plots
    gs = gridspec.GridSpec(2, 2)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0]) # row 0, col 0
    ax1.bar(x, y_value, color='navy', edgecolor='white', width=.9)
    ax1.set_xticks(x)
    ax1.set_xlabel("Date")
    ax1.set_xticklabels(x_value_date,rotation=45,fontsize=10)
    ax1.set_ylabel("# number of cases")

    ax2 = fig.add_subplot(gs[0, 1]) # row 0, col 1
    ax2.bar(x, total_deaths_to_date, color='dodgerblue', edgecolor='white', width=.9)
    ax2.set_xticks(x)
    ax2.set_xlabel("Date")
    ax2.set_xticklabels(x_value_date,rotation=45,fontsize=10)
    ax2.set_ylabel("# of accumulated deaths")

    ax3 = fig.add_subplot(gs[1, :]) # row 1, span all columns
    ax3.plot(x, y_value, label = "# of cases")
    ax3.plot(x, total_deaths_to_date, label = "# of deaths")
    ax3.set_xticks(x)
    ax3.set_xlabel("Date")
    ax3.set_xticklabels(x_value_date,rotation=45,fontsize=10)
    ax3.set_ylabel("# of Cases to Deaths")

    fig.tight_layout()
    fig.savefig('covid19.pdf')
    plt.show()

def selectFromMountainRegionCounties():
    file = open("MountainRegion/MountainRegions.txt")

    mountainCounties = ["Alleghany","Watauga","Wilkes","Avery","Caldwell",
                        "Mitchell","Burke","Yancey","McDowell","Madison","Buncombe",
                        "Rutherford","Polk","Haywood","Henderson","Transylvania",
                        "Jackson","Swain","Macon","Graham","Clay","Cherokee"]

    lineNumber = 1
    for i in mountainCounties:
        print(str(lineNumber) + ". " + i)
        lineNumber += 1

    # Prompt user to select a county
    countySelection = raw_input("Please select a county: ")
    getCountyData(str(countySelection))

def selectFromPiedmontRegionCounties():
    file = open("PiedmontRegion/PiedmontRegions.txt")

    piedmontCounties = ["Franklin","Yadkin","Forsyth","Guildford","Alamance",
                        "Orange","Durham","Wake","Alexander","Catawba","Iredell",
                        "Davie","Rowan","Davidson","Randolph","Chatham","Lincoln",
                        "Cleveland","Gaston","Mecklenburg","Cabarrus","Union","Stanly",
                        "Montgomery","Anson",
                        "Richmond","Moore","Lee"]


    lineNumber = 1
    for i in piedmontCounties:
        print(str(lineNumber) + ". " + i)
        lineNumber += 1

    # Prompt user to select a county
    countySelection = raw_input ("Please select a county: ")
    str(countySelection)
    getCountyData(countySelection)

try:
    print ("1. Mountains")
    print ("2. Piedmont")
    print ("3. Costal Plains")
    regionSelection = raw_input("Please select a region: ")
    userSelection = int(regionSelection)

    if userSelection == 1:
        # Call method to list counties in that region
        selectFromMountainRegionCounties()
    elif userSelection == 2:
        # Call method to list counties in that region
        selectFromPiedmontRegionCounties()
    #elif regionSelection == 3:
        # Call method to list counties in that region
        
    #else:
        # Display incorrect option selected
        # Exit the program
        #print("Incorrect option selected.")
        #sys.exit(1)

except ValueError:
    if not regionSelection:
        raise ValueError("You did not provide a region")
    else:
        raise ValueError("You did not enter an integer")
