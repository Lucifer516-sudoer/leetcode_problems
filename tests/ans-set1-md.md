# Part - A
1. **Purpose of Using Enumeration in C:**
   Enumeration in C is used to define a set of named integer constants. This helps improve code readability and maintainability. The syntax for defining an enumeration is as follows:
   ```c
   enum enum_name { constant1, constant2, constant3, ... };
   ```
   For example:
   ```c
   enum Days { Monday, Tuesday, Wednesday, Thursday, Friday, 
				Saturday, Sunday };
   ```

2. **Precedence of Operators in C:**
   Operators in C have different precedence levels, determining the order of evaluation. Here are some common operator precedences from highest to lowest:
   - Postfix increment/decrement, e.g., `a++`, `a--`
   - Prefix increment/decrement, e.g., `++a`, `--a`
   - Multiplication, division, and modulus, e.g., `*`, `/`, `%`
   - Addition and subtraction, e.g., `+`, `-`
   - Relational operators, e.g., `<`, `>`, `<=`, `>=`
   - Equality operators, e.g., `==`, `!=`
   - Logical AND, `&&`
   - Logical OR, `||`
   - Assignment operators, e.g., `=`, `+=`, `-=`

3. **Difference Between `a = 5` and `a == 5` in C:**
   - `a = 5` is an assignment statement, where the variable `a` is assigned the value 5.
   - `a == 5` is a comparison or equality test, checking whether the value of `a` is equal to 5. It returns a Boolean result (true or false).

4. **Declaration and Initialization of 2D Array in C:**
   To declare and initialize a 2D array in C, you can use this syntax:
   ```c
   data_type array_name[rows][columns] = { {val1, val2, ...}, 
												{val3, val4, ...}, ... };
   ```
   Example with a 2D integer array:
   ```c
   int matrix[2][3] = { {1, 2, 3}, {4, 5, 6} };
   ```

5. **Changing the Size of an Array in C:**
   No, once an array is declared in C, its size cannot be changed. The size is fixed at declaration and cannot be altered during program execution. If a different size is needed, a new array with the desired size must be declared.

# Part - B

6. (a) **Storage Classes in C:**
   Storage classes in C define the scope, lifetime, and visibility of variables. There are four primary storage classes in C:
   1. **Auto**: Variables declared as "auto" are created and destroyed within the function they are declared in. They are the default storage class for local variables.
      ```c
      auto int x; // This is equivalent to: int x;
      ```
   2. **Register**: Variables declared as "register" are stored in CPU registers for fast access. They are suitable for frequently used variables.
      ```c
      register int count;
      ```
   3. **Static**: Static variables have a longer lifetime and retain their values between function calls. They are initialized only once.
      ```c
      static int i = 0;
      ```
   4. **Extern**: Extern variables are declared in one source file but can be used in other source files. They have global visibility.
      ```c
      extern int globalVar;
      ```

6. (b) (i) **C Program to Print Pattern:**
   Here's a C program to print the pattern using looping statements:
   ```c
   #include <stdio.h>
   
   int main() {
       int i, j;
       for (i = 1; i <= 5; i++) {
           for (j = 1; j <= i; j++) {
               printf("%d", i);
           }
           printf("\n");
       }
       return 0;
   }
   ```

   (ii) **Programming Paradigms:**
   Programming paradigms are approaches to solving problems using specific techniques. Common paradigms include:
   - **Procedural**: Focuses on functions and procedures. Example: C language.
   - **Object-Oriented**: Organizes data and methods into objects. Example: Java.
   - **Functional**: Emphasizes pure functions and immutability. Example: Haskell.
   - **Imperative**: Uses statements to change program state. Example: C++.
   - **Declarative**: Describes what to achieve without specifying how. Example: SQL.

7. (a) (i) **Concept of Arrays in Programming:**
   Arrays are data structures that store a collection of elements of the same data type. They offer benefits like efficient storage, easy access using indices, and simplified data manipulation.

   (ii) **C Program to Count Occurrences in an Array:**
   Here's a C program to count the occurrences of a number in an array:
   ```c
   #include <stdio.h>
   
   int main() {
       int arr[] = {1, 2, 3, 4, 2, 3, 2, 5};
       int n = sizeof(arr) / sizeof(arr[0]);
       int target = 2;
       int count = 0;
       for (int i = 0; i < n; i++) {
           if (arr[i] == target) {
               count++;
           }
       }
       printf("The number %d occurs %d times in the array.\n", 
													target, count);
       return 0;
   }
   ```

7. (b) (i) **C Program to Declare and Initialize a One-Dimensional Array:**
   Here's a C program to declare and initialize a one-dimensional array:
   ```c
   #include <stdio.h>
   
   int main() {
       int numbers[] = {1, 2, 3, 4, 5};
       int n = sizeof(numbers) / sizeof(numbers[0]);
       for (int i = 0; i < n; i++) {
           printf("Element %d: %d\n", i, numbers[i]);
       }
       return 0;
   }
   ```

   (ii) **C Program to Find Determinant of a Matrix (2D Array):**
   Calculating the determinant of a matrix involves a complex algorithm. Below is a simplified C program for a 2x2 matrix:
   ```c
   #include <stdio.h>
   
   int main() {
       int matrix[2][2];
       printf("Enter the 2x2 matrix elements:\n");
       for (int i = 0; i < 2; i++) {
           for (int j = 0; j < 2; j++) {
               scanf("%d", &matrix[i][j]);
           }
       }
       int determinant = (matrix[0][0] * matrix[1][1]) 
							- (matrix[0][1] * matrix[1][0]);
       printf("Determinant: %d\n", determinant);
       return 0;
   }
   ```

# Part - C


8. (a) **C Program to Calculate Discount Amount:**
   ```c
   #include <stdio.h>
   
   int main() {
       float billAmount, discount = 0;
       printf("Enter the bill amount: Rs. ");
       scanf("%f", &billAmount);
       
       if (billAmount > 10000) {
           discount = 0.2 * billAmount; // 20% discount
       } else if (billAmount > 1000) {
           discount = 0.1 * billAmount; // 10% discount
       } else if (billAmount > 500) {
           discount = 0.05 * billAmount; // 5% discount
       }
       
       printf("Discount Amount: Rs. %.2f\n", discount);
       printf("Final Amount to Pay: Rs. %.2f\n",billAmount - discount);
       return 0;
   }
   ```

   Explanation:
   - The program takes the bill amount as input from the user.
   - It checks the bill amount against the conditions:
     - If the bill amount is above Rs. 10000, a 20% discount is applied.
     - If the bill amount is above Rs. 1000 but not above Rs. 10000, a 10% discount is applied.
     - If the bill amount is above Rs. 500 but not above Rs. 1000, a 5% discount is applied.
   - The discount amount and the final amount to pay are calculated and displayed.

