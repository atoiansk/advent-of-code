from utils import parse_input, solve_system

a_moves, b_moves, prizes = parse_input('input.txt')

# Part 1
total_cost = 0
for i in range(len(prizes)):
    times_a, times_b = solve_system(a_moves[i], b_moves[i], prizes[i])

    if float(times_a).is_integer() and float(times_b).is_integer():
        if times_a <= 100 and times_b <= 100:
            total_cost += 3*times_a + times_b

print(total_cost)

# Part 2
total_cost = 0
for i in range(len(prizes)):
    prize_x = prizes[i][0] + 10000000000000
    prize_y = prizes[i][1] + 10000000000000

    prize = (prize_x, prize_y)
    times_a, times_b = solve_system(a_moves[i], b_moves[i], prize)

    if float(times_a).is_integer() and float(times_b).is_integer():
        total_cost += 3*times_a + times_b

print(total_cost)




