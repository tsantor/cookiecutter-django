/*global $ */
'use strict';

var legaldocs = {

    // ------------------------------------------------------------------------
    legaldoc: {

        index: function () {
            $('#nda-table').DataTable({
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
                //     { data: 'first_name', name: 'first name' },
                //     { data: 'last_name', name: 'last name' },
                //     { data: 'title', name: 'title' },
                //     { data: 'company', name: 'company' },
                //     { data: 'email', name: 'email' },
                //     { data: 'phone', name: 'phone' },
                //     { data: 'actions', name: 'actions' }
                // ],
            });

        },

        details: function () {
            // $('.date-picker').datetimepicker({
            //     sideBySide: false,
            //     allowInputToggle: true,
            //     icons: {
            //         time: 'fa fa-clock-o',
            //         date: 'fa fa-calendar',
            //         up: 'fa fa-chevron-up',
            //         down: 'fa fa-chevron-down',
            //         previous: 'fa fa-chevron-left',
            //         next: 'fa fa-chevron-right',
            //         today: 'fa fa-calendar-o',
            //         clear: 'fa fa-trash',
            //         close: 'fa fa-close'
            //     }
            // });

        }

    },

    // ------------------------------------------------------------------------

    category: {

        index: function () {
            $('#ndacategory-table').DataTable({
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
                //     { data: 'first_name', name: 'first name' },
                //     { data: 'last_name', name: 'last name' },
                //     { data: 'title', name: 'title' },
                //     { data: 'company', name: 'company' },
                //     { data: 'email', name: 'email' },
                //     { data: 'phone', name: 'phone' },
                //     { data: 'actions', name: 'actions' }
                // ],
            });

        },

        details: function () {

        }

    },

};
