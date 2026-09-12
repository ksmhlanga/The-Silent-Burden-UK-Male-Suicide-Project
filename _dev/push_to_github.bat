@echo off
echo Setting up git remote and pushing to GitHub...
cd /d "C:\Users\Cudzie\Documents\Projects\The Silent Burden - UK Male Suicide Project"
git remote add origin https://github.com/ksmhlanga/UK_Silent_Crisis_Project.git
git push -u origin main --force
echo Done!
pause
