#!python3

ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['C','D','H','S']

list=[f"{i}{j}" for i in ranks for j in suits]

print(list)