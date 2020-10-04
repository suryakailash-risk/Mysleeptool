
import streamlit as st
import pandas as pd 
import numpy as np
import time     
from multiprocessing import Process
import os
import signal
import json
import matplotlib as plt

import matplotlib.pyplot as plt
import seaborn as sns
from ibm_watson import VisualRecognitionV3

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
selection=0
selection1=0
selection2=0
selection3=0
selection4=0
selection5=0
selection6=0
selection7=0
selection8=0
selection9=0
sele=0
check=0
yes=0
Id= "test person 1"
exn=False

st.title("My sleep tool💤")
color=st.beta_color_picker("pick the theme", value=None, key=None)
st.write("Enable the check boxes in order under navigator pannel")
st.sidebar.title("Navigator")
#getting  age, height,weight
st.sidebar.subheader("select the tab")
#tab = st.sidebar.selectbox('tab',('BMI','Nutrition','Exercise','sleep'))
if st.sidebar.checkbox('BMR'):
    html_temp= """<div>
    <h1 style="color:{};text-align:center">BMR CALCULATION</h1>
    </div>"""
    st.markdown(html_temp.format(color),unsafe_allow_html=True)
  
    def load_data():
        basic_file=("Howell1.csv")
        df_h = pd.read_csv(basic_file, sep=';')
        M_df = df_h[(df_h['height'] <= 177) & (df_h['weight'] <= 80) & (df_h['age'] >= 25.0) & (df_h['age']<= 40.0) & (df_h['male']==1)]
        F_df = df_h[(df_h['height'] <= 177) & (df_h['weight'] <= 80) & (df_h['age'] >= 25.0) & (df_h['age']<= 40.0) & (df_h['male']==0)]
        M_X = np.array(M_df[:]['height'])
        M_Y = np.array(M_df[:]['weight'])
        M_Z = np.array(M_df[:]['age'])
        F_X = np.array(F_df[:]['height'])
        F_Y = np.array(F_df[:]['weight'])
        F_Z = np.array(F_df[:]['age'])
        #male
        #st.male
        
        BMR_M = (66.47 + (13.75 * M_Y) + (5.003 * M_X) - (6.775 * M_Z)) 
        #BMR = 66.47 + (13.75 x mass) + (5.003 x height) - (6.775 x age)
        #female
     
        BMR_F = (655.1 + (9.563 * F_Y) + (1.850 * F_X) - (4.676 * F_Z))
        #BMR = 655.1 + (9.563 x mass) + (1.850 x height) - (4.676 x age)
        CRM=BMR_M*1.37
        CRF=BMR_F*1.25
        dataframe = pd.DataFrame(df_h),
        columns=('col %d' % i for i in range(20))
        is_check = st.checkbox('Display Data RAW')
        if is_check:
            st.table(df_h)
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">Selected with Nasa Qualified</h1>
        <h4>Formula used</h4>
        <h6 style = "color:#000000;text-align:Left">Height:177  Weight:80 Age:40</h6>
        </div>"""
        st.markdown(html_temp.format(color),unsafe_allow_html=True)

        link = '[Sources](https://www.nasa.gov/audience/forstudents/postsecondary/features/F_Astronaut_Requirements.html)'
        st.markdown(link, unsafe_allow_html=True)
                
        is_check = st.checkbox('Qualified Data')
        if is_check:
            st.write("male")
            st.table(M_df)
            st.write("female")
            st.table(F_df)

            #data =len(M_df)
            #st.write(data) 
            # Show the data as a chart.
            #chart = st.bar_chart(data)
            #data2 = np.array(len(F_df))
        data = [['Male',len(M_df)],['Female',len(F_df)]]
        df_new = pd.DataFrame(data, columns = ['Gender','Number'])
        df_new.set_index('Gender', inplace=True)
            #new_df_new
        st.bar_chart(df_new)
        # Append the new data to the existing chart.
            #chart.add_rows(data2)   
        html_temp= """<div>
        <h4>Formula used</h4>
        <h6 style = "color:#E000FF;text-align:Left">Male: BMR = 66.47 + (13.75 x mass) + (5.003 x height) - (6.775 x age)</h6>
        <h6 style = "color:#E000FF;text-align:Left">Female:BMR = 655.1 + (9.563 x mass) + (1.850 x height) - (4.676 x age)</h6>
        </div>"""
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        link = '[Sources](https://www.nasa.gov/sites/default/files/atoms/files/stemonstrations_nutrition.pdf)'
        st.markdown(link, unsafe_allow_html=True)
        df = pd.DataFrame(list(zip(M_X,M_Y,M_Z,CRM,F_X,F_Y,F_Z,CRF)),columns =['MALE H', 'MALE W','MALE A','MALE CAL','FEMALE H', 'FEMALE W','FEMALE A','FEMALE CAL']) 
        st.write("Calories")
        df 
    load_data()
if st.sidebar.checkbox('Medication'):
    html_temp= """<div>
    <h1 style="color:{};text-align:center">DEFICIENCY</h1>
    </div>"""
    st.markdown(html_temp.format(color),unsafe_allow_html=True)
    st.write("Select only 4 Deficiency and different course")
    want=("select","main", "side dish","Extra","Drinks")
    html_temp= """<div>
    It can take data from the file from the blood test report csv.
    </div>"""
    st.markdown(html_temp.format(color),unsafe_allow_html=True)
    filename = st.text_input(' Enter a file path:(sample:- d:/NASA/new.csv)')
    try:
        with open(filename) as input:
            st.text(input.read())
    except FileNotFoundError:
        st.text('File not found.')

    #vitamin A
    A=st.checkbox('Vitamin A')
    if A==True:
        selection1 = st.selectbox("Select the course",want)
    #vitamin B
    B=st.checkbox('Vitamin B')
    if B==True:
        selection2 = st.selectbox("Select the course ",want)
    #protens
    P=st.checkbox('Protein')
    if P==True:
        selection3 = st.selectbox("Select the course  ",want)
    #calcium
    C=st.checkbox('Calcium')
    if C==True:
        selection4 = st.selectbox("Select the course   ",want)
    #iron ----- no main dish
    I=st.checkbox('Iron')
    if I==True:
        want=("select", "side dish","Extra","Drinks")
        selection5 = st.selectbox("Select the course    ",want)
    #vitamin D
    D=st.checkbox('Vitamin D')
    if D==True:
        selection6 = st.selectbox("Select the course     ",want)
    #vitamin K
    K=st.checkbox('Vitamin K')
    if K==True:
        selection7 = st.selectbox("Select the course      ",want)
    #vitamin c --- no main dish
    VC=st.checkbox('Vitamin C')
    if VC==True:
        want=("Select","side dish","Extra","Drinks")
        selection8 = st.selectbox("Select the course       ",want)
    COFFEE=st.checkbox('Overtime')
    #cafine
    if COFFEE==True:
        want=("Select","Drinks")
        selection9 = st.selectbox("Select the course          ",want)
    Mel=st.checkbox('Melatonin')
    #cafine
    if Mel==True:
        want=("select","Extra")
        sele = st.selectbox("Select the course           ",want)
        st.write(sele)
if st.sidebar.checkbox('Nutrition'):
    exn=True
    link = '[Check with AI](https://node-red-poljp-2020-10-01.eu-gb.mybluemix.net/foodDetails)'
    st.markdown(link, unsafe_allow_html=True)
    link = '[Sources](https://www.nasa.gov/sites/default/files/atoms/files/stemonstrations_nutrition.pdf)'
    st.markdown(link, unsafe_allow_html=True)
    df_C = pd.read_csv("nutrientschart.csv")
    datavitaminD  = ('Mexican Scrambled Eggs','Scrambled Eggs',	'Seafood Gumbo','Seasoned Scrambled Eggs','Shrimp Cocktail','Shrimp Fried Rice','Tomatoes & Eggplant')
    datavitaminK  = ('Asparagus','Butter Cookies','Butterscotch Pudding','Candy Coated Almonds','Cashews','Cauliflower w / Cheese','Cranapple Dessert','Grape Drink','Grape Drink w/ A/S')
    datavitaminC  = ('Applesauce','Vitamin C','Berry Medley','Blueberry Raspberry Yogurt','Candied Yams','Cherry Blueberry Cobbler','Cherry Drink w/ A/S','Chicken Noodle Soup','Citrus Fruit Salad','Cranberry Peach Drink w/ A/S','Creamed Spinach','Dried Peaches','Granola w/ Blueberries','Lemon Curd Cake','Lemon Meringue Pudding','Lemonade','Lemon-Lime Drink','Mashed Potatoes','Peach-Apricot Drink','Pears','Pineapple','Pineapple Drink','Strawberries','Strawberry Drink')
    datavitaminA  =('Apricot Cobbler','Bran Chex','Carrot Coins','Chicken w / Corn & Black Beans','Chicken-Pineapple Salad','Cornbread Dressing','Curry Sauce w/ Vegetables','Fruit Cocktail','Granola','Green Beansw/ Mushrooms','Mango Peach Smoothie','Minestrone Soup','Mixed Vegetables','Pasta w / Pesto Sauce','Pears','Sweet & Sour Chicken','Sweet & Sour Pork','Tomato Basil Soup','Tomatoes & Artichokes','Tomatoes & Eggplant','Tropical Punch','Tuna','Tuna Salad Spread','Vegetarian Vegetable Soup',)
    datavitaminB  = ('Corn','Cornbread Dressing', 'Crackers','Crawfish Etouffee','Decaf. Coffee Black','Granola w/ Raisins','Grilled Pork Chop','Homestyle Potatoes','Homestyle Potatoes','Italian Vegetables','Lasagna with Meat','Milk','Nut & Fruit Granola Bar','Peanuts','Peanut Butter','Potato Medley','Potato Soup','Potatoes au Gratin','Rice Pudding','Salmon','Smoked Turkey','Southwestern Com','Teriyaki Vegetables','Tomatoes & Artichokes','Tropical Fruit Salad','Tropical Punch','Turkey Tetrazzini','Vegetable Quiche','Vegetarian Vegetable Soup','Yogurt Covered Granola Bar')
    dataProtein  = ('Barbecued Beef Brisket','Beef Fajitas','Beef Pattie','Beef Steak','Beef Stew','Beef Tips w/ Mushrooms','Breakfast Sausage Links','Candy Coated Peanuts','Chicken Consomme','Chicken Fajitas','Chicken in Pouches','Chicken w / Corn & Black Beans','Chicken w / Peanut Sauce','Fiesta Chicken','Lasagna with Meat','Macadamia Nuts','Macaroni & Cheese R','Meatloaf','Noodles & Chicken','Pasta w / Shrimp','Rice & Chicken','Sausage Pattie','Split Pea Soup','Sweet & Sour Chicken','Sweet & Sour Pork','Teriyaki Beef Steak','Teriyaki Chicken','Tortillas')
    dataCalcium  = ('Apple Cider','Broccoli au Gratin','Chicken Terivaki','Milk','Rhubarb Applesauce','Rice Pudding','Shortbread Cookies','Waffles')
    dataIron  = ( 'Apple Cider','Baked Beans','Black Beans','Chicken Consomme','Chicken Terivaki','Dried Apricots','Gritsw/ Butter','Red Beans & Rice')
    dataCaffeine  =('Chocolate Breakfast Drink','Cocoa','Decaf. Coffee Black','Decaf. Coffee w / A/S','Decaf. Coffee w/C & A/S','Decaf. Coffeew/ C & S','Decaf. Coffeew/ Cream','Decaf. Coffeew/ Sugar','Green Tea','Kona Coffee Black','Kona Coffee w/ A/S','Kona Coffee w / C & A/S','Kona Coffee w/ Cream','Tea','Tea w/ Cream & Sugar','Tea w/ Lemon & A/S','Tea w / Lemon & Sugar','Tea w/ Sugar','Tea with A/S','Tea with Cream','Tea with Lemon')
    dataMelatonin =('Cherry','Almonds','Banana','Strawberry')
    #main course
    s=("Select","Apricot Cobbler","Barbecued Beef Brisket","Beef Fajitas","Beef Steak","Beef Stew","Beef Tips w/ Mushrooms","Shrimp Fried Rice","Bran Chex","Broccoli au Gratin","Brown Rice","Cheese Grits","Cheese Tortellini","Chicken Fajitas","Chicken Noodle Soup","Chicken Terivaki","Cornflakes","Crawfish Etouffee","Fiesta Chicken","Granola w/ Raisins",
    "Italian Vegetables", "Noodles & Chicken", "Pasta w / Pesto Sauce", "Pasta w / Shrimp","Red Beans & Rice","Rice & Chicken","Rice Pilaf","Seafood Gumbo","Smoked Turkey","Sweet & Sour Pork"
    "Sweet & Sour Chicken","Teriyaki Beef Steak","Teriyaki Chicken","Tomatoes & Artichokes","Tortillas","Tuna","Turkey Tetrazzini","Vegetable Quiche","Wheat Flat Bread")
    if selection1=="main":
        #st.write("hi")
        s=np.intersect1d(datavitaminA,s)
    if selection2=="main":
        #st.write("hi")
        s=np.intersect1d(datavitaminB,s)
    if selection4=="main":
        #st.write("hi")
        s=np.intersect1d(datavitaminD,s)
    if selection5=="main":
        #st.write("hi")
        s=np.intersect1d(datavitaminK,s)
    if selection6=="main":
        #st.write("hi")
        s=np.intersect1d(dataProtein,s)
    if selection7=="main":
        #st.write("hi")
        s=np.intersect1d(dataCalcium,s)
    sel = st.selectbox('Main?',s)
    s1=("Select","Asparagus","Beef Pattie","Blueberry Raspberry Yogurt","Breakfast Sausage Links","Candied Yams","Cauliflower w / Cheese","Chicken in Pouches",
    "Chicken w / Corn & Black Beans	","Chicken w / Peanut Sauce","Citrus Fruit Salad","Corn","Creamed Spinach","Curry Sauce w/ Vegetables","Dried Peaches","Grilled Pork Chop","Homestyle Potatoes",
    "Lasagna with Meat","Macaroni & Cheese R","Mashed Potatoes","Meatloaf","Mixed Vegetables","Peaches","Peanut Butter","Pears","Peanuts","Potato Medley","Potatoes au Gratin","Rhubarb Applesauce",
    "Salmon	","Sausage Pattie","Scrambled Eggs	","Seasoned Scrambled Eggs	","Southwestern Com","Teriyaki Vegetables","Tuna Salad Spread")
    #side dish
    if selection1=="side dish":
        s1=np.intersect1d(datavitaminA,s1)
    if selection2=="side dish":
        s1=np.intersect1d(datavitaminB,s1)
    if selection3=="side dish":
        s1=np.intersect1d(datavitaminC,s1)
    if selection4=="side dish":
        s1=np.intersect1d(datavitaminD,s1)
    if selection5=="side dish":
        s1=np.intersect1d(datavitaminK,s1)
    if selection6=="side dish":
        s1=np.intersect1d(dataProtein,s1)
    if selection7=="side dish":
        s1=np.intersect1d(dataCalcium,s1)
    if selection8=="side dish":
        s1=np.intersect1d(dataIron,s1)
    sel1 = st.selectbox("side dish",s1)
    s2=("Select","Baked Beans","Banana Pudding","Berry Medley","Black Beans","Bread Pudding","Brownie","Butter Cookies","Butterscotch Pudding",
    "Candy Coated Chocolates","Candy Coated Peanuts","Carrot Coins","Cashews","Cheddar Cheese Spread","Cherry Blueberry Cobbler","Chicken-Pineapple Salad","Chipotle Snack Bread",
    "Cocoa","Cornbread Dressing","Crackers","Cranapple Dessert","Dried Apricots","Granola Bar","Granola w/ Blueberries","Grape Jelly","Gritsw/ Butter","Lemon Curd Cake","Lemon Meringue Pudding",
    "Macadamia Nuts","Nut & Fruit Granola Bar","Peanuts","Rice Pudding","Shortbread Cookies","Strawberries","Tropical Fruit Salad","Vanilla Pudding","Waffles","Yogurt Covered Granola Bar	" )
    #if sele=="Extra":
    #    s2 =('Cherry','Almonds','Banana','Strawberry')
    #extras    
    if selection1=="Extra":
        s2=np.intersect1d(datavitaminA,s2)
    if selection2=="Extra":
        s2=np.intersect1d(datavitaminB,s2)
    if selection3=="Extra":
        s2=np.intersect1d(datavitaminC,s2)
    if selection4=="Extra":
        s2=np.intersect1d(datavitaminD,s2)
    if selection5=="Extra":
        s2=np.intersect1d(datavitaminK,s2)
    if selection6=="Extra":
        s2=np.intersect1d(dataProtein,s2)
    if selection7=="Extra":
        s2=np.intersect1d(dataCalcium,s2)
    if selection8=="Extra":
        s2=np.intersect1d(dataIron,s2)
    if sele=="Extra":
       # st.write("hi")
        s2=dataMelatonin
        
    sel2 = st.selectbox("Extras",s2)
    s3=("Select","Cherry Drink w/ A/S","Chicken Consomme","Chocolate Breakfast Drink","Chocolate Pudding","Cranberry Peach Drink w/ A/S","Decaf. Coffee Black",
    "Decaf. Coffee w / A/S","Decaf. Coffee w/C & A/S","Decaf. Coffeew/ C & S","Decaf. Coffeew/ Cream","Decaf. Coffeew/ Sugar","Fruit Cocktail","Grape Drink","Green Tea","Green Tea w/ Sugar",
    "Hot and Sour Soup","Lemonade","Lemon-Lime Drink","Milk","Minestrone Soup","Orange Drink","Orange Drink w / A/S","Orange Juice","Orange-Grapefruit Drink","Orange-Mango Drink",
    "Orange-Pineapple Drink	","Peach-Apricot Drink","Potato Soup","Shrimp Cocktail","Split Pea Soup","Strawberry Drink","Tomato Basil Soup","Tropical Punch",
    "Tropical Punch w/ A/S","Vanilla Breakfast Drink","Vegetarian Vegetable Soup")
    #drinks
    if selection1=="Drinks":
        s3=np.intersect1d(datavitaminA,s3)
    if selection2=="Drinks":
        s3=np.intersect1d(datavitaminB,s3)
    if selection3=="Drinks":
        s3=np.intersect1d(datavitaminC,s3)
    if selection4=="Drinks":
        s3=np.intersect1d(datavitaminD,s3)
    if selection5=="Drinks":
        s3=np.intersect1d(datavitaminK,s3)
    if selection6=="Drinks":
        s3=np.intersect1d(dataProtein,s3)
    if selection7=="Drinks":
        s3=np.intersect1d(dataCalcium,s3)
    if selection8=="Drinks":
        s3=np.intersect1d(dataIron,s3)
    if selection9=="Drinks":
        s3=np.intersect1d(dataCaffeine,s3)
    sel3 = st.selectbox("Drinks",s3)
    
    #st.write('You selected:', selection,selection1,selection2,selection3)
    df = pd.read_csv("food.csv")
    lis = [sel,sel1,sel2,sel3] # you can add any number of products here
    sel_df = df.loc[df['Product Name'].isin(lis)] 
    sel_dict = sel_df.sum().to_dict()
    
    cal=sel_dict['Kcals']
    pro=sel_dict["Pro"]
    fat=sel_dict["Fat"]
    cho=sel_dict['CHO']
    if sel_dict['Kcals'] != 0:
        st.dataframe(sel_df)
        labels = 'Calories', 'Protein', 'Fats', 'carbohydrates'
        sizes = [cal, pro, fat, cho]
        explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')	
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        is_check = st.checkbox('Data')
        if is_check:
            st.write(sel_dict)
        if sel_dict['Kcals'] >= 500:
            st.write("You must do workout Plan 2")
        else:
            st.write("you must do workout Plan 1")
        if ((sel_dict['Kcals'] >= 633 and sel_dict['Kcals'] <= 1066) and (sel_dict["Pro"] >= 20 and sel_dict['Pro'] <= 25) and (sel_dict["Fat"] <= 22) and (sel_dict['CHO'] >= 90 and sel_dict['CHO'] <= 92)):
            check=True
if st.sidebar.checkbox('Exercise'):
    manual = False
    if exn==False:
        st.write("NOTE: if it shows any error NOT DEFINED please enable the Nurtririon in the navigator")
    if sel_dict['Kcals'] <= 500:
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">EXERCISE</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        
        link = '[Sources](https://www.nasa.gov/sites/default/files/atoms/files/stemonstrations_nutrition.pdf)'
        st.markdown(link, unsafe_allow_html=True)
        st.subheader('')
        
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">Lets Do Workout PLAN 1</h1>
        <h6>With Respect to Food consumed Workout plan is made</h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        #waliking
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">WALKING : 10mins</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        st.image("walking.png", width=50)
        html_temp= """
        <div>
        <h6 style="color:#000000;text-align:center">Timer</h6>
        <h6 style="text-align:center"><b>Note</b>:The below line will work with repect to heartbeat and ecg reading given by star watch </h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        progress_bar = st.progress(0)
        #add the slide bar for manual mode
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.001)
        walkingcal=5*10
        st.write("Total calories burned",walkingcal)
        #running
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">RUNNING : 35mins</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        st.image("running.png", width=50)
        html_temp= """
        <div>
        <h6 style="color:#000000;text-align:center">Timer</h6>
        <h6 style="text-align:center"><b>Note</b>:The below line will work with repect to heartbeat and ecg reading given by star watch </h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        progress_bar = st.progress(0)
        #add the slide bar for manual mode
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.001)
        runcal=8*35
        st.write("Total calories burned",runcal)
        
        #cycling
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">CYCLING : 15mins</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        st.image("cycleing.png", width=50)
        html_temp= """
        <div>
        <h6 style="color:#000000;text-align:center">Timer</h6>
        <h6 style="text-align:center"><b>Note</b>:The below line will work with repect to heartbeat and ecg reading given by star watch </h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        progress_bar = st.progress(0)
        #add the slide bar for manual mode
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.001)
        cyccal=5*15
        st.write("Total calories burned",cyccal)
        #RTM
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">ARED : 60mins</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        st.image("machine.png", width=50)
        html_temp= """
        <div>
        <h6 style="color:#000000;text-align:center">Timer</h6>
        <h6 style="text-align:center"><b>Note</b>:The below line will work with repect to heartbeat and ecg reading given by star watch </h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        progress_bar = st.progress(0)
        #add the slide bar for manual mode
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.001)
        mcal=4*60
        st.write("Total calories burned",mcal)
        
        html_temp= """
        <div>
        <h6 style="color:#000000">Total calories with the workout is</h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        total=mcal+cyccal+runcal+walkingcal
        info_ph = st.empty()
        info_ph.info(total)
    if sel_dict['Kcals'] >= 500:
        link = '[Sources](https://www.nasa.gov/sites/default/files/atoms/files/stemonstrations_nutrition.pdf)'
        st.markdown(link, unsafe_allow_html=True)
        st.subheader('With Respect to Food consumed Workout plan is made')
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">Lets Do Workout PLAN 2</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        #waliking
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">WALKING : 15mins</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        st.image("walking.png", width=50)
        html_temp= """
        <div>
        <h6 style="color:#000000;text-align:center">Timer</h6>
        <h6 style="text-align:center"><b>Note</b>:The below line will work with repect to heartbeat and ecg reading given by star watch </h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True) 
        progress_bar = st.progress(0)
        #add the slide bar for manual mode
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.001)
        walkingcal=5*15
        st.write("Total calories burned",walkingcal)
        #running
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">RUNNING : 45mins</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        st.image("running.png", width=50)
        html_temp= """
        <div>
        <h6 style="color:#000000;text-align:center">Timer</h6>
        <h6 style="text-align:center"><b>Note</b>:The below line will work with repect to heartbeat and ecg reading given by star watch </h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        progress_bar = st.progress(0)
        #add the slide bar for manual mode
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.001)
        runcal=8*45
        st.write("Total calories burned",runcal)
        #cycling
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">CYCLING : 30 mins</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        st.image("cycleing.png", width=50)
        html_temp= """
        <div>
        <h6 style="color:#000000;text-align:center">Timer</h6>
        <h6 style="text-align:center"><b>Note</b>:The below line will work with repect to heartbeat and ecg reading given by star watch </h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        progress_bar = st.progress(0)
        #add the slide bar for manual mode
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.001)
        cyccal=5*30
        st.write("Total calories burned",cyccal)
        #RTM
        html_temp= """
        <div>
        <h1 style="color:{};text-align:center">ARED : 60mins</h1>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        st.image("machine.png", width=50)
        html_temp= """
        <div>
        <h6 style="color:#000000;text-align:center">Timer</h6>
        <h6 style="text-align:center"><b>Note</b>:The below line will work with repect to heartbeat and ecg reading given by star watch </h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        progress_bar = st.progress(0)
        #add the slide bar for manual mode
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.001)        
        mcal=4*60
        st.write("Total calories burned",mcal)

        html_temp= """
        <div>
        <h6 style="color:#000000">Total calories with the workout is</h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        info_ph = st.empty()
        total=mcal+cyccal+runcal+walkingcal
        info_ph.info(total)
if st.sidebar.checkbox('Environment Factors'):
    link = '[Sources](https://www.nasa.gov/mission_pages/station/research/circadian)'
    st.markdown(link, unsafe_allow_html=True)
    link = '[Sources](https://spinoff.nasa.gov/Spinoff2015/hm_2.html)'
    st.markdown(link, unsafe_allow_html=True)
    html_temp= """<div>
    <h1 style="color:{};text-align:center">BLUE LIGHT</h1>
    </div>"""
    st.markdown(html_temp.format(color),unsafe_allow_html=True)
    st.write("Blue light Controler")
    yes=st.checkbox("Yes ")
    if yes==True:
        slider_ph = st.empty()
        info_ph = st.empty()
        value = slider_ph.slider("slider", 0, 100)
        st.write("Light Intensity")
        info_ph.info(value)

        
    html_temp= """<div>
    <h1 style="color:{};text-align:center">CIRCADIAN RHYTHM</h1>
    </div>"""
    st.markdown(html_temp.format(color),unsafe_allow_html=True)
    st.image("CircadianRhythm.png", width=200)
    st.write("Is your circadian Rhythm misalined?")
    yes=st.checkbox("Yes")
    if yes==True:
        html_temp= """
        <div>

        Music To sleep
        
        Drug: Zolpidem
        
        <h6>*incase of emergency</h6>
        <h6 style="color:#ff0000"> your work is rescheduled<h6>
        <h6> your removed from all the work till they recover due to circadian Rhythm misalined<h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
        st.write("Id:-",Id)
if st.sidebar.checkbox('Sleep'):
    html_temp= """
    <div>
    <h1 style="color:{};text-align:center">SLEEP</h1>
    </div> 
    """
    st.markdown(html_temp.format(color),unsafe_allow_html=True)
    link = '[Sources](https://humanresearchroadmap.nasa.gov/Evidence/reports/Sleep.pdf)'
    st.markdown(link, unsafe_allow_html=True)
    #st.write("requires 6.5")
    html_temp= """
    <div>
    <h6 style="color:{};text-align:center">Sleep required per day is : 6.5hrs</h6>
    </div> 
    """
    st.markdown(html_temp.format(color),unsafe_allow_html=True)
    
    link = '[Sources](https://lsda.jsc.nasa.gov/Dataset/dataset_detail_result/J0001204)'
    st.markdown(link, unsafe_allow_html=True)
    link = '[Sources](https://lsda.jsc.nasa.gov/Dataset/dataset_detail_result/3.1.1__2630758615)'
    st.markdown(link, unsafe_allow_html=True)
    df=pd.read_csv("new.csv")
    if st.checkbox('Sleep Difference comparison Per and In mission with everyone'):
        revenue_df   = df.drop('In Mission', axis=1)\
                        .rename(columns={'Pre Mission': 'Value'})\
                        .merge(pd.DataFrame(
                            {'Category': list(pd.np.repeat('Pre Mission', len(df)))}),
                            left_index=True,
                            right_index=True)

        total_income_df = df.drop('Pre Mission', axis=1)\
                            .rename(columns={'In Mission': 'Value'})\
                            .merge(pd.DataFrame(
                            {'Category': list(pd.np.repeat('In Mission', len(df)))}),
                            left_index=True,
                            right_index=True)
        df_revised = pd.concat([revenue_df, total_income_df])
     # Display original df and grouped bar chart
        sns.barplot(x="Subject", y="Value", hue="Category", data=df_revised)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    if st.checkbox('Sleep Efficiency Difference comparison Per and In mission with everyone'):
        df=pd.read_csv("new.csv")
        revenue_df   = df.drop('In-Efficiency', axis=1)\
                        .rename(columns={'Pre-Efficiency': 'Value'})\
                        .merge(pd.DataFrame(
                            {'Category': list(pd.np.repeat('Pre-Efficiency', len(df)))}),
                            left_index=True,
                            right_index=True)

        total_income_df = df.drop('Pre-Efficiency', axis=1)\
                            .rename(columns={'In-Efficiency': 'Value'})\
                            .merge(pd.DataFrame(
                                {'Category': list(pd.np.repeat('In-Efficiency', len(df)))}),
                                left_index=True,
                                right_index=True)
        df_revised = pd.concat([revenue_df, total_income_df])
        sns.barplot(x="Subject", y="Value", hue="Category", data=df_revised)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    if st.checkbox('REM Difference comparison Per and In mission with everyone'):
        df=pd.read_csv("new.csv")
        revenue_df1   = df.drop('Number of wakens(in)', axis=1)\
                        .rename(columns={'Number of Wakens(Pre)': 'Value'})\
                        .merge(pd.DataFrame(
                            {'Category': list(pd.np.repeat('Number of Wakens(Pre)', len(df)))}),
                            left_index=True,
                            right_index=True)
        total_income_df1 = df.drop('Number of Wakens(Pre)', axis=1)\
                            .rename(columns={'Number of wakens(in)': 'Value'})\
                            .merge(pd.DataFrame(
                                {'Category': list(pd.np.repeat('Number of wakens(in)', len(df)))}),
                                left_index=True,
                                right_index=True)
        df_revised = pd.concat([revenue_df1, total_income_df1])
        sns.barplot(x="Subject", y="Value", hue="Category", data=df_revised)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    if st.checkbox('Effect of Illumination (Lights) Difference comparison Per and In mission with everyone'):
        df=pd.read_csv("new.csv")
        revenue_df   = df.drop('Illumination(In)', axis=1)\
                        .rename(columns={'Illumination(Pre)': 'Value'})\
                        .merge(pd.DataFrame(
                            {'Category': list(pd.np.repeat('Illumination(Pre)', len(df)))}),
                            left_index=True,
                            right_index=True)

        total_income_df = df.drop('Illumination(Pre)', axis=1)\
                            .rename(columns={'Illumination(In)': 'Value'})\
                            .merge(pd.DataFrame(
                                {'Category': list(pd.np.repeat('Illumination(In)', len(df)))}),
                                left_index=True,
                                right_index=True)
        df_revised = pd.concat([revenue_df, total_income_df])
        sns.barplot(x="Subject", y="Value", hue="Category", data=df_revised)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    if st.checkbox('Effect of Sleep latency Difference comparison Per and In mission with everyone'):
        df=pd.read_csv("new.csv")
        revenue_df   = df.drop('Sleep latency(In)', axis=1)\
                        .rename(columns={'Sleep latency(Pre)': 'Value'})\
                        .merge(pd.DataFrame(
                            {'Category': list(pd.np.repeat('Sleep latency(Pre)', len(df)))}),
                            left_index=True,
                            right_index=True)

        total_income_df = df.drop('Sleep latency(Pre)', axis=1)\
                            .rename(columns={'Sleep latency(In)': 'Value'})\
                            .merge(pd.DataFrame(
                                {'Category': list(pd.np.repeat('Sleep latency(In)', len(df)))}),
                                left_index=True,
                                right_index=True)
        df_revised = pd.concat([revenue_df, total_income_df])
        sns.barplot(x="Subject", y="Value", hue="Category", data=df_revised)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    if st.button('Todays Work plan'):
        df=pd.read_csv("new.csv")
        hi=df["In Mission"]
        result1=(df.loc[df["In Mission"].argmax()]['Subject'])
        result2=(df.loc[df["In Mission"].argmin()]['Subject'])
        result3=(df[df["In Mission"] == 6.00]["Subject"][0])
        st.write(result1," Can work  in replacement to", result2)    
        st.write(result2," Need to take rest for good health.")
        html_temp= """
        <div>
        <h6 style="color:#FF0000">Warning this may lead to decrease in your performance</h6>
        </div> 
        """
        st.markdown(html_temp.format(color),unsafe_allow_html=True)
