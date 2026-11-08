import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Wealth Multiplier Calculator")
app.geometry("1080x720")

def calculate_wealth():
    try:
        monthly_savings = float(savings_entry.get())
        interest_rate = float(interest_entry.get()) / 100
        duration_years = int(years_entry.get())
    except ValueError:
        result_label.configure(text="Please correct your input! Only numbers are valid.", text_color="red")
        return

    total_wealth = 0.0
    monthly_interest = interest_rate / 12
    total_months = duration_years * 12

    for month in range(1, total_months + 1):
        total_wealth += monthly_savings
        total_wealth += total_wealth * monthly_interest
        total_invested = monthly_savings * total_months
        total_interest = total_wealth - total_invested

        interest_text = f"Earned Interest: {total_interest:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")

    result_label.configure(
        text=f"Total net worth: {total_wealth:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")+ f"\n{interest_text}",
        text_color="green"
    )



title_label = ctk.CTkLabel(
    app, text="Wealth Multiplier", font=("Arial", 24, "italic")
)
title_label.pack(pady=20)

savings_label = ctk.CTkLabel(
    app, text="Monthly saving rate (€):", font=("Arial", 14)
)
savings_label.pack(pady=5)

savings_entry = ctk.CTkEntry(
    app, placeholder_text="e.g. 150", width=200, justify="center"
)
savings_entry.pack(pady=10)

interest_label = ctk.CTkLabel(
    app, text="Expected annual interest (%):", font=("Arial", 14) 
)
interest_label.pack(pady=5)

interest_entry = ctk.CTkEntry(
    app, placeholder_text="e.g. 7.0", width=200, justify="center"
)
interest_entry.pack(pady=10)

years_label = ctk.CTkLabel(
    app, text="Duration (Years):", font=("Arial", 14)
)
years_label.pack(pady=5)

years_entry = ctk.CTkEntry(
    app, placeholder_text="e.g. 10", width=200, justify="center"
)
years_entry.pack(pady=10)

calculate_button = ctk.CTkButton(
    app, text="Calculate net worth", font=("Arial", 14, "italic"), command=calculate_wealth
)
calculate_button.pack(pady=20)

result_label = ctk.CTkLabel(
    app, text="Result: 0.00 €", font=("Arial", 16, "italic"), text_color="green"
)
result_label.pack(pady=10)

app.mainloop()