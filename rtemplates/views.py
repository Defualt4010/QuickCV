from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.contrib import messages
from django.core.mail import EmailMessage
from reportlab.lib.pagesizes import letter
from rfast.settings import EMAIL_HOST_USER
from rtemplates.forms import OptionMail, ResumeDetails
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import styles
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Templates Home function!
def TempHome(request : HttpRequest) -> HttpResponse:
    context ={
        'sign_log': True,
    }
    if request.user.is_authenticated:
        context['sign_log'] = False
        context['loged_in'] = True
        return render(request, 'templatesHome.html', context)    
    return render(request, 'templatesHome.html', context)    

# Function to Render an Form and Validate it for POST Request, if all correct then Send and PDF using Mail
def BuildResume(request : HttpRequest) -> HttpResponse:
    context = {
        "forms" : ResumeDetails()
    }
    if request.method == "POST":
        form = ResumeDetails(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            try:                     
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']

                name = first_name + " " + last_name

                email = form.cleaned_data['email']

                phone = form.cleaned_data['phone']

                print(name)
                print(email)
                print(phone)

                file_path = 'static/pdf/Resume.pdf'
                fonts_file = 'static/fonts/BreeSerif-Regular.ttf'
                c = canvas.Canvas(file_path, pagesize=letter)

                pdfmetrics.registerFont(TTFont('BoldFont', fonts_file))

                c.setFont('BoldFont', 20)
                c.drawString(50, 750, name)
                c.setFont('BoldFont', 12)
                c.drawString(50, 730, email)
                c.drawString(50, 710, str(phone))
                # c.rect(100, 700, 400, 100, stroke=1, fill=0)

                # image_path = 'core/static/core/images/linkedin.png'
                # c.drawImage(image_path, 100, 500, width=200, height=100)

                c.save()

                sent_or_not = EmailMessage(
                    "Test PDF attached mail",
                    "Nothing to see here!.",
                    EMAIL_HOST_USER,
                    [email],
                )

                with open('static/pdf/Resume.pdf', 'rb') as pdf_file:
                    sent_or_not.attach('Resume.pdf', pdf_file.read(), 'application/pdf')

                # Send the email
                sent_or_not.send()

                if sent_or_not:
                    messages.success(request, "Mail Sent")
                    return HttpResponseRedirect('/templates/')
                
                messages.error(request, "Mail not Sent")
                return HttpResponseRedirect('/templates/')
            except Exception as e:
                print(e.__str__())
                messages.error(request, "Something Went Wrong")
                return HttpResponseRedirect('/templates/')

        messages.error(request, "Form Not Valid")
        return render(request, 'build.html', context)
    
    return render(request, 'build.html', context)

# Send mail Function without attachment
# def SendMail(request):
#     try:
#         sent_not = send_mail(
#             "This is the Mail Subject",
#             "This is the Body",
#             EMAIL_HOST_USER,
#             ["dtiwari1013@gmail.com"],
#             fail_silently= False   
#         )

#         if sent_not:
#             messages.success(request, "Mail Sent")
#             return HttpResponseRedirect('/templates/')
        
#         messages.error(request, "Mail Not Sent!")
#         return HttpResponseRedirect('/template/')
#     except Exception as e:
#         print(e.__str__())
#         return redirect('/')


# Function to send mail with Attachment 
def SendMail(request):
    try:
        # Make the PDF and Save it
        file_path = 'static/pdf/Nikhil.pdf'
        c = canvas.Canvas(file_path, pagesize=letter)

        c.drawString(100, 750, "Hello, this is your Resume created by rFast!")
        # c.rect(100, 700, 400, 100, stroke=1, fill=0)

        # image_path = 'core/static/core/images/linkedin.png'
        # c.drawImage(image_path, 100, 500, width=200, height=100)

        c.save()
        # Send Mail to the User!
        email = EmailMessage(
            "Test PDF attached mail",
            "Nothing to see here!.",
            EMAIL_HOST_USER,
            ["singhniksan21hit@student.mes.ac.in"],
        )

        # Attach the PDF file
        with open('static/pdf/Nikhil.pdf', 'rb') as pdf_file:
            email.attach('Nikhil.pdf', pdf_file.read(), 'application/pdf')

        # Send the email
        email.send()

        messages.success(request, "Mail Sent")
        return HttpResponseRedirect('/templates/')

    except Exception as e:
        print(e)
        messages.error(request, "Mail Not Sent!")
        return HttpResponseRedirect('/template/')