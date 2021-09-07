#=
Introduction to Julia (for programmers)
source: https://juliaacademy.com/
=#

# Wello Word
println("Hello Word")

# Numeric variables
my_answer = 42

# Find out type of variable
typeof(my_answer)

my_pi = 3.14159
typeof(my_pi)

😸 = "smiley cat";
typeof(😺)

# String Interpolation
name = "Jane";
println("Hello, my name is $name")

#--- Loops
# Loop 1
n = 10
while n < 10
    n += 1
    println(n)
end

# Loop 2
for n in 1:10
    println(n)
end

# Matrices
m, n  = 5, 5
A = zeros(m, n)

for i in 1:m
    for j in 1:n
        A[i, j] = i + j
    end
end
print(A)
println(A)

# List comprehension
C = [i + j for i in 1:m, j in 1:n]
print(C)

show(C)for n in 1:10
    println(n)
end

#--- Conditionals
x = 3
y = 90

if x > y
    print("$x is larger than $y")
elseif y > x
    print("$y is larger than $x")
else
    print("$x is equal to $y")
end

#--- Functions
function sayhi(name)
    println(name)
end
sayhi("Fernando")
sayhi2 = name -> println(name)
sayhi2("C-3PO")

# Bang Operator
v = [2,1,3]
sort(v)
v

sort!(v)
