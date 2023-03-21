import turtle
import pandas

screen = turtle.Screen()
screen.title("40 Europe Country")
image = "Blank_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Europe all countries")
country_names = data["Country"].tolist()
guessed_country = []


while len(guessed_country) < 40:
    answer = screen.textinput(f"{len(guessed_country)}/40 Countries correct", "Find the country?").title()
    if answer in country_names:
        guessed_country.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        data_cor = data[data.Country == answer] #Taking Row in CSV
        t.goto(int(data_cor.xcor), int(data_cor.ycor))
        t.write(answer)

    if answer == "Exit":
        missing_countries = [i for i in country_names if i not in guessed_country] # list Comprehensions For Schleife vereinfachen
        print(f"These country are missing: {missing_countries}")
        print(f"These country are found: {guessed_country}")
        break

#Erstelle eine CSV mit einem Dict
'''dict_list = {
    "Country": ["Finland", "Sweden", "Norway", "Estonia",
                "Latvia", "Lithuania","Denmark", "Iceland",
                "Ireland","Netherlands","Germany","Poland",
                "Slovakia","Czechia","Belgium","Luxembourg",
                "France","Switzerland","Austria","Hungary",
                "Romania","Italy","Portugal","Spain",
                "Slovenia","Croatia","Bulgaria","Greece",
                "North Macedonia","Albania","Kosovo",
                "Serbia","Bosnia","Malta","Montenegro",
                "Belarus","Russia","Monaco","Liechtenstein",
                "San marino","Holy see"],
    "xcor": ["59","10","-44","64",
             "72","58","-41","-182",
             "-166","-71","-30","37",
             "59","10","-79","-66",
             "-97","-52","3","43",
             "97","-14","-206","-154",
             "6","25","93","81",
             "76","57","66","69",
             "34","10","50","102",
             "172","-62","-39","-14",
             "-10"],
    "ycor": ["83","94","75","41","14","-7","-3","137","-24","-48","-59","-45","-84","-78","-69","-81","-104","-116",
             "-109","-111","-115","-168","-177","-188","-125",
    "-130","-153","-207","-174","-189","-163","-146","-146","-252","-162","-21","37","-156","-113","-153","-182"]
}
dl = pandas.DataFrame(dict_list)
dl.to_csv("Europe all countries")'''





