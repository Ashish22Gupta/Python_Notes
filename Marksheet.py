First_Name = input("Enter Your First Name: ");
Middle_Name = input("Enter Your Middle Name: ");
Last_Name = input("Enter Your Last Name: ");

Roll_No = int(input("Enter Your Roll No: "));

Address = input("Enter Your Address: ");

Maths = float(input("Enter Your Maths Marks: "));
English = float(input("Enter Your English Marks: "));
Science = float(input("Enter Your Science Marks: "));
Geography = float(input("Enter Your Geography Marks: "));
History = float(input("Enter Your History Marks: "));

Marks = (Maths+English+Science+Geography+History);
Total = 500;

Percentage = (Marks*100)/Total;

print("\n********************");
print("Marksheet of Student");
print("********************\n");

print("First_Name: ",First_Name);
print("Middle_Name: ",Middle_Name);
print("Middle_Name: ",Last_Name);
print("Roll No: ", Roll_No);
print("Address: ", Address);

print("Maths Marks: ", Maths);
print("English Marks: ", English);
print("Science Marks: ", Science);
print("Geography Marks: ", Geography);
print("History Marks: ", History);

print("Marks: ", Marks);
print("Total: ", Total);
print("Percentage: ", Percentage,"%");