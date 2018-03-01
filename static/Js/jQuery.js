$(document).ready(function () {
    $('form').each(function (i, e) {
        if ($(this).data('product_id')){
                $(this).on('submit', function (e) {
                    e.preventDefault();
                    var form = $(this);
                    console.log(form);
                    var number = $('#number').val();
                    var submit = $(this);
                    var product_id = submit.data('product_id');
                    var product_name = submit.data('product_name');
                    var price = submit.data('price');
                    console.log(number);
                    console.log(product_id);
                    console.log(product_name);
                    console.log(price);
                    var is_delete=false;
                    basketUpdate(product_id, number, is_delete);


                });
        }
    });

    function basketUpdate(product_id, number, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.number = number;
        if (is_delete){
            data["is_delete"] = 'true'
        }
        var csrf_token = $('form [name = "csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = $('#form_buying_products').attr("action");
        console.log(is_delete);
        $.ajax({
            url: url,
            type: "POST",
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK');
                console.log(data.products_total_number);
                if (data.products_total_number) {
                    $('#basket_total_number').html("");
                    $('#basket_total_number').text('(' + data.products_total_number + ')');
                    $('.basket-item').html("");
                    $.each(data.products, function (k, v) {
                        $('.basket-item').append('<h4><li>' + v.name + ' ' + v.number + ' pieces ' + v.price + ' $  ' + '<label class="delete_item" data-product_id="'+ v.id + '">x</label></li></h4>');
                    });
                     $('.basket-item').append('<div class="checkout text-right">\n' +
                                                '                        <a href="/checkout/" class="text-right">\n' +
                                                '                       <button type="submit" class="btn btn-round">GO CART</button>\n' +
                                                '                        </a>\n' +
                                                '</div>');
                }
                else {
                    $('#basket_total_number').html("");
                    $('#basket_total_number').text('(0)');
                }

            },
            error: function () {
                console.log('Error')
            }

        });
    }

    $(document).on('click', '.delete_item', function (e) {
        e.preventDefault();
        product_id = $(this).data("product_id");
        number = 0;
        is_delete = true;
        basketUpdate(product_id, number, is_delete);
        $(this).closest('li').remove();
        $('.delete_basket_item').each(function () {
            $(document).ajaxComplete(function () {
                window.location.reload()
            })
        });

    });
    $(document).on('click', '.delete_basket_item', function (e) {
        e.preventDefault();
        product_id = $(this).data("product_id");
        number = 0;
        is_delete = true;
        basketUpdate(product_id, number, is_delete);
        $(this).closest('tr').remove();
        var nav_item =  $('.delete_item').find('[data-product_id = ' + product_id + ']');
        $(nav_item).closest('li').remove();
        var tr = 0;
        $('.delete.basket_item').each(function () {
            tr = parseFloat($(this).closest('tr').find('.price_all').replace(',', '.'));
            tr += tr;
        });
        if (tr==0){
            window.location.reload();
        }
    });

    $(document).on('change', '.product_number', function () {
        var product_number = parseInt($(this).val());
        var product_price_per_item = parseFloat($(this).closest('tr').find('.price_per_item').text().replace(',', '.'));
        var product_price_all = parseFloat(product_number * product_price_per_item).toFixed(2);
        $(this).closest('tr').find('.price_all').html('');
        $(this).closest('tr').find('.price_all').append('<h4>'+ product_price_all +'</h4>');

        Total_basket_amount()
    });

    $('select').on('change', function () {
        var price_for_delivery_type = parseFloat($(this, ':selected').val().replace(',', '.')).toFixed(2);
        $('.price_for_delivery_type').html('');
        $('.price_for_delivery_type').append('<h4>'+ price_for_delivery_type +'</h4>');

        Total_amount()
    });

    function Total_basket_amount() {
        var total_amount = 0;
        $('.price_all').each(function () {
            var total_product_amount = parseFloat($(this).text().replace(',', '.'));
            total_amount += total_product_amount
        });
        total_amount = parseFloat(total_amount).toFixed(2);
        $('.total_price').html('');
        $('.total_price').append(total_amount)
    }
    Total_basket_amount();

    function Total_amount() {
        var amount =parseFloat($('.price_for_delivery_type').text().replace(',', '.'));
        if ($('#form_contact').data('total_price')!=undefined){
            var total_price = parseFloat($('#form_contact').data('total_price').replace(',', '.'));
        }
        else {
            var total_price = parseFloat($('#form_contact').data('total_price'));
        }
        var total_amount = amount + total_price;
        $('.amount_price').html('');
        $('.amount_price').append('<h4>'+ total_amount +'</h4>');
    }

    Total_amount();

    $(".slider").each(function () {
        var obj = $(this);
        $(obj).append("<div class='nav'></div>");
        $(obj).find("li").each(function () {
            $(obj).find(".nav").append("<span rel='"+$(this).index()+"'></span>");
            $(this).addClass("slider"+$(this).index());
            var width = $(this).find('img').closest(".Image-responsive").css('width');
            $(obj).css({'width': width});
            $('.slider ul li').css({'width': width})
        });
        $(obj).find("span").first().addClass("on");
     });

    function sliderJS (obj, sl) {
        var ul = $(sl).find("ul");
        var bl = $(sl).find("li.slider" + obj);
        var step = $(bl).width();
        $(ul).animate({marginLeft: "-" + step * obj}, 500);
    }
    $(document).on("click", ".slider .nav span", function() {
        var sl = $(this).closest(".slider");
        $(sl).find("span").removeClass("on");
        $(this).addClass("on");
        var obj = $(this).attr("rel");
        sliderJS(obj, sl);
        return false;
    });
    $(document).on("click", ".slider .slick-arrow", function () {
        var sl = $(this).closest(".slider");
        var obj = $(sl).find("span").closest(".on").attr('rel');
        $(sl).find("span").removeClass("on");
        if ($(this).is('.slick-prev')){
            obj--;
            if ($(sl).find('span').is("[rel = " + obj + "]")) {
                var li = $(sl).find('[rel = ' + obj + ']');
                $(li).addClass("on");
            } else {
                var nmb = -1;
                $(sl).find('span').each(function () {
                    nmb++;
                });
                var li = $('[rel = ' + nmb + ']');
                $(li).addClass("on");
                obj = nmb
            }
        }else
        {
            obj++;
            if ($(sl).find('span').is("[rel = " + obj + "]")) {
                var li = $(sl).find('[rel = ' + obj + ']');
                $(li).addClass("on");
            } else {
                var li = $('[rel = ' + 0 + ']');
                $(li).addClass("on");
                obj = 0
            }
        }

        sliderJS(obj, sl);
        return false;
    });
    $('#payment').on('submit', function () {
        alert('Thank you for your order.\n We will get in touch with youp soon:)')
    });

    $('input[id="phone"]').mask('9 999 999 99 99');
    $('input[name="number_cart"]').mask('9999 9999 9999 9999');
    $('input[name="expiry"]').mask('99/99');
    $('input[name="cvc"]').mask('999');
});
