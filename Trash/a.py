#!/usr/bin/python3

args = 'Place city_id="001" user_id="01" name='Mt_little_home'
if not args:
    print("** class name missing **")

# Split the arguments into class name and parameters
args_list = args.split()
class_name = args_list[0]

# Extract parameters
params = {}
for arg in args_list[1:]:
    # Split the argument into key-value pair
    key_val = arg.split('=')
    if len(key_val) != 2:
        continue  # Skip invalid parameter format

    # Extract key and value
    key = key_val[0]
    value = key_val[1]

    # Remove quotes and replace underscores with spaces in value
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1].replace('_', ' ')
        value = value.replace('\\"', '"')  # Unescape quotes

    # Add key-value pair to parameters dictionary
    params[key] = value
print(params)
