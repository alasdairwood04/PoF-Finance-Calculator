import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, List
from finance_functions import *

class FinanceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Calculator")
        self.root.geometry("800x600")

        # Create main notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)

        # Create tabs for different categories
        self.create_time_value_tab()
        self.create_annuity_tab()
        self.create_bond_tab()
        self.create_stock_tab()
        self.create_firm_valuation_tab()
        self.create_options_tab()

    def create_time_value_tab(self):
        time_value_frame = ttk.Frame(self.notebook)
        self.notebook.add(time_value_frame, text='Time Value of Money')

        # Create calculator selection
        calculations = [
            "Present Value",
            "Future Value",
            "Discount Factor",
            "PV of Cash Flow Stream"
        ]

        ttk.Label(time_value_frame, text="Select Calculation:").pack(pady=5)
        calc_var = tk.StringVar()
        calc_dropdown = ttk.Combobox(time_value_frame, textvariable=calc_var, values=calculations)
        calc_dropdown.pack(pady=5)
        calc_dropdown.set(calculations[0])

        # Create input frame
        input_frame = ttk.Frame(time_value_frame)
        input_frame.pack(pady=10)

        # Input variables
        self.pv_inputs = {}
        
        def update_inputs(*args):
            # Clear existing inputs
            for widget in input_frame.winfo_children():
                widget.destroy()

            # Create new inputs based on selection
            if calc_var.get() == "Present Value":
                fields = ['Future Value', 'Interest Rate', 'Time']
            elif calc_var.get() == "Future Value":
                fields = ['Present Value', 'Interest Rate', 'Time']
            elif calc_var.get() == "Discount Factor":
                fields = ['Interest Rate', 'Time']
            else:  # PV of Cash Flow Stream
                fields = ['Cash Flows', 'Interest Rate', 'Number of Periods']

            self.pv_inputs = {}
            for field in fields:
                frame = ttk.Frame(input_frame)
                frame.pack(pady=5)
                ttk.Label(frame, text=f"{field}:").pack(side='left', padx=5)
                self.pv_inputs[field] = ttk.Entry(frame)
                self.pv_inputs[field].pack(side='left', padx=5)

        calc_dropdown.bind('<<ComboboxSelected>>', update_inputs)
        update_inputs()  # Initial setup

        def calculate():
            try:
                result = 0
                selection = calc_var.get()
                
                if selection == "Present Value":
                    FV = float(self.pv_inputs['Future Value'].get())
                    r = float(self.pv_inputs['Interest Rate'].get())
                    t = float(self.pv_inputs['Time'].get())
                    result = present_value(FV, r, t)
                
                elif selection == "Future Value":
                    PV = float(self.pv_inputs['Present Value'].get())
                    r = float(self.pv_inputs['Interest Rate'].get())
                    t = float(self.pv_inputs['Time'].get())
                    result = future_value(PV, r, t)
                
                elif selection == "Discount Factor":
                    r = float(self.pv_inputs['Interest Rate'].get())
                    t = float(self.pv_inputs['Time'].get())
                    result = discount_factor(r, t)
                
                elif selection == "PV of Cash Flow Stream":
                    CF = float(self.pv_inputs['Cash Flows'].get())
                    r = float(self.pv_inputs['Interest Rate'].get())
                    N = int(self.pv_inputs['Number of Periods'].get())
                    result = PV_of_cashflow_stream(CF, r, N)

                self.result_label.config(text=f"Result: {result:.2f}")
            
            except ValueError as e:
                messagebox.showerror("Error", "Please enter valid numbers")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(time_value_frame, text="Calculate", command=calculate).pack(pady=10)
        self.result_label = ttk.Label(time_value_frame, text="Result: ")
        self.result_label.pack(pady=10)

    def create_annuity_tab(self):
        annuity_frame = ttk.Frame(self.notebook)
        self.notebook.add(annuity_frame, text='Annuities')

        calculations = [
            "PV of Perpetuity",
            "PV of Annuity",
            "FV of Annuity",
            "PV of Perpetuity with Growth",
            "PV of Growing Annuity"
        ]

        ttk.Label(annuity_frame, text="Select Calculation:").pack(pady=5)
        calc_var = tk.StringVar()
        calc_dropdown = ttk.Combobox(annuity_frame, textvariable=calc_var, values=calculations)
        calc_dropdown.pack(pady=5)
        calc_dropdown.set(calculations[0])

        input_frame = ttk.Frame(annuity_frame)
        input_frame.pack(pady=10)

        self.annuity_inputs = {}

        def update_inputs(*args):
            for widget in input_frame.winfo_children():
                widget.destroy()

            if calc_var.get() == "PV of Perpetuity":
                fields = ['Cash Flow', 'Interest Rate']
            elif calc_var.get() == "PV of Annuity":
                fields = ['Cash Flow', 'Interest Rate', 'Number of Periods']
            elif calc_var.get() == "FV of Annuity":
                fields = ['Present Value', 'Interest Rate', 'Number of Periods']
            elif calc_var.get() == "PV of Perpetuity with Growth":
                fields = ['Cash Flow', 'Interest Rate', 'Growth Rate']
            else:  # PV of Growing Annuity
                fields = ['Cash Flow', 'Interest Rate', 'Growth Rate', 'Number of Periods']

            self.annuity_inputs = {}
            for field in fields:
                frame = ttk.Frame(input_frame)
                frame.pack(pady=5)
                ttk.Label(frame, text=f"{field}:").pack(side='left', padx=5)
                self.annuity_inputs[field] = ttk.Entry(frame)
                self.annuity_inputs[field].pack(side='left', padx=5)

        calc_dropdown.bind('<<ComboboxSelected>>', update_inputs)
        update_inputs()

        def calculate():
            try:
                result = 0
                selection = calc_var.get()

                if selection == "PV of Perpetuity":
                    C = float(self.annuity_inputs['Cash Flow'].get())
                    r = float(self.annuity_inputs['Interest Rate'].get())
                    result = pv_perpetuity(C, r)
                
                elif selection == "PV of Annuity":
                    C = float(self.annuity_inputs['Cash Flow'].get())
                    r = float(self.annuity_inputs['Interest Rate'].get())
                    N = int(self.annuity_inputs['Number of Periods'].get())
                    result = pv_annuity(C, r, N)
                
                # Add other calculations...

                self.annuity_result_label.config(text=f"Result: {result:.2f}")
            
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(annuity_frame, text="Calculate", command=calculate).pack(pady=10)
        self.annuity_result_label = ttk.Label(annuity_frame, text="Result: ")
        self.annuity_result_label.pack(pady=10)

    def create_bond_tab(self):
        bond_frame = ttk.Frame(self.notebook)
        self.notebook.add(bond_frame, text='Bonds')
        # Similar implementation for bonds...

    def create_stock_tab(self):
        stock_frame = ttk.Frame(self.notebook)
        self.notebook.add(stock_frame, text='Stocks')
        # Similar implementation for stocks...

    def create_firm_valuation_tab(self):
        valuation_frame = ttk.Frame(self.notebook)
        self.notebook.add(valuation_frame, text='Firm Valuation')
        # Similar implementation for firm valuation...

    def create_options_tab(self):
        options_frame = ttk.Frame(self.notebook)
        self.notebook.add(options_frame, text='Options')
        # Similar implementation for options...


    def create_bond_tab(self):
        bond_frame = ttk.Frame(self.notebook)
        self.notebook.add(bond_frame, text='Bonds')

        calculations = [
            "Coupon Payment",
            "Zero Coupon Bond Price",
            "YTM of Zero Coupon Bond",
            "YTM of Coupon Bond"
        ]

        ttk.Label(bond_frame, text="Select Calculation:").pack(pady=5)
        calc_var = tk.StringVar()
        calc_dropdown = ttk.Combobox(bond_frame, textvariable=calc_var, values=calculations)
        calc_dropdown.pack(pady=5)
        calc_dropdown.set(calculations[0])

        input_frame = ttk.Frame(bond_frame)
        input_frame.pack(pady=10)

        self.bond_inputs = {}

        def update_inputs(*args):
            for widget in input_frame.winfo_children():
                widget.destroy()

            if calc_var.get() == "Coupon Payment":
                fields = ['Face Value', 'Coupon Rate', 'Number of Periods']
            elif calc_var.get() == "Zero Coupon Bond Price":
                fields = ['Face Value', 'YTM', 'Number of Periods']
            elif calc_var.get() == "YTM of Zero Coupon Bond":
                fields = ['Face Value', 'Price', 'Number of Periods']
            else:  # YTM of Coupon Bond
                fields = ['Coupon Payment', 'Face Value', 'YTM', 'Number of Periods']

            self.bond_inputs = {}
            for field in fields:
                frame = ttk.Frame(input_frame)
                frame.pack(pady=5)
                ttk.Label(frame, text=f"{field}:").pack(side='left', padx=5)
                self.bond_inputs[field] = ttk.Entry(frame)
                self.bond_inputs[field].pack(side='left', padx=5)

        calc_dropdown.bind('<<ComboboxSelected>>', update_inputs)
        update_inputs()

        def calculate():
            try:
                result = 0
                selection = calc_var.get()

                if selection == "Coupon Payment":
                    FV = float(self.bond_inputs['Face Value'].get())
                    rate = float(self.bond_inputs['Coupon Rate'].get())
                    N = int(self.bond_inputs['Number of Periods'].get())
                    result = coupon_payment_CPN(FV, rate, N)
                
                elif selection == "Zero Coupon Bond Price":
                    FV = float(self.bond_inputs['Face Value'].get())
                    YTM = float(self.bond_inputs['YTM'].get())
                    N = int(self.bond_inputs['Number of Periods'].get())
                    result = price_zero_coupon_bond(FV, YTM, N)
                
                elif selection == "YTM of Zero Coupon Bond":
                    FV = float(self.bond_inputs['Face Value'].get())
                    P = float(self.bond_inputs['Price'].get())
                    N = int(self.bond_inputs['Number of Periods'].get())
                    result = YTM_of_n_year_zer_coupon_bond(FV, P, N)
                
                else:  # YTM of Coupon Bond
                    CPN = float(self.bond_inputs['Coupon Payment'].get())
                    FV = float(self.bond_inputs['Face Value'].get())
                    YTM = float(self.bond_inputs['YTM'].get())
                    N = int(self.bond_inputs['Number of Periods'].get())
                    result = YTM_of_coupon_bond(CPN, FV, YTM, N)

                self.bond_result_label.config(text=f"Result: {result:.4f}")
            
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(bond_frame, text="Calculate", command=calculate).pack(pady=10)
        self.bond_result_label = ttk.Label(bond_frame, text="Result: ")
        self.bond_result_label.pack(pady=10)

    def create_stock_tab(self):
        stock_frame = ttk.Frame(self.notebook)
        self.notebook.add(stock_frame, text='Stocks')

        calculations = [
            "One Year Stock Price",
            "Total Return",
            "Multi-Year Stock Price",
            "Constant Growth DDM",
            "Dividend per Share"
        ]

        ttk.Label(stock_frame, text="Select Calculation:").pack(pady=5)
        calc_var = tk.StringVar()
        calc_dropdown = ttk.Combobox(stock_frame, textvariable=calc_var, values=calculations)
        calc_dropdown.pack(pady=5)
        calc_dropdown.set(calculations[0])

        input_frame = ttk.Frame(stock_frame)
        input_frame.pack(pady=10)

        self.stock_inputs = {}

        def update_inputs(*args):
            for widget in input_frame.winfo_children():
                widget.destroy()

            if calc_var.get() == "One Year Stock Price":
                fields = ['Dividend Year 1', 'Price Year 1', 'Required Return']
            elif calc_var.get() == "Total Return":
                fields = ['Dividend Year 1', 'Price Year 0', 'Price Year 1']
            elif calc_var.get() == "Multi-Year Stock Price":
                fields = ['Dividend Year 1', 'Dividend Year 2', 'Price Year 2', 'Required Return']
            elif calc_var.get() == "Constant Growth DDM":
                fields = ['Dividend Year 1', 'Required Return', 'Growth Rate']
            else:  # Dividend per Share
                fields = ['Earnings', 'Shares Outstanding', 'Dividend Payment Rate']

            self.stock_inputs = {}
            for field in fields:
                frame = ttk.Frame(input_frame)
                frame.pack(pady=5)
                ttk.Label(frame, text=f"{field}:").pack(side='left', padx=5)
                self.stock_inputs[field] = ttk.Entry(frame)
                self.stock_inputs[field].pack(side='left', padx=5)

        calc_dropdown.bind('<<ComboboxSelected>>', update_inputs)
        update_inputs()

        def calculate():
            try:
                result = 0
                selection = calc_var.get()

                if selection == "One Year Stock Price":
                    div_1 = float(self.stock_inputs['Dividend Year 1'].get())
                    P_1 = float(self.stock_inputs['Price Year 1'].get())
                    r_e = float(self.stock_inputs['Required Return'].get())
                    result = price_of_stock_one_year_investor(div_1, P_1, r_e)
                
                elif selection == "Total Return":
                    div_1 = float(self.stock_inputs['Dividend Year 1'].get())
                    P_0 = float(self.stock_inputs['Price Year 0'].get())
                    P_1 = float(self.stock_inputs['Price Year 1'].get())
                    result = total_return(div_1, P_0, P_1)
                
                elif selection == "Multi-Year Stock Price":
                    div_1 = float(self.stock_inputs['Dividend Year 1'].get())
                    div_2 = float(self.stock_inputs['Dividend Year 2'].get())
                    P_2 = float(self.stock_inputs['Price Year 2'].get())
                    r_e = float(self.stock_inputs['Required Return'].get())
                    result = price_multi_year_investor(div_1, div_2, P_2, r_e)
                
                elif selection == "Constant Growth DDM":
                    div_1 = float(self.stock_inputs['Dividend Year 1'].get())
                    r_e = float(self.stock_inputs['Required Return'].get())
                    g = float(self.stock_inputs['Growth Rate'].get())
                    result = constant_dividend_growth_model(div_1, r_e, g)
                
                else:  # Dividend per Share
                    E = float(self.stock_inputs['Earnings'].get())
                    shares = float(self.stock_inputs['Shares Outstanding'].get())
                    rate = float(self.stock_inputs['Dividend Payment Rate'].get())
                    result = dividend_per_share_ratio(E, shares, rate)

                self.stock_result_label.config(text=f"Result: {result:.4f}")
            
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(stock_frame, text="Calculate", command=calculate).pack(pady=10)
        self.stock_result_label = ttk.Label(stock_frame, text="Result: ")
        self.stock_result_label.pack(pady=10)

    def create_firm_valuation_tab(self):
        valuation_frame = ttk.Frame(self.notebook)
        self.notebook.add(valuation_frame, text='Firm Valuation')

        calculations = [
            "Enterprise Value",
            "Free Cash Flow",
            "Net Investment"
        ]

        ttk.Label(valuation_frame, text="Select Calculation:").pack(pady=5)
        calc_var = tk.StringVar()
        calc_dropdown = ttk.Combobox(valuation_frame, textvariable=calc_var, values=calculations)
        calc_dropdown.pack(pady=5)
        calc_dropdown.set(calculations[0])

        input_frame = ttk.Frame(valuation_frame)
        input_frame.pack(pady=10)

        self.valuation_inputs = {}

        def update_inputs(*args):
            for widget in input_frame.winfo_children():
                widget.destroy()

            if calc_var.get() == "Enterprise Value":
                fields = ['Equity', 'Debt', 'Cash']
            elif calc_var.get() == "Free Cash Flow":
                fields = ['EBIT', 'Tax Rate', 'Depreciation', 'Capital Expenditure', 'Increase in NWC']
            else:  # Net Investment
                fields = ['Capital Expenditure', 'Depreciation']

            self.valuation_inputs = {}
            for field in fields:
                frame = ttk.Frame(input_frame)
                frame.pack(pady=5)
                ttk.Label(frame, text=f"{field}:").pack(side='left', padx=5)
                self.valuation_inputs[field] = ttk.Entry(frame)
                self.valuation_inputs[field].pack(side='left', padx=5)

        calc_dropdown.bind('<<ComboboxSelected>>', update_inputs)
        update_inputs()

        def calculate():
            try:
                result = 0
                selection = calc_var.get()

                if selection == "Enterprise Value":
                    equity = float(self.valuation_inputs['Equity'].get())
                    debt = float(self.valuation_inputs['Debt'].get())
                    cash = float(self.valuation_inputs['Cash'].get())
                    result = enterprise_value(equity, debt, cash)
                
                elif selection == "Free Cash Flow":
                    EBIT = float(self.valuation_inputs['EBIT'].get())
                    t_c = float(self.valuation_inputs['Tax Rate'].get())
                    depreciation = float(self.valuation_inputs['Depreciation'].get())
                    capex = float(self.valuation_inputs['Capital Expenditure'].get())
                    nwc = float(self.valuation_inputs['Increase in NWC'].get())
                    result = free_cashflow(EBIT, t_c, depreciation, capex, nwc)
                
                else:  # Net Investment
                    capex = float(self.valuation_inputs['Capital Expenditure'].get())
                    depreciation = float(self.valuation_inputs['Depreciation'].get())
                    result = net_investment(capex, depreciation)

                self.valuation_result_label.config(text=f"Result: {result:.2f}")
            
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(valuation_frame, text="Calculate", command=calculate).pack(pady=10)
        self.valuation_result_label = ttk.Label(valuation_frame, text="Result: ")
        self.valuation_result_label.pack(pady=10)


def main():
    root = tk.Tk()
    app = FinanceCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()