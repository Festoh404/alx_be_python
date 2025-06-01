weather = input("WHat's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    recommendation = "Don't forget your umbrella and a raincoat."
    print(recommendation)
elif weather == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."
    print(recommendation)
else:
    print("Sorry, I don't have recommendations for this weather.")