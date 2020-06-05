from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os # to get the resume file
import time # to sleep

with open("apply.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)

# sample applications
URL_g1 = 'https://boards.greenhouse.io/braintree/jobs/1316736?gh_jid=1316736&gh_src=1d1244401'
URL_g2 = 'https://boards.greenhouse.io/gusto/jobs/1862076'
URL_g4 = 'https://boards.greenhouse.io/thumbtack/jobs/1814883'
URL_g3 = 'https://boards.greenhouse.io/lyft/jobs/4358047002?gh_jid=4358047002'
URL_l1 = 'https://jobs.lever.co/figma/91da97b9-ff1d-4e08-a2f1-4867537e5eb2'
URL_l2 = 'https://jobs.lever.co/blendlabs/2a469512-a8c2-44fa-a260-ef3ae0c90db7'
URL_l3 = 'https://jobs.lever.co/affirm/5340f1d3-cd6d-44ef-a5c6-f9def8609d02'
URL_l4 = 'https://jobs.lever.co/grandrounds/cbf92d6f-83c2-41a3-b1a7-350e338c76a7'
URL_1 = 'https://boards.greenhouse.io/connectedfitness/jobs/2182265'

# there's probably a prettier way to do all of this
# URLS = [URL_g1, URL_g2, URL_g3, URL_g4, URL_l1, URL_l2, URL_l3, URL_l4] # to test all the URLS
URLS = [URL_1]

# Fill in this dictionary with your personal details!
JOB_APP = {
    "first_name": "Nobuhide",
    "last_name": "Ajito",
    "email": "nobuhide95@gmail.com",
    "phone": "310-562-8100",
    "org": "Auxpack",
    "resume": "resume.pdf",
    "resume_textfile": "resume_short.txt",
    "linkedin": "https://www.linkedin.com/in/nobuhide-ajito/",
    "website": "none",
    "github": "https://github.com/najito",
    "twitter": "",
    "location": "Santa Monica, CA, United States",
    "grad_month": '06',
    "grad_year": '2017',
    "university": "University of California: Santa Barbara",
}

# Greenhouse has a different application form structure than Lever, and thus must be parsed differently
def greenhouse(driver):

    # basic info
    driver.find_element_by_id('first_name').send_keys(JOB_APP['first_name'])
    driver.find_element_by_id('last_name').send_keys(JOB_APP['last_name'])
    driver.find_element_by_id('email').send_keys(JOB_APP['email'])
    driver.find_element_by_id('phone').send_keys(JOB_APP['phone'])

    #grab info for cover letter
    company_name = driver.find_element_by_class_name('company-name').text.lstrip('at').lstrip()
    position = driver.find_element_by_class_name('app-title').text

    cover_letter ='''Hi there,

    I was excited to see the %s open at %s. I'm glad I have the opportunity to apply.
    
    I primarily work in JavaScript/Node.js/SQL but I recently took a deep dive into front-end bundle deployment and bundling optimization for my most recent developer tool name Auxpack. My team and I developed a Webpack bundle analysis and optimization tool that visualizes assets and dependencies and offers recommendations like tree-shaking to reduce bundle size, lower ramp up time, speed up dev workflow and faster meaningful hydration and perceived performance by the user.
    
    I also recently gave a talk at the Ethiq Software Engineering Speaker series about utilizing build tools for creating a better developer workflow and was curious regarding the tool and framework choice utilized at %s- I know there is a constant back and forth regarding frameworks like Flask versus Django between their flexibility and lightweight start vs out-of-the-box toolkit size.
    
    I'd be happy to talk more about the challenges you are working on and wanted to see if you'd be available to chat about %s's architecture, the engineering culture on the team, and also any particulars about the role itself. I'm available next Wed-Fri from 9am PST to noon to chat or please let me know if there is a more convenient time.
    
    Best,
    Nobu''' % (position, company_name, company_name, company_name)

    try:
        loc = driver.find_element_by_id('job_application_location')
        loc.send_keys(JOB_APP['location'])
        loc.send_keys(Keys.DOWN) # manipulate a dropdown menu
        loc.send_keys(Keys.DOWN)
        loc.send_keys(Keys.RETURN)
        time.sleep(2) # give user time to manually input if this fails

    except NoSuchElementException:
        pass

    # # Upload Resume as a Text File
    # driver.find_element_by_css_selector("[data-source='paste']").click()
    # resume_zone = driver.find_element_by_id('resume_text')
    # resume_zone.click()
    # with open(JOB_APP['resume_textfile']) as f:
    #     lines = f.readlines() # add each line of resume to the text area
    #     for line in lines:
    #         resume_zone.send_keys(line.decode('utf-8'))

    # Attach resume to application
    driver.find_element_by_css_selector("[data-field='resume']").find_element_by_css_selector("[data-source='attach']").send_keys('/Documents/Ajito_Nobuhide_Resume.pdf')

    # Type in cover letter
    try:
        driver.find_element_by_css_selector("[data-field='cover_letter']").find_element_by_css_selector("[data-source='paste']").click()
        driver.find_element_by_id('cover_letter_text').send_keys(cover_letter)
    except NoSuchElementException:
        pass

    # add linkedin
    try:
        driver.find_element_by_css_selector("[autocomplete='custom-question-linkedin-profile']").send_keys(JOB_APP['linkedin'])
    except NoSuchElementException:
        pass
        # try:
        #     driver.find_element_by_css_selector("[autocomplete='custom-question-linkedin-profile']").send_keys(JOB_APP['linkedin'])
        # except NoSuchElementException:
        #     pass

    # add graduation year
    # try:
    #     driver.find_element_by_xpath("//select/option[text()='2017']").click()
    # except NoSuchElementException:
    #     pass

    # add university
    # try:
    #     driver.find_element_by_xpath("//select/option[contains(.,'University of California: Santa Barbara')]").click()
    # except NoSuchElementException:
    #     pass

    # add degree
    # try:
    #     driver.find_element_by_xpath("//select/option[contains(.,'Bachelor')]").click()
    # except NoSuchElementException:
    #     pass

    # add major
    # try:
    #     driver.find_element_by_xpath("//select/option[contains(.,'Chemistry')]").click()
    # except NoSuchElementException:
    #     pass

    # add website
    try:
        driver.find_element_by_css_selector("[autocomplete='custom-question-website']").send_keys(JOB_APP['website'])
    except NoSuchElementException:
        pass

    # add where job was found
    try:
        driver.find_element_by_xpath("//label[contains(.,'hear')]").send_keys('Blind Job Board')
    except NoSuchElementException:
        pass

    # add work authorization
    # try:
    #     driver.find_element_by_xpath("//select/option[contains(.,'any employer')]").click()
    # except NoSuchElementException:
    #     pass

    # add sponsorship information (boolean)
    try:
        sponsor = driver.find_element_by_xpath("//label[contains(.,'sponsorship')]")
        for option in sponsor.find_elements_by_tag_name('option'):
            if option.text == 'No':
                option.click()
                break
    except NoSuchElementException:
        pass
    
    # add work authorization (boolean)
    try:
        authorization = driver.find_element_by_xpath("//label[contains(.,'authorized')]")
        for option in authorization.find_elements_by_tag_name('option'):
            if option.text == 'No':
                option.click()
                break
    except NoSuchElementException:
        pass

    # driver.find_element_by_id("submit_app").click()

# Handle a Lever form
def lever(driver):
    # navigate to the application page
    driver.find_element_by_class_name('template-btn-submit').click()

    # basic info
    first_name = JOB_APP['first_name']
    last_name = JOB_APP['last_name']
    full_name = first_name + ' ' + last_name  # f string didn't work here, but that's the ideal thing to do
    driver.find_element_by_name('name').send_keys(full_name)
    driver.find_element_by_name('email').send_keys(JOB_APP['email'])
    driver.find_element_by_name('phone').send_keys(JOB_APP['phone'])
    driver.find_element_by_name('org').send_keys(JOB_APP['org'])

    # socials
    driver.find_element_by_name('urls[LinkedIn]').send_keys(JOB_APP['linkedin'])
    driver.find_element_by_name('urls[Twitter]').send_keys(JOB_APP['twitter'])
    try: # try both versions
        driver.find_element_by_name('urls[Github]').send_keys(JOB_APP['github'])
    except NoSuchElementException:
        try:
            driver.find_element_by_name('urls[GitHub]').send_keys(JOB_APP['github'])
        except NoSuchElementException:
            pass
    driver.find_element_by_name('urls[Portfolio]').send_keys(JOB_APP['website'])

    # add university
    try:
        driver.find_element_by_class_name('application-university').click()
        search = driver.find_element_by_xpath("//*[@type='search']")
        search.send_keys(JOB_APP['university']) # find university in dropdown
        search.send_keys(Keys.RETURN)
    except NoSuchElementException:
        pass

    # add how you found out about the company
    try:
        driver.find_element_by_class_name('application-dropdown').click()
        search = driver.find_element_by_xpath("//select/option[text()='other']").click()
    except NoSuchElementException:
        pass

    # submit resume last so it doesn't auto-fill the rest of the form
    # since Lever has a clickable file-upload, it's easier to pass it into the webpage
    driver.find_element_by_name('resume').send_keys(os.getcwd()+"/Ajito_Nobuhide_Resume.pdf")
    # driver.find_element_by_class_name('template-btn-submit').click()

if __name__ == '__main__':
    # driver = webdriver.Chrome(executable_path='/Users/najito/chromedriver')
    driver = webdriver.Firefox()

    for url in URLS:
        driver.get(url)

        if 'greenhouse' in url:
            greenhouse(driver)

        if 'lever' in url:
            lever(driver)

        time.sleep(1) # can lengthen this as necessary (for captcha, for example)
    # driver.close()