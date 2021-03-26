// Verify email
const emailKEY = '79bc1a63cacf35cf76dc58fc3e07070e';
let email = document.getElementById("CustomerEmailId");

email.addEventListener('blur', ()=> {
    let email = document.getElementById("CustomerEmailId");
    let emailId = email.value;
    const API = `https://apilayer.net/api/check?access_key=${emailKEY}&email=${emailId}`;

    const xhr = new XMLHttpRequest();
    xhr.open('GET', API, true);
    xhr.getResponseHeader('Content-type', 'application/json');

    xhr.onprogress = function () {
        //  add spinner while verifying
    }
    xhr.onload = function() {
        if (this.status == 200)  {
            const verificationResponse = JSON.parse(this.responseText);
            let disposable = verificationResponse.disposable;
            let smtp = verificationResponse.smtp_check;

            if (smtp && !disposable) {
                email.classList.remove('is-invalid');
                email.classList.add('is-valid');
            }
            else {
                email.classList.remove('is-valid');
                email.classList.add('is-invalid');
            }
        }
    }

    xhr.send();
});


// Verify Phone
const phoneKEY = '869f4e2951d11d929ead4481e85dd95d';
let phone = document.getElementById("CustomerPhNum");

phone.addEventListener('blur', ()=> {
    let phone = document.getElementById("CustomerPhNum");
    let phNumber = phone.value;
    const API = `http://apilayer.net/api/validate?access_key=${phoneKEY}&number=${phNumber}&country_code=IN`

    const xhr = new XMLHttpRequest();
    xhr.open('GET', API, true);
    xhr.getResponseHeader('Content-type', 'application/json');

    xhr.onprogress = function () {
        //  add spinner while verifying
    }
    xhr.onload = function() {
        if (this.status == 200)  {
            const verificationResponse = JSON.parse(this.responseText);
            let valid = verificationResponse.valid;

            if (valid) {
                phone.classList.remove('is-invalid');
                phone.classList.add('is-valid');
            }
            else {
                phone.classList.remove('is-valid');
                phone.classList.add('is-invalid');
            }
        }
    }

    xhr.send();
});