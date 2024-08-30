def main():
    letters = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,
           "S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
    print()
    print("====CEASER CIPHER PROGRAM====")
    def input_value():
        message = input("Enter a message: ").upper().replace(" ", "")
        
        for letter in message:
        #print(letter,": ", letters[letter])
                sum = (letters[letter]+3)%26
                #print(sum,": ", letters[sum])
                key = None
                for k, v in letters.items():
                    if v == sum:
                        key = k
                        break
                print(key, end="") 
        print("") 
                
                
    #input_value()


    def decryption():
        message = input("Enter a message: ").upper().replace(" ", "")
        
        for letter in message:
        #print(letter,": ", letters[letter])
                sum = (letters[letter]-3)%26
                #print(sum,": ", letters[sum])
                key = None
                for k, v in letters.items():
                    if v == sum:
                        key = k
                        break
                print(key, end="")  
        print("")

                
                
    #decryption()
    x = True
    while x:
        choice = input("Encryption, Decryption or Quit: ").upper()
        if choice == "ENCRYPTION":
              input_value()
        elif choice == "DECRYPTION":
              decryption()
        elif choice == "QUIT":
              print("Exiting")
              x = False
        else:
             print("Error")      
if __name__=='__main__':
  main()
