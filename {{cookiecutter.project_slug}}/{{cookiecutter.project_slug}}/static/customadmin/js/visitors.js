/*global $ */
'use strict';

var visitors = {

    // ------------------------------------------------------------------------

    visitor: {

        index: function () {
            $('#invite-table').DataTable({
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
                //     { data: 'responsible_individual', name: 'responsible individual' },
                //     { data: 'actions', name: 'actions' }
                // ],
            });

        },

        details: function () {

        }

    },

    // ------------------------------------------------------------------------

};
