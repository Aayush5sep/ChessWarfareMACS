# Chess Warfare

- A Web based Management-application for organizing chess tournament in **Invictus-23, DTU Delhi**.
- The tournament consisted of **150+ participants** and **150+ games** were held in total.
- The application helped in coordination between **20+ staff members** including Arbiters, Registration-staff & Duel Setup staff etc to conduct the operations smoothly.

![homepage](https://drive.google.com/uc?id=1jc9RU5U3k00R3uYeCDktrotv78KcoGR6)


## Management Controls
The homepage at `localhosturl/` gives all the following options to access them to the allowed users.
However, the link is being mentioned as well to directly visit. 

### Registration Staff
> New Registration `localhosturl/admin/chesswar/registration/`
![new registration](https://drive.google.com/uc?id=1IOlzywPP5Ik7Sqc42BjDv9Y_FMo3Afz6)

> New Board Setup `localhosturl/admin/chesswar/board/`
![new board](https://drive.google.com/uc?id=1pe28Whz8fttLA4DiUJLCmKxJ7iIBRKBf)


### Duel Setup Staff

> Duel Setup `localhosturl/newduelpage/`
![new duel](https://drive.google.com/uc?id=1_maIaCHYL8ITWglqMp218lPriNLhfWs7)


### Arbiters

> Announce Result `localhosturl/duelwinpage/`
![arbiter](https://drive.google.com/uc?id=1wk6jEDGurfjS4ifwiLPCS5R--pFsBIHi)



### View Only (For Staff)
All staff members after logging in by any of the roles can check the current status of tournament.

**All Registrations sorted by Qualified Levels**
> ![all registrations](https://drive.google.com/uc?id=191GouMq0Gc8j3Fn0EDxplJj_DX2tD8I7)
**Waiting** shows if they are still eligible to qualify for the next level or not
![waiting list](https://drive.google.com/uc?id=1shS_eT8p05-_j6u3k19FGHr9jVLThyMT)

**Ongoing & Completed Duels**
> ![all duels](https://drive.google.com/uc?id=1NZMAC-Iu80WxUAUi2q9ugIcFIm-426Kn)




## Installation
This app requires python to run on your server/localhost.

### 1. Clone the project on your local computer.

```sh
git clone https://github.com/Aayush5sep/ChessWarfareMACS
```

### 2. Install the dependencies and devDependencies.

```sh
pipenv install -r requirements.txt
pipenv shell
```
>Any other virtual environments may also work. 
>The requirements.txt file contains all the packages that need to be installed.

### 3. Generate  a Secret Key & other credentials.

- Create a new secret key for django with a secret key generator, like [Djecrety](https://djecrety.ir/).
- Set this secret key value for `DJANGO_KEY` in .env file.


### 4. Migrate the project.
Run the following commands in terminal(optional).
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the project.
Run the following command in terminal to start the server.
```sh
python manage.py runserver
```

### 6. Login as per role assigned
`localhosturl/`
![login](https://drive.google.com/uc?id=19anxvrODcpHhlsZBGGB6hEqiBobVifna)

| Role | Username | Password |
|------|----------|----------|
| Registration | registerstaff@macs | secretpass@newreg |
| Duel Setup | duelmanager@macs | startduel@waitings |
| Arbiters | arbiters@macs | announcewinner@duel |
| Superuser(All perms) | macdev@admin | pass@devlogin |

> **Note :** For different id & passwords, you can add the new users to the corresponding groups of Arbiters, Duel, Register by logging in as superuser.
![groups](https://drive.google.com/uc?id=1wejqI-1bGx_d2jDnqTUUMvePhy_lAEm8)


## Contributing to the Project
### 1. Fork the repository
![fork](https://drive.google.com/uc?id=1ZF_tJBjVC5PVDu5eWfTbEQjvFqNoray-)

### 2. Clone the project on your local computer.

```sh
git clone <Your-Repository-URL>
```

### 3. Add the original repository as upstream

```sh
git remote add upstream https://github.com/Aayush5sep/ChessWarfareMACS
```

### 4. Create a local branch

```sh
git checkout -b <your-branch-name>
```

### 5. Commit your changes & push to your github repo

```sh
git commit -m "<feature you have worked on>"
git push origin <your-branch-name>
```

### 6. Begin & Create the local request

Click the green Compare & pull request button to begin the pull request.
![pull](https://drive.google.com/uc?id=11_LX9-eYt8AilvlfbxQYLw0NatqzxEJm)

Complete the pull request to upstream branch
![complete-pull](https://drive.google.com/uc?id=1iMrWJyos5AOTjMziQNB3yTZGuakrIe_0)






> Check out more projects by `Aayush Goyal` at [Aayush5sep][aayush]




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen)

   [git-repo]: <https://github.com/Aayush5sep/UserAuthAPI>
   [aayush]: <https://github.com/Aayush5sep>
