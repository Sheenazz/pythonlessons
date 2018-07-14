def convertFahrenheitsToCelsius(fahrenheit):
  return fahrenheit-32 * 5.0 / 9.0

Fahrenheit = int(input("Enter..."))

Celsius = convertFahrenheitsToCelsius(Fahrenheit)

print(Fahrenheit, "Fahrenheit", Celsius, "Celsius")

def reverseString(string):
  print("Reverse string", string[::-1])

reverseString("test")
# print("Reverse string", reverseString("test"))