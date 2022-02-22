// Button1: selection for current data (all sensors): id, timestamp, distance, temp
function getData() {
    
    let theURL = '/data';
    fetch(theURL)
        .then(response=>response.json())
        .then(function(response) {
          for(var key in response) {
            document.getElementById(key).textContent
               = response[key]
          }
        });
    
}


// Button2: temp selection begins
function getTemp() {
  let temp = document.getElementById('temprange').value; // highest temp or lowest temp
  if(temp.trim() === "" ) {
    document.getElementById("error").textContent = "You have not provided an ID";
  }

  else {
   // sends post request with the age parameters selected, Ex: 20-30
   let data = { temperature : JSON.stringify(temp)};
      fetch("/temperature", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
      }).then(response=>response.json())
      .then(function(response) {
      console.log("Request complete! response:", response);
      if(response == ""){
        document.getElementById("temperature").textContent = " No data found "
        
      }
      else{
        document.getElementById("temperature").textContent = response["temperature"] // shows only temperature
        document.getElementById("distance").textContent = ""  
        document.getElementById("id").textContent = ""      
        document.getElementById("created_at").textContent = ""            
      }

      });


  }
}


// Button3: retrieve 2, 4, or 6 of the latest records
function getRows(){
  let numrows = document.getElementById('numrows').value; 
  if(numrows.trim() === "" ) {
    document.getElementById("error").textContent = "You have not provided an ID";
  }

  else {
   
   let data = {rows : numrows};
      fetch("/datarows", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
      }).then(response=>response.json())
      .then(function(response) {
      console.log("Request complete! response:", response);
      if(response == ""){

      }
      else{
        
        var keys = [];
        var obj = JSON.parse(response)
        document.write("<table border==\"1\"><tr>");
        for (key in obj[0]) {
          console.log('prinkting')
          console.log(key)
          document.write('<td>' + key + '</td>');
        }
        document.write("</tr>");
        for (var i = 0; i < obj.length; i++) {
          document.write('<tr>');
          for (key in obj[i]) {
            document.write('<td>' + obj[i][key] + '</td>');
          }
          document.write('</tr>');
        }
        document.write("</table>");

      
      }

      });

    
  }
}


// Button4: temp display on output device begins 
function getDisplay() {
    
  let theURL = '/display';
  fetch(theURL)
      .then(response=>response.json())
      .then(function(response) {
        
      });
  
}