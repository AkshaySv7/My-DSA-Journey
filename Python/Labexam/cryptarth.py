from itertools import permutations
def solve(word1,word2,word3):
    letter=set(word1+word2+word3)
    if len(letter)>10:
        return []

    for perm in permutations(range(10),len(letter)):
        assigned=dict(zip(letter,perm))
        if any(assigned[word[0]]==0 for word in [word1,word2,result]):
            continue
        
        num1=int(''.join(str(assigned[char]) for char in word1))
        num2=int(''.join(str(assigned[char]) for char in word2))
        num3=int(''.join(str(assigned[char]) for char in result))

        if num1+num2 == num3:
            return [(num1,num2,num3)]

    return []






word1=input("enter the word").strip().lower()
word2=input("enter the word").strip().lower()
result=input("enter the word").strip().lower()

solution= solve(word1,word2,result)

if solution:
    for sol in solution:
        print(f"{sol[0]}+{sol[1]}={sol[2]}")
else:
    print("no solution found")

