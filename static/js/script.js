$(document).ready(function () {
    var array_seats = $('.bench_number').map(function () {
        return $.trim($(this).text());
    }).get();

    var array_exempt_seats = $('.number_reserved_seats').map(function () {
        return $.trim($(this).text())
    }).get();

    for (var i = 0; i < array_exempt_seats.length; i++) {
        for (var j = 0; j < array_seats.length; j++) {
            if (array_exempt_seats[i] == array_seats[j]) {
                $('.bench_number').eq(array_exempt_seats[i] - 1).css({'background': 'red', 'cursor': 'not-allowed'})
            }
        }
    }
});


$(document).on('click', ".bench_number", function () {
    var value = $(this, ".bench_number");
    var seat_value = parseInt(value[0].innerHTML);
    alert(seat_value)
    var film_url = window.location.pathname.split("hall_film_detail/")[1];
    reserved_seat()
    function reserved_seat() {
        $.ajax({
            type: "GET",
            url: "/reserved/" + film_url + seat_value,
            data: {
                "reserved_seat": seat_value
            },
            dataType: "text",
            cache: false,

            success: function (data) {
                if (data == 'reserved') {
                    value.css('background', 'red')
                    alert('Seat is Reserved');
                }
                else if (data == 'seat_is_a_reserveted') {
                    alert('This Seat is Reserved!');
                }
            }
        })
    }
});
