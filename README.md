# About

This project enables the user to easily develop challenges in [challenges](InscryptionSaveManager/src/challenges.py). These challenges are used in [main_scrypt](InscryptionSaveManager/src/main_scrypt.py). Challenges can be combined, as each challenge is a child class of the Challenge class. A ChallengeManager object is instantiated in main_scrypt with a list of challenges. So, one could play a run that clamps attack stat to 2 and adds a beehive on every save. That would be weird. Funny.

# Use

To use this project, install the necessary packages with pipenv install. Then 