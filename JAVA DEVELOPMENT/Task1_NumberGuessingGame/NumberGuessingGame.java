import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        int score = 0;
        char playAgain;

        do {
            int randomNumber = random.nextInt(100) + 1;
            int attempts = 10;
            boolean guessedCorrectly = false;

            System.out.println("\n===== Number Guessing Game =====");
            System.out.println("Guess a number between 1 and 100");
            System.out.println("You have " + attempts + " attempts.");

            while (attempts > 0) {

                System.out.print("Enter your guess: ");
                int guess = sc.nextInt();

                if (guess == randomNumber) {
                    System.out.println("Correct! You guessed the number.");
                    score++;
                    guessedCorrectly = true;
                    break;
                } else if (guess > randomNumber) {
                    System.out.println("Too High!");
                } else {
                    System.out.println("Too Low!");
                }

                attempts--;
                System.out.println("Attempts Left: " + attempts);
            }

            if (!guessedCorrectly) {
                System.out.println("You Lost!");
                System.out.println("The correct number was: " + randomNumber);
            }

            System.out.println("Current Score: " + score);

            System.out.print("\nDo you want to play again? (Y/N): ");
            playAgain = sc.next().charAt(0);

        } while (playAgain == 'Y' || playAgain == 'y');

        System.out.println("\nFinal Score: " + score);
        System.out.println("Thank you for playing!");

        sc.close();
    }
}