# This is a file for PoF equations, helful for the financial markets & corporate finance equations

# Importing the necessary libraries
import numpy as np
import math
from typing import List

# Functions for financial markets

def discount_factor(r, t):
    """
    Function to calculate the discount factor
    :param r: Interest rate
    :param t: Time
    :return: Discount factor
    """
    return 1 / (1 + r) ** t

def future_value(PV, r, t):
    """
    Function to calculate the future value
    :param PV: Present value
    :param r: Interest rate
    :param t: Time
    :return: Future value
    """
    return PV * (1 + r) ** t

def present_value(FV, r, t):
    """
    Function to calculate the present value
    :param FV: Future value
    :param r: Interest rate
    :param t: Time
    :return: Present value
    """
    return FV / (1 + r) ** t

def PV_of_cashflow_stream(cashflows, r, N):
    """
    Function to calculate the present value of a cash flow stream
    :param cashflows: Cash flows
    :param r: Interest rate
    :param n: Number of cash flows
    :return: Present value of cash flow stream
    """
    return sum([cashflows / pow(1 + r, n) for n in range(N+1)])

def pv_perpetuity(C, r):
    """
    Function to calculate the present value of a perpetuity
    :param C: Cash flow
    :param r: Interest rate
    :return: Present value of perpetuity
    """
    return C / r

def pv_annuity(C, r, N):
    """
    Function to calculate the present value of an annuity
    :param C: Cash flow
    :param r: Interest rate
    :param N: Number of cash flows
    :return: Present value of annuity
    """
    return C * (1 - (1 / (1 + r) ** N)) / r


def fv_annuity(pv, r, N):
    """
    Function to calculate the future value of an annuity
    :param C: Cash flow
    :param r: Interest rate
    :param N: Number of cash flows
    :return: Future value of annuity
    """
    return pv * ((1 + r) ** N - 1) / r

def pv_perpetuity_growth(C, r, g):
    """
    Function to calculate the present value of a perpetuity with growth
    :param C: Cash flow
    :param r: Interest rate
    :param g: Growth rate
    :return: Present value of perpetuity with growth
    """
    return C / (r - g)

def pv_growing_annuity(C, r, g, N):
    """
    Function to calculate the present value of a growing annuity
    :param C: Cash flow
    :param r: Interest rate
    :param g: Growth rate
    :param N: Number of cash flows
    :return: Present value of growing annuity
    """
    return C / (r - g) * (1 - (1 + g) ** N / (1 + r) ** N)

def eq_discount_period_conversion(r, n):
    """
    Function to convert discount period
    :param r: Interest rate
    :param n: Number of periods
    :return: Discount period conversion
    """
    return (1 + r) ** n - 1

def interest_rate_per_compounding_period(APR, k_periods_per_year):
    """
    Function to calculate the interest rate per compounding period
    :param APR: Annual percentage rate
    :param k_periods_per_year: Number of periods per year
    :return: Interest rate per compounding period
    """
    return APR / k_periods_per_year

def APR_to_EAR(APR, k):
    """
    Function to convert APR to EAR
    :param APR: Annual percentage rate
    :param k: no_of_compounding_periods_per_year
    :return: Effective annual rate
    """
    return (1 + APR / k) ** k - 1

def growth_in_purch_power(inflation_rate, real_rate):
    """
    Function to calculate the growth in purchasing power
    :param inflation_rate: Inflation rate
    :param real_rate: Real rate
    :return: Growth in purchasing power
    """
    return (1 + real_rate) / (1 + inflation_rate) - 1

def real_interest_rate(real_rate, inflation_rate):
    """
    Function to calculate the real interest rate
    :param real_rate: Real rate
    :param inflation_rate: Inflation rate
    :return: Real interest rate
    """
    return (real_rate - inflation_rate) / (1 + inflation_rate)

### Bond Functions

def coupon_payment_CPN(face_value, coupon_rate, N):
    """
    Function to calculate the coupon payment
    :param face_value: Face value of bond
    :param coupon_rate: Coupon rate
    :param N: Number of periods
    :return: Coupon payment
    """
    return (face_value * coupon_rate) / N

def price_zero_coupon_bond(FV, YTM, N):
    """
    Function to calculate the price of a zero coupon bond
    :param FV: Face value
    :param YTM: Yield to maturity
    :param N: Number of periods
    :return: Price of zero coupon bond
    """
    return FV / (1 + YTM) ** N

def YTM_of_n_year_zer_coupon_bond(FV, P, N):
    """
    Function to calculate the yield to maturity of a n-year zero coupon bond
    :param FV: Face value
    :param P: Price
    :param N: Number of periods
    :return: Yield to maturity
    """
    return (FV / P) ** (1 / N) - 1

def YTM_of_coupon_bond(CPN, FV, YTM, N):
    """
    Function to calculate the yield to maturity of a coupon bond
    :param CPN: Coupon payment
    :param FV: Face value
    :param YTM: Yield to maturity
    :param N: Number of periods
    :return: Yield to maturity of coupon bond
    """
    return CPN * (1 / YTM) * (1 - 1 / (1 + YTM) ** N) + FV / (1 + YTM) ** N

def price_of_stock_one_year_investor(div_1, P_1, r_e):
    """
    Function to calculate the price of a stock for a one-year investor
    :param div_1: Dividend paid in year 1
    :param P_1: Price in year 1
    :param r_e: equity cost of caputal
    :return: Price of stock for one-year investor (market price)
    """
    return (div_1 + P_1) / (1 + r_e)

def total_return(div_1, P_0, P_1):
    """
    Function to calculate the total return
    :param div_1: Dividend paid in year 1
    :param P_0: Price in year 0
    :param P_1: Price in year 1
    :return: Total return
    """
    return (div_1 / P_0) + (P_1 - P_0) / P_0

def price_multi_year_investor(div_1, div_2, P_2, r_e):
    """
    Function to calculate the price of a stock for a multi-year investor
    :param div_1: Dividend paid in year 1
    :param div_2: Dividend paid in year 2
    :param P_2: Price in year 2
    :param r_e: equity cost of caputal
    :return: Price of stock for multi-year investor
    """
    return (div_1) / (1 + r_e) + (div_2 + P_2) / (1 + r_e) ** 2

def dividend_discount_model():
    # Get number of periods from user
    while True:
        try:
            N = int(input("Enter the number of periods (years): "))
            if N <= 0:
                print("Please enter a positive number of periods.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get required return rate
    while True:
        try:
            r_e = float(input("Enter the required return rate (as decimal, e.g., 0.10 for 10%): "))
            if r_e <= 0:
                print("Required return rate must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get dividends for each period
    dividends = []
    for year in range(1, N + 1):
        while True:
            try:
                div = float(input(f"Enter expected dividend for year {year}: "))
                if div < 0:
                    print("Dividend cannot be negative.")
                    continue
                dividends.append(div)
                break
            except ValueError:
                print("Please enter a valid number.")
    
    # Calculate present value using DDM
    present_value = sum(div / (1 + r_e)**year 
                       for year, div in enumerate(dividends, 1))
    
    # Display results
    print("\nCalculation Results:")
    print("-" * 30)
    print(f"Number of periods: {N}")
    print(f"Required return rate: {r_e:.2%}")
    for year, div in enumerate(dividends, 1):
        print(f"Year {year} dividend: ${div:,.2f}")
    print("-" * 30)
    print(f"Stock value: ${present_value:,.2f}")
    
    return present_value


def constant_dividend_growth_model(div_1, r_e, g):
    """
    Function to calculate the price of a stock using the constant dividend growth model
    :param div_1: Dividend paid in year 1
    :param r_e: equity cost of caputal
    :param g: Growth rate
    :return: Price of stock using constant dividend growth model, P_0
    """
    return div_1 / (r_e - g)

def dividend_per_share_ratio(E, shares_outstanding, dividend_payment_rate):
    """
    Function to calculate the dividend per share ratio
    :param E: Earnings
    :param shares_outstanding: Number of shares outstanding
    :param dividend_payment_rate: Dividend payment rate
    :return: Dividend per share ratio
    """
    return E * dividend_payment_rate / shares_outstanding


def ddm_with_constant_long_term_growth():
    # Get model parameters
    while True:
        try:
            N = int(input("Enter the number of initial periods N: "))
            if N <= 0:
                print("Please enter a positive number of periods.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            r_e = float(input("Enter the required return rate r_e (as decimal, e.g., 0.10 for 10%): "))
            if r_e <= 0:
                print("Required return rate must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            g = float(input("Enter the long-term growth rate g (as decimal, e.g., 0.03 for 3%): "))
            if g >= r_e:
                print("Growth rate must be less than required return rate.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get each dividend payment
    dividends = []
    for year in range(1, N + 1):
        while True:
            try:
                div = float(input(f"Enter expected dividend for year {year}: "))
                if div < 0:
                    print("Dividend cannot be negative.")
                    continue
                dividends.append(div)
                break
            except ValueError:
                print("Please enter a valid number.")
    
    # Calculate terminal dividend (div_{N+1})
    div_terminal = dividends[-1] * (1 + g)
    
    # Calculate present value of explicit forecast dividends
    pv_dividends = sum(div / (1 + r_e)**t for t, div in enumerate(dividends, 1))
    
    # Calculate terminal value and discount it
    terminal_value = (div_terminal / (r_e - g))  # Gordon Growth Model
    pv_terminal = terminal_value / (1 + r_e)**N
    
    # Calculate total value
    total_value = pv_dividends + pv_terminal


# firm valuation equations

def enterprise_value(equity, debt, cash):
    """
    Function to calculate the enterprise value
    :param equity: Equity
    :param debt: Debt
    :param cash: Cash
    :return: Enterprise value
    """
    return equity + debt - cash

def free_cashflow(EBIT, t_c, depreciation, capital_expenditure, increase_in_net_working_capital):
    """
    Function to calculate the free cash flow
    :param EBIT: Earnings before interest and taxes
    :param t_c: Tax rate
    :param depreciation: Depreciation
    :param capital_expenditure: Capital expenditure
    :param increase_in_net_working_capital: Increase in net working capital
    :return: Free cash flow
    """
    return EBIT * (1 - t_c) + depreciation - capital_expenditure - increase_in_net_working_capital

def net_investment(capital_expenditure, depreciation):
    """
    Function to calculate the net investment
    :param capital_expenditure: Capital expenditure
    :param depreciation: Depreciation
    :return: Net investment
    """
    return capital_expenditure - depreciation

# options pricing

def call_option(S, K):
    """
    Function to calculate the call option
    :param S: Stock price
    :param K: Strike price
    :return: Call option
    """
    return max(S - K, 0)

def put_option(S, K):
    """
    Function to calculate the put option
    :param S: Stock price
    :param K: Strike price
    :return: Put option
    """
    return max(K - S, 0)

def PB():
    """Function to calculate the Payback Period of a project"""
    while True:
        try:
            years_before_cost_recovery = float(input("Enter the years_before_cost_recovery: "))
            remaining_cost_to_recover = float(input("Enter the remaining_cost_to_recover: "))
            cash_flow_during_the_year = float(input("Enter the cash_flow_during_the_year: "))
            return years_before_cost_recovery + remaining_cost_to_recover / cash_flow_during_the_year    
        except ValueError:
            print("Please enter valid numbers.")


def main():
    print(PB())

main()