Write a blog post that addresses the following prompts. For questions about the dataset, be sure to explain how your code answers the question.

1. Discuss how you used the API to obtain the dataset.

To obtain the dataset, I ran a while loop until the api stopped responding with a 200 status code, and I routed all of the responses into a csv 
file using a dictwriter, which takes a dictionary as input and prints it in the correct format in a csv file.

2. Which sock has the most variations? If there is more than one answer, then list all of them.

There are several socks that have the "most" variations, all of them having 8 different variants.
argyle crew socks,color-blocked socks,frilly knee-high socks,holey tights,kiddie socks,mixed-tweed socks,no-show socks,semi-opaque socks,semi-opaque tights,sequin leggings,simple-accent socks,striped socks,striped tights,tube socks,ultra no-show socks,vivid leggings,vivid socks,vivid tights

3. How many socks of each color are there? If a sock has two different colors, it should be counted in both. However, if a sock has the same Color1 and Color2, make sure you don’t double count it!

Pink: 45, Red: 44, Aqua: 33, Orange: 28, Purple: 39, Green: 51, Blue: 48, Yellow: 34, White: 89, Black: 65, Beige: 16, Gray: 33, Brown: 11, Colorful: 14

4. Discuss your process of how you worked on this lab. Include details such as who you worked with, what methods you tried, what worked or didn’t work, what could have gone better, and what you learned during this lab. Focus more on the programming side of the lab! Feel free to attach images, screenshots, pseudocode, etc to elaborate on your response.

I started with retrieving the api and putting it into a csv file. What I originally thought I could do was just retreive the entire dataset at once in one massive dictionary, but I took a closer look at the parameters and saw that it had an index for input. I ran a couple experiments trying to access multiple indices or a range of indices at the same time, but I gave that up and settled for reading the api into the csv file row by row. 

For the task dealing with finding the socks with the most variation, I thought pretty early on that I would need to record the exact instance of each variation somehow in order to check other variations against it to see if they were unique. I did this by creating a dictionary that would be organized into name-keys that pointed to lists that contained the different variations. Whenever I saw a new variation, I would add its data to the list. 

For checking which ones had the most, I needed to somehow find all of them, which meant that the usual strategy of looping through and repeatedly replacing the initial value if the one being checked is higher wouldn't work. I solved this by creating a running list of the socks, which would be added to if the sock type being checked had the same length and replaced entirely if it had a higher lengeth. You could also do this by looping through the list twice, the first loop finding the highest length value and the second loop finding any socks that have the same value.

For counting the colors, it required that I not double count for one sock, as the socks had two colors listed, but some had both of the colors as the same. To solve this, I always added the firt color and simply checked if the second color was the same as the first one before adding it.
