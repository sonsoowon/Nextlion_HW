function ddayCount(val) {
    const now = new Date();
    const deadline = new Date(val);
    const diff = Math.ceil((deadline- now) / (1000 * 3600 * 24));

    let dday = "";
    if (diff < 0)
        dday = "D+" + Math.abs(diff);
    else if (diff == 0)
        dday = "D-day";
    else
        dday = "D-" + diff;
    
    document.querySelector(".dday h1").innerHTML = dday;
};