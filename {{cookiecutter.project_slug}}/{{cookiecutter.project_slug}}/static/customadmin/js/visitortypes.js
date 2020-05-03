/*global $ */
'use strict';

var visitortypes = {

    // ------------------------------------------------------------------------
    visitortype: {

        index: function () {
            $('#visitortype-table').DataTable({
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
                nonSelectedListLabel: 'Available legal docs',
                selectedListLabel: 'Chosen legal docs',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });

        }

    },

    // ------------------------------------------------------------------------

};
