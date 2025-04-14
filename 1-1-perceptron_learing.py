def compute_output(w, x, bias):
    # z = 0.0
    z = bias
    for i in range(len(w)):
        z += x[i] * w[i]
    if z < 0:
        return -1
    else:
        return 1
    
w_input = input("Please enter the weights(Separate with commas, for example 0.5, -0.6) :")
x_input = input("Please enter the inputs(Separate with commas, for example 2, 1) :")
bias_input = input("Please enter the bias(For example 0.9) :")

w = [float(num) for num in w_input.split(',')]
x = [float(num) for num in x_input.split(',')]
bias = float(bias_input)

output = compute_output(w, x, bias)
print(f"Perceptron output:{output}")

