println("Hello")

my_answer = 42

typeof(my_answer)

my_pi = 3.14159

typeof(my_pi)

😸 = "smiley cat";

typeof(😺)


#=

symbol for multi line comments

=#

# String Interpolation
name = "Jane";
println("Hello, my name is $name")


# Loops
n = 10
while n < 10
    n += 1
    println(n)
end

for n in 1:10
    println(n)
end


m, n  = 5, 5
A = zeros(m, n)

for i in 1:m
    for j in 1:n
        A[i, j] = i + j
    end
end

A

print(A)

println(A)

C = [i + j for i in 1:m, j in 1:n]

C

print(C)

show(C)for n in 1:10
    println(n)
end



# Conditionals
x = 3
y = 90

if x > y
    print("$x is larger than $y")
elseif y > x
    print("$y is larger than $x")
else
    print("$x is equal to $y")
end

# Functions
function sayhi(name)
    println(name)
end

sayhi("Fernando")

sayhi2 = name -> println(name)

sayhi2("C-3PO")

v = [2,1,3]
sort(v)
v

sort!(v)
