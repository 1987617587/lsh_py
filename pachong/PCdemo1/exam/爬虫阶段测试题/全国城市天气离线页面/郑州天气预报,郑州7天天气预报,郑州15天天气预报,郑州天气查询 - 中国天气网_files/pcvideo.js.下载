var timer = null
var domvideo = {}
  $('body').on('click','.videobox img', function(){
    initvideo()
    $('.videobox').css('display', 'none')
    var cut = 0
    timer = setInterval(function(){
      cut++
      $('.ggtime').text(10-cut)
      if(cut == 8 && ifie() < 9){
        $('.v_d').html('<script src="http://api.html5media.info/1.2.2/html5media.min.js"></script>')
        $('.v_d').append('<video src='+domvideo.url+' id="myvideo"  poster='+domvideo.img+'  autoplay="autoplay" controls="controls">'+
        '</video>')
      }
      if(cut == 10){
        $('.pc_guanggao').css('display', 'none')
        if(ifie() > 8){
          var v = $('#myvideo')
          v[0].play()
        }
        clearInterval(timer)
      }
    }, 1000)
  })
  $('.closegg').on('click', function(){
    $('.pc_guanggao').css('display', 'none')
    clearInterval(timer)
    var v = $('#myvideo')
    v[0].play()
  })
  function initvideo(){
    $.ajax({
      type: 'GET',
      url: 'http://e.weather.com.cn/pubm/videos_vms1.htm',
      dataType: 'jsonp',
      jsonpCallback: "getLbDatas",
      success:function (result) {
        domvideo.url = result.documents[0].videourl[0].url
        domvideo.img = result.documents[0].Photo
        $('.v_d').append('<video src='+result.documents[0].videourl[0].url+' id="myvideo"  poster='+result.documents[0].Photo+'  controls="controls">'+
        '</video>')
        var v = $('#myvideo')
        v[0].addEventListener('play',function(){
          $('.pausegg').css('display','none')
          $('.pausegg_close').css('display','none')
        });
        v[0].addEventListener('pause',function(){
          $('.pausegg').css('display','block')
          $('.pausegg_close').css('display','block')
        })
        $('.pausegg_close').on('click', function(){
          $('.pausegg').css('display','none')
          $(this).css('display','none')
        })
      },
      error:function(err){
        console.log(err)
      }
    })
  }
  function ifie(){ // 判断是否为IE11 因为视频地址原因  ie11需特殊处理
    var userAgent = navigator.userAgent;
    var isIE = userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1;
    var isIE11 = userAgent.indexOf('Trident') > -1 && userAgent.indexOf("rv:11.0") > -1;
     if(isIE) {
         var reIE = new RegExp("MSIE (\\d+\\.\\d+);");
         reIE.test(userAgent);
         var fIEVersion = parseFloat(RegExp["$1"]);
         if(fIEVersion == 7) {
             return 7
         }else if(fIEVersion == 8) {
             return 8
         }else if(fIEVersion == 9) {
             return 9
         }else if(fIEVersion == 10) {
             return 10
         }
     } else if(isIE11){
         return 11
     } else {
       return 12 //代表非IE
     }
  }
