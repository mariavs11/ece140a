# LAB 1 

### Tutorial 1 
For this tutorial, I reviewed how to use github to upload your work to the cloud. 
First, I created my repository both locally and remotely and linked the local repo to the remote one. 
After I made changes in my local repository, I pushed these changes to the cloud. 

### Tutorial 2
With this tutorial, I was able to set up python and jupyter notebook.

### Tutorial 3
In this tutorial, I learned the basics of Python such as how to manipulate strings and lists and how to define functions. 
### Tutorial 4
In this tutorial, I learned how to extract data from a website (also known as Web Scraping). 
For this, we used the libraries "requests" and "bs4 to extract data from the website "http://quotes.toscrape.com"

## Challenge 1
Here, I learned how to create my own personalized website where I added my portfolio (index.html). 
In another HTML file (music.html), I created another website that showed my top three artists and that had a video of one the artists embedded in the page.
I also learned how to change font size/family, add color, how to create tables and add emojis in html. Two additional modifications that I made was to style my table and to add an emoji.

ANS1: <!DOCTYPE html> is NOT a html tag. It is there to tell the browser what kind of document to expect. In this case, the document is a HTML5 file.

ANS2: It defines the document's title that shows up in the browser bar. 

ANS3: It is not possible to open with a tag and end with another. In this case, I assume that html defaults to one of the two tags. 

ANS4.1: By inspecting the page and editing in the browser, I can see the changes immediately but after I refresh the page the changes are gone. 

ANS4.2: If I make changes in the HTML file, I can see the changes after I refresh. 



## Challenge 2
For this challenge, we were asked to scrape data from the website "https://www.nobelprize.org/prizes/lists/all-nobel-prizes/". 
We were asked to extract all the text entries containing information for the following properties: awardee, field, year, and work. We, then, had to save all the information in a csv file.
To do all of that, I used the libraries introduced to us in Tutorial 4: bs4 and requests. The function "find_all()" was very useful to complete this task because it could be used to find specific tags. 

I used the data extracted to answer the following questions:

In which year did Barack Obama get the Nobel Peace Prize? 
2009

When and for what did Ernest Rutherford win the Nobel Prize? 
In 1908 for his investigations into the disintegration of the elements, and the chemistry of radioactive substances.

Who got the prize for Physics in 1939?
Frans Eemil Sillanpää 

