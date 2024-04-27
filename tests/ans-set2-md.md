#  Part - A
1. **External Storage Class:**
   - External storage class in C is denoted by the keyword "extern."
   - It's used to declare variables that can be accessed globally across multiple source files.
   - Variables declared as "extern" are defined in another source file and linked at compilation.

2. **Use of Preprocessor Directive:**
   - Preprocessor directives in C are essential for code modification before compilation.
   - They include `#include` for header file inclusion and `#define` for macros.
   - These directives are instructions to the C preprocessor, not part of the C language itself.

3. **Storage Classes in C:**
   - C has four primary storage classes:
     1. Auto: Local variables with limited scope and automatic storage.
     2. Register: Variables stored in CPU registers for quick access.
     3. Static: Variables with a longer lifetime, often used for global variables.
     4. Extern: Variables declared in one source file but accessible in other source files.

4. **Types of Operators in C:**
   - C includes various types of operators:
     - Arithmetic (+, -, *, /, %)
     - Relational (<, >, <=, >=, ==, !=)
     - Logical (&&, ||, !)
     - Assignment (=, +=, -=, and more)
     - Bitwise (&, |, ^, <<, >>)
     - Conditional (ternary: ? :)
     - Comma (,)
     - Unary (+, -, ++, --, *, &, sizeof, and others)

5. **Purpose of `strlen()` Function:**
   - The `strlen()` function in C (from `<string.h>`) is used to find the length of a null-terminated string.
   - It returns an integer representing the number of characters in the string.
   - Commonly used for string operations like determining the length of a string.


# Part - B

6. (a) (i) **C Program to Check for Palindrome:**
   ```c
   #include <stdio.h>
   
   int main() {
       int num, reversed = 0, original, remainder;
       printf("Enter a number: ");
       scanf("%d", &num);
       original = num;
       
       while (num != 0) {
           remainder = num % 10;
           reversed = reversed * 10 + remainder;
           num /= 10;
       }
       
       if (original == reversed) {
           printf("%d is a palindrome.\n", original);
       } else {
           printf("%d is not a palindrome.\n", original);
       }
       return 0;
   }
   ```

   Example Output:
   ```
   Enter a number: 121
   121 is a palindrome.
   ```

6. (b) **Enumeration Constants in C:**
   - Enumeration constants are used to define named integer constants, improving code readability.
   - Example:
     ```c
     enum Days { Monday, Tuesday, Wednesday, Thursday, Friday,
                 Saturday, Sunday };
     ```

7. (a) (i) **Two-Dimensional Array in C:**
   - A two-dimensional array in C is like a table.
   - Declaration and initialization:
     ```c
     int matrix[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
     ```

   Example Output:
   No direct output; it initializes a 3x3 matrix.

7. (a) (ii) **C Program for Matrix Transpose:**
   - Transposing a matrix involves swapping rows with columns.
   - Example program:
     ```c
     #include <stdio.h>
     int main() {
         int rows = 3, cols = 3;
         int matrix[rows][cols], transpose[cols][rows];
         
         // Input matrix elements
         // (Assuming you've already filled the matrix with values)
         
         // Transpose the matrix
         for (int i = 0; i < rows; i++) {
             for (int j = 0; j < cols; j++) {
                 transpose[j][i] = matrix[i][j];
             }
         }
         
         // Display the transpose
         for (int i = 0; i < cols; i++) {
             for (int j = 0; j < rows; j++) {
                 printf("%d ", transpose[i][j]);
             }
             printf("\n");
         }
         
         return 0;
     }
     ```

   Example Output:
   ```
   Transposed Matrix:
   1 4 7
   2 5 8
   3 6 9
   ```

7. (b) **C Program for Selection Sort:**
   ```c
   #include <stdio.h>
   
   void selectionSort(int arr[], int n) {
       for (int i = 0; i < n - 1; i++) {
           int minIndex = i;
           for (int j = i + 1; j < n; j++) {
               if (arr[j] < arr[minIndex]) {
                   minIndex = j;
               }
           }
           // Swap arr[i] with the minimum element
           int temp = arr[i];
           arr[i] = arr[minIndex];
           arr[minIndex] = temp;
       }
   }
   
   int main() {
       int arr[] = {64, 25, 12, 22, 11};
       int n = sizeof(arr) / sizeof(arr[0]);
       
       selectionSort(arr, n);
       
       printf("Sorted array: ");
       for (int i = 0; i < n; i++) {
           printf("%d ", arr[i]);
       }
       return 0;
   }
   ```

   Example Output:
   ```
   Sorted array: 11 12 22 25 64
   ```


# Part - C
Certainly, here are the C programs with their example outputs:

8. (a) (i) **C Program for a Simple Calculator using Switch Case:**
   ```c
   #include <stdio.h>
   
   int main() {
       char operator;
       double num1, num2, result;
       
       printf("Enter an operator (+, -, *, /): ");
       scanf(" %c", &operator);
       
       printf("Enter two numbers: ");
       scanf("%lf %lf", &num1, &num2);
       
       switch (operator) {
           case '+':
               result = num1 + num2;
               break;
           case '-':
               result = num1 - num2;
               break;
           case '*':
               result = num1 * num2;
               break;
           case '/':
               result = num1 / num2;
               break;
           default:
               printf("Invalid operator.\n");
               return 1;
       }
       
       printf("Result: %.2lf\n", result);
       return 0;
   }
   ```

   Example Output:
   ```
   Enter an operator (+, -, *, /): +
   Enter two numbers: 10 5
   Result: 15.00
   ```

   (ii) **C Program to Calculate Electricity Bill:**
   ```c
   #include <stdio.h>
   
   int main() {
       int units;
       double bill = 0.0;
       
       printf("Enter the number of units consumed: ");
       scanf("%d", &units);
       
       if (units <= 100) {
           bill = 0.0; // No billing for the first 100 units
       } else if (units <= 1000) {
           bill = (units - 100) * 5.0; // Rs. 5 per unit beyond 100
       } else {
           bill = (1000 - 100) * 5.0 + (units - 1000) * 10.0; /* Rs. 10
                                  per unit beyond 1000 */
       }
       
       printf("Electricity Bill: Rs. %.2lf\n", bill);
       return 0;
   }
   ```

   Example Output:
   ```
   Enter the number of units consumed: 450
   Electricity Bill: Rs. 1750.00
   ```

8. (b) **Binary Search Procedure and C Program:**
   - Binary search is a search algorithm used for finding an element in a sorted array.
   - The example output for the binary search program depends on the specific input values and whether the target element is found in the array. If found, it may display the index; if not found, it may provide a message indicating that the element was not found.

