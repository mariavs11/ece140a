## Lab5
### Tutorial 1
We learned how to connect python to my sql, using the library mysql-connector-python. 

### Tutorial 2
Here, we combined pyramid and mysql to create a webpage that has access to a database. 
We created an app that had two routes "/students" and "/student/{id}". The first displays a list of all the students and their details and the second returns a json object with the details of a specific student, according to their id.


### Tutorial 3
Here, we combined pyramid, mysql and javascript to create a webpage that you can select from a drop-box the staff. 
### Challenge 1
We hosted a webpage that allowed us to select (from two drop-down boxes) age and height parameters to query our database 'Triton_Gallery'.
We were asked to show the image and author corresponding to the parameters selected.
I included three submit buttons: one to get data based on only age, one to get data based on only height, and one to get data based on height and age.
By clicking the submit button, we trigger one of the 3 functions in my rest.js file.
If our intention is to query the data based on: age parameters, we trigger the getAge(); height parameters, we trigger the getHeight(); height and age parameters, we trigger getInfo().
Inside each of these functions, we get the value selected for age/height from HTML and we send a post request with the value(s) enclosed in the body of the request message. 
On app.py, inside get_info (for example), we load the data from the post request, query the database with the data, and then we return a json object with the results from our query.
Now, in our rest.js file, we used the json object that was returned to write to HTML the image and the author name.

[Link to video of working webpage](https://www.youtube.com/watch?v=0S3umnMWFl4)