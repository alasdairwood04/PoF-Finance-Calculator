import numpy as np
import math

def discount_factor():
    """Function to calculate the discount factor"""
    while True:
        try:
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            t = float(input("Enter time period: "))
            if r < 0:
                print("Interest rate cannot be negative.")
                continue
            return 1 / (1 + r) ** t
        except ValueError:
            print("Please enter valid numbers.")

def future_value():
    """Function to calculate the future value"""
    while True:
        try:
            PV = float(input("Enter present value: "))
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            t = float(input("Enter time period: "))
            if r < 0:
                print("Interest rate cannot be negative.")
                continue
            return PV * (1 + r) ** t
        except ValueError:
            print("Please enter valid numbers.")

def present_value():
    """Function to calculate the present value"""
    while True:
        try:
            FV = float(input("Enter future value: "))
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            t = float(input("Enter time period: "))
            if r < 0:
                print("Interest rate cannot be negative.")
                continue
            return FV / (1 + r) ** t
        except ValueError:
            print("Please enter valid numbers.")

def PV_of_cashflow_stream():
    """Function to calculate the present value of a cash flow stream"""
    while True:
        try:
            cashflows = float(input("Enter cash flow amount: "))
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            N = int(input("Enter number of periods: "))
            if r < 0:
                print("Interest rate cannot be negative.")
                continue
            if N < 0:
                print("Number of periods cannot be negative.")
                continue
            return sum([cashflows / pow(1 + r, n) for n in range(N+1)])
        except ValueError:
            print("Please enter valid numbers.")

def pv_perpetuity():
    """Function to calculate the present value of a perpetuity"""
    while True:
        try:
            C = float(input("Enter cash flow amount: "))
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            if r <= 0:
                print("Interest rate must be positive for perpetuity calculation.")
                continue
            return C / r
        except ValueError:
            print("Please enter valid numbers.")

def pv_annuity():
    """Function to calculate the present value of an annuity"""
    while True:
        try:
            C = float(input("Enter cash flow amount: "))
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            N = int(input("Enter number of periods: "))
            if r <= 0:
                print("Interest rate must be positive.")
                continue
            if N <= 0:
                print("Number of periods must be positive.")
                continue
            return C * (1 - (1 / (1 + r) ** N)) / r
        except ValueError:
            print("Please enter valid numbers.")

def fv_annuity():
    """Function to calculate the future value of an annuity"""
    while True:
        try:
            pv = float(input("Enter present value: "))
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            N = int(input("Enter number of periods: "))
            if r <= 0:
                print("Interest rate must be positive.")
                continue
            if N <= 0:
                print("Number of periods must be positive.")
                continue
            return pv * ((1 + r) ** N - 1) / r
        except ValueError:
            print("Please enter valid numbers.")

def pv_perpetuity_growth():
    """Function to calculate the present value of a perpetuity with growth"""
    while True:
        try:
            C = float(input("Enter cash flow amount: "))
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            g = float(input("Enter growth rate (as decimal, e.g., 0.03 for 3%): "))
            if r <= g:
                print("Interest rate must be greater than growth rate.")
                continue
            return C / (r - g)
        except ValueError:
            print("Please enter valid numbers.")

def pv_growing_annuity():
    """Function to calculate the present value of a growing annuity"""
    while True:
        try:
            C = float(input("Enter cash flow amount: "))
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            g = float(input("Enter growth rate (as decimal, e.g., 0.03 for 3%): "))
            N = int(input("Enter number of periods: "))
            if r <= g:
                print("Interest rate must be greater than growth rate.")
                continue
            if N <= 0:
                print("Number of periods must be positive.")
                continue
            return C / (r - g) * (1 - (1 + g) ** N / (1 + r) ** N)
        except ValueError:
            print("Please enter valid numbers.")

def eq_discount_period_conversion():
    """Function to convert discount period"""
    while True:
        try:
            r = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            n = int(input("Enter number of periods: "))
            if n <= 0:
                print("Number of periods must be positive.")
                continue
            return (1 + r) ** n - 1
        except ValueError:
            print("Please enter valid numbers.")

def interest_rate_per_compounding_period():
    """Function to calculate the interest rate per compounding period"""
    while True:
        try:
            APR = float(input("Enter APR (as decimal, e.g., 0.05 for 5%): "))
            k = int(input("Enter number of compounding periods per year: "))
            if k <= 0:
                print("Number of compounding periods must be positive.")
                continue
            return APR / k
        except ValueError:
            print("Please enter valid numbers.")

def APR_to_EAR():
    """Function to convert APR to EAR"""
    while True:
        try:
            APR = float(input("Enter APR (as decimal, e.g., 0.05 for 5%): "))
            k = int(input("Enter number of compounding periods per year: "))
            if k <= 0:
                print("Number of compounding periods must be positive.")
                continue
            return (1 + APR / k) ** k - 1
        except ValueError:
            print("Please enter valid numbers.")

def growth_in_purch_power():
    """Function to calculate the growth in purchasing power"""
    while True:
        try:
            inflation_rate = float(input("Enter inflation rate (as decimal, e.g., 0.03 for 3%): "))
            real_rate = float(input("Enter real rate (as decimal, e.g., 0.02 for 2%): "))
            return (1 + real_rate) / (1 + inflation_rate) - 1
        except ValueError:
            print("Please enter valid numbers.")

def real_interest_rate():
    """Function to calculate the real interest rate"""
    while True:
        try:
            real_rate = float(input("Enter real rate (as decimal, e.g., 0.02 for 2%): "))
            inflation_rate = float(input("Enter inflation rate (as decimal, e.g., 0.03 for 3%): "))
            return (real_rate - inflation_rate) / (1 + inflation_rate)
        except ValueError:
            print("Please enter valid numbers.")

def coupon_payment_CPN():
    """Function to calculate the coupon payment"""
    while True:
        try:
            face_value = float(input("Enter face value of bond: "))
            coupon_rate = float(input("Enter coupon rate (as decimal, e.g., 0.05 for 5%): "))
            N = int(input("Enter number of periods: "))
            if N <= 0:
                print("Number of periods must be positive.")
                continue
            return (face_value * coupon_rate) / N
        except ValueError:
            print("Please enter valid numbers.")

def price_zero_coupon_bond():
    """Function to calculate the price of a zero coupon bond"""
    while True:
        try:
            FV = float(input("Enter face value: "))
            YTM = float(input("Enter yield to maturity (as decimal, e.g., 0.05 for 5%): "))
            N = int(input("Enter number of periods: "))
            if N <= 0:
                print("Number of periods must be positive.")
                continue
            return FV / (1 + YTM) ** N
        except ValueError:
            print("Please enter valid numbers.")

def YTM_of_n_year_zero_coupon_bond():
    """Function to calculate the yield to maturity of a n-year zero coupon bond"""
    while True:
        try:
            FV = float(input("Enter face value: "))
            P = float(input("Enter price: "))
            N = int(input("Enter number of periods: "))
            if N <= 0:
                print("Number of periods must be positive.")
                continue
            if P <= 0:
                print("Price must be positive.")
                continue
            return (FV / P) ** (1 / N) - 1
        except ValueError:
            print("Please enter valid numbers.")

def YTM_of_coupon_bond():
    """Function to calculate the yield to maturity of a coupon bond"""
    while True:
        try:
            CPN = float(input("Enter coupon payment: "))
            FV = float(input("Enter face value: "))
            YTM = float(input("Enter yield to maturity (as decimal, e.g., 0.05 for 5%): "))
            N = int(input("Enter number of periods: "))
            if N <= 0:
                print("Number of periods must be positive.")
                continue
            return CPN * (1 / YTM) * (1 - 1 / (1 + YTM) ** N) + FV / (1 + YTM) ** N
        except ValueError:
            print("Please enter valid numbers.")

def price_of_stock_one_year_investor():
    """Function to calculate the price of a stock for a one-year investor"""
    while True:
        try:
            div_1 = float(input("Enter dividend paid in year 1: "))
            P_1 = float(input("Enter expected price in year 1: "))
            r_e = float(input("Enter required return rate (as decimal, e.g., 0.10 for 10%): "))
            if r_e <= 0:
                print("Required return rate must be positive.")
                continue
            return (div_1 + P_1) / (1 + r_e)
        except ValueError:
            print("Please enter valid numbers.")

def total_return():
    """Function to calculate the total return"""
    while True:
        try:
            div_1 = float(input("Enter dividend paid in year 1: "))
            P_0 = float(input("Enter initial price: "))
            P_1 = float(input("Enter price in year 1: "))
            if P_0 <= 0:
                print("Initial price must be positive.")
                continue
            return (div_1 / P_0) + (P_1 - P_0) / P_0
        except ValueError:
            print("Please enter valid numbers.")

def price_multi_year_investor():
    """Function to calculate the price of a stock for a multi-year investor"""
    while True:
        try:
            div_1 = float(input("Enter dividend paid in year 1: "))
            div_2 = float(input("Enter dividend paid in year 2: "))
            P_2 = float(input("Enter expected price in year 2: "))
            r_e = float(input("Enter required return rate (as decimal, e.g., 0.10 for 10%): "))
            if r_e <= 0:
                print("Required return rate must be positive.")
                continue
            return (div_1) / (1 + r_e) + (div_2 + P_2) / (1 + r_e) ** 2
        except ValueError:
            print("Please enter valid numbers.")

def constant_dividend_growth_model():
    """Function to calculate the price of a stock using the constant dividend growth model"""
    while True:
        try:
            div_1 = float(input("Enter expected dividend in year 1: "))
            r_e = float(input("Enter required return rate (as decimal, e.g., 0.10 for 10%): "))
            g = float(input("Enter growth rate (as decimal, e.g., 0.03 for 3%): "))
            if r_e <= g:
                print("Required return rate must be greater than growth rate.")
                continue
            return div_1 / (r_e - g)
        except ValueError:
            print("Please enter valid numbers.")

def dividend_per_share_ratio():
    """Function to calculate the dividend per share ratio"""
    while True:
        try:
            E = float(input("Enter earnings: "))
            shares = float(input("Enter number of shares outstanding: "))
            div_rate = float(input("Enter dividend payment rate (as decimal, e.g., 0.40 for 40%): "))
            if shares <= 0:
                print("Number of shares must be positive.")
                continue
            if div_rate < 0 or div_rate > 1:
                print("Dividend payment rate must be between 0 and 1.")
                continue
            return E * div_rate / shares
        except ValueError:
            print("Please enter valid numbers.")

def enterprise_value():
    """Function to calculate the enterprise value"""
    while True:
        try:
            equity = float(input("Enter equity value: "))
            debt = float(input("Enter debt value: "))
            cash = float(input("Enter cash value: "))
            return equity + debt - cash
        except ValueError:
            print("Please enter valid numbers.")

def free_cashflow():
    """Function to calculate the free cash flow"""
    while True:
        try:
            EBIT = float(input("Enter EBIT (Earnings Before Interest and Taxes): "))
            t_c = float(input("Enter tax rate (as decimal, e.g., 0.21 for 21%): "))
            depreciation = float(input("Enter depreciation: "))
            capex = float(input("Enter capital expenditure: "))
            delta_nwc = float(input("Enter increase in net working capital: "))
            if t_c < 0 or t_c > 1:
                print("Tax rate must be between 0 and 1.")
                continue
            return EBIT * (1 - t_c) + depreciation - capex - delta_nwc
        except ValueError:
            print("Please enter valid numbers.")

def net_investment():
    """Function to calculate the net investment"""
    while True:
        try:
            capex = float(input("Enter capital expenditure: "))
            depreciation = float(input("Enter depreciation: "))
            return capex - depreciation
        except ValueError:
            print("Please enter valid numbers.")

def call_option():
    """Function to calculate the call option value"""
    while True:
        try:
            S = float(input("Enter current stock price: "))
            K = float(input("Enter strike price: "))
            if S < 0:
                print("Stock price cannot be negative.")
                continue
            if K < 0:
                print("Strike price cannot be negative.")
                continue
            return max(S - K, 0)
        except ValueError:
            print("Please enter valid numbers.")

def put_option():
    """Function to calculate the put option value"""
    while True:
        try:
            S = float(input("Enter current stock price: "))
            K = float(input("Enter strike price: "))
            if S < 0:
                print("Stock price cannot be negative.")
                continue
            if K < 0:
                print("Strike price cannot be negative.")
                continue
            return max(K - S, 0)
        except ValueError:
            print("Please enter valid numbers.")


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
    return present_value

# TODO: Add Functions on Risk and Return


## corporate finance functions


def NPV():
    """Function to calculate the Net Present Value (NPV) of a project"""
    
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
    
    # Get initial investment (CF_0)
    while True:
        try:
            initial_investment = float(input("Enter the initial investment (CF_0): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get required return rate
    while True:
        try:
            discount_rate = float(input("Enter the required return rate (as decimal, e.g., 0.10 for 10%): "))
            if discount_rate <= 0:
                print("Required return rate must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get cash flows for each period
    cashflows = []
    for year in range(1, N + 1):
        while True:
            try:
                cf = float(input(f"Enter expected cash flow for year {year}: "))
                cashflows.append(cf)
                break
            except ValueError:
                print("Please enter a valid number.")
    
    # Calculate NPV
    npv = -initial_investment + sum(cf / (1 + discount_rate)**year 
                                  for year, cf in enumerate(cashflows, 1))
    return npv


def PB():
    """Function to calculate the Payback Period of a project"""
    while True:
        try:
            years_before_cost_recovery = float(input("Enter the years_before_cost_recovery: "))
            remaining_cost_to_recover = float(input("Enter the years_before_cost_recovery: "))
            cash_flow_during_the_year = float(input("Enter the cash_flow_during_the_year: "))
            return years_before_cost_recovery + remaining_cost_to_recover / cash_flow_during_the_year    
        except ValueError:
            print("Please enter valid numbers.")

def IRR():
    """
    Function to calculate the Internal Rate of Return (IRR) of a project
    Uses trial and error method to find the rate that makes NPV = 0
    """
    
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
    
    # Get initial investment (CF_0)
    while True:
        try:
            initial_investment = float(input("Enter the initial investment (CF_0): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get cash flows for each period
    cashflows = []
    for year in range(1, N + 1):
        while True:
            try:
                cf = float(input(f"Enter expected cash flow for year {year}: "))
                cashflows.append(cf)
                break
            except ValueError:
                print("Please enter a valid number.")
    
    def calculate_npv(rate):
        """Helper function to calculate NPV at a given rate"""
        npv = -initial_investment + sum(cf / (1 + rate)**year 
                                      for year, cf in enumerate(cashflows, 1))
        return float(npv)  # Ensure we're returning a float
    
    # Trial and error method to find IRR
    tolerance = 0.0001  # Acceptable difference from zero
    max_iterations = 1000  # Maximum number of iterations to prevent infinite loops
    
    # Initial guesses for rate
    rate_low = -0.99  # Starting with a wider range
    rate_high = 2.0   # Up to 200%
    iterations = 0
    
    while iterations < max_iterations:
        rate_mid = (rate_low + rate_high) / 2
        npv = calculate_npv(rate_mid)
        
        # Check if we've found a close enough solution
        if abs(npv) < tolerance:
            # Convert to percentage and round to 3 decimal places
            return float(rate_mid)
        
        # If NPV is positive, increase rate by trying upper half
        # If NPV is negative, decrease rate by trying lower half
        if npv > 0:
            rate_low = rate_mid
        else:
            rate_high = rate_mid
            
        iterations += 1
    
    # If no solution found within max iterations
    return None  # Return None instead of string for error case


# TODO: Capital Budgeting


# TODO: Cost of Capital


# TODO: Capital Structure


def main():
    function_sections = {
        "Time Value of Money Calculations": {
            '1': ('Discount Factor', discount_factor),
            '2': ('Future Value', future_value),
            '3': ('Present Value', present_value),
            '4': ('PV of Cash Flow Stream', PV_of_cashflow_stream),
            '5': ('PV of Perpetuity', pv_perpetuity),
            '6': ('PV of Annuity', pv_annuity),
            '7': ('FV of Annuity', fv_annuity),
            '8': ('PV of Perpetuity with Growth', pv_perpetuity_growth),
            '9': ('PV of Growing Annuity', pv_growing_annuity),
        },
        
        "Interest Rate Calculations": {
            '10': ('Equivalent Discount Period Conversion', eq_discount_period_conversion),
            '11': ('Interest Rate per Compounding Period', interest_rate_per_compounding_period),
            '12': ('APR to EAR', APR_to_EAR),
            '13': ('Growth in Purchasing Power', growth_in_purch_power),
            '14': ('Real Interest Rate', real_interest_rate),
        },
        
        "Bond Calculations": {
            '15': ('Coupon Payment', coupon_payment_CPN),
            '16': ('Zero Coupon Bond Price', price_zero_coupon_bond),
            '17': ('YTM of Zero Coupon Bond', YTM_of_n_year_zero_coupon_bond),
            '18': ('YTM of Coupon Bond', YTM_of_coupon_bond),
        },
        
        "Stock Valuation": {
            '19': ('One Year Stock Price', price_of_stock_one_year_investor),
            '20': ('Total Return', total_return),
            '21': ('Multi-Year Stock Price', price_multi_year_investor),
            '22': ('Dividend Discount Model', dividend_discount_model),
            '23': ('Constant Dividend Growth Model', constant_dividend_growth_model),
            '24': ('Dividend Per Share Ratio', dividend_per_share_ratio),
        },
        
        "Firm Valuation": {
            '25': ('Enterprise Value', enterprise_value),
            '26': ('Free Cash Flow', free_cashflow),
            '27': ('Net Investment', net_investment),
        },
        
        "Options": {
            '28': ('Call Option Value', call_option),
            '29': ('Put Option Value', put_option),
        },
        
        "Advanced Models": {
            '30': ('DDM with Constant Long Term Growth', ddm_with_constant_long_term_growth),
        },

        "Capital Budgeting": {
            '31': ('Net Present Value (NPV)', NPV),
            '32': ('Payback Period (PB)', PB),
            '33': ('Internal Rate of Return (IRR)', IRR),
    }
    }

    # Flatten the functions dictionary for easy lookup
    all_functions = {}
    for section in function_sections.values():
        all_functions.update(section)

    while True:
        print("\nFinancial Calculator Menu:")
        print("=" * 50)
        
        # Print each section with its functions
        for section_name, functions in function_sections.items():
            print(f"\n{section_name}")
            print("-" * len(section_name))
            for key, (name, _) in functions.items():
                print(f"{key}. {name}")
        
        print("\n" + "=" * 50)
        print("0. Exit")
        print("=" * 50)

        choice = input("\nEnter your choice (0-30): ")

        if choice == '0':
            print("\nThank you for using the Financial Calculator!")
            break
        elif choice in all_functions:
            try:
                result = all_functions[choice][1]()
                print(f"\nResult: {result:.4f}")
                input("\nPress Enter to continue...")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                input("\nPress Enter to continue...")
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

