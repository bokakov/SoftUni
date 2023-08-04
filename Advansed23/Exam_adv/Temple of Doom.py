def solve_temple_challenge_nc(tools, substances, challenges):
    while len(challenges) > 0:
        tool = tools[0]
        substance = substances[-1]
        result = tool * substance

        if result in challenges:
            challenges.remove(result)
            tools.pop(0)
            substances.pop()
        else:
            tools.append(tools.pop(0) + 1)
            substances[-1] -= 1
            if substances[-1] == 0:
                substances.pop()

        if len(substances) == 0:
            print("Harry is lost in the temple. Oblivion awaits him.")
            return

    print("Harry found an ostracon, which is dated to the 6th century BCE.")

tools_nc = list(map(int, input().split()))
substances_nc = list(map(int, input().split()))
challenges_nc = list(map(int, input().split()))

solve_temple_challenge_nc(tools_nc, substances_nc, challenges_nc)

if len(substances_nc) > 0:
    print("Substances:", ', '.join(map(str, substances_nc)))
    
elif len(tools_nc) > 0:
    print("Tools:", ', '.join(map(str, tools_nc)))

    print("Challenges:", ', '.join(map(str, challenges_nc)))
