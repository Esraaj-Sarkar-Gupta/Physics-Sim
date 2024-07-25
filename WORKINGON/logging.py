import time

T = time.localtime()

filename = f"Logs/Logs_{T[7]}_{T[3]}-{T[4]}-{T[5]}.txt"

def log(text):
    with open(filename , 'a') as file:
        file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n")

def log_display(text):
    with open(filename  , 'a') as file:
        file.write(f"\n (Disp) {T[7]} - {T[3]}:{T[4]}:{T[5]} > {text} \n")
    print(f"{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text}")
    
def initial_log():
    pass

