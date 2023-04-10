measurement_parameter = ["External Inputs", "External Inquiries", "External Outputs",
                          "External Interfaces", "Internal Files"]

j = 0

count_total = 0

for i in measurement_parameter:
    measurement_parameter1 = int(input(f"{measurement_parameter[j]}: "))

    if measurement_parameter[j] == "External Inputs" :
        weighing_factor = {"low":3,"average":4,"high":6}
        input_weight = input("Choose Weight Scale [low/average/high]: ")
        measurement_parameter_weight = measurement_parameter1 * weighing_factor[input_weight]
        count_total += measurement_parameter_weight
        #print(measurement_parameter_weight)

    elif measurement_parameter[j] == "External Inquiries":
        weighing_factor = {"low":3,"average":4,"high":6}
        input_weight = input("Choose Weight Scale [low/average/high]: ")
        measurement_parameter_weight = measurement_parameter1 * weighing_factor[input_weight]
        count_total += measurement_parameter_weight
        #print(measurement_parameter_weight)

    elif measurement_parameter[j] == "External Outputs":
        weighing_factor = {"low":4,"average":5,"high":7}
        input_weight = input("Choose Weight Scale [low/average/high]: ")
        measurement_parameter_weight = measurement_parameter1 * weighing_factor[input_weight]
        count_total += measurement_parameter_weight
        #print(measurement_parameter_weight)

    elif measurement_parameter[j] == "External Interfaces":
        weighing_factor = {"low":5,"average":7,"high":10}
        input_weight = input("Choose Weight Scale [low/average/high]: ")
        measurement_parameter_weight = measurement_parameter1 * weighing_factor[input_weight]
        count_total += measurement_parameter_weight
        #print(measurement_parameter_weight)

    elif measurement_parameter[j] == "Internal Files":
        weighing_factor = {"low":7,"average":10,"high":15}
        input_weight = input("Choose Weight Scale [low/average/high]: ")
        measurement_parameter_weight = measurement_parameter1 * weighing_factor[input_weight]
        count_total += measurement_parameter_weight
        #print(measurement_parameter_weight)
    
    j += 1

sum_complexity_factors = int(input("What is the sum of complexity factors? "))

complexity_adjustment_factor = 0.65 + (0.01*sum_complexity_factors)

function_point = complexity_adjustment_factor * count_total

print(f"\n\nWith the equation (function point = complexity adjustment factor * count total) \n{function_point}")
        