#1
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if n >=2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        else:
            print("Not Weird")

#2
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    sum = a + b
    diff = a - b
    product = a * b

    print(sum)
    print(diff)
    print(product)

#3
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)

#4
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

#5
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True

    return leap


year = int(input())
print(is_leap(year))

#6
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")

#7
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    filtered_coordinates = [c for c in coordinates if sum(c) != n]

    print(filtered_coordinates)

#8
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max = max(arr)
    min = min(arr)

    for i in arr:
        if i > min and i < max:
            min = i

    print(min)

#9
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))

    # Find the second lowest score
    second_lowest_score = sorted(set([score for name, score in students]))[1]

    # Create a dictionary of students with the same score
    students_dict = {score: [name for name, score_ in students if score_ == score]
                     for score in set([score_ for name_, score_ in students])}

    # Get the names of students with the second lowest score
    names = students_dict[second_lowest_score]

    # Print the names in alphabetical order
    for name in sorted(names):
        print(name)


#10
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    scores_ = student_marks[query_name]

    total = sum(scores)

    print(f"{total / len(scores_):.2f}")