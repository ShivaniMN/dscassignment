thriller = ["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Rayn"]
comedy = ["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]
print('Enter the string')
string = input()
if string in thriller:
    print('It is a thriller')
elif string in comedy:
    print('It is a comedy')
else:
    print('Its neither comedy nor of thriller genre')
