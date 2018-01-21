$(document).ready(function () {
    var saleCreateForm = $('#sale-create-modal').find('#sale-create-form');
    var statusField = saleCreateForm.find('#id_status');
    var amountPaidField = saleCreateForm.find('#id_amount_paid');
    var amountBalanceField = saleCreateForm.find('#id_amount_balance');
    var rateField =  saleCreateForm.find('#id_rate');
    var unitsField =  saleCreateForm.find('#id_units');
    // showHint(amountPaidField);
    statusField.change(function () {
        console.log(statusField.val());
        if(statusField.val() == 'partly paid'){
            amountPaidField.removeAttr('disabled');
            amountBalanceField.attr('disabled', true)
        }else{
            amountPaidField.val(0);
            amountBalanceField.val(0);
            rateField.val('');
            unitsField.val('');
            revertDisableFields()
            // amountPaidField.attr('disabled', true);
            // amountBalanceField.attr('disabled', true)
        }
    });
    rateField.keyup(function () {
            calculateAmounts();
    });
    unitsField.keyup(function () {
            calculateAmounts();
    });
    amountPaidField.keyup(function () {
        calculateAmounts();
    });

    saleCreateForm.submit(function (event) {
        event.preventDefault();
        var thisForm = $(this);
        var action = thisForm.attr('action');
        var method = thisForm.attr('method');
        var disabledFields = thisForm.find('[disabled]');
        disabledFields.prop('disabled', false);
        var data = thisForm.serialize();
        console.log(action);
        $.ajax({
            url: action,
            method: method,
            data: data,
            success: function (data) {
                if(data.form_valid){
                    thisForm[0].reset();
                    thisForm.before("<div class='alert alert-success" +
                    " saved'><small>"+data.message+"</small></div>");
                    revertDisableFields();
                    setTimeout(function () {
                        $('.saved').hide();
                    }, 3000);
                    $('#sales-table').find('tbody').html(data.sale_list);
                    $('#day-sales').html(data.day_sales);
                    $('#week-sales').html(data.week_sales);
                    $('#comp-week-sales').html(data.fully_paid);
                    $('#credit-week-sales').html(data.not_paid);
                    $('#inc-week-sales').html(data.part_paid);

                } else {
                    thisForm.before("<div class='alert alert-warning" +
                    " saved'><small>OOps! Something went wrong.</small></div>");
                }
            },
            error: function (error) {
                console.log('didnt work');
            }
        })
    });

    $('#btn-edit-sale').click(function () {

        // $.ajax({
        //     url: $(this).attr('data-url'),
        //     method: 'get',
        //     beforeSend: function () {
        //         $('#sale-create-modal').modal('show');
        //     },
        //     success: function (data) {
        //         $('#sale-create-modal').find('.modal-body').html(data.form)
        //
        //     }
        // })
    });

    function calculateAmounts() {
        var price = parseInt(rateField.val()) * parseInt(unitsField.val());
        var partPrice = price - parseInt(amountPaidField.val());
        if(statusField.val() === 'fully paid'){
            amountPaidField.val(price);
            amountBalanceField.val(0)
        } else if(statusField.val() === 'partly paid'){
            // amountPaidField.val(price);
            amountBalanceField.val(partPrice)
        } else if(statusField.val() === 'not paid'){
            amountPaidField.val(0);
            amountBalanceField.val(price)
        } else {
            console.log('No value')
        }
    }

    function revertDisableFields() {
        amountPaidField.attr('disabled', true);
        amountBalanceField.attr('disabled', true)
    }
    function showHint(elem) {
        elem.hover(function () {
            console.log(elem);
            elem.before("<small><b>This field will be filled for yoy</b></small>")
        })
    }

});