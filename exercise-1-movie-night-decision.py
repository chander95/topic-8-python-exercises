# write a python program that:
# 1. Asks the user about the day's temperature in Celsius
# 2. Asks the user about the type of event they are attending (casual/formal)
# 3. Determines the outfit based on the above criteria
# 4. Displays the recommended outfit to the user 
# hint: Use nested if statements to determine the outfit based on the day's temperature 
# and the type of event. 

#Recommendation criteria:
#happy + sunny = comedy
#happy + not sunny = romance
#sad = drama
#anything else = adventure


temp = int(input("What's the weather outside today? Please enter a number in Celsius "))
mood = input("What's your current mood? ")
event = input("Is this a casual or formal event? ")

def movie_recommendation():

    weather = "sunny" if temp >= 21 else "not sunny"
    #print(weather)


    def outfit():
        if event == "formal":
            if weather == "sunny":
                print("It will be a warm day today. Wear something light but high-class like a light brown or salmon colored suit.")
            else:
                print("It will be a chilly day today. Make sure to wear a full coat over your suit.")
                #print("It will be a warm day today. You should wear shorts and a t-shirt.")
        elif event == "casual":
            if weather == "sunny":
                print("It will be a warm day today. You should wear shorts and a t-shirt.")
                #print("It will be a chilly day today. Make sure to wear a full coat over your suit.")
            else:
                print("It will be a chilly day today. Wear some sweatpants and a hoodie over your long sleeve shirt.")


    outfit()

    def movie_recommendation():
        if mood == "happy" and weather == "sunny":
            print("Since you are happy and it's a sunny day, I recommend a comedy movie.")
        elif mood == "happy" and weather == "not sunny":
            print("Since your are happy but it's gloomy outside, I recommend a romance movie.")
        elif mood == "sad":
            print("Since you're sad, I recommend a drama.")
        else:
            print("I recommend an action movie.")
        
    
    movie_recommendation()


movie_recommendation()