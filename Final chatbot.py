from tkinter import *

root = Tk()
root.configure(bg='white')
root.title('Chat_bot')

def send():
    # Get user input
    send = "You: "+e.get()
    # Display user input
    txt.insert(END, "\n"+send)
    # Process user input
    user = e.get().lower()
    if user == "hello":
        # Display bot response
        txt.insert(END, "\n" + "Bot: Hi")
    elif user in ["hi", "hii", "hiiii"]:
        txt.insert(END, "\n" + "Bot: Hello")
    elif user == "how are you":
        txt.insert(END, "\n" + "Bot: fine! and you")
    elif user in ["fine", "i am good", "i am doing good"]:
        txt.insert(END, "\n" + "Bot: Great! how can I help you.")
    elif user in ["ok", "okay"]:
        txt.insert(END, "\n" + "Bot: great")
    elif "infosys" in user:
        # Display stock data for Infosys
        txt.insert(END, "\n" + "Bot: The stock price for Infosys is:")
        txt.insert(END, "\n" + "Open price: Rs. 1,500")
        txt.insert(END, "\n" + "Close price: Rs. 1,550")
        txt.insert(END, "\n" + "High price: Rs. 1,600")
        txt.insert(END, "\n" + "Change in price: +50")
    elif "tcs" in user:
        # Display stock data for TCS
        txt.insert(END, "\n" + "Bot: The stock price for TCS is:")
        txt.insert(END, "\n" + "Open price: Rs. 3000")
        txt.insert(END, "\n" + "Close price: Rs. 3200")
        txt.insert(END, "\n" + "High price: Rs. 3250")
        txt.insert(END, "\n" + "Change in price: +100")
    elif "microsoft" in user:
        # Display stock data for Microsoft
        txt.insert(END, "\n" + "Bot: The stock price for Microsoft is:")
        txt.insert(END, "\n" + "Open price: Rs. USD 337.26")
        txt.insert(END, "\n" + "Close price: Rs. USD 332.75")
        txt.insert(END, "\n" + "High price: Rs. USD 339.61")
        txt.insert(END, "\n" + "Change in price: -4.51")
    elif "ibm" in user:
        # Display stock data for IBM
        txt.insert(END, "\n" + "Bot: The stock price for IBM is:")
        txt.insert(END, "\n" + "Open price: Rs. USD 129.79")
        txt.insert(END, "\n" + "Close price: Rs. USD 131.13")
        txt.insert(END, "\n" + "High price: Rs. USD 131.47")
        txt.insert(END, "\n" + "Change in price: +1.34")
    elif "hcl" in user:
        # Display stock data for HCL
        txt.insert(END, "\n" + "Bot: The stock price for HCL is:")
        txt.insert(END, "\n" + "Open price: Rs. 1,183.00")
        txt.insert(END, "\n" + "Close price: Rs. 1,194.00")
        txt.insert(END, "\n" + "High price: Rs. 1,199.95")
        txt.insert(END, "\n" + "Change in price: +11.00")
    elif user in ["thank you", "bye"]:
        txt.insert(END, "\n" + "Bot: welcome")
    else:
        txt.insert(END, "\n" + "Bot: Sorry! I didn't get you")
    # Clear input field
    e.delete(0, END)

# Create GUI elements
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=100)
e.grid(row=1, column=0)

send = Button(root, text="Send", command=send)
send.grid(row=1, column=1)

# Start main event loop
root.mainloop()

