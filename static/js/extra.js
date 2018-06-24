function fGetPin(x) {
//    alert($("#loadPinBTN").attr('IDLINE'));
    $.ajax({url: "/endpoints/line/getpin/"+x+"/",
                    success: function(result){
                        $("#LoginResult_Modal").html("โปรดกรอกรหัสนี้ : " + result + "<br> ใน Smart Phone ของคุณเพื่อเข้าระบบไลน์");
                    },
                    error: function(xmlReq, txtStatus, errThrown){
                        
                        $("#LoginResult_Modal").html(xmlReq.responseText + " <br> TextStatus " + txtStatus + " <br> errThrown" + errThrown);
                    }
                });
};
function myTimerGetPin(x) {
    
    

                setInterval(function()
                {
                    // console.log(' myTimerGetPin active each 1 second...');
                    $.ajax({url: "/endpoints/line/getpin/"+x+"/",
                   beforeSend:function(result){
                    $("#closeModal").hide();
                   },
                    success: function(result){
                        $("#LoginResult_Modal"+x).html("Success . . ." + result.responseText);
                            
                    },
                    complete:function(result){
                        $("#LoginResult_Modal"+x).html("โปรดกรอกรหัสนี้ในโทรศัพท์ของคุณ <br><center> (LINE Application)<br><br> " + result.responseText + "</center>");
                        $("#closeModal").show();
                      
                    },
                    error: function(xmlReq, txtStatus, errThrown){
                        $("#LoginResult_Modal"+x).html("โปรดลองใหม่. . .<br><br> <input type='button' value='รีโหลดเว็บเพจ' onClick='window.location.reload()'> <br><br>" + result.responseText);
                        $("#LoginResult_Modal"+x).html(xmlReq.responseText + " <br> TextStatus " + txtStatus + " <br> errThrown" + errThrown);
                       $("#closeModal").show();
                      }
                });
                }, 1000);
            

};

  $(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('.modal').modal({dismissible: false});

         
    // datatable for css class dbtable
    $('table').DataTable( {
      columnDefs: [
          {
              targets: [ 0, 1, 2 ],
              className: 'mdl-data-table__cell--non-numeric'
          }
      ]
  } );


  $("#loadPinBTN").click(function(){
    
    var id = $("#loadPinBTN").attr('IDLINE');
    fGetPin(id);
    
  });

  $(".btnLogin").click(function(){
    $(this).hide();
        




      var urlID = $(this).attr('lineID');
      //setInterval(myTimerGetPin(urlID),1000);
        $("#loadPinBTN").attr('IDLINE',urlID);
        $.ajax({url: "/endpoints/line/login/"+urlID+"/",
                   beforeSend:function(result){
                    $("#closeModal").hide();
                    $("#LoginResult_Modal"+urlID).html("Login! . . ." + result.responseText);
                   },
                    success: function(result){
                        $("#LoginResult_Modal"+urlID).html("Success . . ." + result.responseText);
                        
                    },
                    error: function(xmlReq, txtStatus, errThrown){
                        $("#LoginResult_Modal"+urlID).html("โปรดลองใหม่. . .<br><br> <input type='button' value='รีโหลดเว็บเพจ' onClick='window.location.reload()'> <br><br>" + result.responseText);
                        $("#LoginResult_Modal"+urlID).html(xmlReq.responseText + " <br> TextStatus " + txtStatus + " <br> errThrown" + errThrown);
                       $("#closeModal").show();
                      }
                });
       




        //alert($("#loadPinBTN").attr('IDLINE'));
      myTimerGetPin(urlID);
        
      });

    });
       