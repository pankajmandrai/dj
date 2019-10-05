

function fun1() {


    res1 = document.getElementById("name").value
    len = res1.length
    document.getElementById("count").innerText = len
}

function fun2() {
    ans = document.getElementById("password").value.length
    if (ans < 8)
    {
        document.getElementById("red").innerText = "Weak"
        document.getElementById("blue").innerText = ""
        document.getElementById("yellow").innerText = ""
    }
    else
    {
        if (ans == 8)
        {
            document.getElementById("blue").innerText = "Good"
            document.getElementById("red").innerText = ""
            document.getElementById("yellow").innerText = ""
        }
        else
        {
            document.getElementById("yellow").innerText = "Strong"
            document.getElementById("blue").innerText = ""
            document.getElementById("red").innerText = ""
        }
    }

}