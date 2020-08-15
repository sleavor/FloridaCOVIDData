# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:32:16 2020

@author: Shawn Leavor
"""
import smtplib

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s' % from_addr
    header += 'To: %s' % ','.join(to_addr_list)
    header += 'Cc: %s' % ','.join(cc_addr_list)
    header += 'Subject: %s' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    
def sendBestBuddiesEmail(from_addr, to_addr_list, cc_addr, 
                         companyName, request, yourName, login, password):
    subject = 'You can support Best Buddies Champion of the Year!'
    message = "Hi! <br> I hope you are doing well! I'm reaching out on behalf of the Tampa Best Buddies chapter as we host our virtual gala this year. We hope that even in this unprecedented time, you are able to support our mission through an in-kind auction item donation! I've attached our donation form, if needed, and am more than happy to answer any questions as necessary, if you have any! <br> Best Buddies in Tampa Bay will host its Virtual Champion of the Year Gala on Thursday, November 12, 2020. This prestigious philanthropic competition, hosted by the Best Buddies Tampa Bay Advisory Board and Event Committee, will celebrate local individuals, professionals and community leaders throughout the Tampa Bay area who have been specifically nominated for their strong commitment and passion for our mission: friendship, leadership, integrated employment and inclusion for individuals with disabilities. This friendly, yet competitive competition will culminate with the virtual awards gala- an evening of fun and friendship- along with the crowning and awarding of the coveted title of 'Grand Champion of the Year'. <br> Best Buddies is a nonprofit organization dedicated to establishing a global volunteer movement that creates opportunities for one-to-one friendships, leadership development, integrated employment, and inclusive living for people with intellectual and developmental disabilities (IDD). Locally, Best Buddies has nine programs: Best Buddies Elementary School, Middle School, High School, and College Friendship Programs, Best Buddies Citizens and e-Buddies Friendship Programs, Best Buddies Ambassador and Promoter Programs, and Best Buddies Jobs throughout Hillsborough, Pasco, Pinellas, and Polk counties. <br> Being a part of Best Buddies is a life-changing experience for people with IDD. These programs help to improve the self-esteem, confidence, and feelings of self-worth of participants while critical social and leadership skills needed to secure competitive employment and help place our participants into the workforce in the Tampa Bay Community. <br> Best Buddies in Tampa Bay kindly and sincerely requests donation of a " + request + ". We respectfully request your response by October 29th, 2020 so we can adequately prepare for and publicize " + companyName + "'s generous donation as we promote the gala and ensure recognition through the virtual auction and program book.<br> Without the support of companies like" + companyName + ", we would not be able to fund our local Best Buddies programs. Please join us in our efforts to create friendships, social inclusion, leadership and integrated employment within our schools and communities. <br> Thank you for your consideration. <br> In Friendship, <br>" + yourName
    sendemail(from_addr, to_addr_list, cc_addr, subject, message, login, password)
    
sendBestBuddiesEmail("sleavor@gmail.com", "sleavor@gmail.com", "", "Sleavor", "card", "shawn", "sleavor@gmail.com", "YT%ZfgL`'8Skf4Yg")