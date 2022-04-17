$(function () {
    // - 右侧栏固定
    $(window).scroll(function () {
        let scrollTop = $(document).scrollTop();
        if (scrollTop > 70) {
            $(".introduce").css({
                top: scrollTop - 70,
            })
        }
    });

})