drinks = ['apple','orange','grape']
x = 15.5
y = 20
z = 10.25
total_volume = x + y + z
print('The total volume sold:',total_volume)
# Convert the total volume to an integer
total_volume_int = int(total_volume)
print('Convert the total volume to an integer:',total_volume_int)
# Convert the total volume to a string
total_volume_str = str(total_volume)
print('Convert the total volume to a string:',total_volume_str)
import random
final_total = total_volume + random.randrange(5,10)
print('The final total:',final_total)
