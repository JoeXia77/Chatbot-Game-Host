# Chatbot-Game-Host

This chatbot serves as a game host for Lateral-Thinking Puzzles (also known as Situation Puzzles or Minute Mysteries).

It is powered by ChatGPT (GPT-3.5-turbo) to provide responses to any of your questions (though sometimes it might simply say "I don't know").

While the chatbot doesn't have the capability to create original stories for you to solve, it can utilize any existing story and assist in hosting the game.


How to use:
run chatbot.py after you installed necessary dependencies. The API key is not provided, as it charges me money. You could get one from: https://platform.openai.com/docs/introduction

Environment: The following libraries seems very common, so hope you won't have any trouble with the environment.
    import os
    import json
    import openai
    import tkinter

Then there will be a UI, you can type your question use ENTER to send it to chatbot. You would get an Yes/No answer from chatbot.


Sample:

Here is one of my try:

Story: A woman lives on the 30th floor and hates taking the stairs. Every day she takes the elevator down to the lobby floor to go to work. When she comes home from work, she takes the elevator to the 20th floor and walks the rest of the way up, except on days when it rains. Those days she takes the elevator all the way home.
Question: Why does she walk the last ten flights of stairs if she hates it so much?


Chat history:

The elevator is not able to directly reach 30th floor while not raining. 

No.

The woman have something to do in 20th floor when it is not raining

No.

The woman is not able to let the elevator go to an higher level than 20th while not raining

Yes.

Any person influence her choice of floor

No.

The elevator works differently during raining days and not raining days

No.

The woman is able to let the elevator go to 30th floor when raining, but in not raining days, she can't let the elevator directly go to 30th

Yes.

When raining days and not raining days, the elevator's function didn't changed but the change is more related to the woman

Yes.

could you give me some hint

Sure, here's a hint: The woman uses an object she carries with her on rainy days that helps her reach the 30th floor button in the elevator.

The button is 30th is pretty high, in raining days, she could use umbrella to reach the button but without it, she can only reach the 20th button. Is this correct?
Yes, that's correct! The woman is too petite to reach the button for the 30th floor. She can only reach the 20th floor button. On days when it rains, she uses her umbrella to hit the button for the 30th floor. Great job solving the puzzle!
