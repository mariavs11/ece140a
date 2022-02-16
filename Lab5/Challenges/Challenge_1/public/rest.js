function getAge() {
  let age = document.getElementById('age').value;
  if(age.trim() === "" ) {
    console.log("No ID provided");
    document.getElementById("error").textContent = "You have not provided an ID";
  }

  else {
   // sends post request with the age parameters selected, Ex: 20-30
   let data = { age : age};
      fetch("/age", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
      }).then(response=>response.json())
      .then(function(response) {
      console.log("Request complete! response:", response);
      if(response["ID"]== ""){
        document.getElementById("Owner").textContent = "Author: No data found "
        let img = document.getElementById('image')
        img.src = "" // if no data is found, no image is shown

      }
      else{
        document.getElementById("Owner").textContent = "Author: " + response["Owner"] // shows author name
        let img = document.getElementById('image')
        img.src = response['Name'] // shows image accordingly
      }

      });


  }
}

function getInfo() {
  let height = document.getElementById('height').value; // gets value for height
  let age = document.getElementById('age').value; // gets value for age
  if(height.trim() === ""  && age.trim() === "") {
    console.log("No ID provided");
    document.getElementById("error").textContent = "You have not provided an ID";
  }

  else {
   // sends post request with input height and age parameters
   let data = {age: age, height: height};
      fetch("/photos", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
      }).then(response=>response.json())
      .then(function(response) {
      console.log("Request complete! response:", response);
      if(response["ID"]== ""){
        document.getElementById("Owner").textContent = "Author: No data found "
        let img = document.getElementById('image')
        img.src = "" // if no data is found, no image is shown
      }
      else{
        document.getElementById("Owner").textContent = "Author: " + response["Owner"] // shows author name
        let img = document.getElementById('image')
        img.src = response['Name']  // shows image accordingly
      }

      });


  }
}

function getHeight() {
  let height = document.getElementById('height').value;
  if(height.trim() === "" ) {
    console.log("No ID provided");
    document.getElementById("error").textContent = "You have not provided an ID";
  }

  else {
    // sends post request with input height parameters, Ex: 160-170
   let data = { height: height};
      fetch("/height", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
      }).then(response=>response.json())
      .then(function(response) {
      console.log("Request complete! response:", response);
      if(response["ID"]== ""){
        document.getElementById("Owner").textContent = "Author: No data found "
        let img = document.getElementById('image')
        img.src = ""
      }
      else{
        document.getElementById("Owner").textContent = "Author: " + response["Owner"] // shows author name
        let img = document.getElementById('image')
        img.src = response['Name'] // shows image accordingly
      }

      });


  }
}



