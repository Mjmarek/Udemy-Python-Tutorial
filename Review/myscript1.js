var hot = false
var temp = 15

if  (temp>80) {
  console.log("Hot outside!");    
}else if (temp <= 80 && temp >= 50) {
  console.log("Average temp outside");  
}else if (temp < 50 && temp >= 32) {
  console.log("It's pretty cold outside.");  
}else {
  console.log("It's freezing outside!");  
}

