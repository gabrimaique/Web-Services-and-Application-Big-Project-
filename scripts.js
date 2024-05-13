$(document).ready(function() {
    function fetchPubs() {
        $.ajax({
            url: '/api/pubs',
            type: 'GET',
            success: function(pubs) {
                var pubsList = $('#pubsList');
                pubsList.empty();
                pubs.forEach(function(pub) {
                    pubsList.append(
                        '<div class="pub-item">' +
                        '<p>Name: ' + pub.name + '</p>' +
                        '<p>Address: ' + pub.address + '</p>' +
                        '<p>Year Opened: ' + pub.year_opened + '</p>' +
                        '<p>Budget: ' + pub.budget + '</p>' +
                        '<p>Serve Food: ' + (pub.serve_food ? 'Yes' : 'No') + '</p>' +
                        '<p>Google Review: ' + pub.google_review + '</p>' +
                        '<p>Live Music: ' + (pub.live_music ? 'Yes' : 'No') + '</p>' +
                        '<button onclick="editPub(' + pub.id + ')">Edit</button>' +
                        '<button onclick="deletePub(' + pub.id + ')">Delete</button>' +
                        '</div>'
                    );
                });
            }
        });
    }

    $('#pubForm').submit(function(event) {
        event.preventDefault();
        var id = $('#pub_id').val();
        var url = '/api/pubs' + (id ? '/' + id : '');
        var method = id ? 'PUT' : 'POST';
        var formData = {
            name: $('#name').val(),
            address: $('#address').val(),
            year_opened: parseInt($('#year_opened').val(), 10),
            budget: parseFloat($('#budget').val()),
            serve_food: $('#serve_food').is(':checked'),
            google_review: parseFloat($('#google_review').val()),
            live_music: $('#live_music').is(':checked')
        };

        $.ajax({
            url: url,
            type: method,
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                alert(id ? 'Pub updated!' : 'Pub added!');
                fetchPubs();
                $('#pubForm').get(0).reset();  
                $('#pub_id').val(''); 
                $('#pubForm button[type=submit]').text('Add Pub'); 
            },
            error: function() {
                alert('Error processing your request.');
            }
        });
    });

    window.editPub = function(id) {
        $.getJSON('/api/pubs/' + id, function(pub) {
            $('#pub_id').val(pub.id);
            $('#name').val(pub.name);
            $('#address').val(pub.address);
            $('#year_opened').val(pub.year_opened);
            $('#budget').val(pub.budget);
            $('#serve_food').prop('checked', pub.serve_food);
            $('#google_review').val(pub.google_review);
            $('#live_music').prop('checked', pub.live_music);
            $('#pubForm button[type=submit]').text('Update Pub'); 
            // Scroll to the top of the page or form
            $('html, body').animate({
                scrollTop: $('#pubForm').offset().top - 10 // Slight offset to not stick tightly to the top
            }, 'slow');
        });
    };
    

    window.deletePub = function(pubId) {
        if (!confirm('Are you sure you want to delete this pub?')) return;
        $.ajax({
            url: '/api/pubs/' + pubId,
            type: 'DELETE',
            success: function(result) {
                alert('Pub deleted!');
                fetchPubs();
            }
        });
    };

    fetchPubs();  
});
