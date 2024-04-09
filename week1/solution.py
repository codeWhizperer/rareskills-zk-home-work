#baby step, giant-step algorithm
def discrete_log(g, E_s, n):
    m = int(n ** 0.5) + 1
    
    # Precompute values of g^j mod n for j from 0 to m-1
    precomputed = {pow(g, j, n): j for j in range(m)}
    
    # Compute the value g^(-m) mod n
    g_inverse_m = pow(g, -m, n)
    
    for i in range(m):
        temp = (E_s * pow(g_inverse_m, i, n)) % n
        if temp in precomputed:
            return i * m + precomputed[temp]
    
    return None

# Example values
g = 5
E_s = 5666
n = 9551

# Call your function to get the result
student_solution = discrete_log(g, E_s, n)

# Check if the student's solution is correct
encrypted_number = pow(g, student_solution, n)
assert encrypted_number == E_s
print("student_solution is {}".format(student_solution))


# Example 2:
n2 = 1000004119
g2 = 5
E_s2 = 767805982

student_solution2 = discrete_log(g2,E_s2,n2)
result = pow(g2,student_solution2,n2)
assert result == E_s2
print("student_solution is {}".format(student_solution2))


print(pow(g, a, n) * pow(g, b, n) == pow(g, a + b, n))