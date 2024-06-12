signal = []
filter = []

def convolution(signal, filter):
    result = [0] * (len(signal) + len(filter) - 1)
    
    for i in range(len(signal)):
        for j in range(len(filter)):
            result[i + j] += signal[i] * filter[j]
    
    return result

signal_len = input("لطفا طول سیگنال را وارد کنید ")

for i in range(0, int(signal_len)):
    signal.append(int(input(f"{i+1} امین عضو سیگنال را وارد کنید :")))

filter_len = input("لطفا طول فیلتر را وارد کنید")

for i in range(0, int(filter_len)):
    filter.append(int(input(f"{i+1} امین عضو فیلتر را وارد کنید :")))

res = convolution(signal, filter)
print("Convolution Result:", res)


with open("1", "w") as file:
    file.write(f"{res}\n")
