def temperature_fahrenheit(int_forecast_fahr):
    if int_forecast_fahr > 68:
        rain = input("Will it rain (yes/no): ")
        if rain == "yes":
            print("Wear jeans and a sweater")
            print("Bring an umbrella!")
        elif rain == "no":
            print("Wear jeans and a T-shirt")
        else:
            print("error")
                

    elif 68 >= int_forecast_fahr > 50:
        rain = input("Will it rain (yes/no): ")
        if rain == "yes":
            print("Wear sweats, a long sleeve, and a hoodie")
            print("Bring an umbrella!")
        elif rain == "no":
            print("Wear jeans, a long sleeve, and a sweater")
        else:
            print("error")
    
    elif 50>= int_forecast_fahr > 41:
        rain = input("Will it rain (yes/no): ")
        if rain == "yes":
            print("Wear sweats, a long sleeve, a hoodie, a jacket, and scarf")
            print("Bring an umbrella!")
        elif rain == "no":
            print("Wear sweats, a long sleeve, a hoodie, and a scarf")
        else:
            print("error")
    else:
        print("Forecast unavaiable.")

def temperature_celsius(int_forecast_cel):
    if int_forecast_cel > 20:
        rain = input("Will it rain (yes/no): ")
        if rain == "yes":
            print("Wear jeans and a sweater")
            print("Bring an umbrella!")
        elif rain == "no":
            print("Wear jeans and a T-shirt")
        else:
            print("error")
                

    elif 20 >= int_forecast_cel > 10:
        rain = input("Will it rain (yes/no): ")
        if rain == "yes":
            print("Wear sweats, a long sleeve, and a hoodie")
            print("Bring an umbrella!")
        elif rain == "no":
            print("Wear jeans, a long sleeve, and a sweater")
        else:
            print("error")
    
    elif 10>= int_forecast_cel > 5:
        rain = input("Will it rain (yes/no): ")
        if rain == "yes":
            print("Wear sweats, a long sleeve, a hoodie, a jacket, and scarf")
            print("Bring an umbrella!")
        elif rain == "no":
            print("Wear sweats, a long sleeve, a hoodie, and a scarf")
        else:
            print("error")
    else:
        print("Forecast unavaiable.")


measurement = input("Would you like to use celsius or fahrenheit? ")

if measurement == "celsius":
    print("What is the weather forecast tommorrow? (in celsius)")
    forecast = input("Temperature: ")
    int_forecast_cel = int(forecast)

elif measurement == "fahrenheit":
    print("What is the weather forecast tommorrow? (in fahrenheit)")
    forecast = input("Temperature: ")
    int_forecast_fahr = int(forecast)
else:
    print("unknown measurement")


if measurement == "celsius":
    temperature_celsius(int_forecast_cel)
elif measurement == "fahrenheit":
    temperature_fahrenheit(int_forecast_fahr)
else:
    print("unavailable")