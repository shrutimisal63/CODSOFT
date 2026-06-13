import java.util.Scanner;

public class StudentGradeCalculator{

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Number Of Subjects: ");
        int subjects = sc.nextInt();

        int totalMarks = 0;

        for (int i = 1; i < subjects; i++) {
            int marks;

          do { 
               System.out.println("Enter marks for Subject " + i + " (0-100): ");
               marks=sc.nextInt();

               if(marks<0 || marks > 100){
                    System.out.println("Invalid Marks! Please Enter between 0 and 100.");
               }
               
           } while (marks < 0 || marks > 100 );
               
           totalMarks += marks;
          }

           double averagePercentage = (double)totalMarks / subjects;

           String grade;

           if(averagePercentage >= 90) {
                grade= "A+";
           } else if(averagePercentage >= 80) {
                grade= "A";
           } else if(averagePercentage >= 70) {
                grade = "B";
           } else if(averagePercentage >= 60) {
                grade = "C";
           } else if(averagePercentage >= 50) {
                grade = "D";
           } else {
               grade = "F";
           }
      
            
           
           System.out.println("=====RESULTS======");
           System.out.println("Total Marks = " + totalMarks);
           System.out.println("Average Percentage = " + averagePercentage + "%d");
           System.out.println("Grade = "+ grade);

           sc.close();
    }
}