#!/usr/bin/env python
# coding: utf-8

# #Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data. This task will be done in following steps: 
# 1. First get the webpage https://www.naukri.com/ 
# 2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button. 
# 4. Then scrape the data for the first 10 jobs results you get. 
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[418]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[ ]:


driver =webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe')


# In[79]:


url='https://www.naukri.com/'
driver.get(url)


# In[80]:


#find web eleement for search job bar using class mame 
search_job=driver.find_element_by_class_name('suggestor-input')
search_job


# In[81]:


#finding element for job search bar
search_job.send_keys('Data Scientist')


# In[82]:


#finding web element for search icon bar using absolute xpath
search_icon=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
search_icon


# In[83]:


#finding element for job search bar
search_icon.send_keys('Banglore')
search_icon


# In[84]:


#clicking using class name function
search_btn=driver.find_element_by_class_name('qsbSubmit')
search_btn


# In[85]:


search_btn.click()


# # Extracting job title:-

# In[101]:


#extracting element using relative xpath
job_tag=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
len(job_tag)


# In[102]:


job=[]
for i in job_tag:
    job.append(i.text)
job_title=job[:10]
job_title


# # Extracting job location:-

# In[105]:


#extracting element using relative xpath
loc=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(loc)


# In[106]:


loca=[]
for i in loc:
    loca.append(i.text)
location=loca[:10]
location


# # Extraction compny name:-

# In[110]:


comp_name=driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')
len(comp_name)


# In[111]:


comp=[]
for i in comp_name:
    comp.append(i.text)
company=comp[:10]
company


# # Extraction years of experience:-

# In[114]:


#lets extract all the web elements using contains
exp_tags=driver.find_elements_by_xpath('//*[contains(@title,"Yrs")]')
len(exp_tags)


# In[116]:


exp=[]
for i in exp_tags:
    exp.append(i.text)
Experience=exp[:10]
Experience


# In[118]:


data=pd.DataFrame()


# In[119]:


data['JOB_TITLE']=job_title
data['JOB_LOCATION']= location
data['COMPANY_NAME']=company
data['EXPERIENCE']=Experience
data


#  Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data. This task will be done in following steps: 
# 1. First get the webpage https://www.naukri.com/ 
# 2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button. 
# 4. Then scrape the data for the first 10 jobs results you get. 
# 5. Finally create a dataframe of the scraped data.

# In[474]:


driver=webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe')


# In[475]:


url='https://www.naukri.com/'
driver.get(url)


# In[476]:


skill=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div/div/div/input') 
skill.click()
skill.send_keys('Data Scientist')# Enter Data Scientist in “Skill, Designations, Companies


# In[477]:


loc=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div/div[3]/div/div/div/input')
loc.click()
loc.send_keys('Bangalore')           # Enter Bangalore in location


# In[478]:


search_btn=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_btn.click()  #click 


# In[479]:


#scraping data for job title, compnay, location 
title=[]
company=[]
location=[]
o1=o2=o3=0
tag1=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
for i in tag1:
    if (o1<10):
        title.append(i.text)
        o+=1
    else:
        break
tag2=driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')
for i in tag2:
    if(o2<10):
        company.append(i.text)
        o2+=1
    else:
        break
tag3=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in tag3:
    if (o3<10):
        location.append(i.text.replace('Bangalore',' ').replace('/',''))
        o3+=1
    else:
        break


# In[482]:


title=title[:10]
title


# In[457]:


location


# In[483]:


data=pd.DataFrame({'JOB_TITLE':title ,'COMPANY':company , 'LOCATION':location}) # creating data frame
data


# In[ ]:





# # Q--3)

# You have to use the location and salary filter. You have to scrape data for “Data Scientist” designation for first 10 job results. You have to scrape the job-title, job-location, company name, experience required. The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps: 
# 1. first get the webpage https://www.naukri.com/ 
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button. 
# 4. Then apply the location filter and salary filter by checking the respective boxes 
# 5. Then scrape the data for the first 10 jobs results you get. 
# 6. Finally create a dataframe of the scraped data.

# In[141]:


driver =webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe')


# In[142]:


url='https://www.naukri.com/'
driver.get(url)


# In[143]:


#find web eleement for search job bar using class mame 
search_job=driver.find_element_by_class_name('suggestor-input')
search_job


# In[144]:


#finding element for job search bar
search_job.send_keys('Data Scientist')


# In[145]:


#clicking using class name function
search_btn=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_btn.click()


# In[146]:


loc_check=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[3]/div[2]/div[3]/label/i')
loc_check.click()  #applying location filter 


# In[147]:


sal_check=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[4]/div[2]/div[2]/label/i')
sal_check.click() # applying salary filter


# # Extracting Job title:

# In[149]:


#extracting element using relative xpath
job1_tag=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
len(job1_tag)


# In[158]:


job1=[]
for i in job1_tag:
    job1.append(i.text)
job_title=job1[:10]
len(job_title)


# # Extracting location:

# In[155]:


loc1_tag=driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(loc1_tag)


# In[159]:


loc1=[]
for i in loc1_tag:
    loc1.append(i.text)
location=loc1[:10]
len(location)


# # Extracting YOE:

# In[164]:


exp_tag1=driver.find_elements_by_xpath('//span[contains(@title,"Yrs")]')
len(exp_tag1)


# In[166]:


exp=[]
for i in exp_tag1:
    exp.append(i.text)
experience=exp[:10]
len(experience)


# # Extarcting company name:

# In[172]:


comp1=driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
len(comp1)


# In[175]:


company=[]
for i in comp1:
    company.append(i.text)
company_name=comp1[:10]
len(company_name)


# In[176]:


data=pd.DataFrame()
data['COMPANY_NAME']=company_name
data['JOB_TITLE']=job_title
data['EXPERIENCE']=experience
data['LOCATION']=location
data


# # Q--4)

# In this question you have to scrape data using the filters available on the webpage as shown below:	
# Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes: 
# 1. Brand 2. Product Description 3. Price
# To scrape the data you have to go through following steps: 1. Go to Flipkart webpage by url : https://www.flipkart.com/ 2. Enter “sunglasses” in the search field where “search for products, brands andmore” is written and click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this pageyou can scrap the required data as usual.
# 4. After scraping data from the first page, go to the “Next” Button at the bottom ofthe page , then click on it.
# 5. Now scrape data from this page as usual 6. Repeat this until you get data for 100 sunglasses.

# In[40]:


#open the browser 
driver=webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe')


# In[41]:


#load the webpage
url='https://www.flipkart.com/'
driver.get(url)


# In[42]:


#find element for search product in flipkart
search_pro=driver.find_element_by_class_name('_3704LK')
search_pro


# In[43]:


#send the input to the webpage
search_pro.send_keys('Sunglass')


# In[44]:


#clicking using class name function
search_btn=driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_btn.click()


# In[45]:


product_name=[]
product_des=[]
price=[]
discount=[]

o1=o2=o3=0

tag1 = driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
for i in tag1:
    if(o1<100):
        product_name.append(i.text)
        o1+=1
    else:
        break
    
tag2 = driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
for i in tag2:
    if(o2<100):
        product_des.append(i.text)
        o2+=1
    else:
        break
    
tag3 = driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
for i in tag3:
    if(o3<100):
        price.append(i.text)
        o3+=1
    else:
        break


# In[46]:


len(product_name),len(product_des),len(price)


# In[74]:


disc=driver.find_elements_by_class_name('_3Ay6Sb')
for i in disc:
    discount.append(i.text)
discount=discount[:100]
len(discount)


# In[81]:


nxt_btn=driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[3]')
nxt_btn.click()


# In[80]:


tag1=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
for i in tag1:
    if (o1<100):
        product_name.append(i.text)
        o1+=1
    else:
        break
tag2=driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
for i in tag2:
    if(o2<100):
        product_des.append(i.text)
        o2+=1
    else:
        break
tag3=driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
for i in tag3:
    if(o3<100):
        price.append(i.text)
        o3+=1
    else:break
        
        
        


# In[82]:


nxt_btn=driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[3]')
nxt_btn.click()


# In[83]:


tag1=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
for i in tag1:
    if (o1<100):
        product_name.append(i.text)
        o1+=1
    else:
        break
tag2=driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
for i in tag2:
    if(o2<100):
        product_des.append(i.text)
        o2+=1
    else:
        break
tag3=driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
for i in tag3:
    if(o3<100):
        price.append(i.text)
        o3+=1
    else:break


# In[ ]:





# In[ ]:


#previous class & xpath not working
product_class='_2WkVRV'
next_btn=driver.find_elements_by_xpath('//a[@class="_1LKTO3"]')


# In[84]:


len(product_name)
len(product_des)
len(price)
len(discount)


# In[91]:


df=pd.DataFrame()
df['PRODUCT_NAME']=product_name
df['PRODUCT_DESCRIPTION']=product_des
df['PRICE']=price
df['DISCOUNT']=discount
df


# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the 
# link: https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-poweradapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC TSVZAXUHGREPBFGI&marketplace. From this  page you have to scrape: 
# 1. Rating 
# 2. Review summary 
# 3. Full review 
# 4. You have to scrape this data for first 100 reviews.

# In[119]:


driver =webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe')


# In[120]:


url='https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-poweradapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC TSVZAXUHGREPBFGI&marketplace'
driver.get(url)


# click on review section

# In[121]:


all_review=driver.find_element_by_xpath('//div[@class="_3UAT2v _16PBlm"]')
all_review.click()


# In[122]:


star=[]
rev_sum=[]
full_rev=[]


# Extracting stars,review summery,full review for 1st page

# In[123]:


o1=o2=o3=0
tag1=driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')
for i in tag1:
    if (o1<100):
        star.append(i.text)
        o1+=1
    else:
        break
tag2=driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')
for i in tag2:
    if (o2<100):
        rev_sum.append(i.text)
        o2+=1
    else:
        break
tag3=driver.find_elements_by_xpath('//div[@class="t-ZTKy"]')
for i in tag3:
    if (o3<100):
        full_rev.append(i.text)
        o3+=1
    else:
        break
    
    

        
   


# checking for length of each list

# In[124]:


len(star),len(rev_sum),len(full_rev)


# In[145]:


from selenium.common import exceptions
for j in range(0,10):
    try:
        tag1=driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')
        for i in tag1:
            if (o1<100):
                star.append(i.text)
                o1+=1
            else:
                break

        tag2=driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')
        for i in tag2:
            if(o2<100):
                rev_sum.append(i.text)
                o2+=1
            else:
                break
        tag3=driver.find_elements_by_xpath('//div[@class="t-ZTKy"]')
        for i in tag3:
            if(o3<100):
                full_rev.append(i.text)
                o3+=1
            else:
                break
        if (o1<100):
            c=driver.find_element_by_xpath('//a[@class="_1LKTO3"]')
            c.click()
    except exceptions.StaleElementReferenceException:
        pass





                                                            


# In[146]:


len(star),len(rev_sum),len(full_rev)


# In[149]:


data=pd.DataFrame({'STARS':star, 'REVIEW_SUMMERY':rev_sum ,'FULL_REVIEW':full_rev})
data


# Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com andsearch for “sneakers” in the search field. You have to scrape 4 attributes of each sneaker: 1. Brand 2. Product Description 3. Price 4.percentage off

# In[309]:


driver=webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe')


# In[310]:


url=('https://www.flipkart.com/')
driver.get(url)


# In[311]:


close_pop_up=driver.find_element_by_xpath('//button[@class="_2KpZ6l _2doB4z"]') #closing the popup
close_pop_up.click()


# In[312]:


search=driver.find_element_by_xpath('//input[@class="_3704LK"]')
search.send_keys('sneaker')


# In[313]:


search_btn=driver.find_element_by_xpath('//button[@class="L0Z3Pu"]')
search_btn.click()


# In[314]:


brand=[]
prod_dsc=[]
price=[]
discount=[]


# In[315]:


#extracting  data & storing into those list respectively
from selenium import common
o1=o2=o3=o4=0
for j in range(0,4):
    try:
        tag1=driver.find_elements_by_xpath('//div[@class="_2WkVRV"]') #brand tag
        for i in tag1:
            if (o1<100):
                brand.append(i.text)
                o1+=1
            else:
                break
        tag2=driver.find_elements_by_xpath('//div[@class="_30jeq3"]')#price
        for i in tag2:
            if(o2<100):
                price.append(i.text)
                o2+=1
            else:
                break
        tag3=driver.find_elements_by_xpath('//div[@class="_2B099V"]/a[1]') #product details tag
        for i in tag3:
            if (o3<100):
                prod_dsc.append(i.text)
                o3+=1
            else:
                break
        tag4=driver.find_elements_by_xpath('//div[@class="_3Ay6Sb"]')#discount
        for i in tag4:
            if (o4<100):
                discount.append(i.text)
                o4+=1
            else:
                break
        if (o1<100):
            c=driver.find_element_by_xpath('//a[@class="_1LKTO3"]')  #next button tag
            c.click()
    except exceptions.StaleElementReferenceException:
        pass
        


# In[316]:


#creating dataframe
data=pd.DataFrame({'BRAND':brand,'PRICE':price,'PRODUCT_DESCRIPTION':prod_dsc,'DISCOUNT':discount})
data


# Q7: Go to the link - https://www.myntra.com/shoes Set Price filter to “Rs. 7149 to Rs. 14099 ” , Color filter to “Black”,And then scrape First 100 shoes data you get. The data should include 
# 1.“Brand” of the shoes , 
# 2.Short Shoe description, 
# 3price of the shoe.

# In[287]:


driver=webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe')


# In[288]:


url=('https://www.myntra.com/shoes')
driver.get(url)


# In[289]:


black_check=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label/div')
black_check.click() #click on blavk check box


# In[290]:


price_check=driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label/div')
price_check.click()# click on price check box


# In[291]:


brand=[]
shoe_dsc=[]
price=[]


# In[292]:


o1=o2=o3=0
while o1<100:
    try:
        tag1=driver.find_elements_by_xpath('//div[@class="product-productMetaInfo"]/h3[1]') #brand 
        for i in tag1:
            if (o1<100):
                brand.append(i.text)
                o1+=1
            else:
                break

        tag2=driver.find_elements_by_xpath('//div[@class="product-productMetaInfo"]/h4[1]')#desc
        for i in tag2:
            if(o2<100):
                shoe_dsc.append(i.text)
                o2+=1
            else:
                break
        tag3=driver.find_elements_by_xpath('//div[@class="product-price"]/span[1]') #price
        for i in tag3:
            if (o3<100):
                price.append(i.text.split('Rs.')[1])
                o3+=1
            else:
                break
        if (o1<100):
            next_pg=driver.find_element_by_xpath('//li[@class="pagination-next"]') #navigating to next page 
            next_pg.click()
    except exceptions.StaleElementReferenceException:
        pass

                


# In[293]:


len(brand),len(price),len(shoe_dsc)


# In[294]:


data=pd.DataFrame({'BRAND':brand,'PRICE':price,'SHOE_DESC':shoe_dsc})
data


# Q8: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” and “Intel Core i9”.After setting the filters scrape first 10 laptops data. You have to scrape 3 attributesfor each laptop: 
# 1. Title 
# 2. Ratings 
# 3. Price
# As shown in the below image as the tick marked attributes.

# In[419]:


driver=webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe')


# In[420]:


url='https://www.amazon.in/'
driver.get(url)


# In[421]:


search=driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')#inserting laptop keyword in search bar
search.send_keys('Laptop')


# In[422]:


#then click
search_btn=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search_btn.click()


# In[58]:


#click on chexk box for i7 laptop
check_bx1=driver.find_element_by_xpath('//*[@id="p_n_feature_thirteen_browse-bin/12598163031"]/span/a/div/label/i')
check_bx1.click()


# In[64]:





# In[80]:


title=[]
a1=0
tag1=driver.find_elements_by_xpath('//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')
for i in tag1:
    if (a1<10):
        title.append(i.text)
        a1+=1
    else:
        break


# In[81]:


len(title)


# In[82]:


ratings=[]
tag2=driver.find_elements_by_xpath('//div[@class="a-row a-size-small"]/span[1]')
for i in tag2:
     ratings.append(i.get_attribute('aria-label'))
ratings = ratings[:10]
len(ratings)
    


# In[86]:


price=[]
tag3=driver.find_elements_by_xpath('//span[@class="a-price-whole"]')
for i in tag3:
    price.append(i.text)
price=price[:10]
len(price)


# #dataset for intel i7

# In[90]:


data=pd.DataFrame({'LAPTOP':title ,'RAT0INGS':ratings,'PRICE':price})
data
                   


# NOTE:  As There was no option for i9 processor at the time of scraping, I could't scrape the data for the same

# Q9: Write a python program to scrape data for first 10 job results for Data Scientist Designation in Noida location. You have to scrape company name, No. of days ago when job was posted, Rating of the company. This task will be done in following steps:
# 1. First get the webpage https://www.ambitionbox.com/
# 2. Click on the Job option
# 3.After reaching to the next webpage, In place of “Search by Designations, Companies, Skills” enter “Data Scientist” and click on search button.
# 4. You will reach to the following web page click on location and in place of “Search location” enter “Noida” and select location “Noida”.
# 5. Then scrape the data for the first 10 jobs results you get on the above shown page. 
# 6. Finally create a dataframe of the scraped data.

# In[216]:


driver=webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe') #loading web driver


# In[257]:


url='https://www.ambitionbox.com/'
driver.get(url)                     #access the url


# In[258]:


job=driver.find_element_by_xpath('/html/body/div[1]/nav/nav/a[6]') # click on job module
job.click()


# In[259]:


job_search=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div/div/div/span/input')
job_search.send_keys('Data Scientist') #enter the key of 'Data Scientist'
search_btn=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div/div/button/span')
search_btn.click()    #click on search button


# In[260]:


#click on search location
loc=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/p')
loc.click()
#in locatin entering 'Noida'
loc_tag=driver.find_element_by_xpath('//*[@id="filters-row"]/div/div/div[2]/div[2]/div/div[2]/input')
loc_tag.click()
noida=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input')
noida.send_keys('Noida')


# In[261]:


noida_radio=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/label')
noida_radio.click() #click on the radio button 'Noida'


# In[262]:


#crateing list and storing company name
company=[]
o1=o2=o3=0
tag1=driver.find_elements_by_xpath('//p[@class="company body-medium"]')
for i in tag1:
    if (o1<10):
        company.append(i.text)
        o1+=1
    else:
        break
        
len(company)    


# In[224]:


ratings=[]
tag2=driver.find_elements_by_xpath('//span[@class="body-small"]')
for i in tag2:
    if (o2<10):
        ratings.append(i.text)
        o2+=1
    else:
         break
len(ratings)


# In[172]:


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# In[230]:


post_day = []
day = driver.find_elements_by_xpath('//span[@class="body-small-l"]')
for i in day:
    post_day.append(i.text)
post_day = post_day[::2]
len(post_day)


# In[231]:


data=pd.DataFrame({'COMPANY_NAME':company,'RATINGS':ratings,'POSTED_D_AGO':post_day})
data


# Q10: Write a python program to scrape the salary data for Data Scientist designation. You have to scrape Company name, Number of salaries, Average salary, Minsalary, Max Salary. The above task will be, done as shown in the below steps:
# 1. First get the webpage https://www.ambitionbox.com/
# 2. Click on the salaries option
# 3. After reaching to the following webpage, In place of “Search Job Profile” enters “Data Scientist” and then click on “Data Scientist”
# 4. Scrape the data for the first 10 companies. Scrape the company name, total salary record, average salary, minimum salary, maximum salary, experience required.
# 5. Store the data in a dataframe.

# In[369]:


driver=webdriver.Chrome(r'C:\Users\Soumyajit\Desktop\chromedriver.exe') #loading web driver


# In[371]:


url=' https://www.ambitionbox.com/'
driver.get(url)


# In[372]:


salary_btn=driver.find_element_by_xpath('/html/body/div[1]/nav/nav/a[4]')
salary_btn.click()


# In[373]:


search_job = driver.find_element_by_id("jobProfileSearchbox")
search_job.send_keys("Data Scientist")


# In[374]:


# clicking on “Data Scientist”
drp_clk=driver.find_elements_by_xpath("//div[@class='suggestion_wrap tt-suggestion tt-selectable']")
for i in drp_clk:
    if i.text == 'Data Scientist':   
        i.click() 
        break 


# In[411]:


#scrape Company name, Number of salaries, Average salary, Min salary, Max Salary, experience required.

company_name = []
salary_record = []
average_salary = []
min_salary = []
max_salary = []
exp = []

tag1=driver.find_elements_by_xpath('//div[@class="company-info"]')
for  i in tag1:
    company_name.append(i.text.split('\n')[0])
    salary_record.append(i.text.replace('based on',' ').replace('salaries',' ').split('\n')[1:2])
    exp.append(i.text.replace('yrs exp',' ').split('\n')[-1])
tag2=driver.find_elements_by_xpath('//p[@class="averageCtc"]')
for i in tag2:
    average_salary.append(i.text.replace('₹',' ').replace('L',' '))
tag3=driver.find_elements_by_xpath('//div[@class="salary-values"]')
for i in tag3:
    max_salary.append(i.text.replace('₹','').replace('L',' ').split('\n')[1])
    min_salary.append(i.text.replace('₹','').replace('L',' ').split('\n')[0])


# In[414]:


data=pd.DataFrame({'COMPANY_NAME':company_name ,'SALARY RECORD':salary_record ,'AVERAGE SALARY':average_salary ,'MIN_SALARY':min_salary ,'MAX_SALARY':max_salary ,'EXP':exp})
data


# In[ ]:





# In[ ]:





# In[ ]:




