# Week 1.2, Session 2: Task 6
temperature = int(input("Enter the machine's temperature in degrees Celsius: "))
pressure = int(input("Enter the machine's pressure in PSI: "))
operational = int(input("Enter 1 if operating or 0 if stopped: "))

if temperature > 80:
	print("Temperature is too high. Shut down the machine.")
elif temperature >= 50:
	print("Temperature is within safe limits.")
else:
	print("Machine temperature is low. No action is needed.")

if pressure > 100:
	print("High pressure detected. Maintenance is recommended.")
elif pressure >= 70:
	print("Pressure is stable.")
else:
	print("Pressure is low. The system is operating normally.")

if operational == 1:
	if temperature > 80 or pressure > 100:
		print("The machine is running in unsafe conditions. Shut it down.")
	else:
		print("The machine is running normally.")
else:
	print("The machine is stopped. No immediate action is needed.")

