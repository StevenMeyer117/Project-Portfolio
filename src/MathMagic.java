/*
Math Magic project you will become a mathemagician and write a small program that performs a mathematical magic trick!
It will involve performing arithmetic operations on an integer that you choose.

The program will allow you to change the original number "myNumber" and see the output. The output should be the same
number regardless of myNumber chosen after a series of magical mathematic steps.
 */

public class MathMagic {
    public static void main(String[] args) {
        // Create int variable myNumber which can be any integer
        int myNumber = 48;

        // Write int variables for each step to perform mathematical equation.
        int stepOne = myNumber * myNumber;
        int stepTwo = stepOne + myNumber;
        int stepThree = stepTwo / myNumber;
        int stepFour = stepThree + 17;
        int stepFive = stepFour - myNumber;
        int stepSix = stepFive / 6;
        System.out.println(stepSix);
    }
}