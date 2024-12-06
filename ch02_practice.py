import random
score_p1 = 0
score_p2 = 0
tie = 0

armas = {1: 'Pierda', 2: 'Papel', 3: 'Tijera'}

for i in range(10):
    num_p1 = random.randint(1,3)
    num_p2 = random.randint(1,3)
    if num_p1 == 1 and num_p2 == 3:
        print(f"{armas[num_p1]} vs {armas[num_p2]} > Player 1 win!")
        score_p1 += 1
    elif num_p1 == 1 and num_p2 == 2:
        print(f"{armas[num_p1]} vs {armas[num_p2]} > Player 2 win!")
        score_p2 += 1
    elif num_p1 == 2 and num_p2 == 1:
        print(f"{armas[num_p1]} vs {armas[num_p2]} > Player 1 win!")
        score_p1 += 1
    elif num_p1 == 2 and num_p2 == 3:
        print(f"{armas[num_p1]} vs {armas[num_p2]} > Player 2 win!")
        score_p2 += 1
    elif num_p1 == num_p2:
        print(f"{armas[num_p1]} vs {armas[num_p2]} > It's a tie!")
        tie += 1
    elif num_p1 == 3 and num_p2 == 1:
        print(f"{armas[num_p1]} vs {armas[num_p2]} > Player 2 win!")
        score_p2 += 1
    elif num_p1 == 3 and num_p2 == 2:
        print(f"{armas[num_p1]} vs {armas[num_p2]} > Player 1 win!")
        score_p1 += 1
    
print(f"Player 1: {score_p1}\nPlayer 2: {score_p2}\nTie: {tie}")
        