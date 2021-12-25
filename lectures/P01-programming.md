
# P01: programming concepts

## What's hard about programming?

If you have never written a computer program before, you will find computer programming to be difficult.  Programming a computer requires   
1. figuring out what computation solves the problem you want to solve   
2. specifying what steps to follow to perform that computation, and   
3. explaining those steps to a computer.  

When you write your first program, 1 will be solved for you, 2 will be trivial, and 3 will seem quite hard.  
As you get better at programming, and the programs you write become more complicated, 3 will become fairly easy, while 2 will prove to be quite difficult. Eventually, most of the difficulty will end up in 1.  

## Learning to program

- Programming means giving a computer instructions about what steps to follow to perform some calculation.  

- Computers are very naive and uncomplicated.  They do *exactly* what you tell them; no more, no less.  This makes them easy to deal with when you know exactly what you want, but it can be frustrating if you don't have a clear plan and a clear way of giving instructions that are 100% unambiguous.  
  
- If a computer does something wrong, it is because we told it to do something wrong. In other words, computers don't make mistakes, we make mistakes telling them what to do. 

- Learning to program requires figuring out what calculation to do to solve the problem you are interested in, and then *unambiguously* explaining those steps to a computer that knows nothing about the world or about your specific intentions. 


### Example: 

You want to instruct me to send a new post to the class with the message "hi" using slack.  The trick is that (1) you have to write all the instructions out ahead of time, and (2) I only understand a limited set of commands:

- move mouse {left, right, up, down} (distance in cm, on my screen)   
- click mouse
- press (keyboard button)    

Some observations about what makes this hard:  
- cannot observe intermediate state.     
- my representation differs from yours, and you have to give me instructions in my representation.  
- tedious level of precision required because I don't understand more sophisticated commands.  

Computer programming presents the same challenges: we need to write out very detailed instructions, using a very limited, literal, set of commands.  We need to write the instructions out in advance.   The computer's representation of the world differs from our own.  How the state changes in response to instructions may differ from your expectations.

Another classic example: If you read the directions on the back of a shampoo bottle, it will usually say something like "Lather, Rinse and Repeat.". Suppose you were trying to program a computer to perform these steps and you gave these instructions. What would happen to your supply of shampoo? You need to be precise if you want to avoid unintended consequences. 
