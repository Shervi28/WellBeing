import os
from tkinter import *
from tkinter import Menu
from tkinter import ttk
import urllib.request
import webbrowser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import  Image,ImageTk
from BotTrain import chatbot_response

def covid():
    root = Tk()
    root.title("CORONAVIRUS (COVID-19) APP")
    root.geometry("450x600")
    '''
    --------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    #for the Advice-O-Bot

    def MenuBar():
        subWin = Toplevel()
        subWin.title("Instructions")
        Label(subWin, text = 'Instructions for the App so the first section covers \n a interface that lets you write the country name for the covid data\n then there is a world map with covid 19 data\n there is also the chatbot who can give you tips and  advice for the covid-19\n remember if you speak nonsense to the chatbot then it\n will also speak with nonsense. Also\n the chatbot can only give you advice and tips on covid-19\n it cant recite data of countries'
        ).pack()
        subWin.mainloop()

    def HelpSection():
        subwin2 = Toplevel()
        subwin2.title("Help")
        Label(subwin2, text= "I do I get safe From Covid 19",font="LUCIDA 15 bold").pack()
        Label(subwin2,text="Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub.\n Maintain at least six feet distance between you and people coughing or sneezing.\n Avoid touching your face. \n Stay home if you feel unwell and always maintain social distancing").pack()
        Label(subwin2,text = "How you you get infected?",font="LUCIDA 15 bold" ).pack()
        Label(subwin2,text = "You can get infected by being in contact with another person.\n The virus spreads by Between people who are in \nclose contact with one another (within about 6 feet),Through \nrespiratory droplets produced when an infected person coughs,\n sneezes, or COVID-19 may be spread by people who are not showing symptoms.").pack()
        subwin2.mainloop()


    def send():
        msg = EntryBox.get("1.0",'end-1c').strip()
        EntryBox.delete("0.0",END)

        if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

            res = chatbot_response(msg)
            ChatLog.insert(END, "Bot: " + res + '\n\n')

            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

    def callback(url):
        webbrowser.open_new(url)
    def covid_data():
        from matplotlib import pyplot as plt
        import matplotlib.patches as mpatches
        from covid import Covid
        import os
        covid = Covid()
        cases = []
        confirmed = []
        active = []
        deaths = []
        recovered = []
        try:
            root.update()
            countries = data.get()
            country_names = countries.strip()
            country_names = country_names.replace(" ", ",")
            country_names = country_names.split(",")
            for x in country_names:
                cases.append(covid.get_status_by_country_name(x))
                print(covid.get_status_by_country_name(x))
                root.update()
            for y in cases:
                confirmed.append(y["confirmed"])
                active.append(y["active"])
                deaths.append(y["deaths"])
                recovered.append(y["recovered"])
            confirmed_patch = mpatches.Patch(color='blue', label='Confirmed')
            recovered_patch = mpatches.Patch(color='green', label='Recovered')
            active_patch = mpatches.Patch(color='red', label='Active')
            deaths_patch = mpatches.Patch(color='black', label='Deaths')
            plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])
            for x in range(len(country_names)):
                plt.bar(country_names[x], confirmed[x], color='blue')
                if recovered[x] > active[x]:
                    plt.bar(country_names[x], recovered[x], color='green')
                    plt.bar(country_names[x], active[x], color='red')
                else:
                    plt.bar(country_names[x], active[x], color='red')
                    plt.bar(country_names[x], recovered[x], color='green')
                plt.bar(country_names[x], deaths[x], color='black')
            plt.title('CURRENT COVID CASES')
            plt.xlabel('COUNTRY NAME')
            plt.ylabel('CASES(in millions)')
            plt.show()
        except Exception as e:
            data.set("Enter the correct details please!")

    '''
    ------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-07-2020.csv'

    df = pd.read_csv(path)
    df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)
    df.rename(columns={'Country_Region': "Country"}, inplace=True)
    world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths'].sum().reset_index()

    figure = px.choropleth(world,locations= "Country", locationmode="country names", color="Confirmed", 
        hover_name="Country", color_continuous_scale="tealgrn", range_color=[1,10000000],title="Countries with Confirmed cases")


    tabControl = ttk.Notebook(root)


    tab2 = ttk.Frame(tabControl)  
    tabControl.add(tab2, text='Covid19 Map')

    tab3 = ttk.Frame(tabControl)
    tabControl.add(tab3,text="Advice-O-Bot")

    tab4 = ttk.Frame(tabControl)
    tabControl.add(tab4,text= "Article Page")

    tab5= ttk.Frame(tabControl)
    tabControl.add(tab5,text='Covid Tracker')

    tabControl.pack(expand=1, fill="both")

    '''
    ----------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    #For the Advice-O-Bot
    ChatLog = Text(tab3, bd=0, bg="white", height="8", width="100", font="Arial",)
    ChatLog.config(state=DISABLED)

    scrollbar = Scrollbar(tab3, command=ChatLog.yview, cursor="heart")
    ChatLog['yscrollcommand'] = scrollbar.set

    SendButton = Button(tab3, font=("Verdana",8,'bold'), text="Send", width="12", height=5,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= send )
    EntryBox = Text(tab3, bd=0, bg="white",width="29", height="5", font="Arial")
    '''
    -----------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    menuBar = Menu(root)
    root.config(menu = menuBar)
    Instructions = Menu(menuBar,tearoff=0)
    Instructions.add_command(label="Instructions",command = MenuBar)
    menuBar.add_cascade(label = 'options',menu = Instructions)
    help = Menu(menuBar,tearoff=0)
    help.add_command(label='Help',command = HelpSection)
    menuBar.add_cascade(label='Covid-19 Help',menu = help)

    '''
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    Label(tab4,text = "Interesting Articles", font = "LUCIDA 15 bold").pack()

    article1 = Label(tab4,text="The Covid-19 Pandemic Accelerates the Transition to Virtual Care",fg="blue", cursor="hand2",font=12)
    article1.pack()
    article1.bind("<Button-1>", lambda e: callback("https://catalyst.nejm.org/doi/full/10.1056/CAT.20.0399"))

    article2 = Label(tab4,text="Connected Communities of Care in Times of Crisis",fg="blue", cursor="hand2",font=12)
    article2.pack()
    article2.bind("<Button-1>", lambda e: callback("https://catalyst.nejm.org/doi/full/10.1056/CAT.20.0361"))

    article3 = Label(tab4,text="Earning Trust in the Era of Covid-19",fg="blue", cursor="hand2",font=12)
    article3.pack()
    article3.bind("<Button-1>", lambda e: callback("https://catalyst.nejm.org/doi/full/10.1056/CAT.20.0459"))

    article4 = Label(tab4,text="Children and the Pandemic: Staying Optimistic",fg="blue", cursor="hand2",font=12)
    article4.pack()
    article4.bind("<Button-1>", lambda e: callback("https://catalyst.nejm.org/doi/full/10.1056/CAT.20.0492"))

    article5 = Label(tab4,text="You Need a Herd for Herd Immunity",fg="blue", cursor="hand2",font=12)
    article5.pack()
    article5.bind("<Button-1>", lambda e: callback("https://catalyst.nejm.org/doi/full/10.1056/CAT.20.0348"))

    article6 = Label(tab4,text="The Value of Value-Based Care, During a Pandemic and Beyond",fg="blue", cursor="hand2",font=12)
    article6.pack()
    article6.bind("<Button-1>", lambda e: callback("https://catalyst.nejm.org/doi/full/10.1056/CAT.20.0475"))

    article7 = Label(tab4,text="The Power and Importance of Leadership in a Crisis",fg="blue", cursor="hand2",font=12)
    article7.pack()
    article7.bind("<Button-1>", lambda e: callback("https://catalyst.nejm.org/doi/full/10.1056/CAT.20.0314"))

    note = Label(tab4, text= "Visit https://catalyst.nejm.org/ for more Articles",fg="blue", cursor="hand2")
    note.place(x = 150, y =530)
    note.bind("<Button-1>", lambda e: callback("https://catalyst.nejm.org"))

    '''
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    '''

    Note = Label(tab3,text = 'Read instructions ')
    Note.place(x=150, y=530)
    data = StringVar()
    link = Label(tab2, text="COVID-19 Map Hyperlink", fg="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e: callback(figure.show()))
    map_img = ImageTk.PhotoImage(Image.open("Map.PNG"))
    map_Label = Label(tab2,image = map_img)
    scrollbar.place(x=376,y=6, height=386)
    ChatLog.place(x=6,y=6, height=386, width=370)
    EntryBox.place(x=128, y=401, height=90, width=265)
    SendButton.place(x=6, y=401, height=90)
    map_Label.pack()
    root.resizable(0,0)
    root.mainloop()
