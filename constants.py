import pandas as pd
education = [['Honors Bachelor of Science','Computer Science Major- Business Focus','December 2022','Lakehead University, Canada',
              'Major Average: 80%, Overall: 73%'],
             ['High School','Science with Mathematics','2018','Green Valley High School, Vadodara', '75%'],
             ['Secondary School','Computer Genius, Budding Scientist, Accolades in Singing and theatre',
              '2016','Navrachana International School Vadodara','8.6 CGPA']]
embed_component = {'linkedin': """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="large" data-theme="dark" data-type="HORIZONTAL" data-vanity="rakshit-saxena-5122a11a6" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ca.linkedin.com/in/rakshit-saxena-5122a11a6?trk=profile-badge">Rakshit Saxena</a></div>
                """, 'github': """<div class="github-card" data-github="rakshit-29" data-width="400" data-height="150" data-theme="default"></div>
        <script src="//cdn.jsdelivr.net/github-cards/latest/widget.js"></script>"""}

info = {
    'skills':['Data Science','Machine Learning','Deep Learning','RDBMS','Cryptography','Python','Java/C/C++',
              'Google Cloud Platform','Data Wrangling','Data Visualization','Docker','Tableau','Web Scraping',
              'Algorithms and Data Structures','Software Engineering'],

    'edu':pd.DataFrame(education,columns=['Qualification','Stream','Year','Institute','Score'])}

skill_col_size = 5

HTML_BANNER = """
                        <div style="background-color:#E6FEFF;height: auto;width: auto; margin: auto; 
                        border-radius:auto">
                        <h1 style="color:#002376;position:relative; font-family: Helvetica ;text-align:center;">Rakshit Saxena</h1>
                        <h2 style="color:#002376;position:relative;text-align:center;font-family: Helvetica ;">Welcome to my Portfolio website!
                        </h2>
                        </div>
                        """

html_ender= """
            <div style="background-color:#E6FEFF;height: auto;width: auto; margin: auto; 
                        border-radius:auto">
                        <h1 style="color:#002376;position:relative; font-family: Helvetica ;text-align:center;">Thank you for viewing my profile.</h1>
                        <h2 style="color:#002376;position:relative;text-align:center;font-family: Helvetica ;">If you wish to connect, please send me and email and I would be glad to respond it back positively!✌🏻
                        </h2>
                        </div>
                    
            """
