function constructTable(selector) {

    // Delete the all unnecessary columns
    for (var i = 0; i < PLAYGROUNDS.length; i++) {
        delete PLAYGROUNDS[i]['PhotoSummer'];
        delete PLAYGROUNDS[i]['HelpPhoneExtension'];
        delete PLAYGROUNDS[i]['WorkingHoursSummer'];
        delete PLAYGROUNDS[i]['ClarificationOfWorkingHoursSummer'];
        delete PLAYGROUNDS[i]['EquipmentRentalComments'];
        delete PLAYGROUNDS[i]['TechServiceComments'];
        delete PLAYGROUNDS[i]['DimensionsSummer'];
        delete PLAYGROUNDS[i]['geoData'];
        delete PLAYGROUNDS[i]['geodata_center'];

    }
    // Getting the all column names
    var cols = Headers(PLAYGROUNDS, selector);

    // Traversing the JSON data
    for (var i = 0; i < PLAYGROUNDS.length; i++) {
        var row = $('<tr/>');
        for (var colIndex = 0; colIndex < cols.length; colIndex++) {
            var val = PLAYGROUNDS[i][cols[colIndex]];

            // If there is any key, which is matching
            // with the column name
            if (val == null) val = "";
            row.append($('<td/>').html(val));
        }

        // Adding each row to the table
        $(selector).append(row);
    }
}

function Headers(PLAYGROUNDS, selector) {
    var columns = [];
    var header = $('<tr/>');

    for (var i = 0; i < PLAYGROUNDS.length; i++) {
        var row = PLAYGROUNDS[i];

        for (var k in row) {
            if ($.inArray(k, columns) == -1) {
                columns.push(k);

                // Creating the header
                header.append($('<th/>').html(k + "&nbsp;&nbsp;&nbsp;&#8693;"));
            }
        }
    }

    // Appending the header to the table
    $(selector).append(header);
    return columns;
}