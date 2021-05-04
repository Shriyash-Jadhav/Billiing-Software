#!/usr/bin/env python
# coding: utf-8

# In[28]:


from tkinter import*
import math
import random
import os
from tkinter import messagebox


class Bill_Software:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1560x775+0+0")
        self.root.title("BILLING SOFTWARE")
        bg_color = "Orchid4"
        title = Label(self.root, text="BILLING SOFTWARE", bd=13, relief=GROOVE, bg=bg_color, fg="white", font=("Book Antiqua", 28, "bold"), pady=2).pack(fill=X)

        # --------------------------Varibles-------------------------------------------------------------------------------------
        # ---------------Grocery---------------------
        self.wheat = IntVar()
        self.rice = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        self.oil = IntVar()
        self.spices = IntVar()
        # ---------------Medicine----------------------
        self.paracetmol = IntVar()
        self.antacids = IntVar()
        self.ointment = IntVar()
        self.painkiller = IntVar()
        self.keraboost = IntVar()
        self.ors = IntVar()
        # ---------------Cosmetics---------------------
        self.FaceWash = IntVar()
        self.shampoo = IntVar()
        self.conditioner = IntVar()
        self.soap = IntVar()
        self.spray = IntVar()
        self.lotion = IntVar()
        # -----Total Product price and tax variables------
        self.TotalGrocery = StringVar()
        self.TotalMedicine = StringVar()
        self.TotalCosmetics = StringVar()

        self.GroceryTax = StringVar()
        self.MedicineTax = StringVar()
        self.CosmeticTax = StringVar()
        # ------------Customer Details--------------------
        self.CusName = StringVar()
        self.CusMobile = StringVar()
        self.BillNo = StringVar()
        x = random.randint(1000, 9999)
        self.BillNo.set(str(x))

        self.Search = StringVar()

        # -----------------------Customer details--------------------------------------------------------------------------------

        f1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="CUSTOMER DETAILS", font=("Times New Roman", 13, "bold"), fg="gold", bg=bg_color)
        f1.place(x=0, y=78, relwidth=1)

        cus_name = Label(f1, text="Customer Name", bg=bg_color, fg="white", font=("Times New Roman", 16, "bold")).grid(row=0, column=0, padx=20, pady=6)
        name_entry = Entry(f1, width=22, textvariable=self.CusName, font=("Book antiqua", 14), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=12, pady=6)

        cus_mobile = Label(f1, text="Customer Mobile No.", bg=bg_color, fg="white", font=("Times New Roman", 16, "bold")).grid(row=0, column=2, padx=20, pady=6)
        phone_entry = Entry(f1, width=22, textvariable=self.CusMobile, font=("Book antiqua", 14), bd=5, relief=SUNKEN).grid(row=0, column=3, padx=12, pady=6)

        cus_b_no = Label(f1, text="Bill Number", bg=bg_color, fg="white", font=("Times New Roman", 16, "bold")).grid(row=0, column=4, padx=20, pady=6)
        b_no_entry = Entry(f1, width=22, textvariable=self.Search, font=("Book antiqua", 14), bd=5, relief=SUNKEN).grid(row=0, column=5, padx=12, pady=6)

        bill_Button = Button(f1, text="SEARCH", command=self.Find_Bill, width=10, bd=7, font=("Book Antiqua", 14, "bold")).grid(row=0, column=6, padx=10, pady=10)

        # ----------------------------Grocery Frame------------------------------------------------------------------------------

        f2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="GROCERY", font=("Times New Roman", 13, "bold"), fg="gold", bg=bg_color)
        f2.place(x=5, y=182, width=360, height=410)

        wheat_label = Label(f2, text="Wheat", font=("Book Antiqua", 17, "bold"), bg=bg_color,fg="turquoise1").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        wheat_entry = Entry(f2, width=12, textvariable=self.wheat, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        rice_label = Label(f2, text="Rice", font=("Book Antiqua", 17, "bold"), bg=bg_color,fg="turquoise1").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        rice_entry = Entry(f2, width=12, textvariable=self.rice, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        sugar_label = Label(f2, text="Sugar", font=("Book Antiqua", 17, "bold"), bg=bg_color,fg="turquoise1").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        sugar_entry = Entry(f2, width=12, textvariable=self.sugar, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        tea_label = Label(f2, text="Tea", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tea_entry = Entry(f2, width=12, textvariable=self.tea, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        oil_label = Label(f2, text="Edible Oil", font=("Book Antiqua", 17, "bold"),bg=bg_color, fg="turquoise1").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        oil_entry = Entry(f2, width=12, textvariable=self.oil, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        spices_label = Label(f2, text="Spices", font=("Book Antiqua", 17, "bold"), bg=bg_color,fg="turquoise1").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        spices_entry = Entry(f2, width=12, textvariable=self.spices, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # -------------------------Medicines-------------------------------------------------------------------------------------

        f3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="MEDICINE", font=("Times New Roman", 13, "bold"), fg="gold", bg=bg_color)
        f3.place(x=370, y=182, width=360, height=410)

        med1_label = Label(f3, text="Paracetmol", font=("Book Antiqua", 17, "bold"),bg=bg_color, fg="turquoise1").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        med1_entry = Entry(f3, width=12, textvariable=self.paracetmol, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        med2_label = Label(f3, text="Antacids", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        med2_entry = Entry(f3, width=12, textvariable=self.antacids, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        med3_label = Label(f3, text="Ointment", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        med3_entry = Entry(f3, width=12, textvariable=self.ointment, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        med4_label = Label(f3, text="Painkiller", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        med4_entry = Entry(f3, width=12, textvariable=self.painkiller, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        med5_label = Label(f3, text="KeraBoost", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        med5_entry = Entry(f3, width=12, textvariable=self.keraboost, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        med6_label = Label(f3, text="ORS", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        med6_entry = Entry(f3, width=12, textvariable=self.ors, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ---------------------------Cosmetics-----------------------------------------------------------------------------------

        f4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="COSMETICS", font=("Times New Roman", 13, "bold"), fg="gold", bg=bg_color)
        f4.place(x=735, y=182, width=360, height=410)

        cos1_label = Label(f4, text="Face Wash", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        cos1_entry = Entry(f4, width=12, textvariable=self.FaceWash, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        cos2_label = Label(f4, text="Shampoo", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cos2_entry = Entry(f4, width=12, textvariable=self.shampoo, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        cos3_label = Label(f4, text="Conditioner", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        cos3_entry = Entry(f4, width=12, textvariable=self.conditioner, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        cos4_label = Label(f4, text="Bath Soap", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        cos4_entry = Entry(f4, width=12, textvariable=self.soap, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        cos5_label = Label(f4, text="Hair Spray", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        cos5_entry = Entry(f4, width=12, textvariable=self.spray, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        cos6_label = Label(f4, text="Body Lotion", font=("Book Antiqua", 17, "bold"), bg=bg_color, fg="turquoise1").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        cos6_entry = Entry(f4, width=12, textvariable=self.lotion, font=("Book Antiqua", 17, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # -----------------------------Tax Invoice-------------------------------------------------------------------------------

        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=1110, y=182, width=410, height=410)
        b_title = Label(f5, text="Tax Invoice", font=("Book Antiqua", 17, "bold"), bd=7, relief=GROOVE).pack(fill=X)
        scroll_bar = Scrollbar(f5, orient=VERTICAL)
        self.textarea = Text(f5, yscrollcommand=scroll_bar.set)
        scroll_bar.pack(side=RIGHT, fill=Y)
        scroll_bar.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # --------------------------------Button Frame---------------------------------------------------------------------------

        f6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="BILL MENU", font=("Times New Roman", 13, "bold"), fg="gold", bg=bg_color)
        f6.place(x=0, y=597, relwidth=1, height=180)

        total1 = Label(f6, text="Total Grocery Price", bg=bg_color, fg="white", font=("Times New Roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        total1_entry = Entry(f6, width=19, textvariable=self.TotalGrocery, font=("Book Antiqua", 14, "bold"), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        total2 = Label(f6, text="Total Medicine Price", bg=bg_color, fg="white", font=("Times New Roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        total2_entry = Entry(f6, width=19, textvariable=self.TotalMedicine, font=("Book Antiqua", 14, "bold"), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        total3 = Label(f6, text="Total Cosmetic Price", bg=bg_color, fg="white", font=("Times New Roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        total3_entry = Entry(f6, width=19, textvariable=self.TotalCosmetics, font=("Book Antiqua", 14, "bold"), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        tax1 = Label(f6, text="Grocery Tax", bg=bg_color, fg="white", font=("Times New Roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        tax1_entry = Entry(f6, width=19, textvariable=self.GroceryTax, font=("Book Antiqua", 14, "bold"), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        tax2 = Label(f6, text="Medicine Tax", bg=bg_color, fg="white", font=("Times New Roman", 15, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        tax2_entry = Entry(f6, width=19, textvariable=self.MedicineTax, font=("Book Antiqua", 14, "bold"), bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        tax3 = Label(f6, text="Cosmetic Tax", bg=bg_color, fg="white", font=("Times New Roman", 15, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        tax3_entry = Entry(f6, width=19, textvariable=self.CosmeticTax, font=("Book Antiqua", 14, "bold"), bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        Button_frame = Frame(f6, bd=7, relief=GROOVE)
        Button_frame.place(x=834, width=680, height=150)

        total_button = Button(Button_frame, command=self.TOTAL, text="TOTAL", font=("Times New Roman", 12, "bold"), bd=7, bg="turquoise2", fg="Black", pady=18, width=15).grid(row=0, column=0, padx=5, pady=20)
        GenBill_button = Button(Button_frame, text="GENERATE BILL", command=self.Bill_Area, font=("Times New Roman", 12, "bold"), bd=7, bg="turquoise2", fg="Black", pady=18, width=15).grid(row=0, column=1, padx=5, pady=20)
        Clear_button = Button(Button_frame, text="CLEAR", command=self.Clear, font=("Times New Roman", 12, "bold"), bd=7, bg="turquoise2", fg="Black", pady=18, width=15).grid(row=0, column=2, padx=5, pady=20)
        Exit_button = Button(Button_frame, text="EXIT", command=self.Exit, font=("Times New Roman", 12, "bold"), bd=7, bg="turquoise2", fg="Black", pady=18, width=15).grid(row=0, column=3, padx=5, pady=20)

        self.Welcome_Bill()

    def TOTAL(self):
        self.wheat1 = self.wheat.get()*80
        self.rice1 = self.rice.get()*60
        self.sugar1 = self.sugar.get()*120
        self.tea1 = self.tea.get()*160
        self.oil1 = self.oil.get()*180
        self.spices1 = self.spices.get()*40

        self.Total_Grocery_Price = float(
            self.wheat1 +
            self.rice1 +
            self.sugar1 +
            self.tea1 +
            self.oil1 +
            self.spices1
        )
        self.TotalGrocery.set("Rs. "+str(self.Total_Grocery_Price))
        self.g_tax = round((self.Total_Grocery_Price*0.1), 2)
        self.GroceryTax.set("Rs. "+str(self.g_tax))

        self.paracetmol1 = self.paracetmol.get()*40
        self.antacids1 = self.antacids.get()*90
        self.ointment1 = self.ointment.get()*120
        self.painkiller1 = self.painkiller.get()*400
        self.keraboost1 = self.keraboost.get()*145
        self.ors1 = self.ors.get()*30

        self.Total_Medicine_Price = float(
            self.paracetmol1 +
            self.antacids1 +
            self.ointment1 +
            self.painkiller1 +
            self.keraboost1 +
            self.ors1
        )
        self.TotalMedicine.set("Rs. "+str(self.Total_Medicine_Price))
        self.m_tax = round((self.Total_Medicine_Price*0.08), 2)
        self.MedicineTax.set("Rs. "+str(self.m_tax))

        self.FaceWash1 = self.FaceWash.get()*200
        self.shampoo1 = self.shampoo.get()*459
        self.conditioner1 = self.conditioner.get()*380
        self.soap1 = self.soap.get()*70
        self.spray1 = self.spray.get()*260
        self.lotion1 = self.lotion.get()*250

        self.Total_Cosmetics_Price = float(
            self.FaceWash1 +
            self.shampoo1 +
            self.conditioner1 +
            self.soap1 +
            self.spray1 +
            self.lotion1
        )
        self.TotalCosmetics.set("Rs. "+str(self.Total_Cosmetics_Price))
        self.c_tax = round((self.Total_Cosmetics_Price*0.13), 2)
        self.CosmeticTax.set("Rs. "+str(self.c_tax))

        self.Calculate_Bill = float(self.Total_Grocery_Price+self.Total_Cosmetics_Price+self.Total_Medicine_Price+self.g_tax+self.m_tax+self.c_tax)
        self.Total_Bill = round((self.Calculate_Bill), 2)
        
    def Welcome_Bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\t       Welcome to Shopntag\n")
        self.textarea.insert(END, f"\n Bill Number : {self.BillNo.get()}")
        self.textarea.insert(END, f"\n Customer Name: {self.CusName.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.CusMobile.get()}")
        self.textarea.insert(END, f"\n----------------------------------------------")
        self.textarea.insert(END, f"\n Products\t\t QTY\t\tPrice")
        self.textarea.insert(END, f"\n----------------------------------------------")

    def Bill_Area(self):
        if self.CusName.get()=="" or self.CusMobile.get()=="":
             messagebox.showerror("ERROR", "Please enter customer name and mobile number.")
        elif self.TotalGrocery.get()=="Rs. 0.0" and self.TotalMedicine.get()=="Rs. 0.0" and self.TotalCosmetics.get()=="Rs. 0.0":
             messagebox.showerror("ERROR", "No product purchased!! Please select some products.")
        else:
            self.Welcome_Bill()

        # -----------------------------------------------------Goccery----------------------------------------------------------

            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\n Wheat\t\t {self.wheat.get()}\t\tRs {self.wheat1}")
            if self.rice.get() != 0:
                self.textarea.insert(END, f"\n Rice\t\t {self.rice.get()}\t\tRs {self.rice1}")
            if self.sugar.get() != 0:
                self.textarea.insert(END, f"\n Sugar\t\t {self.sugar.get()}\t\tRs {self.sugar1}")
            if self.tea.get() != 0:
                self.textarea.insert(END, f"\n Tea\t\t {self.tea.get()}\t\tRs {self.tea1}")
            if self.oil.get() != 0:
                self.textarea.insert(END, f"\n Oil\t\t {self.oil.get()}\t\tRs {self.oil1}")
            if self.spices.get() != 0:
                self.textarea.insert(END, f"\n Spices\t\t {self.spices.get()}\t\tRs {self.spices1}")

        # -------------------------------------------------Medicines----------------------------------------------------------

            if self.paracetmol.get() != 0:
                self.textarea.insert(END, f"\n Paracetmol\t\t {self.paracetmol.get()}\t\tRs {self.paracetmol1}")
            if self.antacids.get() != 0:
                self.textarea.insert(END, f"\n Antacids\t\t {self.antacids.get()}\t\tRs {self.antacids1}")
            if self.ointment.get() != 0:
                self.textarea.insert(END, f"\n Ointment\t\t {self.ointment.get()}\t\tRs {self.ointment1}")
            if self.painkiller.get() != 0:
                self.textarea.insert(END, f"\n Painkiller\t\t {self.painkiller.get()}\t\tRs {self.painkiller1}")
            if self.keraboost.get() != 0:
                self.textarea.insert(END, f"\n Keraboost\t\t {self.keraboost.get()}\t\tRs {self.keraboost1}")
            if self.ors.get() != 0:
                self.textarea.insert(END, f"\n Ors\t\t {self.ors.get()}\t\tRs {self.ors1}")

        # ------------------------------------------------------Cosmetics-------------------------------------------------------
            if self.FaceWash.get() != 0:
                self.textarea.insert(END, f"\n FaceWash\t\t {self.FaceWash.get()}\t\tRs {self.FaceWash1}")
            if self.shampoo.get() != 0:
                self.textarea.insert(END, f"\n Shampoo\t\t {self.shampoo.get()}\t\tRs {self.shampoo1}")
            if self.conditioner.get() != 0:
                self.textarea.insert(END, f"\n Conditioner\t\t {self.conditioner.get()}\t\tRs {self.conditioner1}")
            if self.soap.get() != 0:
                self.textarea.insert(END, f"\n soap\t\t {self.soap.get()}\t\tRs {self.soap1}")
            if self.spray.get() != 0:
                self.textarea.insert(END, f"\n Spray\t\t {self.spray.get()}\t\tRs {self.spray1}")
            if self.lotion.get() != 0:
                self.textarea.insert(END, f"\n Lotion\t\t {self.lotion.get()}\t\tRs {self.lotion1}")

            self.textarea.insert(END, f"\n----------------------------------------------")
            if self.GroceryTax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Grocery Tax   \t\t\t\t{self.GroceryTax.get()}")
                
            if self.MedicineTax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Medicine Tax   \t\t\t\t{self.MedicineTax.get()}")
                
            if self.CosmeticTax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Cosmetic Tax   \t\t\t\t{self.CosmeticTax.get()}")   
                
            self.textarea.insert(END, f"\n----------------------------------------------")    
            self.textarea.insert(END, f"\n\t\tTotal Bill :    Rs. {self.Total_Bill}")
            self.Save_Bill()

    def Save_Bill(self):
        option = messagebox.askyesno("SAVE BILL","Do you want to save the BILL?")
        if option>0:
            self.Bill_data = self.textarea.get("1.0", END)
            f7 = open("Bills Folder/"+str(self.BillNo.get())+".txt","w")
            f7.write(self.Bill_data)
            f7.close()
            messagebox.showinfo("SAVED",f"Your Bill Number : {self.BillNo.get()} has been saved Successfully!!")
        else:
            return
        
    def Find_Bill(self):
        Present = "No"
        for x in os.listdir("Bills Folder/"):
            if x.split('.')[0] == self.Search.get():
                f7 = open(f"Bills Folder/{x}","r")
                self.textarea.delete('1.0',END)
                for y in f7:
                    self.textarea.insert(END,y)
                f7.close()
                Present = "Yes"
        if Present == "No":
            messagebox.showerror("ERROR", "Bill Number is Invalid!!")
            
    def Clear(self):
        op = messagebox.askyesno("CLEAR", "Do you really want to Clear the Screen?")
        if op>0:
            self.wheat.set(0)
            self.rice.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            self.oil.set(0)
            self.spices.set(0) 
        # ---------------Medicine----------------------
            self.paracetmol.set(0) 
            self.antacids.set(0)
            self.ointment.set(0)
            self.painkiller.set(0) 
            self.keraboost.set(0) 
            self.ors.set(0) 
        # ---------------Cosmetics---------------------
            self.FaceWash.set(0)
            self.shampoo.set(0)
            self.conditioner.set(0)
            self.soap.set(0)
            self.spray.set(0)
            self.lotion.set(0) 
        # -----Total Product price and tax variables------
            self.TotalGrocery.set("") 
            self.TotalMedicine.set("") 
            self.TotalCosmetics.set("")
        
            self.GroceryTax.set("") 
            self.MedicineTax.set("") 
            self.CosmeticTax.set("") 
        # ------------Customer Details--------------------
            self.CusName.set("") 
            self.CusMobile.set("") 
            self.BillNo.set("") 
            x = random.randint(1000, 9999)
            self.BillNo.set(str(x))

            self.Search.set("")
            self.Welcome_Bill()
        
        
    def Exit(self):
        op = messagebox.askyesno("EXIT", "Do you really want to Exit?")
        if op>0:
            self.root.destroy()
    
root = Tk()

b_obj = Bill_Software(root)
root.mainloop()


# In[ ]:




