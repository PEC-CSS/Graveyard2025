async function Joke(type,cat){
    try{let res = await axios.get(`https://v2.jokeapi.dev/joke/${cat}?type=${type}`);
    return res;
    }
    catch(er){
        return -1
    }
}


function singleJoke(joke,i){
    const entry = document.createElement("h4");
    const br = document.createElement("br");
    entry.className +="curr";
    const node1 = document.createTextNode(`Joke${i}:`);
    const node2 = document.createTextNode(`${joke}`);
    entry.appendChild(node1);
    entry.appendChild(br);
    entry.appendChild(node2);

    const jokes = document.querySelector(".joke");
    jokes.appendChild(entry);
}
function twoPartJoke(setup,delivery,i){
    const entry = document.createElement("h4");
    const br1 = document.createElement("br");
    const br2= document.createElement("br");
    entry.className +="curr";
    const node1 = document.createTextNode(`Joke${i}:`);
    const node2= document.createTextNode(`SetUp: ${setup}`);
    const node3 = document.createTextNode(`Delivery: ${delivery}`);
    entry.appendChild(node1);
    entry.appendChild(br1);
    entry.appendChild(node2);
    entry.appendChild(br2);
    entry.appendChild(node3);

    const joke = document.querySelector(".joke");
    joke.appendChild(entry);
}



function displayRadioValue(name) {
    var ele = document.getElementsByName(name);
    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
            return ele[i].value;
    }
}

document.querySelector(".submit").addEventListener("click",async () =>{
    for(i of [1,2,3,4,5]){
        let li = document.querySelector(".curr");
        if(li){
            li.remove();
        }
    }
    let cat = displayRadioValue("category");
    let type = displayRadioValue("type");
    let n = displayRadioValue("number");

    
    if(type == "single"){
        for(let i = 1;i<=n*1;i++){
            let joke = await Joke(type,cat);
            if(joke != -1){
               singleJoke(joke.data.joke,i) 
               if(i == n*1){
                return;
               }  
            }
        }
    }else{
        for(let i = 1;i<=n*1;i++){
            let joke = await Joke(type,cat);
            if(joke != -1){
                twoPartJoke(joke.data.setup,joke.data.delivery,i) 
                if(i == n*1){
                 return;
                }  
            }
        }
    }
    
    const entry = document.createElement("h4");
    entry.className +="curr";
    const node1 = document.createTextNode(`No jokes were found that match your provided filter(s)`);
    entry.appendChild(node1);

    const jokes = document.querySelector(".joke");
    jokes.appendChild(entry);
    
    
})