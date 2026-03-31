import tkinter as tk
root = tk.Tk()

def on_click_calculate():
    weight = float(weight_textbox.get())
    height = float(height_textbox.get())
    bmi = weight/(height*height)
    answer = f"BMI = {bmi}"
    answer_label.config(text=answer)
root.geometry("600x300")
root.title("BMI Calculator")

#creating weight coulumb
weight_label = tk.Label(root,text="Enter weight(in Kgs)")
weight_label.pack()
weight_textbox=tk.Entry(root)
weight_textbox.pack()

#creating height coulomb
height_label = tk.Label(root,text="Enter height(in Mtr)")
height_label.pack()
height_textbox = tk.Entry(root)
height_textbox.pack()

#creating calculate button
calculate_button = tk.Button(root,text="Calculate",command=on_click_calculate)
calculate_button.pack(anchor=tk.CENTER,padx=10)


#print answer
answer_label = tk.Label(root,text='',font=('Arial',12))
answer_label.pack(pady=10)
root.mainloop()