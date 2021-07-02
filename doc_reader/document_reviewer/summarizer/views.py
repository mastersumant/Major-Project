# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from summarizer.final_code import main
import os
from subprocess import Popen
import PyPDF2
import io

@csrf_exempt
def check_med(request): 
     if request.method != 'POST': 
        return HttpResponse(form_page)
     print("5")
     title=request.POST.get('summary_title',False)
    #  if request.method == 'POST' and request.FILES['pdf']:

    #     pdfFileObj = request.FILES['pdf'].read() 
    #     pdfReader = PyPDF2.PdfFileReader(io.BytesIO(pdfFileObj))
    #     NumPages = pdfReader.numPages
    #     i = 0
    #     content =""
    #     while (i<NumPages):
    #         text = pdfReader.getPage(i)
    #         content+=text.extractText()
    #         i +=1
    #     with open(os.path.join("summarizer\\1.txt"), 'wb') as destination:
    #       content+='\n\n'
    #       destination.write(content.encode())
    #     print(content)
     if request.method == 'POST' and request.FILES['text']:    
        with open(os.path.join("summarizer\\1.txt"), 'wb+') as destination:
          for chunk in request.FILES['text'].chunks():
            destination.write(chunk)
     
     summary,l_before=main()
     l_after=len(summary.strip().split())
    #  print(summary)
     if (not summary):
         summary='No summary found'
     else:
        pass
     context={'title':title ,'summary':summary,'length_before':l_before,'length_after':l_after}
     print("Number of word in original document {}".format(l_before))
     print("Number of word in summary {}".format(l_after))
     return render(request,"summary.html",context)
     
# def about(request):
#     file_n=main()
#     context={'summary':file_n}
#     return render(request,'about.html',context)


form_page="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary Uploader</title>
    <style>
        
body {
  height: auto;
    width: auto;
    background-image: url("http://www.manitowoclibrary.org/wp-content/uploads/2014/12/CO_BACKGROUND-BOOKS.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
  display: flex;
  flex-direction: column;
  padding: 20px;
  position: relative;
}

.wrapper  {
  background-color: #fff;
  padding: 25px;
  border-radius: 5px;
  width: 360px;
  max-width: 100%;
  margin: 50px auto;
  align-self: center;
  box-sizing: border-box;
}

header {
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
  margin-bottom: 20px;
  display: flex;
}
h1 {
  flex: 1;
  padding: 0;
  margin: 0;
  font-size: 16px;
  letter-spacing: 1px;
  font-weight: 700;
  color: #7A7B7F;
}
header span {
  flex: 1;
  text-align: right;
  font-size: 12px;
  color: #999;
}
.ways ul {
  display: flex;
  list-style: none;
  padding: 0;
  border-radius: 5px;
  overflow: hidden;
}
.ways li {
  align-self: center;
  flex: 1;
  background-color: #F5F7FA;
  text-align: center;
  cursor: pointer;
  padding: 15px 0;
  color: #999;
  text-transform: uppercase;
  font-weight: 500;
  font-size: 12px;
  letter-spacing: 1px;
  border: 1px solid #ddd;
}

.ways li:first-child {
  border-right: 0;
}
.ways li:last-child {
  border-left: 0;
}
.ways li.active {
  border: 2px solid #1AA1E5;
  color: #66676C;
}
.ways li.active::before {
  content: '\f00c';
  font-family: 'fontawesome';
  color: #1AA1E5;
}
.ways li:not(.active) {
  padding: 16px 0;
}
section {
  display: none;
}
section.active {
  display: block;
}
section input,
section textarea {
  display: block;
  width: 100%;
  box-sizing: border-box;
  border: 1px solid #ddd;
  outline: 0;
  background-color: #F5F7FA;
  padding: 10px;
  margin-bottom: 10px;
  letter-spacing: 1.4px;
}
section textarea {
  min-height: 200px;
}
section select {
  display: none;
}

.select-option {
  background-color: #F5F7FA;
  color: #999;
  font-size: 15px;
  position: relative;
  cursor: pointer;
}
.select-option::before {
  content: '\f107';
  font-family: 'fontawesome';
  position: absolute;
  right: 0;
  top: 0;
  margin-top: 9px;
  margin-right: 10px;
  font-size: 20px;
}
.select-option div:not(.option) {
  padding: 10px 10px;
  border: 1px solid #ddd;
}
.select-option div:last-child,
.select-option .head {
  border-bottom: 1px solid #ddd;
}
.select-option .option {
  display: none;
}
.select-option .option div {
  text-transform: capitalize;
}
.select-option.active .option {
  display: block;
  position: absolute;
  width: 100%;
  background-color: #F5F7FA;
  box-sizing: border-box;
  padding: 0;
  margin-top: -1px;
  z-index: 2;
}
.select-option .option div {
  border-bottom: 0;
}
.images {
  display: flex;
  flex-wrap:  wrap;
  margin-top: 20px;
}
.images .img,
.images .pic {
  flex-basis: 31%;
  margin-bottom: 10px;
  border-radius: 4px;
}
.images .img {
  width: 112px;
  height: 93px;
  background-size: cover;
  margin-right: 10px;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.images .img:nth-child(3n) {
  margin-right: 0;
}
.images .img span {
  display: none;
  text-transform: capitalize;
  z-index: 2;
}
.images .img::after {
  content: '';
  width: 100%;
  height: 100%;
  transition: opacity .1s ease-in;
  border-radius: 4px;
  opacity: 0;
  position: absolute;
}
.images .img:hover::after {
  display: block;
  background-color: #000;
  opacity: .5;
}
.images .img:hover span {
  display: block;
  color: #fff;
}
.images .pic {
  background-color: #F5F7FA;
  align-self: center;
  text-align: center;
  padding: 40px 0;
  text-transform: uppercase;
  color: #848EA1;
  font-size: 12px;
  cursor: pointer;
}

@media screen and (max-width: 400px) {
  .wrapper {
    margin-top: 0;
  }
  header {
    flex-direction: column;
  }
  header span {
    text-align: left;
    margin-top: 10px;
  }
  .ways li,
  section input, 
  section textarea,
  .select-option .head, 
  .select-option .option div {
   font-size: 8px;
  }
  .images .img,
  .images .pic {
    flex-basis: 100%;
    margin-right: 0;
  }
}

.wrapper footer ul {
  margin: 0;
  margin-top: 30px;
  display: flex;
  list-style: none;
  padding: 0;
}
.wrapper footer ul li {
  flex: 1;
}
.wrapper footer li span {
  text-transform: capitalize;
  cursor: pointer;
}
.wrapper footer li:first-child {
  color: #999;
  text-align: left;
  font-size: 12px;
}
.wrapper footer li:first-child span {
  display: inline-block;
  border-bottom: 1px solid #ddd;
}
.wrapper footer li:last-child {
  text-align: right;
}
.wrapper footer li:last-child span {
  background-color: #22A4E6;
  padding: 10px 20px;
  color: #fff;
  border-radius: 3px;
}

.notification {
  position: absolute;
  left: 20px;
  bottom: 20px;
  top: auto;
  right: auto;
}

.notification p {
  margin: 0;
  padding: 0;
}
.notification .btn {
  padding: 16px 20px;
  border-radius: 5px;
  display: flex;
  margin-bottom: 10px;
  font-size: 12px;
  align-items: center;
  animation: fadeIn .4s ease-in;
}
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
.notification .btn::before {
  margin-right: 12px;
  font-family: 'fontawesome';
  font-size: 15px;
}
.notification span {
  margin-left: 10px;
  cursor: pointer;
  flex: 1;
  text-align: right;
}

.notification .error {
  background-color: #ECC8C5;
  border: 1px solid #BD8181;
}
.notification .error span {
  color: #C79995;
}
.notification .error::before {
  content: '\f05c';
  color: #B2312F;
  
}
.notification .success {
  background-color: #DEF2D6;
  border: 1px solid #B3CEA9;
}
.notification .success span {
  color: #AFC7A7;
}
.notification .success::before {
  content: '\f00c';
  color: #5A7052;
}

footer {
  text-align: center;
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #fff;
  font-size: 12px;
}
footer a {
  color: #fff;
  text-decoration: none;
  border-bottom: 1px solid #fff;
  padding-bottom: 5px;
}
    </style>
</head>
<body>
<div class="wrapper">
  <header>
    <h1>Summarizer</h1>
    <span>ID: 5988014</span>
  </header>
  
  <div class="ways">
    <ul>
      <li class="active">
        submit
      </li>
      <li>
        discussion
      </li>
    </ul>
  </div>
  <div class="sections">
    <form  action="http://127.0.0.1:8000/summary/" id="mForm"  method="post"  enctype="multipart/form-data">
    <section class="active">
      <input  placeholder="Title" id="title" name="summary_title" requiered >
   
      
      
      <div class="images" >
        <input type="file"  name="text" id="input1" accept=".txt" >
      </div>  
      
      
      
    </section>

    <section>
      <input type="text" placeholder="Topic" id="topic"/>
      <textarea placeholder="something..." id="msg"></textarea>
    </section>
  
  </div>
  
  <footer>
    <ul>
      <li><input class="btn btn-up" type="reset" id="reset" value="Reset"></li>
      <li><input class="btn btn-up" type="submit" value="Submit"></li>
    </ul>
  </footer> 
  </form>
</div>
    <script type="text/javascript">
    $(function() {
    $('#input1').focus(function(){
      $('#input2').prop('disabled', 'disabled');
    }).blur(function(){
     $('#input2').prop('disabled', '');
    });
    
    $('#input2').focus(function(){
      $('#input1').prop('disabled', 'disabled');
    }).blur(function(){
     $('#input1').prop('disabled', '');
    });
});
        (function ($) {
  $(document).ready(function () {
    
    generateID()
    choose()
    generateOption()
    selectionOption()
    removeClass()
    uploadImage()
    submit()
    resetButton()
    removeNotification()
    autoRemoveNotification()
    autoDequeue()
    
    var ID
    var way = 0
    var queue = []
    var fullStock = 10
    var speedCloseNoti = 1000
    
    function generateID() {
      var text = $('header span')
      var newID = ''
    
      for(var i = 0; i < 3; i++) {
        newID += Math.floor(Math.random() * 3)
      }
      
      ID = 'ID: 5988' + newID
      text.html(ID)
    }
    
    function choose() {
      var li = $('.ways li')
      var section = $('.sections section')
      var index = 0
      li.on('click', function () {
        index = $(this).index()
        $(this).addClass('active')
        $(this).siblings().removeClass('active')
        
        section.siblings().removeClass('active')
        section.eq(index).addClass('active')
        if(!way) {
          way = 1
        }  else {
          way = 0
        }
      })
    }
    
    function generateOption() {
      var select = $('select option')
      var selectAdd = $('.select-option .option')
      $.each(select, function (i, val) {
          $('.select-option .option').append('<div rel="'+ $(val).val() +'">'+ $(val).html() +'</div>')
      })
    }
    
    function selectionOption() {
      var select = $('.select-option .head')
      var option = $('.select-option .option div')
    
      select.on('click', function (event) {
        event.stopPropagation()
        $('.select-option').addClass('active')
      })
      
      option.on('click', function () {
        var value = $(this).attr('rel')
        $('.select-option').removeClass('active')  
        select.html(value)
    
        $('select#category').val(value)
      })
    }
    
    function removeClass() {
      $('body').on('click', function () { 
        $('.select-option').removeClass('active')   
      })                  
    }
    
    function uploadImage() {
      var button = $('.images .pic')
      var uploader = $('<input type="file" accept="image/*" />')
      var images = $('.images')
      
      button.on('click', function () {
        uploader.click()
      })
      
      uploader.on('change', function () {
          var reader = new FileReader()
          reader.onload = function(event) {
            images.prepend('<div class="img" style="background-image: url(\'' + event.target.result + '\');" rel="'+ event.target.result  +'"><span>remove</span></div>')
          }
          reader.readAsDataURL(uploader[0].files[0])
  
       })
      
      images.on('click', '.img', function () {
        $(this).remove()
      })
    
    }
    
    function submit() {  
      var button = $('#send')
      
      button.on('click', function () {
        if(!way) {
          var title = $('#title')
          var cate  = $('#category')
          var images = $('.images .img')
          var imageArr = []

          
          for(var i = 0; i < images.length; i++) {
            imageArr.push({url: $(images[i]).attr('rel')})
          }
          
          var newStock = {
            title: title.val(),
            category: cate.val(),
            images: imageArr,
            type: 1
          }
          
          saveToQueue(newStock)
        } else {
          // discussion
          var topic = $('#topic')
          var message = $('#msg')
          
          var newStock = {
            title: topic.val(),
            message: message.val(),
            type: 2
          }
          
          saveToQueue(newStock)
        }
      })
    }
    
    function removeNotification() {
      var close = $('.notification')
      close.on('click', 'span', function () {
        var parent = $(this).parent()
        parent.fadeOut(300)
        setTimeout(function() {
          parent.remove()
        }, 300)
      })
    }
    
    function autoRemoveNotification() {
      setInterval(function() {
        var notification = $('.notification')
        var notiPage = $(notification).children('.btn')
        var noti = $(notiPage[0])
        
        setTimeout(function () {
          setTimeout(function () {
           noti.remove()
          }, speedCloseNoti)
          noti.fadeOut(speedCloseNoti)
        }, speedCloseNoti)
      }, speedCloseNoti)
    }
    
    function autoDequeue() {
      var notification = $('.notification')
      var text
      
      setInterval(function () {

          if(queue.length > 0) {
            if(queue[0].type == 2) {
              text = ' Your discusstion is sent'
            } else {
              text = ' Your order is allowed.'
            }
            
            notification.append('<div class="success btn"><p><strong>Success:</strong>'+ text +'</p><span><i class=\"fa fa-times\" aria-hidden=\"true\"></i></span></div>')
            queue.splice(0, 1)
            
          }  
      }, 10000)
    }
    
    function resetButton() {
      var resetbtn = $('#reset')
      resetbtn.on('click', function () {
        reset()
      })
    }
    
    // helpers
    function saveToQueue(stock) {
      var notification = $('.notification')
      var check = 0
      
      if(queue.length <= fullStock) {
        if(stock.type == 2) {
            if(!stock.title || !stock.message) {
              check = 1
            }
        } else {
          if(!stock.title || !stock.category || stock.images == 0) {
            check = 1
          }
        }
        
        if(check) {
          notification.append('<div class="error btn"><p><strong>Error:</strong> Please fill in the form.</p><span><i class=\"fa fa-times\" aria-hidden=\"true\"></i></span></div>')
        } else {
          notification.append('<div class="success btn"><p><strong>Success:</strong> '+ ID +' is submitted.</p><span><i class=\"fa fa-times\" aria-hidden=\"true\"></i></span></div>')
          queue.push(stock)
          reset()
        }
      } else {
        notification.append('<div class="error btn"><p><strong>Error:</strong> Please waiting a queue.</p><span><i class=\"fa fa-times\" aria-hidden=\"true\"></i></span></div>')
      } 
    }
    function reset() {
      
      $('#title').val('')
      $('.select-option .head').html('Category')
      $('select#category').val('')
      
      var images = $('.images .img')
      for(var i = 0; i < images.length; i++) {
        $(images)[i].remove()
      }
      
    </script>
</body>
</html>"""

# display_page="""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Medicine Detection</title>
    
# </head>
# <body>

#     <p>{}</p> 

    
# </body>
# </html>"""