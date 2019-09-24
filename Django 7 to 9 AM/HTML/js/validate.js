
function validate_password()
{
    var len = document.getElementById("p1").value.length;

    if(len < 8)
    {
        document.getElementById("s1").innerText = "Poor"
        document.getElementById("s2").innerText = ""
        document.getElementById("s3").innerText = ""
    }
    else {
        if (len > 8) {
            document.getElementById("s1").innerText = ""
        document.getElementById("s2").innerText = ""
        document.getElementById("s3").innerText = "Strong"
        }
        else {
           document.getElementById("s1").innerText = ""
        document.getElementById("s2").innerText = "Good"
        document.getElementById("s3").innerText = ""
        }
    }

}