if(localStorage.getItem("names") == null){
    localStorage.setItem("names", JSON.stringify([]));
}
let allTasks = JSON.parse(localStorage.getItem("names"));
console.log(allTasks)
let task = allTasks;

var list = document.getElementById('tasks');

for(i in allTasks){
    var entry = document.createElement('li');

    // entry.appendChild(document.createTextNode(allTasks[i]));
    list.appendChild(entry);
    
    var comp = document.createElement('button');
    var del = document.createElement('button');

    comp.appendChild(document.createTextNode("Mark as completed"));
    // list.appendChild(comp);

    del.appendChild(document.createTextNode("Delete"));
    // list.appendChild(del);

    var container = document.createElement('div');
    container.className += `task `
    var div1 = document.createElement('div');
    var div2 = document.createElement('div');
    container.appendChild(div1)
    container.appendChild(div2)
    entry.appendChild(container)

    if(allTasks[i][0] == "`"){
        comp.innerHTML = "Completed"
        div1.appendChild(document.createTextNode(allTasks[i].slice(1)));
        comp.disabled = true;
    }else{
        div1.appendChild(document.createTextNode(allTasks[i]));
    }
    div2.appendChild(comp);
    div2.appendChild(del);

    comp.className += `comp `
    del.className += `del`
}

function addListItem(){
    let newTask = document.querySelector("input");
    let name = newTask.value;
    if(name == ""){
        return;
    }
    task.push(name)

    localStorage.setItem("names", JSON.stringify(task));
    var allTasks = JSON.parse(localStorage.getItem("names"));

    console.log(allTasks)
    var entry = document.createElement('li');
    // entry.appendChild(document.createTextNode(name));
    list.appendChild(entry);
    
    var comp = document.createElement('button');
    var del = document.createElement('button');

    comp.appendChild(document.createTextNode("Mark as completed"));
    list.appendChild(comp);

    del.appendChild(document.createTextNode("Delete"));
    list.appendChild(del);

    
    var container = document.createElement('div');
    container.className += `task `
    var div1 = document.createElement('div');
    var div2 = document.createElement('div');
    container.appendChild(div1)
    container.appendChild(div2)
    entry.appendChild(container)

    div1.appendChild(document.createTextNode(name));
    div2.appendChild(comp);
    div2.appendChild(del);
    

    comp.className += `comp `
    del.className += `del`

    newTask.value = ""
    let delBtn = document.getElementsByClassName("del");

    for(b of delBtn){
        b.addEventListener("click", deleteItem);
    }
    
    let compBtn = document.getElementsByClassName("comp");

    for(c of compBtn){
        c.addEventListener("click", completed);
    }
}


function deleteItem(){
    let li = this.parentElement.parentElement.parentElement
    let text = li.children[0].children[0].innerHTML
    task = task.filter(item => item !== text);
    task = task.filter(item => item !== "`"+text);
    localStorage.setItem("names", JSON.stringify(task));
    // console.log(task)
    li.remove(); 
}

function completed(){
    this.innerHTML = "Completed"
    let li = this.parentElement.parentElement.parentElement
    let text = li.children[0].children[0].innerHTML
    newTask = task.filter(item => item !== text);
    if(newTask.length != task.length){
        newTask.push("`"+text)
    }
    // localStorage.setItem("names", JSON.stringify(task));
    console.log(newTask)
    localStorage.setItem("names", JSON.stringify(newTask));
    this.disabled = true;
    
}

document.querySelector(".add").addEventListener("click", addListItem);

let delBtn = document.getElementsByClassName("del");

for(b of delBtn){
    b.addEventListener("click", deleteItem);
}

let compBtn = document.getElementsByClassName("comp");

for(c of compBtn){
    c.addEventListener("click", completed);
}

// localStorage.clear()