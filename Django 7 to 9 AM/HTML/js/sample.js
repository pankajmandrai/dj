function show()
            {
                alert("Don't Click Me Again and Again");
            }
function read()
{
    var name = document.getElementById("t1").value
    var len = name.length
    if(len == 0)
    {
        alert("Please enter name")
    }
    else
    {
        alert(name)
    }

}

function readName()
{
    var name = document.getElementById("t1").value

    document.getElementById("s1").innerText = name
}

function readNameNCount()
{
    var len = document.getElementById("t2").value.length
    if(len >= 8)
    {
        alert("Name must be 8 char's Only")
    }
    else {
        document.getElementById("s2").innerText = len
    }
}