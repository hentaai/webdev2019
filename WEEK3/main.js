function todoList(){
	var list = document.querySelector("td")
	var kek = document.getElementById("todoList")
	var item = document.getElementById("todoInput").value
	var text = document.createTextNode(item)
	
	var newItem = document.createElement("tr")
	var newwItem = document.createElement("td")
	var newItem1 = document.createElement("input")
	var newItem2 = document.createElement("label")
	var newItem3 = document.createElement("button")
	newItem3.innerHTML = "delete"
	//newItem3.type = "button"
	//newItem3.setAttribute("onclick", "deleteData()")
	newItem3.onclick = function (){	
		this.parentElement.parentElement.parentElement.remove();	
	}

	

	var div = document.createElement("div")
	var div1 = document.createElement("div")
	var div2 = document.createElement("div")
		
	div.className = "first"
	div1.className = "second"
	div2.className = "third"

	newItem2.appendChild(text)
	
	newItem1.type = "checkbox"
	newItem1.onclick = function (){
		var tex = this.parentElement.parentElement.getElementsByClassName('second')[0]
		if (this.checked){
			tex.classList.add("tex")
		}
		else{
			tex.classList.remove("tex")
		}
	}

	div.appendChild(newItem1)
	div1.appendChild(newItem2)
	div2.appendChild(newItem3)
		
	newwItem.appendChild(div)
	newwItem.appendChild(div1)
	newwItem.appendChild(div2)


	
	kek.style.border = "2px solid black"
	
	if (list != null){
		newwItem.className = "rows"
	}
	newItem.appendChild(newwItem)
	document.getElementById("todoInput").value = ""
	document.getElementById("todoList").appendChild(newItem)
	var all = document.querySelector("tr")
	var i = 0
}


function deleteData(){

}