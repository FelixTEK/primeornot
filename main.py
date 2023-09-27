#FELIXTEK2023
def primeornot(): #Function to find prime number
    
    number =  int(input("Insert desired number>"))
    for i in range (2,number - 1):
        if number % i == 0:
            print("This number isn't prime.")
            break
        else:
            i = i + 1
    if i == number - 1:
        print("This number is prime.")        
            
if __name__ == "__main__": #Main function
    primeornot()