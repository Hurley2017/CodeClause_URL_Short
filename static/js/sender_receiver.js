var call = document.querySelector(".request");
call.addEventListener("click", runapp);
function runapp(e)
{
    e.preventDefault();
    var URL= document.getElementById("URL").value;
    const doc = {"URL":URL};
    const jdoc = JSON.stringify(doc);
    $.ajax({
        url:"https://www.ayeee.ga/send",
        type:"POST",
        contentType:"application/json",
        data:jdoc,
        async: false,
        success: function(msg)
        {
            document.getElementById("pushout").innerHTML = `<fieldset>
                                                            <textarea id='output' name='message' rows='3' class='form-control' placeholder='nada'>`+ msg + `</textarea>
                                                            </fieldset>
                                                            <div class="col-lg-12">
                                                            <fieldset>
                                                            <button type="button" id="copy-button" onclick="copyme()" class="main-button center-text request">Copy Me</button>
                                                            </fieldset>
                                                            </div>`;
        }
    })
}
function copyme()
{
    var msg = document.getElementById("output");
    copyToClipboard(msg);
    var button = document.getElementById("copy-button");
    button.innerHTML = "Copied!";
    setTimeout(function() {
        button.innerHTML = "Copy Me";
    }, 2000);
}
function copyToClipboard(elem)
{
    navigator.clipboard.writeText(elem.innerHTML);
}