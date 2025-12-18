# 🚀 Git & Linux Terminal – Complete Lab Guide

Welcome to the Git lab! This guide offers **two learning paths** depending on your situation.

---

## 🎯 Choose Your Path

### 📌 [Scenario A: Create Your Own Repository](#-scenario-a-create-your-own-repository)
**For:** Students who want to start a personal project from scratch.

**You will learn:** `git init`, `git remote add`, creating repo on GitHub, pushing your first code.

---

### 📌 [Scenario B: Join an Existing Team Repository](#-scenario-b-join-existing-team-repository)
**For:** Students joining a shared class/team project.

**You will learn:** `git clone`, branch workflow, team collaboration, Pull Requests.

---

---

# 📘 Scenario A: Create Your Own Repository

Perfect for starting your own project from scratch!

---

## 📋 Table of Contents - Scenario A

1. [Setup Identity](#step-a1-setup-identity)
2. [Create Local Repository](#step-a2-create-local-repository)
3. [Create Files & First Commit](#step-a3-create-files--first-commit)
4. [Create GitHub Repository](#step-a4-create-github-repository)
5. [Connect Local to Remote](#step-a5-connect-local-to-remote)
6. [Push to GitHub](#step-a6-push-to-github)
7. [Make Changes & Update](#step-a7-make-changes--update)

---

## Step A1: Setup Identity

Tell Git who you are (only once per computer).

```bash
git config --global user.name "YourFullName"
git config --global user.email "yourmail@example.com"
```

**Verify:**
```bash
git config --global --list
```

---

## Step A2: Create Local Repository

Create a new project folder and initialize Git.

```bash
mkdir project_one
cd project_one
git init
```

**What happened?** You created an empty Git repository. Check with:
```bash
ls -la
```
You'll see a hidden `.git` folder - this is where Git stores everything!

---

## Step A3: Create Files & First Commit

### Create README file
```bash
nano README.md
```
Write: `# Hello Git` then save (Ctrl+O, Enter) and exit (Ctrl+X).

### Create JavaScript file
```bash
nano index.js
```
Write:
```javascript
function init() {
    console.log("Hello Git");
}
```
Save and exit.

### Check Status
```bash
git status
```
Files appear in **red** (Untracked).

### Stage & Commit
```bash
git add .
git status
```
Files now in **green** (Staged).

```bash
git commit -m "Initial commit: added README and index.js"
```

**Explanation:** You saved a snapshot of your project!

---

## Step A4: Create GitHub Repository

1. Go to https://github.com
2. Click the **"+"** icon (top right) → **"New repository"**
3. Repository name: `project_one`
4. Keep it **Public** or **Private** (your choice)
5. **DO NOT** check "Initialize with README" (we already have files!)
6. Click **"Create repository"**

**Important:** Copy the repository URL from the page (looks like: `https://github.com/YourUsername/project_one.git`)

---

## Step A5: Connect Local to Remote

Connect your local folder to GitHub:

```bash
git remote add origin https://github.com/YourUsername/project_one.git
```

**Verify connection:**
```bash
git remote -v
```
You should see:
```
origin  https://github.com/YourUsername/project_one.git (fetch)
origin  https://github.com/YourUsername/project_one.git (push)
```

**Explanation:** `origin` is the nickname for your GitHub repository.

---

## Step A6: Push to GitHub

Send your code to GitHub:

```bash
git branch -M main
git push -u origin main
```

**What happened?**
- First command: Renamed your branch to `main` (modern standard)
- Second command: Uploaded your files to GitHub

**Verify:** Refresh your GitHub page - your files should appear! 🎉

---

## Step A7: Make Changes & Update

Let's practice the workflow:

### 1. Modify a file
```bash
nano index.js
```
Add a new line:
```javascript
init(); // Call the function
```
Save and exit.

### 2. Check what changed
```bash
git status
git diff
```

**Explanation:** `diff` shows exactly what you added (green `+`) or removed (red `-`).

### 3. Stage, Commit, Push
```bash
git add .
git commit -m "Added function call"
git push origin main
```

**Verify:** Refresh GitHub - your changes are there!

---

## 🎓 Summary - Scenario A

You learned:
- ✅ Create repository from scratch (`git init`)
- ✅ Connect to GitHub (`git remote add`)
- ✅ Stage → Commit → Push workflow
- ✅ Track changes with `status` and `diff`

**Next step:** Learn branching and team collaboration in Scenario B!

---

---

# 👥 Scenario B: Join Existing Team Repository

Perfect for joining a class project or team repository!

---

## 📋 Table of Contents - Scenario B

1. [Setup Identity](#step-b1-setup-identity)
2. [Clone Team Repository](#step-b2-clone-team-repository)
3. [Create Your Branch](#step-b3-create-your-branch)
4. [Terminal & File Skills](#step-b4-terminal--file-skills)
5. [Track Your Changes](#step-b5-track-your-changes)
6. [Sync with Team & Push](#step-b6-sync-with-team--push)
7. [Submit Pull Request](#step-b7-submit-pull-request)
8. [Merge & Update](#step-b8-merge--update)

---

## Step B1: Setup Identity

Tell Git who you are (only once per computer).

```bash
git config --global user.name "YourFullName"
git config --global user.email "yourmail@example.com"
```

**Verify:**
```bash
git config --global --list
```

---

## Step B2: Clone Team Repository

Download the shared project to your computer.

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

**Example:**
```bash
git clone https://github.com/team/data-lab.git
cd data-lab
```

**Check connection:**
```bash
git remote -v
```
You should see the team repository URL.

---

## Step B3: Create Your Branch

**Rule:** Never work directly on `main` branch in a team project!

### Create your personal branch
```bash
git checkout -b feature/YourName
```

**Example:** `git checkout -b feature/Peer`

### Verify you're on your branch
```bash
git branch
```
The `*` and green color should be next to your branch name.

**Explanation:** A branch is your personal workspace. Changes here won't affect others until you merge.

---

## Step B4: Terminal & File Skills

Create your content using terminal commands. **Important:** All files MUST start with your name!

### Create your folder
```bash
mkdir YourName_Lab
cd YourName_Lab
```

### Create Python script
```bash
nano YourName_script.py
```
Write:
```python
print("Hello Cloud")
```
Save (Ctrl+O, Enter) and exit (Ctrl+X).

### Create JSON config
```bash
nano YourName_config.json
```
Write:
```json
{"user": "YourName", "status": "active"}
```
Save and exit.

### View your file
```bash
cat YourName_config.json
```

---

## Step B5: Track Your Changes

See what Git detected.

### Check status
```bash
git status
```
Files appear in **red** (Untracked).

### Stage files
```bash
git add .
git status
```
Files now in **green** (Staged).

### Test the diff command
Modify a file:
```bash
nano YourName_script.py
```
Add: `print("Data Engineering!")`

Now check:
```bash
git diff
```

**Explanation:** `diff` shows exactly what changed. Green = added, Red = removed.

### Stage again and commit
```bash
git add .
git commit -m "Added lab files for YourName"
```

---

## Step B6: Sync with Team & Push

**Critical step:** Before pushing, always sync with teammates' work!

### Sync from remote
```bash
git fetch origin
git pull origin main
```

**Explanation:**
- `fetch`: Checks what's new on GitHub
- `pull`: Downloads and merges teammates' code into your local copy

### Push your branch
```bash
git push origin feature/YourName
```

**What happened?** Your branch is now on GitHub, but NOT yet in `main` branch.

---

## Step B7: Submit Pull Request

Instead of merging yourself, request review (best practice!).

### On GitHub website:
1. Go to your repository on GitHub
2. You'll see a yellow banner: **"Compare & pull request"** - click it
3. Fill in:
   - **Title:** "Added lab files - YourName"
   - **Description:** Briefly describe what you did
4. Click **"Create pull request"**

**Why Pull Request (PR)?**
- Allows code review before merging
- Team can comment and suggest changes
- Prevents bugs from entering main code
- Shows your work to instructor/team

---

## Step B8: Merge & Update

After your PR is approved and merged:

### Switch back to main
```bash
git checkout main
```

**Check:** Your files from the branch disappear - this is normal!

### Pull latest changes
```bash
git pull origin main
```

**Check:** Now your files appear in `main` branch!

**Explanation:** Your changes are now part of the shared codebase.

### Verify the changes
```bash
ls -la
git log --oneline
```

---

## 🎓 Summary - Scenario B

You learned:
- ✅ Clone team repository
- ✅ Branch workflow (never work on `main`!)
- ✅ Create files with `nano`, `mkdir`, `cat`
- ✅ Track changes with `status`, `diff`, `add`, `commit`
- ✅ Sync with team using `fetch` and `pull`
- ✅ Submit Pull Request for review
- ✅ Merge and update local copy

---

---

# 💡 Essential Rules for Both Scenarios

## 🚫 Never Use Rebase in Shared Repositories
**Why?** Rebase rewrites Git history. In team projects, this breaks synchronization for everyone.

**Rule:** Always use `merge`, never `rebase`.

---

## 🏷️ File Naming Convention (Scenario B)
All files MUST start with your name:
- ✅ `Peer_data.json`
- ✅ `Sarah_script.py`
- ❌ `data.json` (will be overwritten by teammates!)

---

## 🔍 Always Check Status First
Before any Git command, run:
```bash
git status
```
This is your compass - it shows:
- Which branch you're on
- Which files changed
- What's staged/unstaged

---

## 📝 Commit Message Best Practices
**Good commits:**
```bash
git commit -m "Added data cleaning script"
git commit -m "Fixed bug in CSV parser"
git commit -m "Updated README with setup instructions"
```

**Bad commits:**
```bash
git commit -m "changes"
git commit -m "fix"
git commit -m "asdfgh"
```

---

## 🆘 Common Issues & Solutions

### "Permission denied" when pushing?
```bash
# Check your remote URL
git remote -v

# Update to use HTTPS
git remote set-url origin https://github.com/username/repo.git
```

### Forgot which branch you're on?
```bash
git branch
```
The `*` shows your current branch.

### Want to see commit history?
```bash
git log --oneline --graph
```

### Made changes but want to discard them?
```bash
git restore <filename>
```

---

## 📚 Quick Command Reference

| Command | Description |
|---------|-------------|
| `git status` | Check current state |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Save snapshot |
| `git push origin <branch>` | Upload to GitHub |
| `git pull origin <branch>` | Download from GitHub |
| `git branch` | List branches |
| `git checkout <branch>` | Switch branch |
| `git diff` | See unstaged changes |
| `git log --oneline` | View history |

---

## 🎯 Next Steps

After mastering these basics:
1. Learn about `.gitignore` files
2. Explore `git stash` for temporary saves
3. Practice resolving merge conflicts
4. Try `git log` with different options

---

**Happy Learning! 🎓**

---

<div dir="rtl">

# 🚀 Git & Linux Terminal – מדריך מלא

ברוכים הבאים למעבדת Git! המדריך מציע **שני מסלולי למידה** לפי המצב שלכם.

---

## 🎯 בחרו את המסלול שלכם

### 📌 [תרחיש א': יצירת Repository משלכם](#-תרחיש-א-יצירת-repository-משלכם)
**מתאים ל:** סטודנטים שרוצים להתחיל פרויקט אישי מאפס.

**תלמדו:** `git init`, `git remote add`, יצירת repo ב-GitHub, העלאה ראשונית.

---

### 📌 [תרחיש ב': הצטרפות לפרויקט קבוצתי](#-תרחיש-ב-הצטרפות-לפרויקט-קבוצתי)
**מתאים ל:** סטודנטים שמצטרפים לפרויקט משותף של הכיתה/צוות.

**תלמדו:** `git clone`, עבודה עם branches, שיתוף פעולה, Pull Requests.

---

---

# 📘 תרחיש א': יצירת Repository משלכם

מושלם להתחלת פרויקט אישי מאפס!

---

## 📋 תוכן עניינים - תרחיש א'

1. [הגדרת זהות](#שלב-א1-הגדרת-זהות)
2. [יצירת Repository מקומי](#שלב-א2-יצירת-repository-מקומי)
3. [יצירת קבצים ו-Commit ראשון](#שלב-א3-יצירת-קבצים-ו-commit-ראשון)
4. [יצירת Repository ב-GitHub](#שלב-א4-יצירת-repository-ב-github)
5. [חיבור Local ל-Remote](#שלב-א5-חיבור-local-ל-remote)
6. [העלאה ל-GitHub](#שלב-א6-העלאה-ל-github)
7. [ביצוע שינויים ועדכון](#שלב-א7-ביצוע-שינויים-ועדכון)

---

## שלב א1: הגדרת זהות

ספרו ל-Git מי אתם (פעם אחת למחשב).

```bash
git config --global user.name "YourFullName"
git config --global user.email "yourmail@example.com"
```

**אימות:**
```bash
git config --global --list
```

---

## שלב א2: יצירת Repository מקומי

צרו תיקיית פרויקט חדשה ואתחלו Git.

```bash
mkdir project_one
cd project_one
git init
```

**מה קרה?** יצרתם repository ריק של Git. בדקו עם:
```bash
ls -la
```
תראו תיקייה מוסתרת `.git` - כאן Git שומר הכל!

---

## שלב א3: יצירת קבצים ו-Commit ראשון

### יצירת קובץ README
```bash
nano README.md
```
כתבו: `# Hello Git` ואז שמרו (Ctrl+O, Enter) וצאו (Ctrl+X).

### יצירת קובץ JavaScript
```bash
nano index.js
```
כתבו:
```javascript
function init() {
    console.log("Hello Git");
}
```
שמרו וצאו.

### בדיקת מצב
```bash
git status
```
הקבצים יופיעו **באדום** (Untracked).

### Stage & Commit
```bash
git add .
git status
```
הקבצים עכשיו **בירוק** (Staged).

```bash
git commit -m "Initial commit: added README and index.js"
```

**הסבר:** שמרתם תמונת מצב של הפרויקט שלכם!

---

## שלב א4: יצירת Repository ב-GitHub

1. היכנסו ל-https://github.com
2. לחצו על **"+"** (פינה ימנית עליונה) → **"New repository"**
3. שם Repository: `project_one`
4. השאירו **Public** או **Private** (לבחירתכם)
5. **אל תסמנו** "Initialize with README" (יש לנו כבר קבצים!)
6. לחצו **"Create repository"**

**חשוב:** העתיקו את כתובת ה-Repository מהעמוד (נראה כך: `https://github.com/YourUsername/project_one.git`)

---

## שלב א5: חיבור Local ל-Remote

חברו את התיקייה המקומית ל-GitHub:

```bash
git remote add origin https://github.com/YourUsername/project_one.git
```

**אימות חיבור:**
```bash
git remote -v
```
אמורים לראות:
```
origin  https://github.com/YourUsername/project_one.git (fetch)
origin  https://github.com/YourUsername/project_one.git (push)
```

**הסבר:** `origin` זה הכינוי של ה-Repository שלכם ב-GitHub.

---

## שלב א6: העלאה ל-GitHub

שלחו את הקוד ל-GitHub:

```bash
git branch -M main
git push -u origin main
```

**מה קרה?**
- פקודה ראשונה: שינתה את שם ה-branch ל-`main` (הסטנדרט המודרני)
- פקודה שנייה: העלתה את הקבצים ל-GitHub

**אימות:** רעננו את עמוד GitHub - הקבצים אמורים להופיע! 🎉

---

## שלב א7: ביצוע שינויים ועדכון

בואו נתרגל את תהליך העבודה:

### 1. שנו קובץ
```bash
nano index.js
```
הוסיפו שורה חדשה:
```javascript
init(); // Call the function
```
שמרו וצאו.

### 2. בדקו מה השתנה
```bash
git status
git diff
```

**הסבר:** `diff` מראה בדיוק מה הוספתם (ירוק `+`) או מחקתם (אדום `-`).

### 3. Stage, Commit, Push
```bash
git add .
git commit -m "Added function call"
git push origin main
```

**אימות:** רעננו את GitHub - השינויים שם!

---

## 🎓 סיכום - תרחיש א'

למדתם:
- ✅ יצירת repository מאפס (`git init`)
- ✅ חיבור ל-GitHub (`git remote add`)
- ✅ תהליך Stage → Commit → Push
- ✅ מעקב אחרי שינויים עם `status` ו-`diff`

**השלב הבא:** למדו branches ושיתוף פעולה בתרחיש ב'!

---

---

# 👥 תרחיש ב': הצטרפות לפרויקט קבוצתי

מושלם להצטרפות לפרויקט כיתה או צוות!

---

## 📋 תוכן עניינים - תרחיש ב'

1. [הגדרת זהות](#שלב-ב1-הגדרת-זהות)
2. [שכפול Repository של הצוות](#שלב-ב2-שכפול-repository-של-הצוות)
3. [יצירת Branch אישי](#שלב-ב3-יצירת-branch-אישי)
4. [עבודה עם טרמינל וקבצים](#שלב-ב4-עבודה-עם-טרמינל-וקבצים)
5. [מעקב אחרי השינויים שלכם](#שלב-ב5-מעקב-אחרי-השינויים-שלכם)
6. [סנכרון עם הצוות והעלאה](#שלב-ב6-סנכרון-עם-הצוות-והעלאה)
7. [הגשת Pull Request](#שלב-ב7-הגשת-pull-request)
8. [מיזוג ועדכון](#שלב-ב8-מיזוג-ועדכון)

---

## שלב ב1: הגדרת זהות

ספרו ל-Git מי אתם (פעם אחת למחשב).

```bash
git config --global user.name "YourFullName"
git config --global user.email "yourmail@example.com"
```

**אימות:**
```bash
git config --global --list
```

---

## שלב ב2: שכפול Repository של הצוות

הורידו את הפרויקט המשותף למחשב שלכם.

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

**דוגמה:**
```bash
git clone https://github.com/team/data-lab.git
cd data-lab
```

**בדיקת חיבור:**
```bash
git remote -v
```
אמורים לראות את כתובת ה-Repository של הצוות.

---

## שלב ב3: יצירת Branch אישי

**כלל:** אף פעם לא עובדים ישירות על `main` branch בפרויקט צוותי!

### צרו את ה-branch האישי שלכם
```bash
git checkout -b feature/YourName
```

**דוגמה:** `git checkout -b feature/Peer`

### וודאו שאתם על ה-branch שלכם
```bash
git branch
```
ה-`*` והצבע הירוק צריכים להיות ליד שם ה-branch שלכם.

**הסבר:** Branch זה סביבת העבודה האישית שלכם. שינויים כאן לא ישפיעו על אחרים עד שתעשו merge.

---

## שלב ב4: עבודה עם טרמינל וקבצים

צרו את התוכן שלכם באמצעות פקודות טרמינל. **חשוב:** כל הקבצים חייבים להתחיל בשמכם!

### צרו את התיקייה שלכם
```bash
mkdir YourName_Lab
cd YourName_Lab
```

### צרו סקריפט Python
```bash
nano YourName_script.py
```
כתבו:
```python
print("Hello Cloud")
```
שמרו (Ctrl+O, Enter) וצאו (Ctrl+X).

### צרו קובץ JSON
```bash
nano YourName_config.json
```
כתבו:
```json
{"user": "YourName", "status": "active"}
```
שמרו וצאו.

### הציגו את הקובץ שלכם
```bash
cat YourName_config.json
```

---

## שלב ב5: מעקב אחרי השינויים שלכם

ראו מה Git זיהה.

### בדיקת מצב
```bash
git status
```
הקבצים יופיעו **באדום** (Untracked).

### Stage קבצים
```bash
git add .
git status
```
הקבצים עכשיו **בירוק** (Staged).

### בדיקת פקודת diff
שנו קובץ:
```bash
nano YourName_script.py
```
הוסיפו: `print("Data Engineering!")`

עכשיו בדקו:
```bash
git diff
```

**הסבר:** `diff` מראה בדיוק מה השתנה. ירוק = הוספה, אדום = מחיקה.

### Stage שוב ו-commit
```bash
git add .
git commit -m "Added lab files for YourName"
```

---

## שלב ב6: סנכרון עם הצוות והעלאה

**שלב קריטי:** לפני העלאה, תמיד הסתנכרנו עם עבודת חברי הצוות!

### סנכרון מה-remote
```bash
git fetch origin
git pull origin main
```

**הסבר:**
- `fetch`: בודק מה חדש ב-GitHub
- `pull`: מוריד וממזג את הקוד של חברי הצוות לעותק המקומי שלכם

### העלאת ה-branch שלכם
```bash
git push origin feature/YourName
```

**מה קרה?** ה-Branch שלכם עכשיו ב-GitHub, אבל עדיין לא ב-`main` branch.

---

## שלב ב7: הגשת Pull Request

במקום לעשות merge בעצמכם, בקשו ביקורת (best practice!).

### באתר GitHub:
1. היכנסו ל-Repository שלכם ב-GitHub
2. תראו באנר צהוב: **"Compare & pull request"** - לחצו עליו
3. מלאו:
   - **Title:** "Added lab files - YourName"
   - **Description:** תיאור קצר של מה עשיתם
4. לחצו **"Create pull request"**

**למה Pull Request (PR)?**
- מאפשר ביקורת קוד לפני מיזוג
- הצוות יכול להגיב ולהציע שינויים
- מונע באגים מלהיכנס לקוד הראשי
- מראה את העבודה שלכם למדריך/צוות

---

## שלב ב8: מיזוג ועדכון

אחרי ש-ה-PR שלכם אושר ומוזג:

### חזרו ל-main
```bash
git checkout main
```

**בדיקה:** הקבצים שלכם מה-branch נעלמים - זה נורמלי!

### משכו את השינויים האחרונים
```bash
git pull origin main
```

**בדיקה:** עכשיו הקבצים שלכם מופיעים ב-`main` branch!

**הסבר:** השינויים שלכם עכשיו חלק מהקוד המשותף.

### אימות השינויים
```bash
ls -la
git log --oneline
```

---

## 🎓 סיכום - תרחיש ב'

למדתם:
- ✅ שכפול repository צוותי
- ✅ תהליך עבודה עם branches (לעולם לא על `main`!)
- ✅ יצירת קבצים עם `nano`, `mkdir`, `cat`
- ✅ מעקב אחרי שינויים עם `status`, `diff`, `add`, `commit`
- ✅ סנכרון עם הצוות באמצעות `fetch` ו-`pull`
- ✅ הגשת Pull Request לביקורת
- ✅ מיזוג ועדכון העותק המקומי

---

---

# 💡 כללים חיוניים לשני התרחישים

## 🚫 לעולם אל תשתמשו ב-Rebase ב-Repositories משותפים
**למה?** Rebase משכתב את היסטוריית Git. בפרויקטים צוותיים, זה שובר סנכרון לכולם.

**כלל:** תמיד השתמשו ב-`merge`, לעולם לא ב-`rebase`.

---

## 🏷️ מוסכמת שמות קבצים (תרחיש ב')
כל הקבצים חייבים להתחיל בשמכם:
- ✅ `Peer_data.json`
- ✅ `Sarah_script.py`
- ❌ `data.json` (יידרס על ידי חברי הצוות!)

---

## 🔍 תמיד בדקו Status קודם
לפני כל פקודת Git, הריצו:
```bash
git status
```
זה המצפן שלכם - הוא מראה:
- על איזה branch אתם
- אילו קבצים השתנו
- מה staged/unstaged

---

## 📝 Best Practices להודעות Commit
**Commits טובים:**
```bash
git commit -m "Added data cleaning script"
git commit -m "Fixed bug in CSV parser"
git commit -m "Updated README with setup instructions"
```

**Commits גרועים:**
```bash
git commit -m "changes"
git commit -m "fix"
git commit -m "asdfgh"
```

---

## 🆘 בעיות נפוצות ופתרונות

### "Permission denied" בזמן push?
```bash
# בדקו את כתובת ה-remote
git remote -v

# עדכנו לשימוש ב-HTTPS
git remote set-url origin https://github.com/username/repo.git
```

### שכחתם על איזה branch אתם?
```bash
git branch
```
ה-`*` מראה את ה-branch הנוכחי.

### רוצים לראות היסטוריית commits?
```bash
git log --oneline --graph
```

### עשיתם שינויים אבל רוצים לבטל?
```bash
git restore <filename>
```

---

## 📚 מדריך מהיר לפקודות

| פקודה | תיאור |
|-------|--------|
| `git status` | בדיקת מצב נוכחי |
| `git add .` | Stage כל השינויים |
| `git commit -m "msg"` | שמירת תמונת מצב |
| `git push origin <branch>` | העלאה ל-GitHub |
| `git pull origin <branch>` | הורדה מ-GitHub |
| `git branch` | רשימת branches |
| `git checkout <branch>` | מעבר ל-branch |
| `git diff` | ראיית שינויים לא staged |
| `git log --oneline` | צפייה בהיסטוריה |

---

## 🎯 צעדים הבאים

אחרי שתשלטו בבסיס:
1. למדו על קבצי `.gitignore`
2. חקרו `git stash` לשמירות זמניות
3. תרגלו פתרון merge conflicts
4. נסו `git log` עם אופציות שונות

---

**למידה מהנה! 🎓**

</div>
