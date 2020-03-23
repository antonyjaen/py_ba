$(document).ready(function () {
  // const axios = require('axios');
  
   $("#ok").click(function () { 
       alert("ok");
       axios.get('http://127.0.0.1:3000/', {
           params: {
             ID: 2
           }
         })
         .then(function (response) {
           console.log(response.data);
           var ok= response.data;
           alert(ok.id);
         })
         .catch(function (error) {
           console.log("se produjo"+error);
         })
         .then(function () {
           alert("termino");
         });  
   });
});