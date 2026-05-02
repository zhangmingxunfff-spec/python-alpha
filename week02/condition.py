tempareture = range(26, 30)

humidity = range(70-100)

status = ["Normal", "Alert", "Alarm"]

tempareture = int(input("Please enter your tempareture: "))
humidity = int(input("Please enter your humidityไ   : "))

# Status Normal = temp > 32 and hum < 70%
print()

# Status Alert = temp >= 31, 32 and hum >= 65, 66, 67, 68, 69, 70
print()

# status Alarm = temp >= 26 to 30 and hum >=70 to 100
print()