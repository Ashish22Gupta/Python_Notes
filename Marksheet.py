Name = input("Enter Your Name: ");

Std = int(input("Enter Your STD: "));

div = input("Enter Your Division: ")

Roll_No = int(input("Enter Your Roll No: "));


Maths = float(input("Enter Your Maths Marks: "));
English = float(input("Enter Your English Marks: "));
Science = float(input("Enter Your Science Marks: "));
Geography = float(input("Enter Your Geography Marks: "));
History = float(input("Enter Your History Marks: "));

Marks = (Maths+English+Science+Geography+History);
Total = 500;

Percentage = (Marks*100)/Total;

print("\n__________________________________");
print("-------Marksheet of Student--------");
print("__________________________________");
print("__________________________________\n");

print("Name:",Name, " Std:",Std);
print("Div :",div,"    Roll No:", Roll_No);
print("__________________________________");
print("Subjects:       ","Marks:");
print("Maths Marks:    ", Maths);
print("English Marks:  ", English);
print("Science Marks:  ", Science);
print("Geography Marks:", Geography);
print("History Marks:  ", History);
print("__________________________________");
print("Marks: ", Marks," Total: ", Total);
print("__________________________________");
print("Percentage:     ", Percentage,"%");
print("__________________________________");