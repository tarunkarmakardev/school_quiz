$(document).ready( function (){

// CSRF function
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// Getting CSRF Token for POST requests:
const csrftoken = getCookie('csrftoken');

// Variables 
// Getting the submit, next and start quiz buttons

let submit_quiz_button = $('#submit_quiz');
let next_button = $('#next-question');
let start_quiz_button = $('.start_quiz');
let today = new Date();
let quiz_form = $('#quiz-question-form');

let table_entry = $('.quiz-results .table-entry')

let ques_num = $('.quiz-question .ques-num').data("ques-num")





// Disabling options when quiz_form is submitted: -----------------------------

// Setting status key in localstorage on clicks

submit_quiz_button.click(function (e) {
    localStorage.setItem("status", "submitted");
});

next_button.click(function () {
    localStorage.setItem("status", "" );
})

start_quiz_button.click(function (e) {
    localStorage.setItem("status", "");
});

// Fetching lastly stored status

let submit_status = localStorage.getItem("status");

// Getting all the MCQ answer choices:

let quiz_question_options = $('.quiz-question-option');

// Disabling choices selection when status is true or when answers were submitted:

if (Boolean(submit_status) === true ) {

    quiz_question_options.each(function () {

        $(this).prop("disabled", true);

    })
    

} else{
    
    quiz_question_options.each(function () {

        $(this).prop("disabled", false);

    })
}


// Recording Quiz attempt time:-------------------------------------------


if (ques_num == 1){
    console.log("Working");
    start_time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    localStorage.setItem("start_time", start_time);
    

}
else if(ques_num == 10){

    quiz_form.submit(function(){
        end_time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        localStorage.setItem("end_time", end_time);
        
        start_time = localStorage.getItem("start_time");
        end_time = localStorage.getItem("end_time");

        start_time = start_time.split(":");
        end_time = end_time.split(":");

        // Getting second values of start_time and end_time
        start_time = parseInt(start_time[0]*60*60) + parseInt(start_time[1]*60) + parseInt(start_time[2]);
        end_time = parseInt(end_time[0]*60*60) + parseInt(end_time[1]*60) + parseInt(end_time[2]);

        time_taken_secs = end_time - start_time;

        let hours = Math.floor(time_taken_secs/3600);
        let minutes = Math.floor((time_taken_secs - (hours*3600))/60);
        let seconds = Math.floor(time_taken_secs - (hours*3600) - (minutes*60));
        
        // Creating and appending time_taken_formatted string: 
        let time_taken_formatted = `${(hours<10?"0"+hours:hours)} hours ${(minutes<10?"0"+minutes:minutes)} mins ${(seconds<10?"0"+seconds:seconds)} s`
        
        localStorage.setItem("time_taken_formatted", time_taken_formatted);
    });
    
}

// Posting time_taken_formatted value to server:

let time_taken_formatted = localStorage.getItem("time_taken_formatted");

if(time_taken_formatted){
    // console.log("time_taken_formatted is available to send!");
    // console.log(time_taken_formatted);

    $('.quiz-results .time-taken').text("Time Taken: " + time_taken_formatted)



    url = $(location).attr('pathname')
    url = url.split('/')

    if(url.includes("display_quiz_results")){
        url = $(location).attr('pathname')
        $.ajax({
            headers: { "X-CSRFToken": csrftoken },
            type: "POST",
            url: url,
            data: {
                'time_taken_formatted': time_taken_formatted
            },
            success: function () {
                console.log("Done!");
                localStorage.setItem("time_taken_formatted", "");
                
            },
            error: function () {
                console.log("Failed!");
            }
        
        })
    }
    
}

// Giving serial numbers to any table entries:

table_entry.each(function(i) {
    $(this).text(i+1);
})


// Ending Document ready check
} );




