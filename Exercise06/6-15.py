'''
@Date: 2019-11-11 21:05:41
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-11 21:51:28
'''
import sys


def computeTax(status, taxableIncome):
    income = taxableIncome
    if status == 0:  # Compute tax for single filers
        if income <= 8350:
            tax = income * 0.10
        elif income <= 33950:
            tax = 8350 * 0.10 + (income - 8350) * 0.15
        elif income <= 82250:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
        elif income <= 171550:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (
                82250 - 33950) * 0.25 + (income - 82250) * 0.28
        elif income <= 372950:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (
                82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (
                    income - 171550) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
              (372950 - 171550) * 0.33 + (income - 372950) * 0.35

    elif status == 1:  # Compute tax for married file jointly
        if income <= 16700:
            tax = income * 0.10
        elif income <= 67900:
            tax = 16700 * 0.10 + (income - 16700) * 0.15
        elif income <= 137050:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (income -
                                                           67900) * 0.25
        elif income <= 208850:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (
                137050 - 67900) * 0.25 + (income - 137050) * 0.28
        elif income <= 372950:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (
                137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + (
                    income - 208850) * 0.33
        else:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (
                137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + (
                    372951 - 208850) * 0.33 + (income - 372950) * 0.35
    elif status == 2:  # Compute tax for married separately
        if income <= 8350:
            tax = income * 0.10
        elif income <= 33950:
            tax = 8350 * 0.10 + (income - 8350) * 0.15
        elif income <= 68525:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
        elif income <= 104425:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (
                68525 - 33950) * 0.25 + (income - 68525) * 0.28
        elif income <= 186475:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (
                68525 - 33950) * 0.25 + (104425 - 82250) * 0.28 + (
                    income - 186475) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (
                68525 - 33950) * 0.25 + (104425 - 82250) * 0.28 + (
                    186475 - 186475) * 0.33 + (income - 186475) * 0.35
    elif status == 3:  # Compute tax for head of household
        if income <= 11950:
            tax = income * 0.10
        elif income <= 45500:
            tax = 11950 * 0.10 + (income - 11950) * 0.15
        elif income <= 117450:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (income -
                                                           45500) * 0.25
        elif income <= 190200:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (
                117450 - 45500) * 0.25 + (income - 117450) * 0.28
        elif income <= 372950:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (
                117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + (
                    income - 190201) * 0.33
        else:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (
                117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + (
                    372950 - 190201) * 0.33 + (income - 372950) * 0.35

    else:
        print("Error: invalid status")
        sys.exit()

    return tax


def main():
    print(
        "----------------------------------------------------------------------\
------------------------------------------------------------------")
    print("  Taxable Income    |          Single            |        Married \
Joint    |         Married Separate  |        Head of a House")
    print(
        "----------------------------------------------------------------------\
------------------------------------------------------------------")
    for income in range(50000, 60050, 50):
        print(
            format(income, "10d"),
            "        |  ",
            format(computeTax(0, income), "15.1f"),
            "          |",
            format(computeTax(1, income), "15.1f"),
            "        |  ",
            format(computeTax(2, income), "15.1f"),
            "        |  ",
            format(computeTax(3, income), "15.1f"),
        )
        print(
            "----------------------------------------------------------------------\
-------------------------------------------------------------------")


main()
