A=B=C=D=E=F=i=n=0

n = int(input("Number of student : "))

while i < n :
  score = int(input("score of student : "))
  if score >= 90 and score <= 100 :
      A += 1
  elif score >= 80 and score <= 89 :
      B += 1
  elif score >= 70 and score <= 79 :
      C += 1
  elif score >= 60 and score <= 69 :
      D += 1
  elif score >= 50 and score <= 59 :
      E += 1
  elif score >= 0 and score <= 49 :
      F += 1
  else :
    print("ERROR")
    score -= 1
  i += 1

print("90-100 :",end = " ")
for score in range(0,A):
    print("*",end = " ")

print("\n80-89 :",end = " ")
for score in range(0,B):
    print("*",end = " ")

print("\n70-79 :",end = " ")
for score in range(0,C):
    print("*",end = " ")

print("\n60-69 :",end = " ")
for score in range(0,D):
    print("*",end = " ")

print("\n50-59 :",end = " ")
for score in range(0,E):
    print("*",end = " ")

print("\n0-49 :",end = " ")
for score in range(0,F):
    print("*",end = " ")
