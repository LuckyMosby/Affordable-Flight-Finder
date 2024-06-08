screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# Calculate x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (200 // 2)
y = (screen_height // 2) - (100 // 2)
window.geometry("400x100+{}+{}".format(x, y))  # Set window position and size
window.configure(bg="#1df6f6")  # Set background color of window
label = tk.Label(window, text="No flights available for the given criteria.", anchor="center", font=("Oswald", 15))
label.configure(bg="#1df6f6")  # Set background color of label
window.title("Email Automation")
label.pack(pady=20)
window.after(3000, lambda: window.destroy())
window.mainloop()