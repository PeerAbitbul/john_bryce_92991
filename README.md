# john_bryce_92991

🚀 Practical Lab: Git & Linux Terminal – Learning Path
Welcome to our Cloud & Big Data lab! This guide is designed linearly. Follow the steps sequentially to master the essential tools of a Data Engineer.

📋 Table of Contents
Setup & Identity

Branch Management

Terminal & File Skills

Tracking Changes (Status & Diff)

Sync & Push

Pull Request Submission

💡 Key Rules & No Rebase Policy

Step 1: Setup & Identity
Before we begin, tell Git who you are and download the project to your computer.

Set Username:

Bash

git config --global user.name "YourFullName"
Set Email:

Bash

git config --global user.email "yourmail@example.com"
Clone Repository:

Bash

git clone <URL_OF_REPOSITORY>
cd <REPOSITORY_NAME>
Check Remote: Run git remote -v.

Explanation: This shows your GitHub URL. Ensure it appears twice (for fetch and push).

Step 2: Branch Management
In a team, we never work directly on the main branch.

Create a New Branch:

Bash

git checkout -b feature/YourName
Verify Branch: Run git branch.

Explanation: Ensure the asterisk * and green color are next to your branch name.

Step 3: Terminal & File Skills
Now we will use mkdir and nano to create content. Every file/folder name must start with your name!

Create Folder: mkdir YourName_Lab then enter it with cd YourName_Lab.

Create Python Script: Run nano YourName_script.py. Write print("Hello Cloud"), save (Ctrl+O, Enter), and exit (Ctrl+X).

Create JSON Config: Run nano YourName_config.json. Add: {"user": "YourName", "status": "active"}.

View Content: Use cat YourName_config.json to verify the content on your screen.

Step 4: Tracking Changes
See how Git monitors your work.

Check Status: Run git status. Files will appear in red (Untracked).

Stage Files: Run git add . then git status again. Files will appear in green (Staged).

Inspect Differences (Diff): Open a file with nano, modify it, and save. Then run:

Bash

git diff
Explanation: Diff shows exactly what was added (Green) or removed (Red) since the last stage.

Step 5: Sync & Push
Stay updated with your classmates' work before sending yours.

Commit:

Bash

git commit -m "Added lab files for YourName"
Sync from Cloud (Fetch & Pull):

Bash

git fetch origin
git pull origin main
Explanation: fetch checks for updates; pull downloads and merges them into your local copy.

Step 6: Pull Request Submission
Instead of merging yourself, you submit a request for review (PR).

Push Branch: git push origin feature/YourName.

On GitHub Website: Click the green Compare & Pull Request button.

Why PR? It acts as a "gatekeeper," allowing for Code Review before changes enter the main system. This prevents critical bugs in production.

💡 Key Rules & No Rebase Policy
🚫 No Rebase: In a shared repository, rebase rewrites history. Doing so can break the sync for your teammates. Only use merge.

🏷️ Naming Convention: All files MUST start with your name (e.g., John_data.json).

🔍 Status First: Always run git status before any other Git command.

🚀 מעבדה מעשית: Git & Linux Terminal – מסלול למידה (עברית)
ברוכים הבאים למעבדה שלנו! המדריך הזה בנוי בצורה ליניארית. עקבו אחר השלבים כדי לשלוט בכלים הבסיסיים של מהנדס נתונים.

📋 תוכן עניינים
הגדרות זהות וסנכרון ראשוני

ניהול ענפים (Branches)

עבודה עם הטרמינל וקבצים (Nano)

מעקב אחרי שינויים (Status & Diff)

סנכרון ושליחה (Pull & Push)

הגשה ב-Pull Request

💡 כללי אצבע ואיסור Rebase

שלב 1: הגדרות זהות וסנכרון ראשוני
לפני הכל, נגדיר ל-Git מי אנחנו ונוריד את הפרויקט למחשב.

הגדרת שם משתמש:

Bash

git config --global user.name "YourFullName"
הגדרת אימייל:

Bash

git config --global user.email "yourmail@example.com"
הורדת המאגר (Clone):

Bash

git clone <URL_OF_REPOSITORY>
cd <REPOSITORY_NAME>
בדיקת חיבור לשרת (Remote): הריצו git remote -v.

הסבר: כאן תראו את הכתובת של ה-GitHub שלכם. וודאו שהיא מופיעה פעמיים (fetch ו-push).

שלב 2: ניהול ענפים (Branches)
בצוות, לעולם לא עובדים ישירות על ה-Main.

יצירת Branch חדש:

Bash

git checkout -b feature/YourName
בדיקה איפה אנחנו: הריצו git branch.

הסבר: וודאו שהכוכבית והצבע הירוק מופיעים ליד השם שלכם.

שלב 3: עבודה עם הטרמינל וקבצים
כעת נלמד להשתמש בפקודות mkdir ו-nano כדי ליצור תכנים. חובה להתחיל כל שם של קובץ/תיקייה בשמכם!

יצירת תיקייה: mkdir YourName_Lab ואז היכנסו אליה עם cd YourName_Lab.

יצירת סקריפט Python: הריצו nano YourName_script.py. כתבו print("Hello Cloud"), שמרו (Ctrl+O) וצאו (Ctrl+X).

יצירת קובץ JSON: הריצו nano YourName_config.json. כתבו מבנה נתונים פשוט: {"user": "YourName", "status": "active"}.

בדיקת תוכן: השתמשו ב-cat YourName_config.json כדי לראות את התוכן על המסך.

שלב 4: מעקב אחרי שינויים
נלמד איך Git מזהה מה עשינו.

בדיקת מצב (Status): הריצו git status. הקבצים יהיו באדום (Untracked).

הוספה למעקב (Add): הריצו git add . והריצו שוב git status. כעת הם בירוק (Staged).

בדיקת הבדלים (Diff): פתחו שוב את אחד הקבצים ב-nano, שנו בו משהו ושמרו. כעת הריצו:

Bash

git diff
הסבר: ה-Diff מראה בדיוק מה השתנה מאז השמירה האחרונה. ירוק = הוספה, אדום = מחיקה.

שלב 5: סנכרון ושליחה
לפני שנשלח, נתעדכן במה שחברים אחרים עשו.

שמירה (Commit):

Bash

git commit -m "Added lab files for YourName"
סנכרון מהענן (Fetch & Pull):

Bash

git fetch origin
git pull origin main
הסבר: fetch רק בודק מה חדש, pull מוריד וממזג את הקוד של שאר הכיתה אליכם.

שלב 6: הגשה ב-Pull Request
במקום לעשות Merge בעצמנו, אנחנו מבקשים אישור (Request).

שליחת הענף: git push origin feature/YourName.

באתר GitHub: לחצו על Compare & Pull Request.

למה PR? זהו "שומר הסף". הוא מאפשר בדיקת קוד (Code Review) לפני שהשינויים נכנסים למערכת המרכזית. זה מונע טעויות קריטיות בייצור.

💡 כללי אצבע ואיסור Rebase
🚫 אסור לעשות Rebase: ב-Repository משותף, Rebase משכתב את ההיסטוריה. אם תעשו זאת, אתם עלולים להרוס לחברים לכיתה את הסנכרון. השתמשו רק ב-merge.

🏷️ שמות קבצים: קובץ ללא שם התלמיד בראשו יימחק. שמרו על סדר כדי למנוע דריסת קבצים.

🔍 בדיקה מתמדת: השתמשו ב-git status לפני כל פעולה. זה המצפן שלכם.
