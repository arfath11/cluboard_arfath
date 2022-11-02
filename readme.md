# Containerized Cluboard 
This is <b>Mohammed Arfath<b> student of NTIK 2nnd year  .
	
This is my final submission for the task of containerization of cluboard app under Systems SIG recruitments	

<h2> Cluboard </h2>	
A Full-Stack Web Application to facilitate sharing resources in college clubs. Clubs have resources that any of their members can borrow upon request. Members can borrow resources when approved by the convener of the club.
	
	

This Application is Containerized using [<b>DOCKER<b>](https://www.docker.com/)


	
 

<h2> Table of Contents </h2>


1. [Installation Guide](https://github.com/mittal-parth/Cluboard/blob/main/readme.md#installation-guide)
5. [Sample Git Workflow](https://github.com/mittal-parth/Cluboard/blob/main/readme.md#-sample-git-workflow-)
6. [Implemented Features](https://github.com/mittal-parth/Cluboard/blob/main/readme.md#implemented-features)
7. [References](https://github.com/mittal-parth/Cluboard/blob/main/readme.md#references)
<br>


<h2>Installation Guide</h2>

<h3> Using Git and Github </h3>

- [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the repo
- [Clone](https://docs.github.com/en/get-started/quickstart/contributing-to-projects#cloning-a-fork) the forked repository



<h3>Install required packages:</h3>

- Download Docker desktop [here](https://www.docker.com/) 
	
<h3>To create container:</h3>

-  Enter into the  main folder of the project and run the below commands
	To  Create image and start container in detached mode
``` shell 
docker-compose up -d .
```
	

 
	
	
- Visit development server at http://127.0.0.1:8000

<h3>Create Super user:</h3>
    While the container is running in  detached mode
	
 - Enter into interactive mode 
 
``` shell 
docker exec -it django_container_usingcompose /bin/bash
```

 - `python manage.py createsuperuser`
 - Enter desired credentials
 - You can  now do development 	




<h3>Admin Site:</h3>

http://127.0.0.1:8000/admin

<br>


