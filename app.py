import streamlit as st
from server import Bank

bank = Bank()

st.title("🏦 Bank System")

menu = st.sidebar.selectbox("Menu",[
    "Create Account",
    "Deposit",
    "Withdraw",
    "Show Details",
    "Update",
    "Delete"
])

# -------- CREATE -------- #
if menu == "Create Account":
    name = st.text_input("Name")
    age = st.text_input("Age")
    email = st.text_input("Email")
    pin = st.text_input("PIN", type="password")

    if st.button("Create"):
        info = {"name":name,"age":age,"email":email,"pin":pin}
        result = bank.createAccount(info)

        if result == "age_error":
            st.error("Age must be 18+")
        elif result == "email_error":
            st.error("Invalid email")
        elif result == "pin_error":
            st.error("PIN must be 4 digits")
        else:
            st.success("Account created")
            st.write(result)

# -------- DEPOSIT -------- #
elif menu == "Deposit":
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", step=1)
    amount = st.number_input("Amount", min_value=0)

    if st.button("Deposit"):
        result = bank.depositmoney(acc, pin, amount)

        if result == "invalid":
            st.error("Invalid account")
        elif result == "amount_error":
            st.error("Amount must be > 0")
        else:
            st.success("Deposited successfully")

# -------- WITHDRAW -------- #
elif menu == "Withdraw":
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", step=1)
    amount = st.number_input("Amount", min_value=0)

    if st.button("Withdraw"):
        result = bank.withdrawmoney(acc, pin, amount)

        if result == "invalid":
            st.error("Invalid account")
        elif result == "balance_error":
            st.error("Insufficient balance")
        elif result == "amount_error2":
            st.error("Amount must be greater than 0")
        else:
            st.success("Withdraw successful")

# -------- SHOW -------- #
elif menu == "Show Details":
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", step=1)

    if st.button("Show"):
        result = bank.showdetails(acc, pin)

        if result == "invalid":
            st.error("Invalid account")
        else:
            st.json(result)

# -------- UPDATE -------- #
elif menu == "Update":
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", step=1)

    name = st.text_input("New Name")
    email = st.text_input("New Email")
    newpin = st.text_input("New PIN")

    if st.button("Update"):
        result = bank.updatedetails(acc, pin, name, email, newpin)

        if result == "invalid":
            st.error("Invalid account")
        elif result == "email_error":
            st.error("Invalid email")
        elif result == "pin_error":
            st.error("PIN must be 4 digits")
        else:
            st.success("Updated successfully")

# -------- DELETE -------- #
elif menu == "Delete":
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", step=1)
    confirm = st.text_input("Type 'y' to confirm delete")

    if st.button("Delete"):
        result = bank.Delete(acc, pin, confirm)

        if result == "invalid":
            st.error("Invalid account")
        elif result == "cancelled":
            st.warning("Deletion cancelled")
        else:
            st.success("Account deleted")