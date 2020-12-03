function btndisplay(i1){
    document.getElementById(i1).style.display="block";
}

function display(i1,i2,i3) {
    document.getElementById(i1).style.display="block";
    document.getElementById(i2).style.display="block";
    document.getElementById(i3).style.display="block";
    // alert(document.getElementById("slct1").value)
}

function show(i1,i2,i3) {
    // alert(document.getElementById("slct").value)
    var array=["English","Hindi","Punjabi"];
    var ar=["en","hi","pa"]
    var ip=document.getElementById("slct");
    var op=document.getElementById("slct1");
    var a=document.getElementById("op1");
    var b=document.getElementById("op2");
    if(ip.value=="en"){
        a.innerHTML=array[1];
        b.innerHTML=array[2];
        a.value=ar[1];
        b.value=ar[2];
    }
    else if(ip.value=="hi"){
        // alert("hello")
        a.innerHTML=array[0];
        b.innerHTML=array[2];
        a.value=ar[0];
        b.value=ar[2];
    }
    else{
        // alert("bhoot")
        a.innerHTML=array[0];
        b.innerHTML=array[1];
        a.value=ar[0];
        b.value=ar[1];
    }
document.getElementById(i1).style.display="block";
document.getElementById(i2).style.display="block";
document.getElementById(i3).style.display="flex";
}

function validate()
{
    var iplang=document.getElementById("slct").value;
    var oplang=document.getElementById("slct1").value;
    var file=document.getElementById("fileip").value;
    var text=document.getElementById("iptext").value;
    if(file=="" && text!="")
    {
        // alert("textchoosen")
        return true;
    }
    else if(file=="" && text=="")
    {
        alert("UPLOAD FILE OR TYPE TEXT");
        return false;
    }
    else if (file!="" && text=="")
    {   
        // alert("file choosen");
        return true;
    }
    else if(file!="" && text!="")
    {
        alert("UPLOAD IMAGE OR TYPE TEXT BUT NOT BOTH");
        return false;
    }
}