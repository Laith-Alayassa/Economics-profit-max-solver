# Micro-economics problem solver
![github](https://user-images.githubusercontent.com/60319236/171945613-fc684e28-4d6c-422a-b514-f49b8ab65e58.png)


Find and use the webiste [**here**](https://leoayasa.pythonanywhere.com/)

I found myself solving similar equations multiple times during my microeconomics course, solving the problems required taking derivatives and maximizing functions. A high result accuracy was required as well, which made using a simple calculator or the phone insufficient. Double-checking the work was a time-intensive and error-prone process.

I decided to write this project so that I can quickly find a solution and easily check my work, and for the fun of python. This program turned solving a problem that took around 10 minutes into a matter of a second with no errors.

So far, I have learned and used the SymPy library which has been extremely useful at solving equations and really great when dealing with unknown variables as this library allows the user to define an unknown variable (as a symbol) and manipulate and use it in its unknown form until a solution for it is found. An example of this is when needing to equate two functions containg the variable `Q`, which was made possible by the use of unknown variables `symbols`:

```angular2html
Q = symbols("Q")

max Profit = MR - MC = 0
max Profit = 100 - (2*Q + 3) = 0
max Profit = 100 = 2*Q + 3

Q could be: 97/2 units
```

# Things I Learned:
1. Creating a webiste with **FLASK** library
2. Deploying a flask website (using pythonanywhere)
3. Using **virtual enviornemts** and the **terminal**
4. Using the numpy library, especially using variables with no defined value and operating on them in their symbolic form
5. Using Figma, HTML, CSS to design the website as this was my first webiste

![screencapture-leoayasa-pythonanywhere-solve-2022-06-03-15_03_40](https://user-images.githubusercontent.com/60319236/171942473-d55244dc-cb75-4d72-a5ef-f47111bbedd7.png)
