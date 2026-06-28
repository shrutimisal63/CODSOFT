function sendMessage(){

let input=document.getElementById("message");

let msg=input.value;

if(msg=="") return;

let chat=document.getElementById("chatbox");

chat.innerHTML+="<div class='user'>You: "+msg+"</div>";

fetch("/get",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

message:msg

})

})

.then(res=>res.json())

.then(data=>{

chat.innerHTML+="<div class='bot'>Bot: "+data.reply+"</div>";

chat.scrollTop=chat.scrollHeight;

});

input.value="";

}

document.getElementById("message").addEventListener("keypress",function(e){

if(e.key==="Enter"){

sendMessage();

}

});