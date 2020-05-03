/*global $ */
'use strict';

var locations = {

    // ------------------------------------------------------------------------
    // Location
    // ------------------------------------------------------------------------
    location: {

        index: function () {
            $('#location-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                // processing: true,
                // serverSide: true,
                // ajax: {
                //     url: window.pagination_url,
                //     type: 'get',
                // },
                // columns: [
                //     { data: 'name', name: 'name' },
                //     { data: 'description', name: 'description' },
                //     { data: 'actions', name: 'actions' }
                // ],
            });

        },

        details: function () {

            $('.legal-docs-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Here are the available documents that the Visitor(s) will need to complete prior to your meeting. <br/>If you feel that a document is missing, please speak to your department\'s Legal Team.',
                selectedListLabel: 'Chosen legal docs<br/>&nbsp;',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });

        }

    },

    // ------------------------------------------------------------------------

};
