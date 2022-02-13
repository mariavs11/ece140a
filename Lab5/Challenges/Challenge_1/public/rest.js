

function getInfo() {
  let height = document.getElementById('height').value;
  let age = document.getElementById('age').value;
  if(height.trim() === ""  && age.trim() === "") {
    console.log("No ID provided");
    document.getElementById("error").textContent = "You have not provided an ID";
  }
  else {
  let data = {age: age, height: height};
      fetch("/photos", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    }).then(res => {
      console.log("Request complete! response:", res);
    });.then(response=>response.json())
      .then(function(response) {
        let img = document.getElementById('image')
        img.src = ./public/response['Name']
        for(var key in response) {
          document.getElementById(key).textContent
             = key.toUpperCase() + ": " + response[key]
        }
      });


  }
}




