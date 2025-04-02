window.addEventListener("load",InitControls);
window.addEventListener("load",addListener);

function InitControls()
{
	document.getElementById("txtcoursename1").textContent = "";
	document.getElementById("txtteacher1").textContent = "";
	document.getElementById("txtroom1").textContent = "";
	
	document.getElementById("txtcoursename2").textContent = "";
	document.getElementById("txtteacher2").textContent = "";
	document.getElementById("txtroom2").textContent = "";
	
	document.getElementById("txtcoursename3").textContent = "";
	document.getElementById("txtteacher3").textContent = "";
	document.getElementById("txtroom3").textContent = "";
	
	document.getElementById("txtcoursename4").textContent = "";
	document.getElementById("txtteacher4").textContent = "";
	document.getElementById("txtroom4").textContent = "";
	
	document.getElementById("txtcoursename5").textContent = "";
	document.getElementById("txtteacher5").textContent = "";
	document.getElementById("txtroom5").textContent = "";
	
	document.getElementById("txtcoursename6").textContent = "";
	document.getElementById("txtteacher6").textContent = "";
	document.getElementById("txtroom6").textContent = "";
	
	document.getElementById("txtcoursename7").textContent = "";
	document.getElementById("txtteacher7").textContent = "";
	document.getElementById("txtroom7").textContent = "";
	
	document.getElementById("txtcoursename8").textContent = "";
	document.getElementById("txtteacher8").textContent = "";
	document.getElementById("txtroom8").textContent = "";
}

function addListener()
{
	document.getElementById("btnenter").addEventListener("click",CheckInfo);
}

function CheckInfo()
{
	
	limit = 8
	
	for(let i = 1; i < limit; i++)
	{ 
		
		let course = document.getElementById("txtcoursename" + String(i)).value;
		alert(course)
		if (course == "")
		{
			alert("Information is missing!");
			break;
		}
	}
}
