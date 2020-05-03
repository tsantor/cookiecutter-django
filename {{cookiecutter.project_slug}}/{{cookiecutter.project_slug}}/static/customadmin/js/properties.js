/*global $ */
'use strict';

var properties = {

    // ------------------------------------------------------------------------
    property: {

        index: function () {
            $('#property-table').DataTable({
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

        }

    },

    // ------------------------------------------------------------------------

};
