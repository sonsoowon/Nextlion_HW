const now = new Date();

let today = ""
today = now.getFullYear() + "년 " + (now.getMonth() + 1) + "월 " + now.getDate() + "일";
document.querySelector("h2").innerHTML = today;