async function getFacts(isoCode){
    try{let res = await axios.get(`https://restcountries.com/v3.1/alpha/${isoCode}`);
    return res;
    }
    catch(er){
        // console.log(er);
        return "XX"
    }
}

function addListItems(value,label,i){
    if(i == 0){
        const entry = document.createElement("li");
        entry.className +="curr";
        const node = document.createTextNode(`${label}: ${value}`);
        entry.appendChild(node);

        const list = document.querySelector(".list");
        list.appendChild(entry);
    }else if(i == 1){
        const entry = document.createElement("li");
        entry.className +="curr";
        let el = Object.values(value)[0].name;
        const node = document.createTextNode(`${label}: ${el}`);
        entry.appendChild(node);

        const list = document.querySelector(".list");
        list.appendChild(entry);
    }else{
        const entry = document.createElement("li");
        entry.className +="curr";
        let el = []
        i = 0
        Object.keys(value).forEach(key => {
            const values = value[key];
            el.push(values)
        });
        el2 = el.join(",")
        const node = document.createTextNode(`${label}: ${el2}`);
        entry.appendChild(node);

        const list = document.querySelector(".list");
        list.appendChild(entry);
        
    }
}

function notFound(){
    const entry = document.createElement("h3");
        entry.className +="curr";
        const node = document.createTextNode(`Country not found`);
        entry.appendChild(node);

        const list = document.querySelector(".details");
        list.appendChild(entry);
}

document.querySelector(".search").addEventListener("click",async () =>{
    for(i of [1,2,3,4,5]){
        let li = document.querySelector(".curr");
        console.log(li)
        if(li){
            li.remove();
        }
       
    }
    let iso = document.getElementById("ISO");
    let isoCode = iso.value;
    iso.value = "";
    if(isoCode == ""){
        return;
    }
    let data = await getFacts(isoCode);
    if(data == "XX"){
        notFound();
        return;
    }

    let labels = ["Country Name", "Region", "Capital", "Currency", "Languages"]
    
    addListItems(data.data[0].name.common,labels[0],0)
    addListItems(data.data[0].region,labels[1],0)
    addListItems(data.data[0].capital,labels[2],0)
    addListItems(data.data[0].currencies,labels[3],1)
    addListItems(data.data[0].languages,labels[4],2)
})
