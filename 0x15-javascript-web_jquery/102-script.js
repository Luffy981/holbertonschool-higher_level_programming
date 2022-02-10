$(function(){
  $('#btn_translate').click(function(){
    const language  = $('#language_code').val();
    $('#hello').text(language);
    $.ajax({
      url:"https://www.fourtonfish.com/hellosalut/hello/",
      data: {lang: language},
      success: function(result){
        $('#hello').text(result.hello);
      }
    });
  });
});
