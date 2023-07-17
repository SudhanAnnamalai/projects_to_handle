#Import all Tkinter modules
from tkinter import * 

#Function to convert fahrenheit to Celsius
def fahrenheit_to_celsius(temperature):
    output = (temperature+32) * (5/9)
    return output

def celsius_to_fahrenheit(temperature):
    output = (temperature*(9/5))-32
    return output

##------------Function for button to Invoke----------------------#
def execute():
    try:
        temperature = float(input_entry.get())
        input_entry.delete(0,END)
        #Check radio button status
        logic_function = fahrenheit_to_celsius if var.get()==1 else celsius_to_fahrenheit
        converted_temp = logic_function(temperature)
        output_entry.delete(0,END)
        output_entry.insert(END,round(converted_temp,2))
    except Exception as e:
        output_entry.delete(0,END)
        output_entry.insert(END,"Invalid Input, Error:"+str(e))



root = Tk()
root.title("Temperature Converter")

#-----------Input Label and Entry field--------#
label = Label(root, text="Enter the Temperature: ")
label.pack(expand=10)
input_entry = Entry(root)
input_entry.pack(expand=10)

#---------Radio Buttons---------------------#
var = IntVar()
f_to_c = Radiobutton(root, text = "Fahreheit to Celsius", variable=var, value=1)
f_to_c.pack()
c_to_f = Radiobutton(root, text = " Celsius to Fahreheit", variable=var, value=0)
c_to_f.pack()

#------------Button to Invoke a Function----------------------#
btn = Button(root, text="Convert", command=execute)
btn.pack()

#----------------Output labels------------------------#
output_label = Label(root, text="Converted temperature is :")
output_label.pack()
output_entry = Entry(root)
output_entry.pack()



###---------------Final Run command------------------------------------------------#
root.mainloop()




