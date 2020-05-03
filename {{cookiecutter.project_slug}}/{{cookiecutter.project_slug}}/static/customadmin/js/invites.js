/*global $ */
'use strict';

var invites = {

    // ------------------------------------------------------------------------
    invite: {

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
                //     { data: 'description', name: 'description' },
                //     { data: 'actions', name: 'actions' }
                // ],
            });

        },

        details: function () {

            $('.date-picker').datetimepicker({
                sideBySide: false,
                allowInputToggle: true,
                icons: {
                    time: 'fa fa-clock-o',
                    date: 'fa fa-calendar',
                    up: 'fa fa-chevron-up',
                    down: 'fa fa-chevron-down',
                    previous: 'fa fa-chevron-left',
                    next: 'fa fa-chevron-right',
                    today: 'fa fa-calendar-o',
                    clear: 'fa fa-trash',
                    close: 'fa fa-close'
                }
            });

            // $('#datetimepicker1').datetimepicker({
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

            // $('.typeahead').typeahead({
            //     source: [
            //         { "name": "Boyles, Jeffrey", "value": "2" },
            //         { "name": "Puglisi, Nick", "value": "1" },
            //         { "name": "Sifre, Linette", "value": "3" },
            //     ]
            // });

            function getDisplay(data, id) {
                for (var i = 0; i < data.length; i++) {
                    var x = data[i];
                    console.log(x)
                    if (x["id"] == id) {
                        return x["select_name"];
                    }
                }
            }

            $.get('/api/v1/core/hosts/', function (data) {
                $('input[id="id_host_search"]').val(
                    getDisplay(data, $('input[id="id_host"]').val())
                );
                $(".typeahead").typeahead({
                    source: data.data,
                    displayText: function (item) {
                        return item.select_name;
                    },
                    afterSelect: function (item) {
                        // this.$element[0].value = item.id;
                        $('input[id="id_host"]').val(item.id);
                    }
                });
            }, 'json');

            $('.legal-docs-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Here are the available documents that the Visitor(s) will need to complete prior to your meeting. <br/>If you feel that a document is missing, please speak to your department\'s Legal Team.',
                selectedListLabel: 'Chosen legal docs<br/>&nbsp;',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });

            // $(".location-select").select2({
            //     theme: 'bootstrap4',
            // });
        }

    },

    // ------------------------------------------------------------------------

};
