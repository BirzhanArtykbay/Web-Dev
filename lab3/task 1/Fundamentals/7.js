//ex 1
if ("0") {
    alert( 'Hello' );
}

//ex 2

//ex 3
let value = prompt('Type a number', 0);

if (value > 0) {
    alert( 1 );
} else if (value < 0) {
    alert( -1 );
} else {
    alert( 0 );
}

//ex 4
let result = (a + b < 4) ? 'Below' : 'Over';

//ex 5
let message = (login == 'Employee') ? 'Hello' :
    (login == 'Director') ? 'Greetings' :
        (login == '') ? 'No login' :
            '';