console.log("start home.js");
// Email verify
email = document.getElementById("CustomerEmailId");
let API = `https://apilayer.net/api/check? access_key = YOUR_ACCESS_KEY& ${email.value}`;
console.log("end home.js");