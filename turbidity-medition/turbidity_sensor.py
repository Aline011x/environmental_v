
def read_sensor():
    # Reading sensor value (Be could analogic or digital)
    # Example:
    sensor_value = 750  # Change this for the real value that sensor readed
    return sensor_value

def convert_to_turbidity(sensor_value):
    #Read calibration values where since the file 
    calibration_data = {}
    with open('calibration_data.txt', 'r') as file:
        for line in file:
            turbidity, value = line.strip().split(',')
            calibration_data[int(value)] = int(turbidity)
    
    # Found turbidity value that coincide sensor value 
    turbidity = calibration_data.get(sensor_value)
    if turbidity is None:
        # if exact value is not in the calibration, perform a linear interpolation 
        
        sorted_values = sorted(calibration_data.keys())
        for i in range(len(sorted_values) - 1):
            if sorted_values[i] <= sensor_value <= sorted_values[i + 1]:
                turbidity = ((sensor_value - sorted_values[i]) * calibration_data[sorted_values[i + 1]] +
                             (sorted_values[i + 1] - sensor_value) * calibration_data[sorted_values[i]]) / \
                            (sorted_values[i + 1] - sorted_values[i])
                break
    
    return turbidity

if __name__ == "__main__":
    sensor_value = read_sensor()
    turbidity = convert_to_turbidity(sensor_value)
    print(f"Turbidez del agua: {turbidity}")
