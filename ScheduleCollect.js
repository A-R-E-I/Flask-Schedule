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
	var course1, course2
	limit = 8
	for(let i = 0; i < limit; i++)
	{
		alert("hi")
		course1 = document.getElementById("txtcoursename1").value;
		course2 = document.getElementById("txtcoursename2").value;
		if (course[i] == " ")
		{
			alert("Information is missing!");
			i = 8
			InitControls();
		}
	}
}
