import tkinter as tk
window =tk.Tk()
window.title("GUI App")
window.geometry("400x400")

#LABEL
title=tk.Label(text="Hello ,Its Allan!", font=("Times New Roman", 20))
title.grid() #same as title.grid(column=0,row=0)

#BUTTON
button1=tk.Button(text="Click Me!" , font=("Times New Roman", 20),bg="blue")
button1.grid(column=1,row=1)

#ENTRY_FIELD
entry_field1=tk.Entry()
entry_field1.grid(column=0 , row=2)

#TEXT FIELD
text_field=tk.Text(master=window , height=10 , width=30)
text_field.grid()
window.mainloop()