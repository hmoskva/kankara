$(document).ready(function () {
    var loadForm = function () {
        var thisBtn = $(this);
        $.ajax({
            url: thisBtn.attr('data-url'),
            method: 'get',
            beforeSend: function () {
                $("#sale-create-modal").modal("show");
            },
            success: function (data) {
                 $("#sale-create-modal").find('.modal-content').html(data.sale_form)
            },
            error: function (error) {
                console.log('not working')
            }

        })
    };

    var saveForm = function (event) {
        event.preventDefault();
      var form = $(this);
      $.post(form.attr('action'), form.serialize(), function (data) {
            if(data.saved){
                  form[0].reset();
                  $('#sale-create-modal').find('.modal-body').first().before("<div class='form-group saved'><div class='alert alert-success'>Success</div></div>");
                  setTimeout(function () {
                        $('.saved').hide();
                    }, 3000);
                  console.log('success')
              }
              else {
                  console.log('not saved')
              }
      });
      // $.ajax({
      //     url: form.attr('action'),
      //     method: form.attr('method'),
      //     data : form.serialize(),
      //     success: function (data) {
      //
      //     },
      //     error: function (error) {
      //         console.log('fail')
      //     }
      // })
    };

    $('#sale-action').click(loadForm);
    $("#sale-create-modal").on("submit", "#sale-create-form", saveForm);
});