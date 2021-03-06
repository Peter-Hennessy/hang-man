# Hang-man 

## Welcome to <a href="https://hang-man2022.herokuapp.com/" target="_blank" rel="noopener">Hang-man</a> A Game that hangs in the balance with every wrong answer

The idea for my project comes from a game I liked to play myself as a child,  with friends and family. It is  a really simple game but can keep you entertained for hours if needed. 

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
    * [Game Structure](<#game-structure>)
    
* [**Features**](<#features>)     
* [**Technologies Used**](<#technologies-used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Acknowledgements**](<#acknowledgements>)

# User Stories
- As a user I want to be able Know what I need to do to start  the game
- As a user I need to be able clearly understand what I need to do
- As a user I need to be able to see text and images clearly
- As a user I need to be able to understand the rules of the game
- As a user I need to want to return to the game after the initial game is finished

 [Top](<#contents>)

# Game Structure
* The game begins by asking the user their name to invite them in on a personal journey
* I created a game where the player has 8 lives to guess a word through the process of elimination
* If the user gets a incorrect letter, then a piece of the hangman image will appear
* Every letter that is guessed will appear as to avoid repitition in the guesses
* If all guesses are made a message will appear to say the user is free to go, or needs to be taken to the undertaker, depending on the outcome


 [Top](<#contents>)


 # Future Features

 - In the future I would like to be able to apply styling to the platform, and animation images to the game

 [Top](<#contents>)

 
 
# Technologies Used

* [Gitpod](https://www.gitpod.io/#get-started) - used to deploy the website.
* [Github](https://github.com/) - used to host and edit the website.
* [Python](https://www.w3schools.com/python/) - provides the interactivity for the game
* [Heroku](https://www.heroku.com/) - enables the game to be deployed in a browser

 [Top](<#contents>)

# Testing

Please refer to [**_here_**](TESTING.md) for more information on testing

 [Top](<#contents>)

# Deployment

### **To deploy the project**
Deploying your app to heroku
1. IN YOUR TERMINAL ON GITPOD Login to heroku and enter your details. to do this, type the following
command: heroku login -i
2. Get your app name from heroku.
command: heroku apps
3. Set the heroku remote. (Replace <app_name> with your actual app name)
command: heroku git:remote -a <app_name>
4. Add, commit and push to github
command: git add . && git commit -m "Deploy to Heroku via CLI"
5. Push to both github and heroku
command: git push origin main
command: git push heroku main

MFA/2FA enabled?
1. Click on Account Settings (under the avatar menu)
2. Scroll down to the API Key section and click Reveal. Copy the key.
3. Enter the command: heroku_config , and enter your api key you copied when prompted
4. Complete the steps above, if you see an input box at the top middle of the editor...
 a. enter your heroku username
 b. enter the api key you just copied

![Heroku deployed image HERE](assets/readme-images/deployed.png)

  The live link to the Github repository can be found here -  https://hang-man2022.herokuapp.com/


### **To create a local clone of this project**
The method from cloning a project from GitHub is below: ![Cloned Repository](assets/readme-images/clone.png)

1. Under the repository???s name, click on the **code** tab.
2. In the **Clone with HTTPS** section, click on the clipboard icon to copy the given URL.
3. In your IDE of choice, open **GitHub Desktop**.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Press **clone**, and a local clone will be created

 [Top](<#contents>)

# Acknowledgements
- The project was completed as a Portfolio Project 3 piece for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/). 

- The concept for the game came from a online tutorial, [Kylie Ying](https://www.youtube.com/watch?v=cJJTnI22IF8).
 
- I would like to acknowledge the [Slack Community](https://slack.com/) for the help and the eagerness to help others in this community, also the encouragement and support that is given from students in similar situations as yourself

- Also [Kasia Boguka](https://github.com/bezebee) for her help & guidance with the project, and support and encouragement, and is always there to answer any questions

- [Tutor support](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentecommerce/support) really helped during this project, first time using them and would encourage students stuck on a problem to reach out for help

 [Top](<#contents>)